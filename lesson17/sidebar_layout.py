import  streamlit as st

st.sidebar.header("sidebar")

st.sidebar.write("this is the sidebar ")

st.sidebar.selectbox("chose an option", ["option 1, option 2, option3, "])

st.sidebar.radio("go to", ["home", "data", "settings"])
