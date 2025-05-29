import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data.csv')

# Spend by Category
st.title('Spend by Category')
category_spend = data.groupby('Category')['TotalCost'].sum().reset_index()
st.dataframe(category_spend)

# Bar chart for spend by category
fig, ax = plt.subplots()
ax.bar(category_spend['Category'], category_spend['TotalCost'])
ax.set_xlabel('Category')
ax.set_ylabel('Total Spend')
ax.set_title('Total Spend by Category')
plt.xticks(rotation=45)
st.pyplot(fig)
