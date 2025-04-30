# Covid_19_Global_Analysis-
A Python-based project for analyzing and visualizing global COVID-19 trends using time-series data. It calculates key health KPIs, performs WHO region-wise aggregation, and generates insightful visualizations including maps and bar charts. Ideal for reporting and pandemic trend analysis.


📊 COVID-19 Global Analysis & Visualization
A comprehensive data analysis and visualization project tracking the COVID-19 pandemic across countries and WHO regions. This project includes data transformation, modeling, KPI calculation, and interactive as well as static visualizations using Python.

📌 Table of Contents
Overview

Features & KPIs

Data Source

Technologies Used

Installation

Usage

Project Structure

Visualizations

Contributing

License

🧾 Overview
This project scrapes, cleans, transforms, and visualizes global COVID-19 data from the start of the pandemic (Jan 2020) through the second wave and beyond. It includes:

Country-level and regional statistics

Computation of daily and cumulative metrics

WHO Region-wise analysis

Interactive choropleth maps and bar charts

Exported visual outputs for reporting and dashboards

✅ Features & KPIs
The project computes and visualizes the following metrics:

🔢 Global KPIs:
Total Confirmed Cases

Total Deaths

Total Recovered

Total Active Cases

Global Recovery Rate

🌍 WHO Region-Wise KPIs:
Cumulative Confirmed, Deaths, Recovered, Active

Mortality Rate (%)

Bar charts for regional comparisons

Choropleth map of confirmed cases by country

🗂️ Data Source
The dataset is built using:

COVID-19 time series data from Johns Hopkins University CSSE GitHub repo.

Modeled using custom data scraping and merging pipeline to align and aggregate across dates and regions.

🛠️ Technologies Used

Category	Libraries / Tools
Data Handling	pandas, numpy
Mapping	pycountry, plotly, kaleido
Visualization	matplotlib, seaborn, plotly.express
Output Saving	PNG image export with matplotlib and plotly
Geocoding	pycountry for ISO 3166-1 Alpha-3 codes
⚙️ Installation
Install all required Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
If you don't have a requirements.txt, use:

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn plotly pycountry kaleido
▶️ Usage
Place the modeled dataset: modeled_global_covid_data.csv in the root folder.

Run the main script:

bash
Copy
Edit
python covid_analysis.py
Outputs will be saved in the output_images/ folder:

global_confirmed_cases_map.png

confirmed_cases_by_region.png

active_and_mortality_by_region.png

region_summary.csv

🗂 Project Structure
text
Copy
Edit
📁 project-root
├── covid_analysis.py               # Main analysis and visualization script
├── modeled_global_covid_data.csv  # Final processed dataset (input)
├── output_images/                 # Folder for PNG outputs and CSV
│   ├── global_confirmed_cases_map.png
│   ├── confirmed_cases_by_region.png
│   ├── active_and_mortality_by_region.png
│   └── region_summary.csv
└── README.md
📸 Visualizations
Choropleth Map

Confirmed Cases by WHO Region

Active Cases & Mortality Rate

🤝 Contributing
Contributions are welcome! If you'd like to:

Add new KPIs

Improve map granularity

Build a dashboard (e.g., Streamlit, Dash)

Feel free to fork the repo and submit a PR.

📊 COVID-19 Global Analysis & Visualization
A comprehensive data analysis and visualization project tracking the COVID-19 pandemic across countries and WHO regions. This project includes data transformation, modeling, KPI calculation, and interactive as well as static visualizations using Python.

📌 Table of Contents
Overview

Features & KPIs

Data Source

Technologies Used

Installation

Usage

Project Structure

Visualizations

Contributing

License

🧾 Overview
This project scrapes, cleans, transforms, and visualizes global COVID-19 data from the start of the pandemic (Jan 2020) through the second wave and beyond. It includes:

Country-level and regional statistics

Computation of daily and cumulative metrics

WHO Region-wise analysis

Interactive choropleth maps and bar charts

Exported visual outputs for reporting and dashboards

✅ Features & KPIs
The project computes and visualizes the following metrics:

🔢 Global KPIs:
Total Confirmed Cases

Total Deaths

Total Recovered

Total Active Cases

Global Recovery Rate

🌍 WHO Region-Wise KPIs:
Cumulative Confirmed, Deaths, Recovered, Active

Mortality Rate (%)

Bar charts for regional comparisons

Choropleth map of confirmed cases by country

🗂️ Data Source
The dataset is built using:

COVID-19 time series data from Johns Hopkins University CSSE GitHub repo.

Modeled using custom data scraping and merging pipeline to align and aggregate across dates and regions.

🛠️ Technologies Used

Category	Libraries / Tools
Data Handling	pandas, numpy
Mapping	pycountry, plotly, kaleido
Visualization	matplotlib, seaborn, plotly.express
Output Saving	PNG image export with matplotlib and plotly
Geocoding	pycountry for ISO 3166-1 Alpha-3 codes
⚙️ Installation
Install all required Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
If you don't have a requirements.txt, use:

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn plotly pycountry kaleido
▶️ Usage
Place the modeled dataset: modeled_global_covid_data.csv in the root folder.

Run the main script:

bash
Copy
Edit
python covid_analysis.py
Outputs will be saved in the output_images/ folder:

global_confirmed_cases_map.png

confirmed_cases_by_region.png

active_and_mortality_by_region.png

region_summary.csv

🗂 Project Structure
text
Copy
Edit
📁 project-root
├── covid_analysis.py               # Main analysis and visualization script
├── modeled_global_covid_data.csv  # Final processed dataset (input)
├── output_images/                 # Folder for PNG outputs and CSV
│   ├── global_confirmed_cases_map.png
│   ├── confirmed_cases_by_region.png
│   ├── active_and_mortality_by_region.png
│   └── region_summary.csv
└── README.md
📸 Visualizations
Choropleth Map

Confirmed Cases by WHO Region

Active Cases & Mortality Rate

🤝 Contributing
Contributions are welcome! If you'd like to:

Add new KPIs

Improve map granularity

Build a dashboard (e.g., Streamlit, Dash)

Feel free to fork the repo and submit a PR.



