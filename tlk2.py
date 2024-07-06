import streamlit as st
import requests
from PIL import Image
from io import BytesIO

def listen_for_command():
    command = st.text_input("Enter your command:")
    if command:
        st.write("You entered:", command)
        respond(command)
        return command.lower()
    return None

def respond(response_text):
    st.write(response_text)

def new():
    st.write("Adding new task")
    new_task = st.text_input("Type new task")
    if new_task:
        st.session_state.moretasks.append(new_task)
        st.success(f"Added '{new_task}' to your task list.")

def main():
    st.set_page_config(page_title="Virtual Assistant", page_icon="🤖")
    
    if 'tasks' not in st.session_state:
        st.session_state.tasks = ["work"]
    if 'listeningToTask' not in st.session_state:
        st.session_state.listeningToTask = False
    if 'moretasks' not in st.session_state:
        st.session_state.moretasks = []

    st.title("Virtual Assistant")
    
    # Display a placeholder image
    
    img = "face.png"
    st.image(img, width=120)
    
    st.sidebar.title("Brian C- wakeup word 'ready'")
    st.sidebar.write("Interact with the assistant using the text input below.")
    st.sidebar.write("options: ready")
    st.sidebar.write("add task, list tasks, open youtube, exit")

    command = listen_for_command()
    triggerKeyword = "ready"
    
    if command:
        if st.session_state.listeningToTask:
            st.session_state.tasks.append(command)
            st.session_state.listeningToTask = False
            respond(f"Adding {command} to your task list. You have {len(st.session_state.tasks)} currently in your list.")
        elif "add task" in command:
            st.session_state.listeningToTask = True
            respond("Sure, what is the task?")
            new()
        elif "list tasks" in command:
            respond("Sure. Your tasks are:")
            for task in st.session_state.tasks:
                respond(task)
        elif "open youtube" in command:
            respond("Opening YouTube.")
            st.markdown("[Click here to open YouTube](https://www.youtube.com/)")
        elif "exit" in command:
            respond("Goodbye!")
            st.stop()
        elif "ready" in command:
            respond("I am awake - ready now")
        else:
            respond("Sorry, I'm not sure how to handle that command, try again.")
    
    st.sidebar.write("Tasks:")
    for task in st.session_state.tasks:
        st.sidebar.write("- " + task)
    
    st.sidebar.write("More Tasks:")
    for moretask in st.session_state.moretasks:
        st.sidebar.write("- " + moretask)

if __name__ == "__main__":
    main()