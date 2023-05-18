from tkinter import *

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Hello World")
texto.place(x = 75, y = 100)
botao = Button(master = janelaPrincipal, text = "Aperte!")
botao.place(x = 90, y = 80)

janelaPrincipal.mainloop()