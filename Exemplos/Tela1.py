from tkinter import *

class Application:
    def __init__(self, master = None):
        self.widget1 = Frame(master)
        self.widget1.pack(expand=True)
        self.msg = Label(self.widget1, text="Primeiro Widget")
        self.msg["font"] = ("Calibri", "9", "bold")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack()
    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro Widget":
            self.msg["text"] = "O botão foi clicado"
        else:
            self.msg["text"] = "Primeiro Widget"
            
root = Tk()
root['bg'] = "#82CEEC"
Application(root)
root.mainloop()