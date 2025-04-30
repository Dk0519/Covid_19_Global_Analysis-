import pandas as pd

# Load the dataset you previously created
df = pd.read_csv("global_covid_data_by_date.csv")

# ---------------------------
# 1. DATA CLEANING
# ---------------------------

# A. Convert data types
df['Date'] = pd.to_datetime(df['Date'])
numeric_cols = ["Confirmed", "Deaths", "Recovered", "Active", "New cases", "New deaths", "New recovered"]
df[numeric_cols] = df[numeric_cols].fillna(0).astype(int)

# B. Standardize country names (examples)
df['Country/Region'] = df['Country/Region'].replace({
    "US": "United States",
    "Korea, South": "South Korea",
    "Russian Federation": "Russia",
    "Iran (Islamic Republic of)": "Iran",
    "Viet Nam": "Vietnam",
    "Taiwan*": "Taiwan"
    # Add more mappings if needed
})

# ---------------------------
# 2. FEATURE ENGINEERING
# ---------------------------

# A. Daily Growth Rate (handle divide by zero safely)
df["Growth Rate"] = df["New cases"] / df["Confirmed"].replace(0, pd.NA)

# B. Mortality & Recovery Rate
df["Mortality Rate"] = df["Deaths"] / df["Confirmed"].replace(0, pd.NA)
df["Recovery Rate"] = df["Recovered"] / df["Confirmed"].replace(0, pd.NA)

# C. 7-Day Moving Averages
df["MA_7_NewCases"] = df.groupby("Country/Region")["New cases"].transform(lambda x: x.rolling(7).mean())
df["MA_7_Deaths"] = df.groupby("Country/Region")["New deaths"].transform(lambda x: x.rolling(7).mean())
df["MA_7_Recovery"] = df.groupby("Country/Region")["New recovered"].transform(lambda x: x.rolling(7).mean())

# ---------------------------
# 3. TIME-BASED SEGMENTATION
# ---------------------------

# Tag COVID waves (India-centric example, adjust per country)
def assign_wave(date):
    if pd.Timestamp("2020-03-01") <= date <= pd.Timestamp("2020-08-31"):
        return "First Wave"
    elif pd.Timestamp("2021-03-01") <= date <= pd.Timestamp("2021-07-31"):
        return "Second Wave"
    elif pd.Timestamp("2022-01-01") <= date <= pd.Timestamp("2022-03-31"):
        return "Third Wave"
    else:
        return "Other"

df["Wave"] = df["Date"].apply(assign_wave)

# ---------------------------
# 4. OPTIONAL: POPULATION JOIN
# ---------------------------

# Load a population dataset (ensure column 'Country/Region' exists in both)
# Example population_df = pd.read_csv("country_population.csv")
# df = df.merge(population_df, on="Country/Region", how="left")
# df["Cases per 100k"] = (df["Confirmed"] / df["Population"]) * 100000

# ---------------------------
# 5. EXPORT TO FILE
# ---------------------------

df.to_csv("modeled_global_covid_data.csv", index=False)

# Optional: Quick check
print(df.head(10))
