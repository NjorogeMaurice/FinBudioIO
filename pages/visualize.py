import pandas as pd
import streamlit as st
from io import StringIO
import time
from tabula import read_pdf


add_sidebar_title = st.sidebar.write("Welcome to FinBudIO")

add_divider = st.sidebar.divider() 
st.sidebar.page_link("app.py", label="Home")
st.sidebar.page_link("pages/visualize.py", label="Visualize data")
st.sidebar.page_link("pages/playground.py", label="Playground")
st.sidebar.page_link("pages/chat.py", label="Chat with your data")

def is_pdf(file):
    return file.name.endswith('.pdf')

def clean_data(df):
    df = read_pdf(df,pages='all')
    summary = df[0]
    summary['PAID IN'] = summary['PAID IN'].apply(lambda x: float(x.replace('$','').replace(',','')))
    summary['PAID OUT'] = summary['PAID OUT'].apply(lambda x: float(x.replace('$','').replace(',','')))
    # delete the last row in a dataframe
    summary = summary.drop(summary.index[-1])
    summary = summary.drop(['Unnamed: 0'],axis='columns')

    df.pop(0)
    transactions = df
    all_transactions = pd.concat(transactions)
    all_transactions.columns = all_transactions.columns.str.strip().str.replace('\r', '')
    all_transactions['Completion Time'] = pd.to_datetime(all_transactions['Completion Time']).dt.date
    # all_transactions['Withdrawn'] = all_transactions['Withdrawn'].apply(lambda x: float(x.replace('$','').replace(',','')))
    all_transactions['Balance'] = all_transactions['Balance'].apply(lambda x: float(x.replace('$','').replace(',','')))
    all_transactions['Paid in'] = all_transactions['Paid in'].apply(lambda x: float(x.replace('$','').replace(',','')))
    return summary, all_transactions


st.header('Visualize your data', divider='blue')
uploaded_file = st.file_uploader("Choose a file(PDF format)")
if uploaded_file is not None:
    progress_text = "Document is being uploaded. Please wait..."
    my_bar = st.progress(0)

    # Display progress while uploading
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)

    time.sleep(1)
    if is_pdf(uploaded_file):
        st.success("File uploaded successfully!")
        summary,all_transactions = clean_data(uploaded_file)
        try:
            summary,all_transactions = clean_data(uploaded_file)
            st.write("## Summary of all transactions")
            st.divider()
            st.write("### Time Series of Paid Out Amounts")
            st.bar_chart(data=summary,x='TRANSACTION TYPE', y='PAID OUT', use_container_width=True)
            st.divider()
            st.write("### Time Series of Paid Out Amounts")
            st.bar_chart(data=summary,x='TRANSACTION TYPE', y='PAID IN', use_container_width=True)
            st.divider()
            st.write("## Details of all transactions")
            st.divider()
            st.write("### Time Series of Paid in Amounts")
            st.line_chart(data=all_transactions,x='Completion Time',y=["Paid in"], use_container_width=True)
            st.divider()
            st.write("### Time Series of Withdrawn Amounts")
            st.line_chart(data=all_transactions,x='Completion Time',y=["Withdrawn"], use_container_width=True)
            st.divider()
            st.write("### Time Series of Balance Amounts")
            
            st.line_chart(data=all_transactions,x='Completion Time',y=["Balance"], use_container_width=True)
        except:
            st.warning("Warning: Uploaded PDF file is not supported")


    else:
        st.warning("Warning: Uploaded file is not a PDF.")

    my_bar.empty()


    