import streamlit as st
import base64

def content():
    st.title('Contact me')
    left_column, right_column = st.beta_columns(2)
    left_column.write('Phone: +33 6 85 14 36 13')
    left_column.write('Email: luther.ollier@locean.ipsl.fr')
    right_column.write('[LinkedIn](https://linkedin.com/in/luther-ollier)')
    right_column.write('[Github](https://github.com/Sma6500)')
