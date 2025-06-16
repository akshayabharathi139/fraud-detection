# fraud-detection

# 💳 Fraud Transaction Detection Web Application

This project is a machine learning-powered web application that detects fraudulent financial transactions using a simulated dataset. It provides a user-friendly interface built with Streamlit for entering transaction details and classifying transactions as **fraudulent** or **legitimate**.

---

## 📌 Objective

To build a system that can classify whether a financial transaction is fraudulent based on key features like transaction amount, customer ID, and terminal ID.

---

## 📁 Dataset Description

The dataset simulates real-world fraud patterns, including:

1. **High-amount frauds**: Any transaction with an amount > 220 is marked as fraud.
2. **Compromised terminals**: Random terminals used fraudulently for a duration.
3. **Leaked customer credentials**: Fraudulent high-value transactions made on behalf of real customers.

### 📄 Columns:

- `TRANSACTION_ID`: Unique identifier for the transaction.
- `TX_DATETIME`: Timestamp of transaction.
- `CUSTOMER_ID`: Unique ID for each customer.
- `TERMINAL_ID`: Unique ID for each terminal.
- `TX_AMOUNT`: Transaction amount.
- `TX_FRAUD`: `0` = legitimate, `1` = fraud.

---

## 🧠 Model

A `RandomForestClassifier` is trained on extracted features to classify transactions.

- Features used:
  - `TX_AMOUNT`
  - `CUSTOMER_ID`
  - `TERMINAL_ID`

---

## 🗂️ Folder Structure

fraud_detection/
├── data/ # Daily .pkl transaction files
├── outputs/
│ └── fraud_model.pkl # Trained ML model and feature list
├── src/
│ ├── load_data.py # Function to load multiple daily pkl files
│ ├── preprocess.py # Data preprocessing logic (if any)
│ └── model.py # Model training function
├── app.py # Streamlit web app
├── train.py # Script to train and save the model
├── requirements.txt # Python dependencies
└── README.md # Project documentation



---

## 🚀 How to Run the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
💻 Example Input
In the Streamlit sidebar, enter:

Transaction Amount: 45.0

Customer ID: 100015

Terminal ID: 200045

Click Check Transaction to see if it’s classified as fraud.
python train.py


✅ Expected Output
If the transaction is legitimate:

pgsql
Copy
Edit
✅ Transaction is Legitimate. Probability of Fraud: 0.02
If it’s fraud:

yaml
Copy
Edit
🚨 Fraudulent Transaction Detected! Probability: 0.93



🧪 Requirements
Python 3.7+

scikit-learn

pandas

joblib

Streamlit

All required libraries are listed in requirements.txt.



👩‍💻 Author
Akshaya Bharathi






