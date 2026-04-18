# Project: Aspirational Districts Resource Tracker
# Created by: Anurag Teotia
# Date: April 2026
# Purpose: Internship Portfolio Project (Data Engineering)
import pandas as pd
try:
    # Load the data
    df = pd.read_csv('data.csv', encoding='unicode_escape')

    # 1. Clean the data: Fill missing (NaN) utilization with 0 so our math doesn't break
    df['Grand Total - Total Amount Utilised'] = df['Grand Total - Total Amount Utilised'].fillna(
        0)

    # 2. CALCULATE EFFICIENCY: (Utilised / Sanctioned) * 100
    df['Utilization_Rate'] = (df['Grand Total - Total Amount Utilised'] /
                              df['Grand Total - Total Amount Sanctioned']) * 100

    # --- NEW: ADD THE FILTER HERE ---
    # We only care about districts where the government sent more than 5.0 (significant funds)
    significant_funds = df[df['Grand Total - Total Amount Sanctioned'] > 5.0]

    # 3. IDENTIFY UNDERPERFORMERS: Now we sort the FILTERED list
    low_efficiency = significant_funds.sort_values(
        by='Utilization_Rate', ascending=True)

    print("\n--- CRITICAL AUDIT: LARGE SANCTIONS WITH LOW UTILIZATION ---")
    # Using head(5) to see the bottom 5 "bottleneck" districts
    print(low_efficiency[[
          'District', 'Grand Total - Total Amount Sanctioned', 'Utilization_Rate']].head(5))

except Exception as e:
    print(f"❌ Error: {e}")
