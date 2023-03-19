import streamlit as st

st.title('Unit Converter')

col1, col2 = st.columns(2)

with col2:
    feet = st.number_input(label='Enter a value')
    st.write()

with col1:
    st.write(f'{feet} is equivalent to {feet * 0.305}')

