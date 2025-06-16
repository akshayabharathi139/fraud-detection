import streamlit as st
from src.predict import predict_fraud

st.set_page_config(page_title="Fraud Detection App", page_icon="🕵️‍♂️")
st.title("🕵️ Real-Time Fraud Transaction Detector")

st.markdown("### Enter Transaction Details:")

tx_amount = st.number_input("Transaction Amount ($)", min_value=0.0, step=1.0)
tx_hour = st.slider("Transaction Hour", 0, 23)
daily_tx_count = st.number_input("Customer's Daily Transaction Count", min_value=0)
terminal_tx_count = st.number_input("Terminal's Total Transaction Count", min_value=0)

if st.button("🔍 Predict Fraud"):
    features = {
        'TX_AMOUNT': tx_amount,
        'TX_HOUR': tx_hour,
        'daily_tx_count': daily_tx_count,
        'terminal_tx_count': terminal_tx_count
    }

    pred = predict_fraud("outputs/fraud_model.pkl", features)

    if pred == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legitimate Transaction")
