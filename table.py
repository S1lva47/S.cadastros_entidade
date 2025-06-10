import tkinter as tk 
from tkinter import messagebox
from config import *
from mysql.connector import MySQLConnection, Error
import threading


#Intanciando a tabela com os valores cadastrados 
class Table: 
    def __init__(self, foreing_window, kwargs): 
        self.foreing_window = foreing_window
        self.kwargs = kwargs
        
        # 
        self.table_gui(foreing_window)
        #
        self.scrollbar = tk.Scrollbar(self.table_window, orient='vertical', command=self.table_window.yview )
        self.scrollbar.place(x=1285, relheight=1.0)
        self.table_window.configure(yscrollcommand=self.scrollbar.set)
        #
        self.table_window.create_window((70,0), window=self.table_frame, anchor='nw')
        
        #Cabeçalho da tabela
        self.header()
        # Estrutura da tabela
        
        self.add_table(kwargs)
         
        self.table_frame.update_idletasks()
        self.table_window.config(scrollregion=self.table_frame.bbox('all'))
        #

    #
    def table_gui(self, event):
         #
        self.table_window = tk.Canvas(event)
        self.table_window['height'] = HEIGHT 
        self.table_window['width'] = WIDTH + 500
      
        #
        self.table_frame = tk.Frame(self.table_window)
        self.table_frame['width'] = WIDTH + 360
        self.table_frame['height'] = HEIGHT + 200
        
        #buttom de att.
        self.buttom_att = tk.Label(self.table_window)
    
        self.buttom_att['pady'] = 12
        self.buttom_att['width'] = 7
        self.buttom_att['text'] = TITLE[8]
        self.buttom_att['fg']= COLOR[2] 
        self.buttom_att['height'] = 2
        self.buttom_att['font'] = ('Times', 12)
        self.buttom_att['bg'] = COLOR[3]
        self.buttom_att.bind('<Enter>',self.inside_att )
        self.buttom_att.bind('<Leave>', self.outside_att)
        self.buttom_att.bind('<Button-1>', self.load_animation)

        self.buttom_att.place(x=0,rely=0.9)

        # Button Delete
        self.buttom_delete = tk.Label(self.table_window)
    
        self.buttom_delete['pady'] = 12
        self.buttom_delete['width'] = 7
        self.buttom_delete['text'] = TITLE[9]
        self.buttom_delete['fg']= COLOR[2] 
        self.buttom_delete['height'] = 2
        self.buttom_delete['font'] = ('Times', 12)
        self.buttom_delete['bg'] = COLOR[3]
        self.buttom_delete.bind('<Enter>', self.inside_delete )
        self.buttom_delete.bind('<Leave>',self.outside_delete)
        self.buttom_delete.bind('<Button-1>', self.delete)

        self.buttom_delete.place(x=0,rely=0.7)
        return True

   
    def header(self):
        for pointer in range(len(TITLE[:8])):
            #Adicionando as colunas  
            self.bloco = tk.Label(self.table_frame)
            self.bloco['height'] = 3
            self.bloco['font'] = ('Arial', 12)
            self.bloco.config(relief='sunken')
            #
            if pointer % 2 == 0:
                self.bloco['text'] = TITLE[pointer]
                self.bloco['bg'] = COLOR[2]
                self.bloco.grid(row=0, column=pointer)
            else:
                self.bloco['text'] = TITLE[pointer]
                self.bloco['bg'] = COLOR[3]
                self.bloco.grid(row=0, column=pointer)
            #
            self.bloco['width'] = len(self.bloco['text']) + 10

    #
    def inside_att(self,event):
        self.buttom_att['bg'] = COLOR[2]
        self.buttom_att['fg'] = COLOR[1]
    #
    def outside_att(self,event):
        self.buttom_att['bg'] = COLOR[3]
        self.buttom_att['fg'] = COLOR[2]

    # 
    def inside_delete(self,event):
        self.buttom_delete['bg'] = COLOR[2]
        self.buttom_delete['fg'] = COLOR[1]
       
    #
    def outside_delete(self,event):
        self.buttom_delete['bg'] = COLOR[3]
        self.buttom_delete['fg'] = COLOR[2]
 
    #
    def add_table(self, event):
        if len(event) == 0:
            return False
        else:
            pointer = 0
            for array in event:
                pointer += 1
                color = COLOR[2],COLOR[3]
                #
                for values in range(len(array)): 

                    self.bloco = tk.Label(self.table_frame)
                    self.bloco['height'] = 3
                    self.bloco['font'] = ('Arial', 11)
                    self.bloco['width'] = len(TITLE[values]) + 10
                    self.bloco['text'] = array[values]
                    #
                    if 4 <= values <= 6 :
                        if array[values]== 1: 
                            self.bloco['text'] = 'S'
                        else:
                            self.bloco['text'] = 'N'

                    #
                    if values == len(array)- 1:
                            self.bloco['font'] = ('Arial', 8)  
                            self.bloco['width'] = len(TITLE[values]) + 20
                            self.bloco['height'] = 4
                            self.bloco['text'] = array[values]                   
                    #        
                    if pointer % 2 != 0:
                        if values % 2 == 0:
                            self.bloco['bg'] = color[1]
                            self.bloco.grid(row=pointer, column=values)
                        else:
                            self.bloco['bg'] = color[0]
                            self.bloco.grid(row=pointer, column=values)
                    else:
                        if values % 2 == 0:
                            self.bloco['bg'] = color[0]
                            self.bloco.grid(row=pointer, column=values)
                        else:
                            self.bloco['bg'] = color[1]
                            self.bloco.grid(row=pointer, column=values)
        
    #
    def load_animation(self, event=None):
        self.buttom_att.config(state='disabled')
        self.loading = Loading(self.table_window)
        self.load_screen = self.table_window.create_window((600,300),window=self.loading,anchor='center')

        def att():
            if self.reload_table():
                self.buttom_att.config(state='normal')         
           
            self.table_window.delete(self.load_screen)

        threading.Thread(target= att).start()
      
    
    def reload_table(self) -> bool:

       self.reload = MySQLConnection(**CONFIG)
       self.cursor = self.reload.cursor()
       #
       self.cursor.execute('SELECT * FROM individuo ORDER BY Id DESC')
       self.add_table(self.cursor.fetchall())
       #
       self.table_frame.update_idletasks()
       self.table_window.config(scrollregion=self.table_frame.bbox('all'))
       return True
   

    def delete(self, event= False) -> bool:
        self.reload = MySQLConnection(**CONFIG)
        self.cursor = self.reload.cursor()    
        self.warning = messagebox.askyesno(title='Warning',message='Deseja deletar todos os registros?')
        self.cursor.execute('SELECT * FROM individuo')
    
        if len(self.cursor.fetchall()) > 0: 
            if self.warning:
                try:    
                    self.cursor.execute('DELETE FROM individuo')
                    self.reload.commit()
                except Error as erro:
                    print(f'\033[31m{erro}\033[m')
                    
                else:
                    self.reload.close()
                    self.cursor.close()
                    self.clear_table()
                    print(f'\033[33mregistros deletados!\033[m')
        else:
            messagebox.askokcancel(message='A tabela ja está vazia')
       
                

    def clear_table(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        #
        self.header()
    


