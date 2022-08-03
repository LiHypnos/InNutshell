# import some files right there:
# _______________________________________________________________________________________________________________________
import Posicionamento
from tkinter import *
import tkinter as tk
# from tkcalendar import *
# _______________________________________________________________________________________________________________________
from Posicionamento import *


# _______________________________________________________________________________________________________________________
def menu():
    Interface.forget()
    Menu.pack()


class Face(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Shell")

        # creating a frame and assigning it to container
        f0 = tk.Frame(self, bg='Black', border=0)
        # specifying the region where the frame is packed in root
        f0.pack(expand=False)

        self.minsize(width=450, height=750)
        self.maxsize(width=450, height=750)

        # configuring the location of the container using grid
        f0.grid_rowconfigure(0, weight=1)
        f0.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (Interface, Menu, LoginUser):
            frame = F(f0, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(Interface)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


class Interface(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global interfacer
        interfacer = PhotoImage(file=r'1.png')
        labelInter = tk.Label(self, image=interfacer)
        labelInter.after(3000, labelInter.forget)
        labelInter.pack()

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        lub = PhotoImage(file=r'2.png')
        sam = PhotoImage(file=r'mostra aqui nesse o que tu quer fazer, beleza.png')
        lus = tk.Label(self, image=lub)
        sd = tk.Frame(self)
        switch_window_button = tk.Button(
            lus,
            text="Ir ao Menu",
            command=lambda: controller.show_frame(Menu)
        )

        lus.pack(fill=tk.X)
        switch_window_button.place(width=90, height=87, x=52, y=391)
        sd.pack()


class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global men
        men = PhotoImage(file=r'3.png')
        menur = tk.Label(self, image=men)
        menur.pack()
        menu = tk.Frame(self)

        switch_window_button = tk.Button(
            menur,
            text="Star",
            command=lambda: controller.show_frame(LoginUser),
            bg='#FF0099',
            relief=FLAT
        )
        switch_window_button.place(width=90, height=87, x=52, y=391)
        menu.pack()


class LoginUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        musk= PhotoImage(file=r'login user.png')
        label = tk.Label(self, image=musk)
        label.pack()
        labelr = tk.Frame(self)
        switch_window_button = tk.Button(
            label, text="Return to menu", command=lambda: controller.show_frame(Interface)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)
        labelr.pack


if __name__ == "__main__":
    root = Face()
    # verificar os pixels
    root.bind('<Button-1>', Poc.inicio_place)
    root.bind('<ButtonRelease-1>', lambda arg: Poc.fim_place(arg, root))
    root.bind('<Button-2>', lambda arg: Poc.para_geometry(root))
    root.mainloop()














