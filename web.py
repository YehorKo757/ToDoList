import streamlit as st
import modules.functions

todos = modules.functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"]
    todos.append(todo_local + "\n")
    modules.functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        modules.functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add a new todo: ",
              placeholder="Add a new todo...",
              label_visibility="collapsed",
              on_change=add_todo,
              key="new_todo")
