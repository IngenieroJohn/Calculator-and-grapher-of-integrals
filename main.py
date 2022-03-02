# Programa que calcule la derivada y la integral de una función
from sympy import *
from sympy.parsing.sympy_parser import parse_expr # Leer función introducida
from tkinter import *

def derivada():
    try:
        x = symbols('x') #Declarar variable independiente
        fun_escrita = funcion.get()
        f = parse_expr(fun_escrita)
        derivada = diff(f,x)
        etiqueta.configure(text=derivada)
    except:
        etiqueta.configure(text="Introduce la función correctamente")
        
        
def integral():
    try:
        x = symbols('x') #Declarar variable independiente
        fun_escrita2 = funcion.get()
        g = parse_expr(fun_escrita2)
        integral = integrate(g,x)
        etiqueta.configure(text=integral)
    except:
        etiqueta.configure(text="Introduce la función correctamente")
    
ventana = Tk()
ventana.geometry('400x280')
ventana.title("Cálculo Diferencial e Integral: f(x)")

anuncio = Label(ventana, text="Introduce una función de x:", font=("Arial", 15), fg="blue")
anuncio.pack()

funcion = Entry(ventana, font=("Arial", 15))
funcion.pack()

etiqueta = Label(ventana, text="Resultado", font=("Arial", 15), fg="red")
etiqueta.pack()

boton1 = Button(ventana, text="Derivar Función", font=("Arial", 15), command=derivada)
boton1.pack()

boton2 = Button(ventana, text="Integrar Función", font=("Arial", 15), command=integral)
boton2.pack()

def _quit(): #Función salir
    ventana.quit()     # detiene mainloop
    ventana.destroy()  # elimina la ventana de la memoria
                    

button3 = Button(master=ventana, text="Salir", font=("Arial", 15), command=_quit)
button3.pack()

ventana.mainloop()