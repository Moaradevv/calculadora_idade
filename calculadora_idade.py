from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Calculadora de idade")
janela.geometry('310x400')


#cores
cor1 = "#3b3b3b" #preta / leve
cor2 = "#333333" #preta / forte
cor3 = "#ffffff" #branca
cor4 = "#fcc058" #laranja


#criando frames

frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=cor2)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=110, height=300, pady=0, padx=0, relief=FLAT, bg=cor1)
frame_baixo.grid(row=1, column=0)

#criando labels para frame cima
calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief='flat', anchor='center', font=('Ivi 15 bold'), bg=cor2, fg=cor3)
calculadora.place(x=0, y=30)

idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief='flat', anchor='center', font=('Arial 35 bold'), bg=cor2, fg=cor4)
idade.place(x=0, y=70)


#criando labels para frame baixo
data_inicial = Label(frame_baixo, text="Data inicial", height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 11'), bg=cor2, fg=cor3)
data_inicial.place(x=50, y=30)

data_nascimento = Label(frame_baixo, text="Data de nascimento", height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 11'), bg=cor2, fg=cor3)
data_nascimento.place(x=50, y=30)



 
janela.mainloop