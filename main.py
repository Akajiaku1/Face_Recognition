"""
Simple Face Recognition Desktop App

This application provides a simple interface for user login, logout, and registration using face recognition. 
It uses libraries like dlib, OpenCV, and face_recognition to detect and recognize faces.

Dependencies:
- cmake==3.17.2
- dlib==19.18.0
- opencv-python==4.6.0.66
- Pillow==9.2.0
- face_recognition==1.3.0
"""

import os.path
import datetime
import pickle

import tkinter as tk
import cv2
from PIL import Image, ImageTk
import face_recognition

import util


# Main Window User Interface setup
class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")

        self.login_button_main_window = util.get_button(self.main_window, 'login', 'blue', self.login)
        self.login_button_main_window.place(x=750, y=200)

        self.logout_button_main_window = util.get_button(self.main_window, 'logout', 'red', self.logout)
        self.logout_button_main_window.place(x=750, y=300)

        self.register_new_user_button_main_window = util.get_button(self.main_window, 'register new user', 'gray',
                                                                    self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=750, y=400)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)

        self.db_dir = './db'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

        self.log_path = './log.txt'

# Accessing user webcam
    def add_webcam(self, label):
        for index in range(10):
            cap = cv2.VideoCapture(index)
            if cap.isOpened():
                self.cap = cap
                break
        else:
            raise Exception("No webcam found.")

        self._label = label
        self.process_webcam()

# Processing webcam image
    def process_webcam(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to capture image from webcam.")
            self._label.after(20, self.process_webcam)  # Retry after 20 ms
            return

        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)

# User login functionality
    def login(self):
        name = util.recognize(self.most_recent_capture_arr, self.db_dir)
        if name in ['unknown_person', 'no_persons_found']:
            util.msg_box('Ups...', 'Unknown user. Please register new user or try again.')
        else:
            util.msg_box('Welcome back!', 'Welcome, {}.'.format(name))
            with open(self.log_path, 'a') as f:
                f.write('{},{},in\n'.format(name, datetime.datetime.now()))

# User logout functionality
    def logout(self):
        name = util.recognize(self.most_recent_capture_arr, self.db_dir)
        if name in ['unknown_person', 'no_persons_found']:
            util.msg_box('Ups...', 'Unknown user. Please register new user or try again.')
        else:
            util.msg_box('Hasta la vista!', 'Goodbye, {}.'.format(name))
            with open(self.log_path, 'a') as f:
                f.write('{},{},out\n'.format(name, datetime.datetime.now()))

# Function to register new user
    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+370+120")

        self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Accept', 'green', self.accept_register_new_user)
        self.accept_button_register_new_user_window.place(x=750, y=300)

        self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Try again', 'red', self.try_again_register_new_user)
        self.try_again_button_register_new_user_window.place(x=750, y=400)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=150)

        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window, 'Please, \ninput username:')
        self.text_label_register_new_user.place(x=750, y=70)

# Closes window to reregister user if  failed.
    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

#Updates the Interface label with most recent capture
    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()

# This begins the main event loop for the application.
    def start(self):
        self.main_window.mainloop()

# Registers a new user by saving their face embeddings to a file.
    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0, "end-1c")

        embeddings = face_recognition.face_encodings(self.register_new_user_capture)[0]

        file_path = os.path.join(self.db_dir, '{}.pickle'.format(name))
        with open(file_path, 'wb') as file:
            pickle.dump(embeddings, file)

        util.msg_box('Success!', 'User was registered successfully!')

        self.register_new_user_window.destroy()


if __name__ == "__main__":
    app = App()
    app.start()
