# streamlit_app.py
import streamlit as st
import pandas as pd
import os
from glob import glob
import plotly.express as px

st.set_page_config(page_title="Personal Finance Dashboard", layout="wide")
st.title("📊 Personal Finance Dashboard")

@st.cache_data
def load_data():
    files = glob("data/*.csv")
    df_list = []
    for f in files:
        try:
            df = pd.read_csv(f)
            df['Source File'] = os.path.basename(f)
            df_list.append(df)
        except Exception as e:
            st.warning(f"Could not read {f}: {e}")
    if not df_list:
        return pd.DataFrame()
    df = pd.concat(df_list, ignore_index=True)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
    df = df.dropna(subset=['Date'])
    df['Amount (GBP)'] = pd.to_numeric(df['Amount (GBP)'], errors='coerce')
    df = df.dropna(subset=['Amount (GBP)'])
    df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)
    df['Type'] = df['Type'].fillna('UNKNOWN')
    df['Spending Category'] = df['Spending Category'].fillna('Uncategorized')
    return df

# Load data
df = load_data()
if df.empty:
    st.error("No data found. Please upload CSVs to the 'data/' folder.")
    st.stop()

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    min_date, max_date = df['Date'].min(), df['Date'].max()
    date_range = st.date_input("Date Range", [min_date, max_date])

    categories = st.multiselect("Categories", options=sorted(df['Spending Category'].unique()))
    types = st.multiselect("Transaction Types", options=sorted(df['Type'].unique()))

# Apply filters
mask = (df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))
if categories:
    mask &= df['Spending Category'].isin(categories)
if types:
    mask &= df['Type'].isin(types)
filtered = df[mask]

# Summary
st.subheader("💡 Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Income", f"£{filtered[filtered['Amount (GBP)'] > 0]['Amount (GBP)'].sum():,.2f}")
col2.metric("Total Expenses", f"£{abs(filtered[filtered['Amount (GBP)'] < 0]['Amount (GBP)'].sum()):,.2f}")
col3.metric("Net Flow", f"£{filtered['Amount (GBP)'].sum():,.2f}")

# Monthly Trend
st.subheader("📈 Monthly Net Flow")
monthly = filtered.groupby('YearMonth')['Amount (GBP)'].sum().reset_index()
st.plotly_chart(px.bar(monthly, x='YearMonth', y='Amount (GBP)', title='Net Flow per Month'))

# Category breakdown
st.subheader("📊 Spending by Category")
cat_sum = filtered[filtered['Amount (GBP)'] < 0].groupby('Spending Category')['Amount (GBP)'].sum().abs().sort_values(ascending=False).reset_index()
st.plotly_chart(px.pie(cat_sum, names='Spending Category', values='Amount (GBP)', title='Expense Breakdown'))

# Income sources
st.subheader("📥 Top Income Sources")
income = filtered[filtered['Amount (GBP)'] > 0]
income_sources = income.groupby('Counter Party')['Amount (GBP)'].sum().sort_values(ascending=False).reset_index().head(10)
st.plotly_chart(px.bar(income_sources)), x:=Co
