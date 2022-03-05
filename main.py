# Programa que calcule la derivada y la integral de una función
from sympy import *
from sympy.parsing.sympy_parser import parse_expr # Leer función introducida
from tkinter import *

def grafint(): #esto es para graficar pero hay un error en las librerias de importación
    from matplotlib.pyplot import * #esta libreria si las pones afuera tambn dan error
    from numpy import * #esta tambn
    x=arange(0,10,0.001)

    fun_escrita = funcion.get()
    f = parse_expr(fun_escrita)
    fun_escrita2 = funcion2.get()
    g = parse_expr(fun_escrita2)


    plot(x,g,x,f)
    fill_between(x,f,g) 
    x= symbols('x')
    h=g-f
    res=integrate(h,(x,1,6))
    print (f'La respuesta es {res}')
    show()
    
    
def derivada():
    try:
        x = symbols('x') #Declarar variable independiente
        fun_escrita = funcion.get()
        f = parse_expr(fun_escrita)
        derivada = diff(f,x)
        etiqueta.configure(text=derivada)
    except:
        etiqueta.configure(text="Introduce la función correctamente")
        

def derivada2():
    try:
        x = symbols('x') #Declarar variable independiente
        fun_escrita = funcion2.get()
        f = parse_expr(fun_escrita)
        derivada = diff(f,x) 
        etiqueta2.configure(text=derivada)
    except:
        etiqueta2.configure(text="Introduce la función 2 correctamente")     
        
        
        
        
def integral():
    try:
        x = symbols('x') #Declarar variable independiente
        fun_escrita2 = funcion.get()
        g = parse_expr(fun_escrita2)
        integral = integrate(g,x)
        etiqueta.configure(text=integral)
    except:
        etiqueta.configure(text="Introduce la función correctamente")
        
        
def integral2():
    try:
        x = symbols('x') #Declarar variable independiente
        fun_escrita2 = funcion2.get()
        g = parse_expr(fun_escrita2)
        integral = integrate(g,x)
        etiqueta2.configure(text=integral)
    except:
        etiqueta2.configure(text="Introduce la función correctamente")
        
        
    
ventana = Tk()
ventana.geometry('400x280')
ventana.title("Cálculo Diferencial e Integral: f(x)")

anuncio = Label(ventana, text="Introduce una función de x:", font=("Arial", 15), fg="blue")
anuncio.pack()

funcion = Entry(ventana, font=("Arial", 15))
funcion.pack()

anuncio2 = Label(ventana, text="Introduce G(x):", font=("Arial", 15), fg="blue")
anuncio2.pack()

funcion2 = Entry(ventana, font=("Arial", 15))
funcion2.pack()

etiqueta = Label(ventana, text="Resultado", font=("Arial", 15), fg="red")
etiqueta.pack()

etiqueta2 = Label(ventana, text="Resultado de g(x)", font=("Arial", 15), fg="red")
etiqueta2.pack()

boton1 = Button(ventana, text="Derivar Función", font=("Arial", 15), command=derivada)
boton1.pack()

boton2 = Button(ventana, text="Integrar Función", font=("Arial", 15), command=integral)
boton2.pack()


boton3 = Button(ventana, text="Mostrar integral", font=("Arial", 15), command= grafint)
boton3.pack()

def _quit(): #Función salir
    ventana.quit()     # detiene mainloop
    ventana.destroy()  # elimina la ventana de la memoria
                    

button4 = Button(master=ventana, text="Salir", font=("Arial", 15), command=_quit)
button4.pack()

ventana.mainloop()
