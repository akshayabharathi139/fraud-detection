# train.py

from src.load_data import load_transaction_data
from src.preprocess import preprocess
from src.model import train_and_save_model

def main():
    print("📥 Loading transaction data...")
    df = load_transaction_data("data")

    print(f"✅ Loaded {len(df)} transactions.")

    print("🧹 Preprocessing data...")
    df = preprocess(df)

    print("🤖 Training model...")
    train_and_save_model(df, save_path="outputs/fraud_model.pkl")

    print("✅ Model training completed and saved to 'outputs/fraud_model.pkl'.")

if __name__ == "__main__":
    main()
