import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime
import joblib
import time
import os

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), "model.joblib")
model = joblib.load(model_path)
# Cities
cities = ['Mumbai', 'Delhi', 'Bengaluru', 'Chennai', 'Kolkata']

# Function to simulate weather data
def simulate_weather():
    return {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'location': random.choice(cities),
        'humidity': round(np.random.uniform(40, 90), 2),
        'wind_speed': round(np.random.uniform(5, 25), 2)
    }

# Initialize app state
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['timestamp', 'location', 'humidity', 'wind_speed', 'predicted_temperature'])

st.title("🌦️ Simulated Weather Prediction Dashboard")

speed = st.slider("⏱️ Simulation speed (seconds)", 1, 5, 2)

if st.button("▶️ Start Simulation"):
    st.session_state.run = True

if st.button("⏹️ Stop Simulation"):
    st.session_state.run = False

# Main loop
# Only simulate one row per run
if st.session_state.get("run", False):
    # Generate one row of data
    row = simulate_weather()
    df_input = pd.DataFrame([row])

    # Predict temperature using the model
    pred = model.predict(df_input[['location', 'humidity', 'wind_speed']])[0]
    row['predicted_temperature'] = round(pred, 2)

    # Add the new row to the session data
    st.session_state.data = pd.concat(
        [st.session_state.data, pd.DataFrame([row])],
        ignore_index=True
    )

    # Display updated data
    st.subheader("📊 Live Weather Data")
    st.dataframe(st.session_state.data.tail(10), use_container_width=True)

    st.line_chart(st.session_state.data[['predicted_temperature']].tail(50))

    # Wait and rerun
    time.sleep(speed)
    st.rerun()
