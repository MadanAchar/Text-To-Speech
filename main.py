import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

# Initialize main window
root = Tk()
root.title("Text To Speech")
root.geometry("900x450+300+300")
root.resizable(False, False)
root.configure(bg="#043FCD")

# Initialize pyttsx3 engine
engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    # Corrected property name to 'voices'
    voices = engine.getProperty('voices')  

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
        
    # Only speak if there is non-whitespace text
    if text.strip():
        if speed == "Fast":
            engine.setProperty('rate', 250)
        elif speed == "Normal":
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        setvoice()

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')  # Use lowercase

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        path = filedialog.askdirectory()
        if path:  # Ensure a directory was selected
            file_path = os.path.join(path, 'text.mp3')
            engine.save_to_file(text, file_path)
            engine.runAndWait()
            
    if text.strip():
        if speed == "Fast":
            engine.setProperty('rate', 250)
        elif speed == "Normal":
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        setvoice()

# Set icon for the window
image_icon = PhotoImage(file="Icons/icon.png")
root.iconphoto(False, image_icon)

# Top frame with title and logo
Top_frame = Frame(root, bg="#DAF9E4", width=900, height=120)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="Icons/icon2.png")
Label(Top_frame, image=Logo, bg="#DAF9E4").place(x=10, y=5)

Label(Top_frame, text="TEXT TO SPEECH", font="impact 36", bg="#DAF9E4", fg="#043FCD").place(x=120, y=30)

# Text area widget for input
text_area = Text(root, font="Roboto 20", bg="White", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

# Labels for comboboxes
Label(root, text="VOICE", font="arial 15 bold", bg="#043FCD",fg="#DAF9E4").place(x=580, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#043FCD",fg="#DAF9E4").place(x=760, y=160)

# Combobox for selecting gender
gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='readonly', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

# Combobox for selecting speed
speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='readonly', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

# Speak button with icon
imageicon = PhotoImage(file="Icons/icons8-talk-40.png")
btn = Button(root, text="SPEAK", compound=LEFT, image=imageicon, width=130, font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280)

# Save button with icon
imageicon2 = PhotoImage(file="Icons/icons8-download-40.png")
save = Button(root, text="SAVE", compound=LEFT, image=imageicon2, width=130, font="arial 14 bold", command=download)
save.place(x=730, y=280)

# Start the main event loop
root.mainloop()
