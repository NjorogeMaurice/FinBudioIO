import streamlit as st



add_sidebar_title = st.sidebar.write("Welcome to FinBudIO")

add_divider = st.sidebar.divider() 
st.sidebar.page_link("app.py", label="Home")
st.sidebar.page_link("pages/visualize.py", label="Visualize data")
st.sidebar.page_link("pages/playground.py", label="Playground")
st.sidebar.page_link("pages/chat.py", label="Chat with your data")

st.header('Playground', divider='blue')
st.write("###  Learn more from your financial data (Still under development)")
st.write("Try predictive analysis, anomaly detection etc using different machine learning models")

