import streamlit as st

tab1, tab2, tab3 = st.tabs(['tab1', 'tab2', 'tab3'])

with tab1:
    st.header("content for tab 1")
    st.write("this is the content of the first tab")

with tab2:
    st.header("content for tab 2")
    st.write("this is the content of the second tab")

with tab3:
    st.header("content for tab 3")
    st.write("this is the content of the third tab")
