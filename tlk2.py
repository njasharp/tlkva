import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
from io import BytesIO

def respond(response_text):
    st.write(response_text)

def new_task():
    st.write("Adding new task")
    new_task = st.text_area("Type new task", key="new_task_input")
    if new_task:
        st.session_state.moretasks.append(new_task)
        st.success(f"Added '{new_task}' to your task list.")

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp

def main():
    st.set_page_config(page_title="Virtual Assistant", page_icon="🤖")
    
    if 'tasks' not in st.session_state:
        st.session_state.tasks = ["work"]
    if 'listeningToTask' not in st.session_state:
        st.session_state.listeningToTask = False
    if 'moretasks' not in st.session_state:
        st.session_state.moretasks = []
    if 'audio_files' not in st.session_state:
        st.session_state.audio_files = []

    st.title("Virtual Assistant")

    img_path = "face.PNG"  # Correct the path to the uploaded image
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
            response_text = f"Adding {command} to your task list. You have {len(st.session_state.tasks)} tasks currently in your list."
            respond(response_text)
            audio_fp = text_to_speech(response_text)
            st.session_state.audio_files.append(audio_fp)
        elif "add task" in command:
            st.session_state.listeningToTask = True
            respond("Sure, what is the task?")
            new_task()
        elif "list tasks" in command:
            response_text = "Sure. Your tasks are:"
            respond(response_text)
            audio_fp = text_to_speech(response_text)
            st.session_state.audio_files.append(audio_fp)
            for task in st.session_state.tasks:
                respond(task)
                audio_fp = text_to_speech(task)
                st.session_state.audio_files.append(audio_fp)
        elif "open youtube" in command:
            response_text = "Opening YouTube."
            respond(response_text)
            st.markdown("[Click here to open YouTube](https://www.youtube.com/)")
            audio_fp = text_to_speech(response_text)
            st.session_state.audio_files.append(audio_fp)
        elif "exit" in command:
            response_text = "Goodbye!"
            respond(response_text)
            audio_fp = text_to_speech(response_text)
            st.session_state.audio_files.append(audio_fp)
            st.stop()
        elif "ready" in command:
            response_text = "I am awake - ready now"
            respond(response_text)
            audio_fp = text_to_speech(response_text)
            st.session_state.audio_files.append(audio_fp)
        else:
            response_text = "Sorry, I'm not sure how to handle that command, try again."
            respond(response_text)
            audio_fp = text_to_speech(response_text)
            st.session_state.audio_files.append(audio_fp)
    
    st.sidebar.write("Tasks:")
    for task in st.session_state.tasks:
        st.sidebar.write("- " + task)
    
    st.sidebar.write("More Tasks:")
    for moretask in st.session_state.moretasks:
        st.sidebar.write("- " + moretask)

    st.sidebar.write("Audio Responses:")
    for i, audio_fp in enumerate(st.session_state.audio_files):
        st.sidebar.audio(audio_fp, format="audio/wav", start_time=0)

if __name__ == "__main__":
    main()