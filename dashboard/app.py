import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Page config
st.set_page_config(page_title="Biz Intel Dashboard", layout="wide")

# Title and header
st.title("📊 Biz Intel Dashboard")
st.markdown("An interactive dashboard for job intelligence scraped from various platforms.")

# Load data
DATA_PATH = os.path.join("..", "data", "jobs.csv")
try:
    df = pd.read_csv('data/jobs.csv')
except Exception as e:
    st.error(f"⚠️ Could not load data: {e}")
    st.stop()

# Sidebar filters
st.sidebar.header("🔍 Filter Jobs")
companies = df["company"].dropna().unique()
locations = df["location"].dropna().unique()

selected_companies = st.sidebar.multiselect("Company", options=companies)
selected_locations = st.sidebar.multiselect("Location", options=locations)

filtered_df = df.copy()
if selected_companies:
    filtered_df = filtered_df[filtered_df["company"].isin(selected_companies)]
if selected_locations:
    filtered_df = filtered_df[filtered_df["location"].isin(selected_locations)]

# Tabs
tab1, tab2, tab3 = st.tabs(["📄 Listings", "📈 Charts", "📉 Trends"])

with tab1:
    st.subheader("Job Listings")
    for _, row in filtered_df.iterrows():
        st.markdown(f"**{row['title']}** at *{row['company']}*")
        if pd.notna(row['location']):
            st.write(f"📍 Location: {row['location']}")
        st.markdown(f"[🔗 Apply Here]({row['url']})")
        st.markdown("---")

with tab2:
    st.subheader("Jobs by Company")
    company_counts = filtered_df['company'].value_counts().reset_index()
    company_counts.columns = ['company', 'count']
    fig1 = px.bar(company_counts.head(10), x='count', y='company', orientation='h', title='Top 10 Hiring Companies')
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Jobs by Location")
    location_counts = filtered_df['location'].value_counts().reset_index()
    location_counts.columns = ['location', 'count']
    fig2 = px.pie(location_counts.head(10), values='count', names='location', title='Top 10 Job Locations')
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.subheader("📉 Trends (Mock Data)")
    st.markdown("Coming soon: Apply NLP + Time-based analysis of job trends.")

# Download section
st.sidebar.markdown("### 📦 Download")
st.sidebar.download_button(
    label="Download CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_jobs.csv",
    mime="text/csv"
)

# Footer
st.markdown("---")
st.caption("Built with ❤️ by Doc27 | v1.0 Beta")














