from tkinter import *
import tkinter
from datetime import datetime

# Colors
color1 = "#3d3d3d"  # preta
color2 = "#fafcff"  # branca
color3 = "#21c25c"  # verde
color4 = "#eb463b"  # vermelha
color5 = "#dedcdc"  # cinza
color6 = "#3080f0"  # azul

background = color1
color = color2

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
    l2.config(text=dia_semana + "   " + str(dia) + "/" + str(mes) + "/" + str(ano))


l1 = Label(janela, text="", font=("Arial", 80), bg=background, fg=color)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="", font=("Arial", 20), bg=background, fg=color)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()