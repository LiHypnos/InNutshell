from class_face import *
from tkinter import *
import tkinter as ttk

class Format:

    def format_limit(event=None):
        text = Entry.get().replace(".", "").replace("-", "")[:11]
        new_text = ""

        if event.keysym.lower() == "backspace": return

        for index in range(len(text)):

            if not text[index] in "0123456789": continue
            if index in [2, 5]:
                new_text += text[index] + "."
            elif index == 8:
                new_text += text[index] + "-"
            else:
                new_text += text[index]

        Entry.delete(0, "end")
        Entry.insert(0, new_text)

    def format_data(event=None):
        text = Entry.get().replace("/", "")[:8]
        new_text = ""

        if event.keysym.lower() == "backspace": return

        for index in range(len(text)):

            if not text[index] in "0123456789": continue
            if index in [1, 3]:
                new_text += text[index] + "/"
            else:
                new_text += text[index]

        Entry.delete(0, "end")
        Entry.insert(0, new_text)
