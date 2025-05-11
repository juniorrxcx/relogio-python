from tkinter import *
import tkinter
from datetime import datetime


# Colors
background = "#561183" # Cor de fundo
color = "#bf6af6" # Cor do texto

janela = Tk()
janela.title("Relógio")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=background)

def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + "   " + str(dia) + "/" + str(mes) + "/" + str(ano))


l1 = Label(janela, text="", font=("Consolas", 70), bg=background, fg=color)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="", font=("Consolas", 25), bg=background, fg=color)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()