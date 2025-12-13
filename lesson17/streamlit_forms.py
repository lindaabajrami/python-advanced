import streamlit as st

with st.form("my_form", clear_on_submit=True):
    name = st.text_input('name')
    age = st.slider('age', min_value=0, max_value=100)
    email = st.text_area('short bio')
    terms = st.checkbox('i agree to the terms and conditions')

    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f'name: {name}')
    st.write(f'age:{age}')
    st.write(f'email: {email}')
    st.write(f'short bio: {biography}')

    if terms:
        st.write("you agreed to the terms and conditions")
    else:
        st.write("you did not agreee to the terms and conditions")
