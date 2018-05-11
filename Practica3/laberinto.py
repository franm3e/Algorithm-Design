#coding: utf8

#######################################################
#######################################################
#                                                     #
#      Diseño de Algoritmos 2015-2016                 #
#                                                     #
#      Práctica 2: Algoritmos sobre grafos            #
#                                                     #
#      Luis de la Ossa                                #    
#                                                     #
#######################################################
#######################################################

# Francisco Martínez Esteso

import random
import sys

from collections import deque

sys.setrecursionlimit(80000) 

# Esta clase implementa un laberinto. 
class laberinto:  
      
    # Constructor
    def __init__(self, anchura=20, altura=40, semilla=0):    
        self.altura = altura
        self.anchura = anchura
        self.G = {};           
        self.entrada = None 
        self.salida = None 
        # Crea el laberinto
        random.seed(semilla)
        self.creaLaberinto()
        
    # Crea un laberinto.
    def creaLaberinto(self):        
        # Toma un punto de origen aleatoriamente.
        origen = (random.randint(0,self.anchura-1),random.randint(0,self.altura-1))
        visitados = set(origen)
        # Explora el grado recursivamente y elimina los muros.
        self.explora(origen,visitados)
        # Fija la entrada y la salida.
        self.entrada = (0, random.randint(0,self.altura-1))
        self.salida = (self.anchura-1 ,random.randint(0,self.altura-1))
        
    # Explora un nodo.   
    def explora(self, nodo1, visitados):
        adyacentes = self.adyacentes(nodo1)
        random.shuffle(adyacentes)
        ###################################################################
        # COMPLETAR 
        ###################################################################
        for i in adyacentes: #      Recorremos adyacentes
            if i not in visitados: #        Si el nodo adyacente no ha sido visitado
                visitados.add(i) #      Añadimos el nodo actual a visitados
                self.anadeEnlace(nodo1, i) #        Añadimos enlace entre el nodo actual y el nodo adyacente
                self.explora(i, visitados) #        Volvemos a explorar los adyacentes del nodo actual


    # Obtiene los nodos adyacentes a uno dado.
    def adyacentes(self, (posX,posY)):
        adyacentes = []
        ###################################################################
        # COMPLETAR
        # Añade vecino izquierda
        # Añade vecino derecha
        # Añade vecino abajo
        # Añade vecino arriba            
        ###################################################################        

        # Añade vecino izquierda
        if posX > 0:
            adyacentes = adyacentes + [(posX-1, posY)]
        # Añade vecino derecha
        if posX < self.anchura-1:
            adyacentes = adyacentes + [(posX+1, posY)]
        # Añade vecino abajo
        if posY > 0:
            adyacentes = adyacentes + [(posX, posY-1)]
        # Añade vecino arriba
        if posY < self.altura-1:
            adyacentes = adyacentes + [(posX, posY+1)]

        return adyacentes

    
    # Busca el camino mediante exploración en anchura
    def encuentraCaminoAnchura(self):
        # Cola utilizada en la exploración en anchura.
        cola = deque()
        # Punteros para recuperar el camino. 
        # Si desde nodo1 se va a nodo2, entonces predecesor[nodo2]=nodo1
        predecesor = {}    
        # Comienza la exploración
        nodo = self.entrada 
        predecesor[nodo] = None

        (posX,posY) = nodo #    Obtengo la posicion del nodo actual
        visitados = [] #    Creo una lista de visitados

        while nodo != self.salida:
            # pass #Quitar
            ######################################################################
            #COMPLETAR
            ######################################################################

            adyacentes = self.adyacentes((posX, posY))  #   Obtengo los nodos adyacentes al nodo actual 
            visitados.append(nodo) #    Añado a visitados el nodo actual
            for i in adyacentes: #      Para cada adyacente
                if i not in visitados and self.existeEnlace(nodo, i): #     Si el nodo actual no esta visitado y existe un enlace hasta el
                    cola.append(i) #        Añado adyacente a la cola
                    predecesor[i] = nodo #      Completo el predecesor del nodo adyacente
            nodo = cola.popleft() #     Saco el ultimo elemento insertado en la cola
            (posX, posY) = nodo #       Obtengo la posicion del nodo actual

        # Recupera la lista hacia atrás.            
        camino = [self.salida]
        anterior = predecesor[self.salida]
        while anterior != self.entrada:
            # pass #Quitar
            ######################################################################
            #COMPLETAR
            ######################################################################

            camino.append(anterior) #       Añado al camino el nodo anterior
            anterior = predecesor[anterior] #       Inicializo anterior como el predecesor del nodo actual
        camino.append(self.entrada) #       Añado la entrada al camino
        return camino

            
    ######################################################################
    # Las siguientes funciones están completadas
    ######################################################################            
                    
    # Añade un enlace. 
    def anadeEnlace(self, nodo1, nodo2):
        # Si no existe la entrada correspondiente, la crea.
        if nodo1 not in self.G:
            self.G[nodo1]=[]
        if nodo2 not in self.G:
            self.G[nodo2]=[]                   
        # Añade el enlace (NO DIRIGIDO)
        self.G[nodo1].append(nodo2)
        self.G[nodo2].append(nodo1)      
               
    # Comprueba si existe el enlace.
    def existeEnlace(self, nodo1, nodo2):    
        return nodo2 in self.G[nodo1]
    
    # Esta función debe eliminar el número de muros.
    def eliminaMuros(self, numero):
        for i in xrange(numero):
            # Selecciona un nodo al que se le puedan añadir adyacentes
            # Comprueba self.G[nodo1] tiene un tamaño menor que el posible.
            nodo1 = random.choice(self.G.keys())
            adyacentes = self.adyacentes(nodo1)
            while len(adyacentes)==len(self.G[nodo1]):
                nodo1 = random.choice(self.G.keys())
                adyacentes = self.adyacentes(nodo1)                   
            # Desordena los adyacentes.          
            random.shuffle(adyacentes)            
            # Saca los vecinos hasta que encuentre uno que 
            # no forma parte del grafo.
            nodo2 = adyacentes.pop()
            while nodo2 in self.G[nodo1]:
                nodo2 = adyacentes.pop()
            # Añade el enlace.
            self.anadeEnlace(nodo1, nodo2)

                          
    ######################################################################
    # Estas funciones sirven para dibujar un laberinto en un objeto canvas.
    ######################################################################
    
    # Dibuja un laberinto de una determinada altura y anchura. 
    # Deja un margen de dos celdas por cada lado.
    def dibuja(self, canvas):
        # Toma como referencia la dimensión que permite un tamaño de celda menor.
        alturaPx = canvas.winfo_height()
        anchuraPx = canvas.winfo_width()        
        if alturaPx/self.altura < anchuraPx/self.anchura:
            cell_size =  alturaPx/(self.altura+4)
        else:
            cell_size =  anchuraPx/(self.anchura+4)                       
        # Dibuja una rejilla.    
        self.dibujaRejilla(canvas, cell_size)        
        # Elimina las paredes.
        for celda in self.G.keys():
            for sucesor in self.G[celda]:
                self.eliminaPared(celda, sucesor, canvas, cell_size)                
        # Entrada y salida
        self.eliminaPared((-1, self.entrada[1]), self.entrada, canvas, cell_size)  
        self.eliminaPared(self.salida, (self.anchura, self.salida[1]), canvas, cell_size) 
        return
                
    # Dibuja la rejilla base.
    def dibujaRejilla(self, canvas, cell_size):
        # Dibuja las líneas verticales
        for x in xrange(self.anchura+1):
                pos_x = (x+2)*cell_size
                pos_y1 = cell_size*2;
                pos_y2 = (self.altura+2)*cell_size
                canvas.create_line(pos_x,pos_y1,pos_x,pos_y2,fill='black', width=2)                   
        for y in xrange(self.altura+1):
                pos_y = (y+2)*cell_size
                pos_x1 = cell_size*2;
                pos_x2 = (self.anchura+2)*cell_size
                canvas.create_line(pos_x1,pos_y,pos_x2,pos_y,fill='black', width=2)     
        
    # Dadas dos celdas adyacentes, elimina la pared entre ellas.    
    def eliminaPared(self, (origenX, origenY),(destinoX,destinoY), canvas, cell_size):
        if origenX==destinoX:
            if abs(origenY-destinoY)==1:
                pos_x1 = (origenX+2)*cell_size+1
                pos_x2 = (origenX+3)*cell_size-1
                minY = min(origenY, destinoY)
                pos_y = (minY+3)*cell_size
                canvas.create_line(pos_x1,pos_y,pos_x2,pos_y,fill='white', width=2)
                return         
        if origenY==destinoY:
            if abs(origenX-destinoX)==1:
                pos_y1 = (origenY+2)*cell_size+1
                pos_y2 = (origenY+3)*cell_size-1
                minX=min(origenX, destinoX)
                pos_x = (3+minX)*cell_size
                canvas.create_line(pos_x,pos_y1,pos_x,pos_y2,fill='white', width=2)    
                return
        # Si no se da ninguna 
        print "Las celdas no son adyacentes."
        return         

    # Marca un camino
    def marcaCamino(self, camino, color, canvas):        
        alturaPx = canvas.winfo_height()
        anchuraPx = canvas.winfo_width()
        # Toma como referencia la dimensión que permite un tamaño de celda menor.
        if alturaPx/self.altura < anchuraPx/self.anchura:
            cell_size =  alturaPx/(self.altura+4)
        else:
            cell_size =  anchuraPx/(self.anchura+4)      
                     
        for (posX,posY) in camino:
            self.marcaCelda(posX,posY, color, canvas, cell_size)
      
    # Marca una celda.
    def marcaCelda(self, posX, posY, color, canvas, cell_size):
        canvas.create_rectangle((posX+2)*cell_size+1, (posY+2)*cell_size+1, (posX+3)*cell_size-2, (posY+3)*cell_size-2, 
                                 outline=color, fill=color)    