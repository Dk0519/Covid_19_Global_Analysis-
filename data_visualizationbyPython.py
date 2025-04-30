import pandas as pd
import pycountry
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Ensure images folder exists
os.makedirs("output_images", exist_ok=True)

# Load data
df = pd.read_csv("modeled_global_covid_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Latest date
latest_date = df['Date'].max()
df_latest = df[df['Date'] == latest_date]

# Global KPIs
total_confirmed = df_latest['Confirmed'].sum()
total_deaths = df_latest['Deaths'].sum()
total_recovered = df_latest['Recovered'].sum()
total_active = df_latest['Active'].sum()
recovery_rate = (total_recovered / total_confirmed) * 100 if total_confirmed else 0

# Print KPIs
print("===== Global COVID-19 KPIs =====")
print(f"Date: {latest_date.date()}")
print(f"Total Confirmed: {total_confirmed:,}")
print(f"Total Deaths: {total_deaths:,}")
print(f"Total Recovered: {total_recovered:,}")
print(f"Total Active: {total_active:,}")
print(f"Recovery Rate: {recovery_rate:.2f}%")
print("================================")

# WHO Region Mapping (extend as needed)
region_map = {
    "India": "South-East Asia",
    "United States": "Americas",
    "Brazil": "Americas",
    "Russia": "Europe",
    "China": "Western Pacific",
    "Germany": "Europe",
    "Egypt": "Eastern Mediterranean",
    "South Africa": "Africa",
    "Italy": "Europe",
    "France": "Europe",
    "Spain": "Europe",
    "UK": "Europe",
    "Mexico": "Americas",
    "Indonesia": "South-East Asia",
    "Iran": "Eastern Mediterranean",
    "Turkey": "Europe"
}

df_latest["WHO Region"] = df_latest["Country/Region"].map(region_map)

# Region Summary
region_summary = df_latest.groupby("WHO Region")[["Confirmed", "Deaths", "Recovered", "Active"]].sum().reset_index()
region_summary["Mortality Rate"] = region_summary["Deaths"] / region_summary["Confirmed"].replace(0, pd.NA)

# Save Region Summary as CSV
region_summary.to_csv("output_images/region_summary.csv", index=False)

# Plotly ISO mapping
def get_alpha3(country):
    try:
        return pycountry.countries.lookup(country).alpha_3
    except:
        return None

df_latest['iso_alpha'] = df_latest['Country/Region'].apply(get_alpha3)
df_latest = df_latest.dropna(subset=['iso_alpha'])

# Plotly Choropleth Map
fig = px.choropleth(
    df_latest,
    locations="iso_alpha",
    color="Confirmed",
    hover_name="Country/Region",
    color_continuous_scale="Reds",
    title=f"Global COVID-19 Confirmed Cases as of {latest_date.date()}",
    projection="natural earth"
)
fig.update_layout(
    geo=dict(showframe=False, showcoastlines=True),
    coloraxis_colorbar=dict(title="Confirmed Cases")
)

# Save Map
fig.write_image("output_images/global_confirmed_cases_map.png", scale=2)

# Seaborn: Region-wise Confirmed Cases
plt.figure(figsize=(12, 6))
sns.barplot(data=region_summary.sort_values("Confirmed", ascending=False),
            x="Confirmed", y="WHO Region", palette="OrRd")
plt.title("Confirmed COVID-19 Cases by WHO Region")
plt.xlabel("Confirmed Cases")
plt.ylabel("WHO Region")
plt.tight_layout()
plt.savefig("output_images/confirmed_cases_by_region.png", dpi=300)
plt.show()

# Seaborn: Active Cases & Mortality Rate
fig, ax = plt.subplots(1, 2, figsize=(18, 6))

# Active Cases
sns.barplot(data=region_summary.sort_values("Active", ascending=False), 
            x="Active", y="WHO Region", palette="Blues_r", ax=ax[0])
ax[0].set_title("Active COVID-19 Cases by WHO Region")
ax[0].set_xlabel("Active Cases")

# Mortality Rate
sns.barplot(data=region_summary.sort_values("Mortality Rate", ascending=False), 
            x="Mortality Rate", y="WHO Region", palette="Reds_r", ax=ax[1])
ax[1].set_title("Mortality Rate by WHO Region")
ax[1].set_xlabel("Mortality Rate (%)")

plt.tight_layout()
plt.savefig("output_images/active_and_mortality_by_region.png", dpi=300)
plt.show()
