# 🇮🇳 Aspirational Districts: Resource Equity & Budget Tracker

[![Python Version](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io/)
[![Visualization](https://img.shields.io/badge/Visualization-Plotly-purple.svg)](https://plotly.com/)
[![Data Source](https://img.shields.io/badge/Data%20Source-data.gov.in-green.svg)](https://data.gov.in/)

An end-to-end Data Orchestration & Analytics Dashboard engineered to evaluate the financial efficiency and expenditure performance of districts across Uttar Pradesh under the Aspirational Districts Programme.

---

## 📸 Dashboard Preview

<img width="1888" height="1028" alt="Screenshot 2026-08-17 002602" src="https://github.com/user-attachments/assets/bbc644f7-6f65-43d9-a414-7d6808799179" />

*Figure 1: Real-time interactive dashboard featuring dynamic expenditure filtering, performance rankings, and district utilization analytics.*

---

## 📌 Project Overview

Public development programs often face friction between fund sanctioning and ground-level execution. This project ingests real-world public expenditure data from the **Open Government Data (OGD) Platform India (`data.gov.in`)** to pinpoint administrative bottlenecks, resource misalignments, and regional disparities.

Built for **Public Administrators, Policy Researchers, and Data Analysts**, this dashboard enables stakeholders to identify delayed projects, assess fund utilization rates, and drive data-backed audit interventions.

---

## 🚀 Key Features

* **Data Cleaning & Normalization Engine:** Systematically handles missing values (`NaN`), normalizes schema variations, and standardizes multi-district budget figures.
* **Custom Performance Metric (`Utilization_Rate`):** Computes actual expenditure against sanctioned capital:
  $$\text{Utilization Rate} = \left( \frac{\text{Actual Expenditure}}{\text{Sanctioned Budget}} \right) \times 100$$
* **Dynamic Parameter Filtering:** Interactive sidebar controls to isolate high-value investments (e.g., projects $> ₹10\text{ Cr}$).
* **Exploratory Visual Analytics:** Interactive Plotly-driven charts highlighting top/bottom-performing districts requiring immediate administrative review.

---

## 🛠️ Tech Stack & Architecture

* **Core Language:** Python
* **Data Processing & EDA:** Pandas, NumPy
* **Interactive Visualization:** Plotly Express / Graph Objects
* **Application Framework:** Streamlit
* **Data Source:** [Open Government Data (OGD) Platform India](https://data.gov.in)

---

## 🔍 Key Administrative Insights

* **Reporting Lags vs. Stalled Execution:** Several districts reflect $0\%$ utilization despite substantial capital sanctions—highlighting critical data-entry latencies or ground-level execution stalls.
* **Resource Misalignment:** High-sanction zones do not consistently correlate with high absorption capacity, signaling the need for phased disbursements and localized monitoring.

---

## ⚙️ Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/anuragteotia/GovTech-Equity-Tracker.git](https://github.com/anuragteotia/GovTech-Equity-Tracker.git)
   cd GovTech-Equity-Tracker
   ``` 

## 👤 Author
Anurag Teotia

B.Tech in Computer Science & Engineering
ITS Engineering College, Greater Noida

GitHub: github.com/anuragteotia
LinkedIn: linkedin.com/in/anurag-teotia
