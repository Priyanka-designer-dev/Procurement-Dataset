import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Procurement Analysis Dashboard 🚀")

# Load data (replace with your dataset path)
data = pd.read_csv("Procurement_Dataset.csv")

st.write("## Summary of Data")
st.dataframe(data.head())

# Simple bar chart example
st.write("## Spend by Category")
category_spend = data.groupby('Category')['Spend'].sum().reset_index()
fig, ax = plt.subplots()
ax.bar(category_spend['Category'], category_spend['Spend'], color='skyblue')
plt.xticks(rotation=45)
st.pyplot(fig)

# More interactive charts, filters, etc. can be added!

