import streamlit as st

def respond(response_text):
    st.write(response_text)

def new_task():
    st.write("Adding new task")
    new_task = st.text_area("Type new task", key="new_task_input")
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

    img_path = "face.png"  # Correct the path to the uploaded image
    try:
        st.image(img_path, width=120)
    except FileNotFoundError:
        st.warning("Image not found. Please check the path or upload the image.")
    
    st.sidebar.title("Brian C - wakeup word 'ready'")
    st.sidebar.write("Interact with the assistant using the text input below.")
    st.sidebar.write("Options: ready, add task, list tasks, open youtube, exit")

    command = st.text_input("Enter your command (or type 'ready' to wake up):")
    triggerKeyword = "ready"
    
    if command:
        if st.session_state.listeningToTask:
            st.session_state.tasks.append(command)
            st.session_state.listeningToTask = False
            respond(f"Adding {command} to your task list. You have {len(st.session_state.tasks)} tasks currently in your list.")
        elif "add task" in command:
            st.session_state.listeningToTask = True
            respond("Sure, what is the task?")
            new_task()
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
