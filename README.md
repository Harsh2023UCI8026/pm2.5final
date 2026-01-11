# 🌫️ PM2.5 Air Quality Forecasting System

A hybrid time-series forecasting system that predicts **PM2.5 air pollution levels** using a combination of **ARIMA and LSTM models**, exposed through a Flask-based REST API and visualized on the frontend.

---

## 🚀 Project Overview

This project forecasts PM2.5 concentrations for the next **72 hours** by combining:
- **ARIMA** for linear trend forecasting
- **LSTM neural network** for modeling non-linear residual patterns

The predictions are served through an API and displayed using an interactive line chart.

---

## 🧠 Methodology

1. ARIMA predicts baseline PM2.5 values  
2. LSTM predicts residual errors from ARIMA  
3. Final forecast = ARIMA prediction + LSTM residuals  
4. Forecast data is returned via a Flask API in JSON format  

---

## 🛠️ Technologies Used

- **Python**
- **Flask** – REST API development  
- **Pandas & NumPy** – Data processing  
- **ARIMA (Statsmodels)** – Time-series forecasting  
- **LSTM (TensorFlow / Keras)** – Deep learning model  
- **Joblib** – Model persistence  
- **Chart.js** – Frontend visualization  
- **HTML/CSS/JavaScript** – UI and API consumption  

---



