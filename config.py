import tkinter as tk
import math
from PIL import Image, ImageTk

# Configurações de conexão
CONFIG = {'host':'localhost','user':'root','database':'entidade'}

# 
TITLE = [ 'Id', 'Specie', 'City', 'Date', 
         ' Stable', 'Injured', 'Stressed', 'Observations', 
         'Update', 'Delete'
         ]

EXTRAS = ['Register Sistem','Add', 'Cancel', 'Exit']

WIDTH = 200
HEIGHT = 200
COLOR =  'Red','white', 'grey', 'light gray'

COORDINATE = None


# Class de animação de carregamento
class Loading(tk.Canvas):
 
    def __init__(self, master=None):
        super().__init__(master )
        self.mat = math
        
        self.load_area = self
        self.load_area['width'] = 200
        self.load_area['height'] = 200
        self.load_area['bg'] = 'SystemButtonFace'

        self.load_area.pack()        
       
        #
        self.indicie_atual = [0]
        self.load_circle()
        self.animation_circle()

    
        
    def load_circle(self):
        coordenadas = list()
        cx, cy = 100, 100  # centro do canvas
        R = 50    # raio do círculo de loading
        r = 10    # raio das bolinhas
        n = 12    # número de bolinhas

        for i in range(n):
            color = 'black'
            if i == 0:
                color = 'white'
                
            angle = 2 * self.mat.pi * i / n
            x = cx + R * self.mat.cos(angle)
            y = cy + R * self.mat.sin(angle)
            
            # Cria oval centrado em (x, y)
            espher = self.load_area.create_oval(x - r, y - r, x + r, y + r, fill=color)
            coordenadas.append(espher)
            #
        return coordenadas
      
       
    def animation_circle(self):
        coords = self.load_circle()
        atual = self.indicie_atual[0]

        for i in range(len(coords)):
            if i == atual:
                color = 'white'     
            else:
                color= 'black'

            self.load_area.itemconfig(coords[i], fill=color)

        num = atual+1
        if atual >= len(coords):
            num = 0
    
        self.indicie_atual[0] = num 
    
        self.load_area.after(150, self.animation_circle)

   