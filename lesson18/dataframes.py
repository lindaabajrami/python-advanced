import pandas as pd
import  streamlit as st

st.header("display dataframes")

data = pd.DataFrame({
    'Name':['alice', 'bob', 'charlie', 'david', 'eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['new  york', 'los angelos', 'chicago', 'houston', 'phoenix']

})

st.dataframe(data)
