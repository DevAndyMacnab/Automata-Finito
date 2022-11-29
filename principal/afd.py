from genericpath import exists
import math
import sys
import os
from string import Template
from wsgiref.handlers import read_environ
from tkinter import Tk, messagebox as messagebox


class AutomotaFinitoDeterminista:
    def __init__(self,textoPlano)  :
        self.textoPlano= textoPlano
        self.diccionario=[]
        
        
        
    def recibiendoInformacion(textoPlano):
        errores=0
        textoFinal=[]

        palabraClave=""
        listaFilas=textoPlano.split("\n")
        print(listaFilas)
        for elemento in listaFilas:
            palabraClave=""
            if elemento[0]!="<":
                errores+=1
                print(errores)
                
            
            for caracter in elemento:
                
                if caracter =='<':
                   continue
                if caracter =='>':
                    continue
                else:
                    palabraClave+= caracter
                
                if palabraClave == "Operacion":
                    
                    listaOperacion=[]
                    
                    
                    operacion=elemento.split(" ")
                    
                    if operacion[1]== "SUMA>":
                        listaOperacion.append("suma")
                    if operacion[1]== "RESTA>":
                        listaOperacion.append("resta")
                    if operacion[1]== "MULTIPLICACION>":
                        listaOperacion.append("multiplicacion")
                    if operacion[1]== "DIVISION>":
                        listaOperacion.append("division")
                    if operacion[1]== "RAIZ>":
                        listaOperacion.append("raiz")
                    if operacion[1]== "POTENCIA>":
                        listaOperacion.append("potencia")
                    if operacion[1]== "COSENO>":
                        listaOperacion.append("coseno")
                    if operacion[1]== "SENO>":
                        listaOperacion.append("seno")
                        
                if palabraClave == "Numero":
                    numero = elemento.split(" ")
                    
                    listaOperacion.append(numero[1])

                if palabraClave == "/Operacion":

                    if listaOperacion[0]=="suma":
                        result=float(listaOperacion[1]) + float(listaOperacion[2])
                        listaOperacion.append(result)
                        listaOperacion.append("+")
                        textoFinal.append(listaOperacion)
                    
                    if listaOperacion[0]=="resta":
                        result=float(listaOperacion[1]) - float(listaOperacion[2])
                        listaOperacion.append(result)
                        listaOperacion.append("-")
                        textoFinal.append(listaOperacion)
                        
                    if listaOperacion[0]=="multiplicacion":
                        result=float(listaOperacion[1]) * float(listaOperacion[2])
                        listaOperacion.append(result)
                        listaOperacion.append("*")
                        textoFinal.append(listaOperacion)
                        
                    if listaOperacion[0]=="division":
                        result=float(listaOperacion[1]) / float(listaOperacion[2])
                        listaOperacion.append(result)
                        listaOperacion.append("/")
                        textoFinal.append(listaOperacion)
                        
                    if listaOperacion[0]=="raiz":
                        result=math.pow(float(listaOperacion[2]),1/float(listaOperacion[1]))
                        listaOperacion.append(result)
                        listaOperacion.append("raiz(")
                        textoFinal.append(listaOperacion)
                        
                    if listaOperacion[0]=="potencia":
                        result=math.pow(float(listaOperacion[1]),float(listaOperacion[2]))
                        listaOperacion.append(result)
                        listaOperacion.append("^")
                        textoFinal.append(listaOperacion)
                        
                    if listaOperacion[0]=="seno":
                        result=math.sin(float(listaOperacion[1]))
                        listaOperacion.append(result)
                        listaOperacion.append("seno(")
                        textoFinal.append(listaOperacion)
                        
                    if listaOperacion[0]=="coseno":
                        result=math.cos(float(listaOperacion[1]))
                        listaOperacion.append(result)
                        listaOperacion.append("coseno(")
                        textoFinal.append(listaOperacion)
                        
            
        print(textoFinal)

        conteo=0
        dup = {x for x in textoFinal if textoFinal.count(x) > 1}
        print("------------------------")
        print(dup)
        textoArreglado=[]
        for element in textoFinal:
            print(element)
            conteo+=1
            lineaPrimera="Operacion " + str(element[0]) + " " + str(conteo) + " :"
            
            if element[0]=="seno":
                lineaSegunda=str(element[-1])  + str(element[1]) + " = " + str(element[2])
            
            elif element[0]=="coseno":
                lineaSegunda=str(element[-1])  + str(element[1]) + " = " + str(element[2])
                
            else:
                lineaSegunda= str(element[1]) + " " +  str(element[-1]) + " "+str(element[2]) + " = " + str(element[3]) 
            print(lineaPrimera)
            print(lineaSegunda)
            textoArreglado.append({'lineaPrimera':lineaPrimera,"lineaSegunda":lineaSegunda})
        print(textoArreglado)
        
        filein= open('C:\\Users\\andyr\\Desktop\\PROGRA PARA USAC\\Programa de Automata Finito\\principal\\plantilla.html','r')        
        src= Template(filein.read())
        for eleme in textoArreglado:
       
            d={'lineaPrimera':eleme["lineaPrimera"],"lineaSegunda":eleme["lineaSegunda"]}
            reemplazo=src.substitute(d)
                
            try:
                os.mkdir("archivo")
                filein2= open("archivo/"+"RESULTADOS_202111490"+".html","a")
                filein2.writelines(reemplazo)
                print("Se ha creado el archivo correctamente")
            except OSError:
                if os.path.exists("archivo"):
                    filein2= open("archivo/"+"RESULTADOS_202111490"+".html","a")
                    filein2.writelines(reemplazo)
        
        messagebox.showinfo("Archivo generado!","Se ha generado el archivo HTML correctamente")
          
            
        return textoFinal
    

        
        
        
        
          
        
            
            
            
            
                
                
                
                
            
            
        
        