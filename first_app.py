import streamlit as st
import os

st.title('My first streamlit app ever!')

st.write('Welcome to my streamlit application LITERALLY!')

st.button("Reset", type="primary")
if st.button("Say Hola!"):
  st.write("Hola!")
else:
  st.write("Tata!")