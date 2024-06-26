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

no_of_transaction = 0

def is_pdf(file):
    return file.name.endswith('.pdf')

def convert_to_float(column,all_transactions):
    if all_transactions[column].dtype != 'float64':
        all_transactions[column] = all_transactions[column].apply(lambda x: str(x).replace(',', '').replace('-',''))
    return all_transactions[column]

def clean_data(df):
    try:
        df = read_pdf(df,password='208228',pages='all')
       
    except:
        df = read_pdf(df,password='208228')
        
    no_of_transaction = len(df)
    summary = df[1] 
    
    summary['PAID IN'] = summary['PAID IN'].apply(lambda x: float(x.replace('$','').replace(',','')))
    summary['PAID OUT'] = summary['PAID OUT'].apply(lambda x: float(x.replace('$','').replace(',','')))
    # delete the last row in a dataframe
    summary = summary.drop(summary.index[-1])
    summary = summary.drop(['Unnamed: 0'],axis='columns')

   
    
    if no_of_transaction > 1:
        transactions = df[2:no_of_transaction-1]
        all_transactions = pd.concat(transactions)
        all_transactions.columns = all_transactions.columns.str.strip().str.replace('\r', '')
        all_transactions['Completion Time'] = pd.to_datetime(all_transactions['Completion Time']).dt.date
        all_transactions['Withdrawn'] = convert_to_float('Withdrawn',all_transactions=all_transactions).astype(float)
        all_transactions['Balance'] = convert_to_float('Balance',all_transactions).astype(float)
        all_transactions['Paid In'] = convert_to_float('Paid In',all_transactions).astype(float).fillna(0)
    else:
        all_transactions=None

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
        
        try:
            summary,all_transactions = clean_data(uploaded_file)
            # summary,all_transactions = clean_data(uploaded_file)
            st.write("## Summary of all transactions")
            st.divider()
            st.write(summary)
            st.write("### Time Series of Paid Out Amounts")
            st.bar_chart(data=summary,x='TRANSACTION TYPE', y='PAID OUT', use_container_width=True)
            st.divider()
            st.write("### Time Series of Paid Out Amounts")
            st.bar_chart(data=summary,x='TRANSACTION TYPE', y='PAID IN', use_container_width=True)
            st.divider()
            st.write("## Details of all transactions")
            st.divider()

            if all_transactions is not None:
                # st.write(all_transactions.head())
                st.write("### Time Series of Paid in Amounts")
                st.line_chart(data=all_transactions,x='Completion Time',y=["Paid In"], use_container_width=True)
                st.divider()
                st.write("### Time Series of Withdrawn Amounts")
                st.line_chart(data=all_transactions,x='Completion Time',y=["Withdrawn"], use_container_width=True)
                st.divider()
                st.write("### Time Series of Balance Amounts")
                
                st.line_chart(data=all_transactions,x='Completion Time',y=["Balance"], use_container_width=True)
            else:
                st.write("No transaction records found in the uploaded file")
        except:
            st.warning("Warning: Uploaded PDF file is not supported")


    else:
        st.warning("Warning: Uploaded file is not a PDF.")

    my_bar.empty()


    