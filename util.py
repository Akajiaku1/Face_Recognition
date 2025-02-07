"""
UTILITIES FOR MAIN FACIAL RECOGNITION APPLICATION
"""

import os
import pickle

import tkinter as tk
from tkinter import messagebox
import face_recognition


# Create a button with specified properties and return it
def get_button(window, text, color, command, fg='white'):
    button = tk.Button(
        window,
        text=text,
        activebackground="black",
        activeforeground="white",
        fg=fg,
        bg=color,
        command=command,
        height=2,
        width=20,
        font=('Helvetica bold', 20)
    )
    return button


# Create a label for displaying images and return it
def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label


# Create a text label with specified text and return it
def get_text_label(window, text):
    label = tk.Label(window, text=text)
    label.config(font=("sans-serif", 21), justify="left")
    return label


# Create a text entry field and return it
def get_entry_text(window):
    inputtxt = tk.Text(window, height=2, width=15, font=("Arial", 32))
    return inputtxt


# Display a message box with a title and description
def msg_box(title, description):
    messagebox.showinfo(title, description)


# Recognize a face from the provided image using the database at db_path
def recognize(img, db_path):
    # Extract face embeddings from the given image
    embeddings_unknown = face_recognition.face_encodings(img)
    
    # If no face is found in the image, return 'no_persons_found'
    if len(embeddings_unknown) == 0:
        return 'no_persons_found'
    else:
        embeddings_unknown = embeddings_unknown[0]

    # List all files in the database directory
    db_dir = sorted(os.listdir(db_path))

    match = False
    j = 0

    # Iterate through the database files to find a match
    while not match and j < len(db_dir):
        path_ = os.path.join(db_path, db_dir[j])

        # Load the embeddings from the current database file
        file = open(path_, 'rb')
        embeddings = pickle.load(file)

        # Compare the current embeddings with the unknown face embeddings
        match = face_recognition.compare_faces([embeddings], embeddings_unknown)[0]
        j += 1

    # If a match is found, return the username (file name without extension)
    if match:
        return db_dir[j - 1][:-7]
    else:
        return 'unknown_person'
