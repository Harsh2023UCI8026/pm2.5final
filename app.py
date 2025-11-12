from flask import Flask, jsonify
import pandas as pd
import joblib
import numpy as np
from tensorflow.keras.models import load_model
from datetime import timedelta

app = Flask(__name__)

# --- Load models and data ---
arima_model = joblib.load("model/arima_model.pkl")
lstm_model = load_model("model/lstm_residual_model.h5", compile=False)
scaler = joblib.load("model/scaler.pkl")
df = pd.read_csv("data/processed/ghaziabad_pm25_yearly.csv")
df['datetime'] = pd.to_datetime(df['datetime'])
df = df.sort_values('datetime')

@app.route("/api/forecast", methods=["GET"])
def forecast():
    forecast_steps = 72
    arima_forecast = arima_model.forecast(steps=forecast_steps)
    last_24 = df['pm25'].values[-24:].reshape(-1, 1)
    scaled_last_24 = scaler.transform(last_24)
    current_seq = scaled_last_24.reshape(1, 24, 1)
    pred_residuals = []

    for _ in range(forecast_steps):
        pred = lstm_model.predict(current_seq, verbose=0)
        pred_residuals.append(pred[0][0])
        current_seq = np.append(current_seq[:, 1:, :], [[pred]], axis=1)

    pred_residuals = scaler.inverse_transform(np.array(pred_residuals).reshape(-1, 1)).flatten()
    hybrid_forecast = arima_forecast + pred_residuals

    future_dates = [df['datetime'].iloc[-1] + timedelta(hours=i+1) for i in range(forecast_steps)]

    forecast_df = pd.DataFrame({
        'datetime': [d.strftime('%Y-%m-%d %H:%M:%S') for d in future_dates],
        'hybrid_forecast': hybrid_forecast
    })

    return jsonify(forecast_df.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)
