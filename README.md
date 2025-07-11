# 🛡️ DDoS & PortScan Detection System (ML-based IDS)

This project implements a lightweight Intrusion Detection System (IDS) to detect **DDoS** and **PortScan** attacks using a trained **Random Forest** model and a web-based GUI built with **Streamlit**.

---

## Features

- 📁 Upload `.csv` network logs (e.g., CIC-IDS 2017)
- 🤖 Classify each flow as `BENIGN`, `DDoS`, or `PortScan` (with some Web-Attacks)
- 📊 Displays predictions and counts
- 💾 Download results as CSV
- 🌐 Deployed easily via Streamlit Cloud

---

## How It Works

1. Trained on CIC-IDS 2017 attack datasets
2. Extracted key features (flow duration, packets/sec, etc.)
3. Preprocessed using `StandardScaler` and `LabelEncoder`
4. Deployed Random Forest model via Streamlit app

---

## Tech Stack

- Python 3.10+
- scikit-learn
- pandas, numpy
- Streamlit
- joblib

---

## Installation

```bash
pip install -r requirements.txt
streamlit run ddos_gui.py
