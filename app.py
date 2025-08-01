import pandas as pd
import streamlit as st
import plotly.express as px

# Page title
st.title("📊 Daily Household Energy Consumption Dashboard")

# Load CSV
@st.cache_data
def load_data():
    df = pd.read_csv("energy_data_india.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
appliance = st.sidebar.multiselect("Select Appliances", options=df['Appliance'].unique(), default=df['Appliance'].unique())

filtered_df = df[df['Appliance'].isin(appliance)]

# Show Data
st.subheader("Filtered Energy Consumption Data")
st.dataframe(filtered_df)

# Line Chart
st.subheader("📈 Line Graph - Daily Consumption by Appliance")
line_chart = px.line(filtered_df, x="Date", y="Consumption_kWh", color="Appliance", markers=True)
st.plotly_chart(line_chart)

# Scatter Plot
st.subheader("🔵 Scatter Plot - Energy Consumption Trends")
scatter = px.scatter(filtered_df, x="Date", y="Consumption_kWh", color="Appliance", size="Consumption_kWh", hover_data=['Appliance'])
st.plotly_chart(scatter)

# Pie Chart (Total consumption by appliance)
st.subheader("🥧 Pie Chart - Total Consumption by Appliance")
pie_df = filtered_df.groupby("Appliance")["Consumption_kWh"].sum().reset_index()
pie_chart = px.pie(pie_df, names="Appliance", values="Consumption_kWh", title="Total Energy Used per Appliance")
st.plotly_chart(pie_chart)

# Footer
st.markdown("Developed by Varshini 👩‍💻")
