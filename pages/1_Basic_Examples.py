
import streamlit as st
import pandas as pd
import numpy as np
import time
from streamlit import  session_state

if 'solution' not in session_state.keys():
    session_state['solution'] = None

@st.cache(suppress_st_warning=True, show_spinner=False)
def helloCimputation(a, b):
    st.write("Cache Missed")
    time.sleep(2)
    return a*b

num1 = st.number_input("Enter Your Number", min_value=1)
num2 = st.number_input("Enter Your Number2",min_value=1)
solButton = st.button("Find Solution")
if solButton:
    res = helloCimputation(num1, num2)
    session_state['solution'] = res
    st.write(res)







