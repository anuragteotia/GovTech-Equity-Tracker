# Project: Aspirational Districts Resource Tracker
# Created by: Anurag Teotia
# Date: April 2026
# Purpose: Internship Portfolio Project (Data Engineering)
import pandas as pd
try:
    
    df = pd.read_csv('data.csv', encoding='unicode_escape')

   
    df['Grand Total - Total Amount Utilised'] = df['Grand Total - Total Amount Utilised'].fillna(
        0)

    
    df['Utilization_Rate'] = (df['Grand Total - Total Amount Utilised'] /
                              df['Grand Total - Total Amount Sanctioned']) * 100

    
    significant_funds = df[df['Grand Total - Total Amount Sanctioned'] > 5.0]

   
    low_efficiency = significant_funds.sort_values(
        by='Utilization_Rate', ascending=True)

    print("\n--- CRITICAL AUDIT: LARGE SANCTIONS WITH LOW UTILIZATION ---")
   
    print(low_efficiency[[
          'District', 'Grand Total - Total Amount Sanctioned', 'Utilization_Rate']].head(5))

except Exception as e:
    print(f"❌ Error: {e}")
