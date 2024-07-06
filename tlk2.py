import streamlit as st
import base64
import requests

def listen_for_command():
    command = st.text_input("Enter your command:")
    if command:
        st.write("You entered:", command)
        respond(command)
        return command.lower()
    return None

def respond(response_text):
    st.write(response_text)
    # Text-to-speech functionality is removed as it's not supported on Streamlit Cloud

def new():
    st.write("Adding new task")
    new_task = st.text_input("Type new task")
    if new_task:
        moretasks.append(new_task)
        st.success(f"Added '{new_task}' to your task list.")

tasks = ["work"]
listeningToTask = False
image_width = 120 
moretasks = []

def main():
    global tasks
    global listeningToTask
    global moretasks

    st.title("Virtual Assistant")
    
    # Display a placeholder image
    st.image("face.png", width=image_width)
    
    st.sidebar.title("Brian C- wakeup word 'ready'")
    st.sidebar.write("Interact with the assistant using the text input below.")
    st.sidebar.write("options: ready")
    st.sidebar.write("add task, list tasks, open youtube, exit")

    command = listen_for_command()
    triggerKeyword = "ready"
    
    if command:
        if listeningToTask:
            tasks.append(command)
            listeningToTask = False
            respond(f"Adding {command} to your task list. You have {len(tasks)} currently in your list.")
        elif "add task" in command:
            listeningToTask = True
            respond("Sure, what is the task?")
            new()
        elif "list tasks" in command:
            respond("Sure. Your tasks are:")
            for task in tasks:
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
    for task in tasks:
        st.sidebar.write("- " + task)
    
    st.sidebar.write("More Tasks:")
    for moretask in moretasks:
        st.sidebar.write("- " + moretask)

if __name__ == "__main__":
    main()