import streamlit as st

st.title('Unit Converter')

col1, col2, col3 = st.columns(3)

with col2:
    feet = st.number_input(label='Enter a value')
    st.write()

with col1:
    st.write(f'{feet} is equivalent to {feet * 0.305}')

