import matplotlib.pyplot as plt
from numpy import arange, sin, cos, pi
from tkinter import *  # Se importa el módulo Tkinter
from tkinter import ttk, font
import getpass

# creación de la ventana o interfaz
Interfaz = Tk()
Interfaz.title("Movimiento Uniformemente acelerado (MUA)")
Interfaz.geometry("500x270")  # Tamaño de la interfaz(alto x ancho)
Interfaz.config(bg="alice blue")
Vara = StringVar()
Varx = StringVar()
# Se crean los widgets a usar y se posicionan en la interfaz
TituloInterfaz = Label(Interfaz, text="CALCULADORA DE LA ACELERACIÓN Y DESPLAZAMIENTO EN UN MUA")
TituloInterfaz.place(x=70, y=10)  # x es horizotalmente(izqui-dere) y Y es verticalmente(arriba-abajo)
TituloInterfaz.config(bg="cyan4")
Mensaje = Label(Interfaz, text="Ingrese los siguientes parámetros del cuerpo")
Mensaje.place(x=40, y=40)
Mensaje.config(bg="cyan4")
Vo = Label(Interfaz, text="Vo(m/s)=")
Vo.place(x=70, y=70)
Vo.config(bg="cyan4")
Vf = Label(Interfaz, text="Vf(m/s)=")
Vf.place(x=70, y=90)
Vf.config(bg="cyan4")
t = Label(Interfaz, text="t(s)=")
t.place(x=80, y=110)
t.config(bg="cyan4")
# Ingreso de los datos a través de cuadros de texto
# -
vo = Entry(Interfaz)
vo.place(x=130, y=70)
# -
vf = Entry(Interfaz)
vf.place(x=130, y=90)
# -
t = Entry(Interfaz)
t.place(x=130, y=110)


# Se crean las funciones que ejecutarán los botones
def CalculoAce():
    a = (float(vf.get()) - float(vo.get())) / float(t.get())
    # Se devuelve la variable a en la variable string Vara
    return Vara.set(a)


boton1 = Button(Interfaz, text="Aceleración(m/s^2)", relief="raised", command=CalculoAce)
boton1.place(x=25, y=150)
boton1.config(bg="cyan4")
resa = Label(Interfaz, textvariable=Vara, bg="#FFFFFF")
resa.place(x=150, y=150)


def CalculoDes():
    x = (float(vo.get()) * float(t.get())) + ((float(Vara.get()) * ((float(t.get()) ** 2))) / 2)
    # Se devuelve la variable x en la variable string Varx
    return Varx.set(x)


boton2 = Button(Interfaz, text="Desplazamiento(m)", relief="raised", command=CalculoDes)
boton2.place(x=26, y=180)
boton2.config(bg="cyan4")
resx = Label(Interfaz, textvariable=Varx, bg="#FFFFFF")
resx.place(x=150, y=180)

# Se grega una imagen de MUA
imagen2 = PhotoImage(file="movimiento.png")
FondoInterfaz2 = Label(Interfaz, image=imagen2).place(x=270, y=90)


# Se declara la funcion del botón para graficar
def graficar():
    # Para mostrar ambos gráficos en la misma ventana, se usa subplot(fila,columna,N°Gráfico)
    # Gráfico N°1 aceleración
    plt.subplot(1, 2, 1)
    plt.plot(str(Vara.get()), color='b', linestyle='-')
    plt.title("Gráfico aceleración")
    plt.xlabel("Tiempo(t)")
    plt.ylabel("Aceleración(m/s^2)")
    plt.grid()
    plt.axis([0, 15, -10, 10])
    # Los comandos xticks y yticks son para establecer los rangos de los ejes
    plt.axis([0, 15, -10, 10])
    # Gráfico N°2 desplazamiento
    plt.subplot(1, 2, 2)
    plt.plot(str(Varx.get()), color='b', linestyle='-')
    plt.title("Gráfico desplazamiento")
    plt.xlabel("Tiempo(t)")
    plt.ylabel("Desplazmiento(m)")
    plt.grid()
    plt.axis([0, 15, -10, 10])
    plt.show()


BotonGraficar = Button(Interfaz, text="Graficar", relief="raised", command=graficar, bg="cyan4")
BotonGraficar.place(x=180, y=210)