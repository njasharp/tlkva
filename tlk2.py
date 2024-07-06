import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
import webbrowser

def listen_for_command():
    # Replacing actual microphone input with text input for Streamlit Cloud compatibility
    st.sidebar.write("Listening for commands...")
    command = st.text_input("Type command (for demo, as microphone input isn't supported)", key="command_input")
    if command:
        st.write("You said:", command)
        respond(command)
        return command.lower()
    else:
        return None

def respond(response_text):
    st.write(response_text)
    tts = gTTS(text=response_text, lang='en')
    tts.save("response.mp3")
    sound = AudioSegment.from_mp3("response.mp3")
    sound.export("response.wav", format="wav")
    st.audio("response.wav")  # Using Streamlit's audio player instead of winsound

def new():
    st.write("Adding a new task")
    new_task = st.text_area("Type new task")
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

    respond("Listening")
    st.image("face.png", width=image_width)
    st.title("Virtual Assistant Voice Control")
    
    st.sidebar.title("Brian C - wakeup word 'ready'")
    st.sidebar.write("Interact with the assistant using the buttons below.")
    st.sidebar.write("Options: ready, add task, list tasks, screenshot, open youtube, exit")

    if st.sidebar.button("Press to Speak", key="speak_button"):
        command = listen_for_command()
        triggerKeyword = "ready"
        
        if command and triggerKeyword in command:
            if listeningToTask:
                tasks.append(command)
                listeningToTask = False
                respond(f"Adding '{command}' to your task list. You have {len(tasks)} currently in your list.")
            elif "add task" in command:
                listeningToTask = True
                respond("Sure, what is the task?")
                new()
            elif "list tasks" in command:
                respond("Sure. Your tasks are:")
                for task in tasks:
                    respond(task)
            elif "screenshot" in command:
                respond("Screenshot feature is not supported on Streamlit Cloud.")
            elif "open youtube" in command:
                respond("Opening YouTube.")
                webbrowser.open("http://www.youtube.com/")
            elif "exit" in command:
                respond("Goodbye!")
                return
            elif "ready" in command:
                respond("I am awake - ready now")
                return
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