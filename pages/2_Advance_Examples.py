import streamlit as st
from streamlit import  session_state

st.subheader("The result is : "+str(session_state['solution']))