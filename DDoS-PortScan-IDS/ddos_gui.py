import os
import urllib.request

def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"⏬ Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
    else:
        print(f"✅ {filename} already exists.")

# 🔁 Replace these with your actual Drive file IDs
download_file("https://drive.google.com/uc?export=download&id=12QAHwvKhVnMdLcvgFz2OO4F8KVMZpD82", "rf_model.pkl")
download_file("https://drive.google.com/uc?export=download&id=13T4O57Ts9hLJjhhUnjEx4DlMJ3M8tge2", "scaler.pkl")
download_file("https://drive.google.com/uc?export=download&id=1oQnRYWUhVO0isT1AVFSBxf-xcS883IJh", "label_encoder.pkl")

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model, scaler, and encoder
model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")

# Features used in training
features = [
    'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',
    'Total Length of Fwd Packets', 'Total Length of Bwd Packets',
    'Fwd Packet Length Max', 'Bwd Packet Length Max',
    'Fwd Packets/s', 'Bwd Packets/s',
    'Flow IAT Mean', 'Fwd IAT Mean', 'Bwd IAT Mean'
]

# UI
st.set_page_config(page_title="DDoS & PortScan Detector", layout="centered")
st.title("🛡️ DDoS & PortScan Intrusion Detection System")

uploaded_file = st.file_uploader("📂 Upload a CIC-IDS CSV File", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        df.columns = df.columns.str.strip()
        df = df.replace([np.inf, -np.inf], np.nan).dropna()

        if all(f in df.columns for f in features):
            X = df[features]
            X_scaled = scaler.transform(X)
            y_pred = model.predict(X_scaled)
            y_labels = encoder.inverse_transform(y_pred)

            df['Prediction'] = y_labels
            st.success("✅ Prediction complete!")

            # Show summary
            st.subheader("🔎 Prediction Summary")
            st.write(df['Prediction'].value_counts())

            # Show table
            st.subheader("📋 Sample Predictions")
            st.dataframe(df[['Prediction']].head(100))

            # Downloadable result
            csv = df.to_csv(index=False).encode()
            st.download_button("📥 Download Results as CSV", csv, "predicted_results.csv", "text/csv")

        else:
            st.error("❌ Required features not found in uploaded CSV.")
    except Exception as e:
        st.error(f"🚫 Error: {e}")
