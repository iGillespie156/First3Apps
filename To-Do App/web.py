import streamlit as st
import Functions as fun

todos = fun.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    fun.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is designed to increase your productivity")



for i in todos:
    st.checkbox(i)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

st.session_state
