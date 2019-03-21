from Tkinter import *
from core import *

class Aplicacion(Frame):
    def __init__(self, master=None):
        master.geometry('500x500')
        Frame.__init__(self,master)
        self.pack()
        self.hacerWidgets()
        #Carga de los regresores
        self.core = CoreRegressors()

    def hacerWidgets(self):
        #Empezar con el row en 10 para poder poner cosas antes y despues
        self.txt_resultados = Label(self,text="Resultados").grid(columnspan=60,row=10)

        self.txt_popularidad = Label(self,text="Popularidad").grid(column=10,row=15)
        self.tbx_popularidad = Entry(self).grid(column=10,row=20)

        self.txt_puntaje = Label(self,text="Puntaje").grid(column=20,row=15)
        self.tbx_puntaje = Entry(self).grid(column=20,row=20)

        self.txt_favoritos = Label(self,text="Favoritos").grid(column=30,row=15)
        self.tbx_favoritos = Entry(self).grid(column=30,row=20)

        self.txt_generos= Label(self,text="Generos").grid(column=30,row=30, sticky=E)

        self.txt_config= Label(self,text="Parametros").grid(column=30, columnspan=15,row=30)



#Carga de la ventana
window = Tk()
app = Aplicacion(master=window)
app.mainloop()
