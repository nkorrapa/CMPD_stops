import seaborn as sbn
import pandas as pd
import streamlit as st
import matplotlib.pyplot

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df


stops = load_data("data/Officer_Traffic_Stops.csv")

age_hist = sbn.histplot(data = stops, x="Driver_Age", bins=20)

st.pyplot(age_hist.get_figure())