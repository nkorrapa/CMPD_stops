import streamlit as st
import pandas as pd

st.write("CMPD Traffic Stops")
st.write("Katherine Davis was here")

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df


stops = load_data("data/Officer_Traffic_Stops.csv")

st.write("CMPD Traffic Stops")

st.dataframe(stops)