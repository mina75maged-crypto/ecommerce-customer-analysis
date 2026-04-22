import streamlit as st  # استيراد المكتبة
import pandas as pd
import plotly.express as px
st.title("Sales Analytics Dashboard — Arabic Business Data")  # عنوان المشروع

df = pd.read_csv("ecommerce_customer_churn_dataset.csv")

country = st.selectbox(
    "Select Country",
    df["Country"].unique()
)
filtered_df = df[df["Country"] == country]
st.write(filtered_df)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total customers", len(filtered_df))
with col2:
    st.metric("Top country", df["Country"].value_counts().index[0])
with col3:
    Churn_rate = filtered_df["Churned"].mean() * 100
    st.metric("Churn rate", f"{Churn_rate:.1f}%")
fig = px.bar(
    filtered_df,
    x="Country",
    title="Customers by Country"
)    
st.plotly_chart(fig)

fig2 = px.histogram(
    filtered_df,
    x="Age",
    title="Customer distribution by Age"
)
st.plotly_chart(fig2)