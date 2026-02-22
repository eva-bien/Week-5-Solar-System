import tkinter as tk
import os
from solar_system import Question, planets

# To set up this GUI, I have used the following articles:
# https://www.geeksforgeeks.org/python/how-to-bind-the-enter-key-to-a-tkinter-window/
# https://www.geeksforgeeks.org/python/changing-the-mouse-cursor-tkinter/
# https://www.geeksforgeeks.org/python/python-add-style-to-tkinter-button/
# https://www.geeksforgeeks.org/python/how-to-change-the-tkinter-label-text/
# https://www.geeksforgeeks.org/python/how-to-use-images-as-backgrounds-in-tkinter/

def ask_question():
    user_question = question_area.get("1.0", "end-1c")
    question = Question(user_question, planets)
    answer.config(text = question.answer())
    
def clearQuestion():
    question_area.delete("1.0", "end-1c")

root = tk.Tk()
root.title("Cosmos")
root.geometry("900x550")  
# Opens in full screen
root.attributes("-fullscreen", True)

# Background file directory
BASE_DIR = os.path.dirname(__file__)
image_path = os.path.join(BASE_DIR, "images", "background.png")
background = tk.PhotoImage(file=image_path)

# Canvas background
canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)

bg_image = canvas.create_image(0, 0, image=background, anchor="nw")

# Resize background with window
def resize_bg(event):
    canvas.config(width=event.width, height=event.height)
    canvas.coords(bg_image, 0, 0)

canvas.bind("<Configure>", resize_bg)

# Center container frame
content = tk.Frame(root, bg="#ffffff", bd=2, relief="ridge")
content_window = canvas.create_window(0, 0, window=content)

def center_content(event):
    canvas.coords(content_window, event.width/2, event.height/2)

canvas.bind("<Configure>", center_content)

# Widgets inside frame 
label = tk.Label(
    content,
    text="Hello, my name is Cosmos 🌝 - I am the Solar System Master.\nUse the form below to ask me a question.",
    font=("Segoe UI", 18, "bold"),
    bg="white",
    justify="center"
)
label.pack(padx=20, pady=(20, 15))

# Answer area
answer = tk.Label(
    content,
    text="",
    font=("Segoe UI", 14),
    bg="white",
    justify="center",
    wraplength=500
)
answer.pack(padx=20, pady=(20, 15))

# Question label
question_label = tk.Label(content, text="Your Question", bg="white") 
question_label.pack(anchor="w", padx=20, pady=10)

# Question text area
question_area = tk.Text(content, height=6, bd=2, relief="sunken", highlightthickness=1, highlightbackground="#999")
question_area.pack(padx=20, pady=10)

# Ask button
ask_button = tk.Button(content, text="Ask", width=25, command=ask_question, foreground = "purple", font=("Segoe UI", 16, "bold"), cursor="star")
ask_button.pack(pady=(5, 20))

# Clear button
clear_button = tk.Button(content, text="Clear", width=25, command=clearQuestion, font=("Segoe UI", 16, "bold"))
clear_button.pack(pady=(5, 20))

# Exit button
exit_button = tk.Button(content, text="Exit", width=25, command=root.destroy, foreground = "red", font=("Segoe UI", 16, "bold"))
exit_button.pack(pady=(5, 20))

# Author blurb
author = tk.Label(
    content,
    text="By Ewa Bienasz",
    font=("Segoe UI", 14),
    bg="white",
    justify="center"
)
author.pack(padx=20, pady=(20, 15))

root.mainloop()