import streamlit as st
import streamlit.components.v1 as components
st.title("Welcome to PyData MeetUP - Dubai ")
st.video('https://www.youtube.com/watch?v=J8cVPXnafos')

st.title("Welcome to Streamlit Session")
components.html("""
<div align="right">
<table>
<tr>
<th>Speaker</th>
<td>Javalingappa(Java)</td>
</tr>
<tr>
<th>Contact</th>
<td>Javaindubai@gmail.com</td>
</tr>
<tr>
<td colspan="2">Senior Developer</td>
</tr>
</table>
</div>
""", height=200)

myDate = None
with st.sidebar:
    st.subheader("Welcome")
    myDate = st.date_input("Select Your Date")

if myDate:
    st.write("The selected Date "+str(myDate))
