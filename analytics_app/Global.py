import psycopg2
import db_params
import streamlit as st
import numpy as np
import pandas as pd
import datetime
#from statsmodels import robust
# from scipy import stats as sts
import plotly.express as px
import locale

locale.setlocale(locale.LC_ALL, "")

# SQL DB connection
# connection = psycopg2.connect(
#     "postgres://postgres:{db_params.password}@localhost:5433/imaginary-inc"
# )

connection = psycopg2.connect(**st.secrets["postgres"])





# to have wide mode by default
st.set_page_config(layout="wide")

# Filters/Inputs
date_range = st.date_input(
    "Date Range", [datetime.date(2016, 1, 1), datetime.date(2022, 12, 1)]
)


# CURRENT PORTFOLIO
st.markdown("## Imaginary Inc Global Portfolio")

# Running SQL script to get data
sql_global = open("global.sql", "r")
df = pd.read_sql_query(sql_global.read(), con=connection)
sql_global.close()

# apply filters
df = df[(df.month >= date_range[0]) & (df.month <= date_range[1])]

# Nb paid customers Bar Chart
# paid_customers_container = st.empty()

# with paid_customers_container:
#     col1, col2 = st.columns([6, 1])  # layout
#     with col1:
#         st.markdown("##### Nb Paid Customers")
#         chart = px.bar(df, x="month", y="nb_paid_customers")
#         st.plotly_chart(chart, use_container_width=True)
#     with col2:
#         st.markdown("Trend for nb paid customers")
#         st.markdown("**Filters**: Date Range")

# Nb paid seats Bar Chart
# paid_seats_container = st.empty()
# with paid_seats_container:
#     col1, col2 = st.columns([6, 1])  # layout
#     with col1:
#         st.markdown("##### Nb Paid Seats")
#         chart = px.bar(df, x="month", y="nb_paid_seats")
#         st.plotly_chart(chart, use_container_width=True)
#     with col2:
#         st.markdown("Trend for nb paid seats")
#         st.markdown("**Filters**: Date Range")

# MRR Bar Chart
mrr_container = st.empty()
with mrr_container:
    col1, col2 = st.columns([6, 1])  # layout
    with col1:
        st.markdown("##### MRR")
        chart = px.bar(df, x="month", y="mrr").update_layout(yaxis_tickprefix="$")
        st.plotly_chart(chart, use_container_width=True)
    with col2:
        st.markdown("Trend for MRR")
        st.markdown("**Filters**: Date Range")

# separator line
st.markdown("""---""")