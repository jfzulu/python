import os
from tkinter import Tk, Text, Button, END, Label
from gtts import gTTS


def save_text():
    text= text_area.get("1.0", END)
    with open('user_input.txt', 'w', encoding='utf-8') as file:
        file.write(text)
    status_label.config(text="Text saved successfully")

def text_to_speech():
    text = text_area.get("1.0", END)
    speech = gTTS(text=text, lang='es', slow=False)
    speech.save('outputFinal.mp3')
    os.system('start outputFinal.mp3')
    status_label.config(text='Playing audio...')

# Create main window
root = Tk()
root.title("Text to Voice")

text_area = Text(root, height=10, width=50)
text_area.pack()

save_button=Button(root, text="Save Text", command=save_text)
save_button.pack()

play_button=Button(root, text="Play Text", command=text_to_speech)
play_button.pack()

status_label= Label(root, text="", fg='green')
status_label.pack()

root.mainloop()
