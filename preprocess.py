import pandas as pd

def preprocess(df):
    df['TX_DATETIME'] = pd.to_datetime(df['TX_DATETIME'])
    df['TX_DAY'] = df['TX_DATETIME'].dt.date
    df['TX_HOUR'] = df['TX_DATETIME'].dt.hour

    daily_tx_count = df.groupby(['CUSTOMER_ID', 'TX_DAY'])['TRANSACTION_ID'].count().reset_index(name='daily_tx_count')
    df = df.merge(daily_tx_count, on=['CUSTOMER_ID', 'TX_DAY'])

    df['terminal_tx_count'] = df.groupby('TERMINAL_ID')['TRANSACTION_ID'].transform('count')
    return df
