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
        for F in (Interface, Menu, LoginUser, LoginFun, Feed, FeedFun, MudarS, Postar, Suspender, Banir, Criar, Excluir, Nuts):
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

#_________________________________________________________________________
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
#_________________________________________________________________________
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
#_________________________________________________________________________
class LoginUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global musk
        musk= PhotoImage(file=r'login user.png')
        label = tk.Label(self, image=musk)
        label.pack()
        labelr = tk.Frame(self)
        lub= tk.Entry(self, bg='#FF0099', foreground='White', font='Arial 20', relief=FLAT)
        lix= tk.Entry(self,bg='#FF0099', foreground='White', font='Arial 18', relief=FLAT)
        switch_window_button = tk.Button(
            label, text="✦", command=lambda: controller.show_frame(Feed), bg='#001B40', relief=FLAT, foreground='#FF0099', font='Arial 30'
        )
        switch_window_button2 = tk.Button( label, text="•", command=lambda: controller.show_frame(Criar), bg='#001B40', relief=FLAT, foreground='#d572e0', font='Arial 30')
        switch_window_button2.place(width=39, height=19, x=204, y=509)
        switch_window_button.place(width=54, height=34, x=200, y=349)
        labelr.pack()
        lub.place(width=237, height=24, x=167, y=216)
        lix.place(width=213, height=26, x=207, y=291)
#_________________________________________________________________________
class LoginFun(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global muskr
        muskr= PhotoImage(file=r'login funcionario.png')
        label = tk.Label(self, image=muskr)
        label.pack()
        userF= tk.Entry(self, bg='#FF0099', foreground='White', font='Arial 20', relief=FLAT)
        userS= tk.Entry(self, bg='#FF0099', foreground='White', font='Arial 20', relief=FLAT)
        labelr = tk.Frame(self)
        switch_window_button = tk.Button(
            label, text="✧", command=lambda: controller.show_frame(FeedFun), font='Arial 30', background='#001B40', relief=FLAT, foreground='#FF0099'
        )
        switch_window_button.place(width=32, height=26, x=208, y=457)
        labelr.pack
        userF.place(width=232, height=23, x=174, y=263)
        userS.place(width=214, height=25, x=203, y=335)
#_________________________________________________________________________
class Feed(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global lii
        lii= PhotoImage(file=r'feed.png')
        label = tk.Label(self, image=lii)
        label.pack()
        labelr = tk.Frame(self)
        nomer= tk.Label(self, bg='#001B40',foreground='#FF0099', font='Arial 20')
        datar= tk.Label(self, bg='#001B40',foreground='#FF0099', font='Arial 20')
        #post
        switch_window_button = tk.Button(
            label, text="•", command=lambda: controller.show_frame(Postar), font='Arial 25', foreground='#FF0099', bg='#001B40', relief=FLAT
        )
        #nuts
        switch_window_button2 = tk.Button(
            label, text="•", command=lambda: controller.show_frame(Nuts), font='Arial 25', foreground='#FF0099', bg='#001B40', relief=FLAT
        )
        #config
        switch_window_button3 = tk.Button(
            label, text="•", command=lambda: controller.show_frame(MudarS), font='Arial 25', foreground='#FF0099',
            bg='#001B40', relief=FLAT
        )
        #excluir
        switch_window_button4 = tk.Button(
            label, command=lambda: controller.show_frame(Excluir), font='Arial 25',
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
        nomer.place(width=259, height=31, x=106, y=20)
        datar.place(width=92, height=19, x=208, y=83)
        labelr.pack
        labelrs = tk.Label(self, bg='#ff57bc')
        labelrs.place(width=307, height=501, x=104, y=142)
#_________________________________________________________________________
class FeedFun(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liip
        liip= PhotoImage(file=r'feed adm.png')
        label = tk.Label(self, image=liip)
        label.pack()
        labelr = tk.Frame(self)

        #home
        switch_window_button2=tk.Button(
            label, text="•", command=lambda: controller.show_frame(Interface), font='Arial 30', background='black', relief=FLAT
        )
        switch_window_button2.place(width=20, height=11, x=37, y=560)
        #back
        switch_window_button3 = tk.Button(
            label, text="•", command=lambda: controller.show_frame(Menu), font='Arial 30', background='#FF0099',
            relief=FLAT
        )
        #suspender
        switch_window_button4 = tk.Button(
            label, command=lambda: controller.show_frame(Suspender), font='Arial 30', background='#5E17EB',
            relief=FLAT
        )
        #banir
        switch_window_button5 = tk.Button(
            label, command=lambda: controller.show_frame(Banir), font='Arial 30', background='#5E17EB',
            relief=FLAT
        )
        switch_window_button5.place(width=8, height=10, x=39, y=52)
        switch_window_button4.place(width=7, height=11, x=32, y=120)
        switch_window_button2.place(width=20, height=11, x=37, y=560)
        switch_window_button3.place(width=9, height=15, x=24, y=614)
        nomeF = tk.Label(self, bg='#001B40', foreground='#FF0099', font='Arial 20')
        datar = tk.Label(self, bg='#001B40', foreground='#FF0099', font='Arial 20')
        nomeF.place(width=259, height=31, x=106, y=20)
        datar.place(width=92, height=19, x=208, y=83)
        labelr.pack
#_________________________________________________________________________
class MudarS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liippp
        liippp= PhotoImage(file=r'mudar senha_nome.png')
        label = tk.Label(self, image=liippp)
        label.pack()
        labelr = tk.Frame(self)
        nomer = tk.Label(self, bg='#001B40', foreground='#FF0099', font='Arial 20')
        datar = tk.Label(self, bg='#001B40', foreground='#FF0099', font='Arial 20')
        nomer.place(width=259, height=31, x=106, y=20)
        datar.place(width=92, height=19, x=208, y=83)
        newname= tk.Entry(self, bg='#FF0099', relief=FLAT, foreground='WHITE')
        newpass= tk.Entry(self, bg='#FF0099', relief=FLAT, foreground='WHITE')
        confirmpass = tk.Entry(self, bg='#FF0099', relief=FLAT, foreground='WHITE')
        newname.place(width=228, height=24, x=110, y=428)
        newpass.place(width=235, height=26, x=160, y=217)
        confirmpass.place(width=227, height=27, x=167, y=286)
        confirmB= tk.Button(self, text='C', font='Arial 20', bg='#FF0099', foreground='White', relief=FLAT)
        confirmB.place(width=29, height=19, x=288, y=511)

        switch_window_button = tk.Button(
            label, command=lambda: controller.show_frame(Menu), font='Arial 30', background='Black',
            relief=FLAT
        )
        switch_window_button1 = tk.Button(
            label, command=lambda: controller.show_frame(Feed), font='Arial 30', background='Black',
            relief=FLAT
        )
        switch_window_button.place(width=15, height=8, x=37, y=566)
        switch_window_button1.place(width=7, height=9, x=25, y=626)
#_________________________________________________________________________
class Banir(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liipxp
        liipxp= PhotoImage(file=r'ban.png')
        label = tk.Label(self, image=liipxp)
        label.pack()
        labelr = tk.Frame(self)
        nomeF = tk.Label(self, bg='#001B40', foreground='#FF0099', font='Arial 20')
        datar = tk.Label(self, bg='#001B40', foreground='#FF0099', font='Arial 20')
        nomeF.place(width=259, height=31, x=106, y=20)
        datar.place(width=92, height=19, x=208, y=83)

        nomeban= tk.Entry(self, bg='#FF0099', font='Arial 20', foreground='White', relief=FLAT)
        idban= tk.Entry(self, bg='#FF0099', font='Arial 20', foreground='White', relief=FLAT)
        databan= tk.Entry(self, bg='#FF0099', font='Arial 20', foreground='White', relief=FLAT)
        confirmBan= tk.Button(self, bg='#FF0099', font='Arial 20', relief=FLAT)
        nomeban.place(width=233, height=27, x=154, y=171)
        idban.place(width=235, height=23, x=156, y=238)
        databan.place(width=226, height=30, x=161, y=303)
        confirmBan.place(width=97, height=29, x=237, y=418)

        switch_window_button = tk.Button(
            label, command=lambda: controller.show_frame(Menu), font='Arial 30', background='Black',
            relief=FLAT
        )
        switch_window_button1 = tk.Button(
            label, command=lambda: controller.show_frame(FeedFun), font='Arial 30', background='Black',
            relief=FLAT
        )
        switch_window_button.place(width=15, height=8, x=37, y=566)
        switch_window_button1.place(width=7, height=9, x=25, y=626)
#_________________________________________________________________________
class Suspender(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liiptt
        liiptt= PhotoImage(file=r'suspensão.png')
        label = tk.Label(self, image=liiptt)
        label.pack()
        labelr = tk.Frame(self)

        nomeF = tk.Label(self, bg='#001B40', foreground='#FF0099', font='Arial 20')
        datar = tk.Label(self, bg='#001B40', foreground='#FF0099', font='Arial 20')
        nomeF.place(width=259, height=31, x=106, y=20)
        datar.place(width=92, height=19, x=208, y=83)

        switch_window_button = tk.Button(
            label, command=lambda: controller.show_frame(Menu), font='Arial 30', background='Black',
            relief=FLAT
        )
        switch_window_button1 = tk.Button(
            label, command=lambda: controller.show_frame(FeedFun), font='Arial 30', background='Black',
            relief=FLAT
        )
        switch_window_button.place(width=15, height=8, x=37, y=566)
        switch_window_button1.place(width=7, height=9, x=25, y=626)

        nomesus= tk.Entry(self, bg='#FF0099', font='Arial 20', relief=FLAT)
        idsus= tk.Entry(self,bg='#FF0099', font='Arial 20', relief=FLAT)
        temposus= tk.Entry(self,bg='#FF0099', font='Arial 20', relief=FLAT)
        confirmsus = tk.Button(self,bg='#FF0099', font='Arial 20', relief=FLAT)
        nomesus.place(width=235, height=26, x=154, y=170)
        idsus.place(width=235, height=25, x=154, y=237)
        temposus.place(width=226, height=28, x=160, y=303)
        confirmsus.place(width=102, height=24, x=234, y=420)
#_________________________________________________________________________
class Postar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liipa
        liipa= PhotoImage(file=r'postar.png')
        label = tk.Label(self, image=liipa)
        label.pack()
        post= tk.Entry(self, bg='#FF0099', foreground='White', relief=FLAT)
        postar= tk.Button(self, text='Postar', foreground='#001B40', bg='#FF0099')
        labelr = tk.Frame(self)
        nomer = tk.Label(self, bg='#001B40', foreground='#FF0099', font='Arial 20')
        datar = tk.Label(self, bg='#001B40', foreground='#FF0099', font='Arial 20')
        nomer.place(width=259, height=31, x=106, y=20)
        datar.place(width=92, height=19, x=208, y=83)
        post.place(width=393, height=382, x=27, y=134)
        postar.place(width=262, height=43, x=94, y=552)
#_________________________________________________________________________
class Criar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liipr
        liipr= PhotoImage(file=r'Criar.png')
        label = tk.Label(self, image=liipr)
        label.pack()
        labelr = tk.Frame(self)

        userc= tk.Entry(self, foreground='White', bg='#FF0099', relief=FLAT, font='Arial 18')
        senhac= tk.Entry(self, foreground='White', bg='#FF0099', relief=FLAT, font='Arial 18')
        confirmc= tk.Entry(self, foreground='White', bg='#FF0099', relief=FLAT, font='Arial 18')

        userc.place(width=238, height=23, x=171, y=262)
        senhac.place(width=206, height=24, x=206, y=335)
        confirmc.place(width=225, height=24, x=196, y=404)

        sing= tk.Button(self, bg='#001B40', foreground='#FF0099', text='☭', font='Arial 15', relief=FLAT)
        sing.place(width=27, height=15, x=208, y=513)
#_________________________________________________________________________
class Excluir(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liipx
        liipx= PhotoImage(file=r'excluir.png')
        label = tk.Label(self, image=liipx)
        label.pack()
        labelr = tk.Frame(self)
        excluirP= tk.Entry(self, bg='#FF0099', foreground='White', relief=FLAT)
        excluirP.place(width=298, height=288, x=78, y=227)
        ide= tk.Entry(self, bg='#FF0099', foreground='White', relief=FLAT)
        ide.place(width=54, height=24, x=135, y=171)
        excluBconfirm = tk.Button(self, bg='#FF0099', relief=FLAT)
        excluBconfirm.place(width=26, height=23, x=356, y=557)
        switch_window_button = tk.Button(
            label, command=lambda: controller.show_frame(Menu), font='Arial 30', background='Black',
            relief=FLAT
        )
        switch_window_button1 = tk.Button(
            label, command=lambda: controller.show_frame(Feed), font='Arial 30', background='Black',
            relief=FLAT
        )
        switch_window_button.place(width=15, height=8, x=37, y=566)
        switch_window_button1.place(width=7, height=9, x=25, y=626)
        nomer = tk.Label(self, bg='#001B40', foreground='#FF0099', font='Arial 20')
        datar = tk.Label(self, bg='#001B40', foreground='#FF0099', font='Arial 20')
        nomer.place(width=259, height=31, x=106, y=20)
        datar.place(width=92, height=19, x=208, y=83)

        pesquisarid= tk.Button(self, bg='#FF0099', relief=FLAT)
        pesquisarid.place(width=41, height=26, x=320, y=170)
#_________________________________________________________________________
class Nuts(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global liipxs
        liipxs= PhotoImage(file=r'curtidas _nuts.png')
        label = tk.Label(self, image=liipxs)
        label.pack()
        nuts= tk.Label(self, bg='#FF0099')
        labelr = tk.Frame(self)
        nomer = tk.Label(self, bg='#001B40', foreground='#FF0099', font='Arial 20')
        datar = tk.Label(self, bg='#001B40', foreground='#FF0099', font='Arial 20')
        nomer.place(width=259, height=31, x=106, y=20)
        datar.place(width=92, height=19, x=208, y=83)
        nuts.place(width=300, height=506, x=111, y=135)

        switch_window_button = tk.Button(
            label, command=lambda: controller.show_frame(Menu), font='Arial 30', background='Black',
            relief=FLAT
        )
        switch_window_button1 = tk.Button(
            label, command=lambda: controller.show_frame(Feed), font='Arial 30', background='Black',
            relief=FLAT
        )
        switch_window_button.place(width=15, height=8, x=37, y=566)
        switch_window_button1.place(width=7, height=9, x=25, y=626)
#_________________________________________________________________________

if __name__ == "__main__":
    root = Face()
    # verificar os pixels
    root.bind('<Button-1>', Poc.inicio_place)
    root.bind('<ButtonRelease-1>', lambda arg: Poc.fim_place(arg, root))
    root.bind('<Button-2>', lambda arg: Poc.para_geometry(root))
    root.mainloop()














