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
        for F in (Interface, Menu, LoginUser, LoginFun, Feed, FeedFun, MudarS, Postar, Suspender, Banir, Criar, Excluir):
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
        global sam
        sam = PhotoImage(file=r'mostra aqui nesse o que tu quer fazer, beleza.png')
        lus = tk.Label(self, image=lub)
        sd = tk.Frame(self)
        switch_window_button = tk.Button(
            lus,
            text="Ir ao Menu",
            font='Arial 50',
            command=lambda: controller.show_frame(Menu),
            bg='#001B40',
            activebackground='#570bba',
            foreground='White',
            activeforeground='#ff03e2',
            image=sam,
            relief=FLAT
        )
        lus.pack(fill=tk.X)
        switch_window_button.place(width=450, height=750, x=0, y=0)
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
            text="✦",
            font='Arial 50',
            foreground='#6102fa',
            command=lambda: controller.show_frame(LoginUser),
            bg='#FF0099',
            relief=FLAT,
            activeforeground='#b402fa'
        )
        switch_window_button2 = tk.Button(
            menur,
            text="✦",
            font='Arial 50',
            foreground='#6102fa',
            command=lambda: controller.show_frame(LoginFun),
            bg='#FF0099',
            relief=FLAT,
            activeforeground='#b402fa'
        )
        switch_window_button.place(width=90, height=87, x=52, y=391)
        switch_window_button2.place(width=90, height=87, x=286, y=391)
        menu.pack()


class LoginUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global musk
        musk= PhotoImage(file=r'login user.png')
        label = tk.Label(self, image=musk)
        label.pack()
        labelr = tk.Frame(self)
        switch_window_button = tk.Button(
            label, text="✦", command=lambda: controller.show_frame(Feed), bg='#001B40', relief=FLAT, foreground='#FF0099', font='Arial 30'
        )
        switch_window_button2 = tk.Button( label, text="•", command=lambda: controller.show_frame(Feed), bg='#001B40', relief=FLAT, foreground='#d572e0', font='Arial 30')
        switch_window_button2.place(width=39, height=19, x=204, y=509)
        switch_window_button.place(width=54, height=34, x=200, y=349)
        labelr.pack()

class LoginFun(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global muskr
        muskr= PhotoImage(file=r'login funcionario.png')
        label = tk.Label(self, image=muskr)
        label.pack()
        labelr = tk.Frame(self)
        switch_window_button = tk.Button(
            label, text="✧", command=lambda: controller.show_frame(FeedFun), font='Arial 30', background='#001B40', relief=FLAT, foreground='#FF0099'
        )
        switch_window_button.place(width=32, height=26, x=208, y=457)
        labelr.pack

class Feed(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global lii
        lii= PhotoImage(file=r'feed.png')
        label = tk.Label(self, image=lii)
        label.pack()
        labelr = tk.Frame(self)
        #post
        switch_window_button = tk.Button(
            label, text="•", command=lambda: controller.show_frame(Interface), font='Arial 25', foreground='#FF0099', bg='#001B40', relief=FLAT
        )
        #nuts
        switch_window_button2 = tk.Button(
            label, text="•", command=lambda: controller.show_frame(Interface), font='Arial 25', foreground='#FF0099', bg='#001B40', relief=FLAT
        )
        #config
        switch_window_button3 = tk.Button(
            label, text="•", command=lambda: controller.show_frame(Interface), font='Arial 25', foreground='#FF0099',
            bg='#001B40', relief=FLAT
        )
        #excluir
        switch_window_button4 = tk.Button(
            label, command=lambda: controller.show_frame(Interface), font='Arial 25',
            bg='#FF0099', relief=FLAT
        )
        #home
        switch_window_button5 = tk.Button(
            label, command=lambda: controller.show_frame(Menu), font='Arial 25',
            bg='black', relief=FLAT
        )
        #back
        switch_window_button6 = tk.Button(
            label, command=lambda: controller.show_frame(LoginUser), font='Arial 25',
            bg='#FF0099', relief=FLAT
        )
        switch_window_button.place(width=15, height=20, x=40, y=22)
        switch_window_button2.place(width=9, height=10, x=37, y=96)
        switch_window_button3.place(width=13, height=13, x=45, y=171)
        switch_window_button4.place(width=18, height=23, x=37, y=502)
        switch_window_button5.place(width=27, height=8, x=31, y=568)
        switch_window_button6.place(width=12, height=16, x=20, y=621)
        labelr.pack
        labelrs = tk.Label(self, bg='#ff57bc')
        labelrs.place(width=307, height=501, x=104, y=142)

class FeedFun(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liip
        liip= PhotoImage(file=r'feed adm.png')
        label = tk.Label(self, image=liip)
        label.pack()
        labelr = tk.Frame(self)
        #config
        switch_window_button = tk.Button(
            label, text="•", command=lambda: controller.show_frame(Interface), font='Arial 30', background='#001B40', relief=FLAT, foreground='#FF0099'
        )
        switch_window_button.place(width=13, height=13, x=36, y=175)
        #home
        switch_window_button2=tk.Button(
            label, text="•", command=lambda: controller.show_frame(Menu), font='Arial 30', background='black', relief=FLAT
        )
        switch_window_button2.place(width=20, height=11, x=37, y=560)
        #back
        switch_window_button3 = tk.Button(
            label, text="•", command=lambda: controller.show_frame(Menu), font='Arial 30', background='#FF0099',
            relief=FLAT
        )
        #suspender
        switch_window_button4 = tk.Button(
            label, command=lambda: controller.show_frame(Menu), font='Arial 30', background='#5E17EB',
            relief=FLAT
        )
        #banir
        switch_window_button5 = tk.Button(
            label, command=lambda: controller.show_frame(Menu), font='Arial 30', background='#5E17EB',
            relief=FLAT
        )
        switch_window_button5.place(width=8, height=10, x=39, y=52)
        switch_window_button4.place(width=7, height=11, x=32, y=120)
        switch_window_button2.place(width=20, height=11, x=37, y=560)
        switch_window_button3.place(width=9, height=15, x=24, y=614)
        labelr.pack

class MudarS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liip
        liip= PhotoImage(file=r'feed adm.png')
        label = tk.Label(self, image=liip)
        label.pack()
        labelr = tk.Frame(self)

class Banir(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liip
        liip= PhotoImage(file=r'feed adm.png')
        label = tk.Label(self, image=liip)
        label.pack()
        labelr = tk.Frame(self)

class Suspender(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liip
        liip= PhotoImage(file=r'feed adm.png')
        label = tk.Label(self, image=liip)
        label.pack()
        labelr = tk.Frame(self)

class Postar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liip
        liip= PhotoImage(file=r'feed adm.png')
        label = tk.Label(self, image=liip)
        label.pack()
        labelr = tk.Frame(self)

class Criar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liip
        liip= PhotoImage(file=r'feed adm.png')
        label = tk.Label(self, image=liip)
        label.pack()
        labelr = tk.Frame(self)

class Excluir(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liip
        liip= PhotoImage(file=r'feed adm.png')
        label = tk.Label(self, image=liip)
        label.pack()
        labelr = tk.Frame(self)

if __name__ == "__main__":
    root = Face()
    # verificar os pixels
    root.bind('<Button-1>', Poc.inicio_place)
    root.bind('<ButtonRelease-1>', lambda arg: Poc.fim_place(arg, root))
    root.bind('<Button-2>', lambda arg: Poc.para_geometry(root))
    root.mainloop()














