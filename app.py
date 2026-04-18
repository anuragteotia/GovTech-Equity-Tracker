# Project: Aspirational Districts Resource Tracker
# Created by: Anurag Teotia
# Date: April 2026
# Purpose: Internship Portfolio Project (Data Engineering)
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Gov-Tech Equity Dashboard", layout="wide")

st.title("🇮🇳 Aspirational Districts: Resource Equity Tracker")
st.sidebar.markdown("---")
st.sidebar.write("### 🛠️ Developer Profile")
st.sidebar.write("**Name:** Anurag Teotia ")
st.sidebar.write("**Role:** Data engineering enthusiast ")
st.sidebar.markdown("---")
st.markdown(
    "Analyzing budget utilization to identify administrative bottlenecks.")


df = pd.read_csv('data.csv', encoding='unicode_escape')
df['Grand Total - Total Amount Utilised'] = df['Grand Total - Total Amount Utilised'].fillna(
    0)
df['Utilization_Rate'] = (df['Grand Total - Total Amount Utilised'] /
                          df['Grand Total - Total Amount Sanctioned']) * 100


min_sanction = st.sidebar.slider("Minimum Sanctioned Amount (Cr)", 0, 100, 5)
filtered_df = df[df['Grand Total - Total Amount Sanctioned'] > min_sanction]


fig = px.bar(filtered_df.sort_values('Utilization_Rate').head(10),
             x='District', y='Utilization_Rate',
             title="Top 10 Districts Needing Attention (Lowest Utilization)",
             color='Utilization_Rate', color_continuous_scale='Reds')

st.plotly_chart(fig, use_container_width=True)
