# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 21:24:03 2024

@author: adity
"""
# Tensorgo Assignment 20MIP10008 ADITYA KUMAR VIT BHOPAL


#Libraries
import streamlit as st
import pandas as pd
import os
from pandasai import SmartDataframe
from pandasai import Agent
#os.environ['PANDASAI_API_KEY'] = "$2a$10$qRm2WxEQUQiUQr9pL/jcgexrBqyjKdL/WIb1JPr36q04tPHrDHjPK"
os.environ['PANDASAI_API_KEY']="$2a$10$9mmDHvAZ/d.rjCBxiTgWQO/PWIxGC8lrOGACanJXdNeKpDr3AV/OK"

#Func Defination


#UI
st.set_page_config(page_title="CSV Wizard 🌟",layout="wide")

st.markdown("<h1 style='text-align: center; color: black;'>CSV Wizard 🌟</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'>Please upload your CSV file below.</h5>", unsafe_allow_html=True)
data = st.file_uploader("Upload a CSV" , type=["csv"])

if data!=None:
    df = pd.read_csv(data)
    st.dataframe(df.head())
    sdf = SmartDataframe(df)
    agent = Agent(df)

#user input --> eg. What is the mean of [xyz] column? --> Numeric output
                #   How many rows are in dataset --> Numerix output
                #   Plot Bar chart for [XYZ] column and [abc] values --> IMG output
query = st.text_area("Give a prompt")

if st.button('Generate result'):
    #st.write('clicked') #for debug
    #ans = sdf.chat(query)
    agentans = agent.chat(query)
    #st.write(ans)
    st.write(agentans)

st.markdown("<h3 style='text-align: center; color: black;'>Some examples</h3>", unsafe_allow_html=True)
st.write("""
    ```python
    # Some example of prompts.
    How many total rows in dataset?
    What is mean of [ABC] column
    Plot Bar chart for [XYZ] column and [abc] values --> IMG output
    Plot Pie chart for [KMN] column --> IMG output
    ```
    """
    )

st.write('')

st.markdown("<h3 style='text-align: center; color: black;'>FAQs</h3>", unsafe_allow_html=True)
with st.expander("About Project"):
    st.write(
        "This project is LLM Powered CSV analyzer which helps data scientists & analysts to perform varios data analysis process and plotting charts using Nautural languge. Users just have to provide their dataset(csv) file and give appropriate prompts to get desired outputs in analysis process."
    )
    st.write(
        "This project is using bambooLLM from pandasAI, pandasAI smart dataframe"
    )
with st.expander("How to use this project?"):
    st.write('Click on BROWSE FILE button then select CSV dataset on which you want to perform anaysis, Once dataset loaded you will be able to see preview of it the you need to give promts to get insights from data or to generate plots hen click in GENERATE button this will show you the results.')


