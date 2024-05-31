from tabula import read_pdf
import pandas as pd


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
    return summary, all_transactions