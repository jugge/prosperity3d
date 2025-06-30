import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sys
from strategies.taught_life import TaughtLife
from strategies.early_extreme_saving import EarlyExtremeSaving

# Streamlit UI
st.title("Prosperity Strategy Simulator")

st.sidebar.header("Simulation Settings")
age_range = np.linspace(25, 70, 100)
start_income = st.sidebar.number_input("Start Income (SEK)", value=30000, step=1000)
current_age = st.sidebar.number_input("Enter your current age in years", value=25)
stop_working_age = st.sidebar.number_input("Enter estimated age to stop working", value=67)


# Strategy selection
strategy_options = {
    "Taught Life": TaughtLife,
    "Extreme Saver": EarlyExtremeSaving
}
selected_strategy_name = st.sidebar.selectbox("Choose Strategy", list(strategy_options.keys()))
strategy_class = strategy_options[selected_strategy_name]

# Instantiate and run strategy
strategy = strategy_class(selected_strategy_name, age_range, start_income)
strategy.run()
results = strategy.results()

# Plot the result in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(results['income'], results['cost'], results['prosperity'], label=selected_strategy_name)
ax.set_xlabel("Income")
ax.set_ylabel("Cost")
ax.set_zlabel("Prosperity")
ax.set_title("Strategy: " + selected_strategy_name)
ax.legend()

st.pyplot(fig)

# Optionally: show table
if st.checkbox("Show raw data"):
    st.dataframe({
        "Income": results['income'],
        "Cost": results['cost'],
        "Prosperity": results['prosperity']
    })

# Stop button
if st.button("Stop Streamlit App"):
    st.write("Shutting down...")
    st.stop()