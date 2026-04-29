import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")
st.title("📘 Student Performance Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("data/students.csv")

df = load_data()

classes = st.sidebar.multiselect("Select Class", options=df["Class"].unique(), default=list(df["Class"].unique()))
gender = st.sidebar.multiselect("Select Gender", options=df["Gender"].unique(), default=list(df["Gender"].unique()))

filtered = df[(df["Class"].isin(classes)) & (df["Gender"].isin(gender))]

col1,col2,col3 = st.columns(3)
col1.metric("Total Students", len(filtered))
col2.metric("Average Marks", round(filtered["Marks"].mean(),2))
col3.metric("Pass Rate (%)", round((filtered["Marks"] >= 50).mean()*100,2))

fig1 = px.bar(filtered, x="Student", y="Marks", color="Gender", title="Marks by Student")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.box(filtered, x="Subject", y="Marks", color="Subject", title="Subject Performance")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Student Data")
st.dataframe(filtered)