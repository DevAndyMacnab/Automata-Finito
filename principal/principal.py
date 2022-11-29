
from tkinter import Button, scrolledtext as st
from tkinter import messagebox as messagebox
from tkinter import Frame, Tk,ttk
from .manejoArchivo import Aplicacion
from .afd import AutomotaFinitoDeterminista as automata
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import sys
import webbrowser as web
import os


class Principal:
    def __init__(self,window):
        self.principal= window
        self.principal.title("Automata Finito")

        
        self.frameFunciones= Frame(self.principal)
        self.frameFunciones.grid(row=0,column=0)
        self.frameFunciones.config(width="300",height="700" )
        self.frameFunciones.config(bg="#D4E6F1",padx=10,pady=10)
        
        self.frameInfo= Frame(self.principal)
        self.frameInfo.grid(row=0,column=1)
        self.frameInfo.config(width="300",height="700" )
        self.frameInfo.config(bg="#D5F5E3",padx=10,pady=70)
        
        
        self.textArea=st.ScrolledText(self.principal, width=70, height=40)
        self.textArea.config(bg="#FCF3CF")
        self.textArea.grid(row=0,column=2,padx=10,pady=25)
        
        
        #GRUPO DE BOTONES PARA EL FRAME DE INFORMACION DEL PROGRAMA
        
        self.botonUsuario=Button(self.frameInfo,text="Manual de Usuario",
                                 command=self.manualUsuario,
                                 width=16,
                                 height=4)
        self.botonUsuario.grid(row=0,column=0,padx=20,pady=20)
        
        self.botonTecnico=Button(self.frameInfo,text="Manual Técnico",
                                 command=self.manualTecnico,
                                 width=16,
                                 height=4)
        self.botonTecnico.grid(row=1,column=0,padx=20,pady=20)
        
        self.botonAyuda=Button(self.frameInfo,text="Temas de Ayuda",
                               command=self.temasdeAyuda,
                                 width=16,
                                 height=4)
        self.botonAyuda.grid(row=2,column=0,padx=20,pady=20)
        
        #GRUPO DE BOTONES PARA EL FRAME DE FUNCIONES DEL PROGRAMA
        
        self.botonAbrir=Button(self.frameFunciones,text="Abrir",
                                 width=16,
                                 height=4,
                                 command=lambda:Aplicacion.recuperar(self.principal,self.textArea))
        self.botonAbrir.grid(row=0,column=0,padx=20,pady=10)
        
        self.botonGuardar=Button(self.frameFunciones,text="Guardar Como",
                                 width=16,
                                 height=4,
                                 command=lambda:Aplicacion.guardar(self.principal,self.textArea))
        self.botonGuardar.grid(row=1,column=0,padx=20,pady=10)
        
        self.botonAnalizar=Button(self.frameFunciones,text="Analizar",
                                  command=lambda:self.convertToTextPlane(),
                                 width=16,
                                 height=4)
        self.botonAnalizar.grid(row=2,column=0,padx=20,pady=10)
        
        self.botonErrores=Button(self.frameFunciones,text="Errores",
                                 width=16,
                                 height=4)
        self.botonErrores.grid(row=3,column=0,padx=20,pady=10)
        
        
        self.botonSalir=Button(self.frameFunciones,text="Salir",
                                 width=16,
                                 height=4,
                                 command=lambda:sys.exit())
        self.botonSalir.grid(row=4,column=0,padx=20,pady=10)
        
    def convertToTextPlane(self):
        self.textoPlano=str(self.textArea.get("1.0","end-1c"))
        print(self.textoPlano)
        print("-----------------")
        automata.recibiendoInformacion(self.textoPlano)
    
    def temasdeAyuda(self):
        web.open("https://pythondiario.com/2015/06/afd-en-python-automata-finito.html",new=2,autoraise=True)
        messagebox.showinfo("Informacion del creador","Andy Roberto Jimenez Macnab \n Carnet: 202111490")
    
        
    def manualUsuario(self):
        web.open_new("file:///C:/Users/andyr/Desktop/PROGRA%20PARA%20USAC/Programa%20de%20Automata%20Finito/MANUAL%20DE%20USUARIO.pdf")
        messagebox.showinfo("Manual de Usuario", "El documento PDF del manual de usuario ha sido abierto correctamente")
        
    def manualTecnico(self):
        web.open_new("file:///C:/Users/andyr/Desktop/PROGRA%20PARA%20USAC/Programa%20de%20Automata%20Finito/MANUAL%20TECNICO.pdf")
        messagebox.showinfo("Manual de Tecnico", "El documento PDF del manual técnico ha sido abierto correctamente")
        
        
        
                
        
        
        