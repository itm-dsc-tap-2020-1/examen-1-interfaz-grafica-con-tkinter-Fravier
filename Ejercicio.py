import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext

def funcion_click1():
    if P1.get()=="" or P2.get()=="" :        
        mBox.showinfo("Atencion","Datos incompletos")
    else:
        texto6.configure(text="")
        x=0
        if P1.get()=="20 Cm":
            x=x+20
        if P2.get()=="Si":
            x=x+20
        if option1.get()==1:
            x=x+20
        if option2.get()==1:
            x=x+20
        if option_1.get()==1 and option_2.get()==1:
            x=x+20
    mBox.showinfo("Puntos",x)

ventana=tk.Tk()
ventana.title("Examen Astronomia")
ventana.resizable(0,0)

texto1=ttk.Label(text="Cual tamaño del satelite mas pequeño?:").grid(column=0,row=1) 
P1=tk.StringVar()
Preg_P1=ttk.Entry(width=20, textvariable=P1).grid(column=1,row=1)

texto2=ttk.Label(text="El sol se esta evaporando?:").grid(column=0,row=2) 
P2=tk.StringVar()
Preg_P2=ttk.Entry(width=20, textvariable=P2).grid(column=1,row=2)

texto3=ttk.Label(text="Planeta donde vivimos:").grid(column=0,row=3)
option1=tk.IntVar()
radio1=tk.Radiobutton(text="Tierra", variable=option1,value=1).grid(column=0,row=4,sticky=tk.W)
radio2=tk.Radiobutton(text="Marte", variable=option1,value=2).grid(column=1,row=4,sticky=tk.W)
radio3=tk.Radiobutton(text="Jupiter", variable=option1,value=3).grid(column=2,row=4,sticky=tk.W)

texto4=ttk.Label(text="Liquido mas abundante:").grid(column=0,row=5)
option2=tk.IntVar()
radio4=tk.Radiobutton(text="Agua", variable=option2,value=1).grid(column=0,row=6,sticky=tk.W)
radio5=tk.Radiobutton(text="Aceite", variable=option2,value=2).grid(column=1,row=6,sticky=tk.W)
radio6=tk.Radiobutton(text="Petroleo", variable=option2,value=3).grid(column=2,row=6,sticky=tk.W)

texto5=ttk.Label(text="Planetas en el sistema:").grid(column=0,row=7)
option_1=tk.IntVar()
casilla_1=tk.Checkbutton(text="8",variable=option_1).grid(column=0,row=8)
option_2=tk.IntVar()
casilla_2=tk.Checkbutton(text="7",variable=option_2).grid(column=1,row=8)
option_3=tk.IntVar()
casilla_3=tk.Checkbutton(text="5",variable=option_3).grid(column=2,row=8)
option_4=tk.IntVar()
casilla_4=tk.Checkbutton(text="9",variable=option_3).grid(column=3,row=8)
option_5=tk.IntVar()
casilla_5=tk.Checkbutton(text="15",variable=option_3).grid(column=4,row=8)

Calificar=ttk.Button(text="Calificar",command=funcion_click1).grid(column=5, row=10)
texto6=ttk.Label(text="")
texto6.grid(column=3,row=10)

ventana.mainloop()