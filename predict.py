import numpy as np
import joblib

def predict_fraud(model_path, features_dict):
    model = joblib.load(model_path)
    input_vector = np.array([[features_dict['TX_AMOUNT'], features_dict['TX_HOUR'],
                              features_dict['daily_tx_count'], features_dict['terminal_tx_count']]])
    prediction = model.predict(input_vector)
    return int(prediction[0])
