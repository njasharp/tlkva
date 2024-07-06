import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import winsound
from pydub import AudioSegment
import pyautogui
import webbrowser

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.sidebar.write("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        st.write("You said:", command)
        respond(command)
        return command.lower()
    except sr.UnknownValueError:
        st.write("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        st.write("Unable to access the Speech Recognition API.")
        return None

def respond(response_text):
    st.write(response_text)
    tts = gTTS(text=response_text, lang='en')
    tts.save("response.mp3")
    sound = AudioSegment.from_mp3("response.mp3")
    sound.export("response.wav", format="wav")
    winsound.PlaySound("response.wav", winsound.SND_FILENAME)
    
def new():
    st.write("adding")
    new_task = st.text_area("Type new task")
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

    respond("listening")
    st.image("face.png", width=image_width)
    st.title("Virtual Assistant voice control")
    
    st.sidebar.title("Brian C- wakeup word 'ready'")
    st.sidebar.write("Interact with the assistant using the buttons below.")
    st.sidebar.write("options: ready")
    st.sidebar.write("add task, list tasks, screenshot, open youtube, exit")
    if st.sidebar.button("press to speak"):
        command = listen_for_command()
        triggerKeyword = "ready"
        
        if command or triggerKeyword in command:
            if listeningToTask:
                tasks.append(command)
                listeningToTask = False
                respond("Adding " + command + " to your task list. You have " + str(len(tasks)) + " currently in your list.")
            elif "add task" in command:
                listeningToTask = True
                respond("Sure, what is the task?")
                new()
            elif "list tasks" in command:
                respond("Sure. Your tasks are:")
                for task in tasks:
                    respond(task)
            elif "screenshot" in command:
                pyautogui.screenshot("screenshot.png")
                respond("I took a screenshot for you.")
                st.image("screenshot.png")
            elif "open youtube" in command:
                respond("Opening youtube.")
                webbrowser.open("http://www.youtube.com/")
            elif "exit" in command:
                respond("Goodbye!")
                return
            elif "ready" in command:
                respond("i am awake - ready now")
                return
            else:
                respond("Sorry, I'm not sure how to handle that command, try again.")
    
    st.sidebar.write("Tasks:")
    for task in tasks:
        st.sidebar.write("- " + task)
    
    st.sidebar.write(" more Tasks:")
    for moretask in moretasks:
        st.sidebar.write("- " + moretask)

if __name__ == "__main__":
    main()