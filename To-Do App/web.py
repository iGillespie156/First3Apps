import streamlit as st
import Functions as fun

todos = fun.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is designed to increase your productivity")

st.checkbox("Buy grocery")
st.checkbox("Throw the trash")


for i in todos:
    st.checkbox(i)

st.text_input(label="", placeholder="Add new todo...")