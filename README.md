# 🇮🇳 Aspirational Districts: Resource Equity & Budget Tracker

## 📌 Project Overview
This project is a **Data Orchestration & Analytics Dashboard** designed to track the financial efficiency of Indian districts. Using real-world data from the **Open Government Data (OGD) Platform**, the tool identifies "Administrative Bottlenecks" by comparing sanctioned funds versus actual utilization.

This tool is built for **Public Administrators** and **Policy Researchers** to ensure that development funds are not just allocated, but effectively spent.

## 🚀 Live Features
- **Data Cleaning Engine:** Automatically handles missing (NaN) government data records.
- **Efficiency Metric:** Calculates a custom `Utilization_Rate` to rank districts by performance.
- **Dynamic Filtering:** A sidebar slider allows users to focus on high-stakes projects (e.g., only projects > 10 Cr).
- **Interactive Visuals:** Real-time bar charts showing the top districts requiring immediate administrative audit.

## 🛠️ Tech Stack
- **Language:** Python 3.14
- **Libraries:** - `Pandas`: For data manipulation and cleaning.
  - `Streamlit`: For building the web interface.
  - `Plotly`: For interactive data visualization.
- **Data Source:** [data.gov.in](https://data.gov.in) (Aspirational Districts Healthcare/Expenditure Datasets).

## 📊 Key Administrative Insights
During the development of this tracker, the following was observed:
1. **Reporting Lags:** Several districts show 0% utilization despite high sanctions, indicating either a data-entry lag or a ground-level project stall.
2. **Resource Misalignment:** High-funding zones don't always correlate with high-utilization zones, suggesting a need for localized administrative intervention.

## ⚙️ How to Run
1. Clone this repository.
2. Ensure you have the dataset named as `data.csv` in the root folder.
3. Install dependencies:
   ```bash
   pip install pandas streamlit plotly

---
## 👤 Author
**ANURAG TEOTIA** 2nd Year B.Tech, Computer Science & Engineering **I.T.S ENGINNERING COLLEGE , GREATER NOIDA**

