import os
import pandas as pd

def load_transaction_data(data_dir):
    all_data = []
    for file in sorted(os.listdir(data_dir)):
        if file.endswith('.pkl'):
            df = pd.read_pickle(os.path.join(data_dir, file))
            all_data.append(df)
    return pd.concat(all_data, ignore_index=True)
