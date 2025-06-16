import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

def train_and_save_model(df, save_path='outputs/fraud_model.pkl'):
    features = ['TX_AMOUNT', 'TX_HOUR', 'daily_tx_count', 'terminal_tx_count']
    X = df[features]
    y = df['TX_FRAUD']

    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print("Model Evaluation:\n")
    print(classification_report(y_test, model.predict(X_test)))

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    joblib.dump(model, save_path)
