
from sympy import*
import sympy as sp
from numpy import diff
from sympy import integrate, re, symbols
from sympy.parsing.sympy_parser import parse_expr # Leer función introducida
import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from math import *

root = tkinter.Tk()
root.wm_title("Graficador (Gracias al asesoramiento de Lily Rodríguez, Estudiante de Economía <3)")
ta=root.geometry("1000x700")#1000x700
#root.configure(background="SkyBlue4")

style.use('fivethirtyeight')#'

#fig = Figure(figsize=(5, 4), dpi=100)
fig = Figure()
ax1 = fig.add_subplot(111)
expresiones=[""]
canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
#toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

act_rango=False
ul_ran=""
ran=""

funciones={"sin":"np.sin","cos":"np.cos","tan":"np.tan","log":"np.log",
           "pi":"np.pi","sqrt":"np.sqrt"}

def reemplazo(s):
    for i in funciones:
        if i in s:
            s=s.replace(i, funciones[i])
    return s
    
def animate(i):
    global ejes
    global act_rango
    global ul_ran
    if act_rango==True:
        try:
            lmin = float(ran[0]); lmax = float(ran[1])
            if lmin < lmax:
                x = np.arange(lmin, lmax, .01)#.01
                ul_ran = [lmin, lmax]
            else:
                act_rango = False
        except:
            messagebox.showwarning("Error","Entrada no válida")
            #print("Se repite")
            act_rango=False
            ets.delete(0,len(ets.get()))
    else:
        if ul_ran!="":
            x = np.arange(ul_ran[0],ul_ran[1], .01)#.01
        else:
            x = np.arange(1, 700, .01)#.01
    try:
        if graph_data2!="":
            solo2=eval(graph_data2)
            solo=eval(graph_data)
            ax1.clear()
            ax1.plot(x,solo,x,solo2)
            ax1.fill_between(x, solo2, solo, color = 'g')
            
        

        else:
            solo=eval(graph_data)
            ax1.clear()
            ax1.plot(x,solo)
    except:
        ax1.plot()
    ax1.axhline(0, color="gray")
    ax1.axvline(0, color="gray")
    ani.event_source.stop()

def represent():
    global graph_data
    global ran
    global act_rango
    global graph_data2
    texto_orig=et.get()
    texto_orig2=etn.get()
    if ets.get()!="":
        rann=ets.get()
        ran=rann.split(",")
        act_rango=True
    graph_data=reemplazo(texto_orig)
    graph_data2=reemplazo(texto_orig2)
    ani.event_source.start()
    
def integraldefi():
    
    x = symbols('x') #Declarar variable independiente
    fun_escrita1 = et.get()
    fun_escrita2 = etn.get()
    g2 = parse_expr(fun_escrita1)
    g = parse_expr(fun_escrita2)
    h = g2 -g
    lim1= x0.get()
    lim2= x1.get()
    respuesta = integrate(h,(x,lim1,lim2))
    etiquetafinal=tkinter.Label(master = root, text =f'La respuesta es {respuesta}' )
    etiquetafinal.place(x=80, y=620)

def des_x():
    x = symbols('x') #Declarar variable independiente
    oferta= et.get()
    demanda= etn.get()
    f1 = parse_expr(oferta)
    f2 = parse_expr(demanda)
    puntox= solve(f1 -1*(f2),x)
    x = symbols('x') #Declarar variable independiente
    f2.subs("x",puntox)

    messagebox.showinfo(message=f'x: {puntox} y: {f2}' , title="Despeje de variables")
    


def ex_productor():
    messagebox.showinfo(message="Reescriba la función del productor: (y- función1)", title="Calculo de Excedentes")
    x = symbols('x') #Declarar variable independiente
    oferta= et.get()
    
    f1 = parse_expr(oferta)
    
    lim1= x0.get()
    lim2= x1.get()
    respuesta= integrate(f1,(x,lim1,lim2))
    productor=tkinter.Label(master = root, text =f'El excedente del productor es:  {respuesta}' )
    productor.place(x=530, y=620)


def ex_consumidor():
    messagebox.showinfo(message="Reescriba la función del consumidor: (función2 - y)", title="Calculo de Excedentes")
    x = symbols('x') #Declarar variable independiente
    demanda= etn.get()
    f1 = parse_expr(demanda)
    lim1= x0.get()
    lim2= x1.get()
    respuesta= integrate(f1,(x,lim1,lim2))
    consumidor=tkinter.Label(master = root, text =f'El excedente del consumidor es:  {respuesta}' )
    consumidor.place(x=530, y=670)

def integral():

        x = symbols('x') #Declarar variable independiente
        fun_escrita2 = et.get()
        fun_escrita3 = etn.get()
        g2 = parse_expr(fun_escrita3)
        g = parse_expr(fun_escrita2)
        integral = integrate(g,x)
        integral2 = integrate(g2,x)
        label2 = tkinter.Label(master = root, text = integral)
        label2.place(x=800, y=20)
        label3 = tkinter.Label(master = root, text = integral2)
        label3.place(x=800, y=45)

def derivadas():
    
        x = symbols('x') #Declarar variable independiente
        fun_escrita2 = et.get()
        fun_escrita3 = etn.get()
        g2 = parse_expr(fun_escrita3)
        g = parse_expr(fun_escrita2)
        derivada = sp.diff(g,x)
        derivada2 = sp.diff(g2,x)
        label2 = tkinter.Label(master = root, text = derivada)
        label2.place(x=50, y=20)
        label3 = tkinter.Label(master = root, text = derivada2)
        label3.place(x=50, y=40)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

etn = tkinter.Entry(master=root,width=60)
etn.config(bg="gray87", justify="left")
button = tkinter.Button(master=root, text="SET", bg="gray69", command= represent)
button.pack(side=tkinter.BOTTOM)
etn.pack(side=tkinter.BOTTOM)


#button = tkinter.Button(master=root, text="VER EJES", command=marca_ejes)
#button.pack(side=tkinter.LEFT)

ets=tkinter.Entry(master=root,width=10)
ets.pack(side=tkinter.RIGHT)
et=tkinter.Entry(master=root,width=60)
et.place(x=317,y=620)
label = tkinter.Label(master = root, text = "RANGO DE 'X'")
label.pack(side = tkinter.RIGHT)



button= tkinter.Button(master=root, text = "Punto de equilibrio", bg="gray69", command= des_x)
button.place(x=745,y=625)

button = tkinter.Button(master=root, text="Integrar definida", bg="gray69", command=integraldefi)
button.place(x=360, y=20)

button = tkinter.Button(master=root, text="Excedente del productor", bg="gray69", command=ex_productor)
button.place(x=380, y=45)

button = tkinter.Button(master=root, text="Excedente del consumidor", bg="gray69", command=ex_consumidor)
button.place(x=520, y=45)

buttonintegrales = tkinter.Button(master=root, text="Integrar funciones", bg="gray69", command=integral)
buttonintegrales.place(x=460, y=20)

buttonderivadas = tkinter.Button(master=root, text="Derivar funciones", bg="gray69", command=derivadas)
buttonderivadas.place(x=570, y=20)


x0=tkinter.Entry(master=root,width=5)
x0.place(x=320,y=10)

x1=tkinter.Entry(master=root,width=5)
x1.place(x=320,y=45)

elim1 = tkinter.Label(master = root, text = "a")
elim1.place(x=300, y=10)
elim2 = tkinter.Label(master = root, text = "b")
elim2.place(x=300, y=45)


var=tkinter.StringVar()
var.set(expresiones[0])
guardado=tkinter.OptionMenu(root, var, *expresiones)
guardado.pack(side=tkinter.LEFT)
#sti=var.get()

tkinter.mainloop()
#label = tkinter.Label(master = root, text = "RANGO PARA 'X'")
#label.pack(side = tkinter.RIGHT)
