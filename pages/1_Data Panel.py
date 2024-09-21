import streamlit as st
import time
import numpy as np
import pandas as pd
from data_fetcher import fetch_from_FRED

st.set_page_config(page_title="Data Panel", page_icon="📈")

st.markdown("# Data Panel")
st.sidebar.header("Data Panel")
##################################################choose data you want to see
col_fred, col_stock,col_commodity,col_currency = st.columns(4)
if 'data_selected' not in st.session_state:
    st.session_state.data_selected=None
def select_data(data):
    st.session_state.data_selected=data

with col_fred:
    fred = st.selectbox(
    label='',
    options=('Total Nonfarm Payroll','Initial Jobless Claims','Continued Claims','JOLTS',
     'Labor demand','Labour supply','Government vs Total private','wages'),
    on_change=select_data,
    args=('fred', ),
    label_visibility='collapsed',
    placeholder='FRED',
    index=None
)
with col_stock:
    stock = st.selectbox(
    label='',
    options=('Total Nonfarm Payroll','Initial Jobless Claims','Continued Claims','JOLTS',
     'Labor demand','Labour supply','Government vs Total private','wages'),
    on_change=select_data,
    args=('stock', ),
    label_visibility='collapsed',
    placeholder='Stocks',
    index=None
)
with col_commodity:
    commodity = st.selectbox(
    label='',
    options=('Total Nonfarm Payroll','Initial Jobless Claims','Continued Claims','JOLTS',
     'Labor demand','Labour supply','Government vs Total private','wages'),
    on_change=select_data,
    args=('commodity', ),
    label_visibility='collapsed',
    placeholder='Commodities',
    index=None
)
with col_currency:
    currency = st.selectbox(
    label='',
    options=('Total Nonfarm Payroll','Initial Jobless Claims','Continued Claims','JOLTS',
     'Labor demand','Labour supply','Government vs Total private','wages'),
    on_change=select_data,
    args=('currency', ),
    label_visibility='collapsed',
    placeholder='Currencies',
    index=None
)

##################################################introduction for this data
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)
##############################################Choose date range
col1, col2,col3,col4 = st.columns(4)
with col1:
    start_date = st.date_input("Start", value=None)
with col2:
    end_date = st.date_input("End", value=None)
with col3:
    st.empty()
with col4:
    st.empty()
###############################################Plot chart

if st.session_state.data_selected=='fred':
    chart_data = fetch_from_FRED(fred,start_date, end_date)
    if "ma" not in st.session_state:
        # set the initial default value of the slider widget
        st.session_state.ma = 1
    chart_data=chart_data.rolling(st.session_state.ma).mean()
    chart = st.line_chart(chart_data)

    ma = st.slider("Moving Average", 1, 8, step=2,key='ma')