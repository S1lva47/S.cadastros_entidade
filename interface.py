from config import *
from tkinter import *
from tkinter import ttk, messagebox
from mysql.connector import MySQLConnection 
from mysql.connector import Error 
from table import *

# 
class Connection:  
    def __init__(self, kwarg):   
    
        #CONEXÂO  
        try: 
            self.conn = MySQLConnection(**kwarg)
            self.cursor = self.conn.cursor()
                
        except Error as error:
            print(f'\033[31mErro:{error}\033[m')
        else:
            print('\033[32mDatabase connected!\033[m')

    def add(self,*kwargs):  
        try:
            self.cursor.execute('INSERT INTO individuo(Id, Specie, City, Date, Stable, Injured, Stressed, Observation ) VALUE (%s,%s,%s,%s,%s,%s,%s,%s)',
                                kwargs )                         
        except Error as erro:
            print(f'\033[31m]erro de {erro}\033[m')
        else:
            #CONFIRMA A INSERÇÃO DOS NOVOS DADOS DE FORMA PERMANENTE
            self.conn.commit()
            # 
            print('\033[34mIndividuo cadastrado!\033[m') 
       
   
    def disconnect(self):
        try:
            self.conn.close()
            self.cursor.close()
        except Error as erro:
            print(f'\033[31mErro: {erro}\033[m')
        else:
            print('\033[34mDatabase disconnected...\033[m')


class Window(Connection):
    def __init__(self, kwarg ):
        # Inicializando a super classe "Connection" 
        Connection.__init__(self, kwarg)
        #
        self.main_window = Tk()
        self.main_window.title('Sistema de cadastros')
        self.main_window.geometry('1000x1000')
        #
        self.opened = False
        #
        self.interface() 
    
        
    def interface(self, event=False):
        if self.datas_exists():
            self.main_window = self.creat_aba()
            self.opened = True
      
        # Aparência        
        self.frame_canva = Frame(self.main_window)
        self.frame_canva['height'] = HEIGHT + 360
        self.frame_canva['width'] = WIDTH + 700
        self.frame_canva['bg'] = COLOR[2]
               
        self.frame_canva.place(x=200, y=30)
    
        #Title 
        self.frame = Frame(  self.frame_canva) 
        self.label = Label(self.frame)
        self.label['text']= EXTRAS[0]  
        self.label['fg']= COLOR[1] 
        self.label['height'] = 3
        self.label['font'] = ('Arial', 20 )
        self.label['bg'] = COLOR[2]

        self.label.pack(fill='y')
        self.frame.place(y= 70, x=340)

        #Entry boxes
        #Id
        self.frame_id = Frame( self.frame_canva)
        self.label_id = Label(self.frame_id )
        self.label_id['text'] = TITLE[0]
        self.label_id['width'] = 26
        self.label_id['bg'] = COLOR[2]
        # dynamics datas of entry and exit for "ids"
        self.entry_id_clear = StringVar()
        self.entry_id = Entry(self.frame_id)    
        self.entry_id['textvariable']= self.entry_id_clear
        self.entry_id['width'] = 30
        #   
        #
        self.label_id.pack()
        self.entry_id.pack()
        self.frame_id.place(x=70, y =170)
        #

        #Type of specie
        self.frame_specie = Frame( self.frame_canva)
        self.label_specie = Label(self.frame_specie )
        self.label_specie['text'] = TITLE[1]
        self.label_specie['width'] = 26
        self.label_specie['bg'] = COLOR[2]

        # dynamics datas of entry and exit for "Type of Species"
        self.entry_specie_clear = StringVar()
        self.entry_specie= Entry(self.frame_specie)
        self.entry_specie['textvariable']=self.entry_specie_clear
        self.entry_specie['width'] = 30
        #
        #
        self.label_specie.pack()
        self.entry_specie.pack()
        self.frame_specie.place(x=290, y =170)
        #
    
        #City
        self.frame_city = Frame(  self.frame_canva )
        self.label_city = Label(self.frame_city )
        self.label_city['text'] = TITLE[2]
        self.label_city['width'] = 26
        self.label_city['bg'] = COLOR[2]

        # dynamics datas of entry and exit for city
        self.entry_city_clear = StringVar()
        self.entry_city = Entry(self.frame_city)
        self.entry_city['textvariable']=self.entry_city_clear
        self.entry_city['width'] = 30
        #
        # 
        self.label_city.pack()
        self.entry_city.pack()
        self.frame_city.place(x=510, y =170)
        #
      
        # Date
        self.frame_date = Frame(  self.frame_canva )
        self.label_date = Label(self.frame_date )
        self.label_date['text'] = TITLE[3]
        self.label_date['width'] = 9
        self.label_date['bg'] = COLOR[2]

        # dynamics datas of entry and exit for date
        self.entry_date_clear = StringVar()
        self.entry_date = Entry(self.frame_date)
        self.entry_date['textvariable']=self.entry_date_clear
        self.entry_date['width'] = 10
        #       
        #
        self.label_date.pack()
        self.entry_date.pack()
        self.frame_date.place(x=720, y =170)
        #

        #Observations
        self.entry_style = ttk.Style()
        self.entry_style.configure('Custom.TEntry', padding=50, width=30)

        self.frame_obs = Frame(self.frame_canva)
        self.entry_obs_clear = StringVar(value=' _ ')
        self.entry_obs = ttk.Entry(self.frame_obs, style='Custom.TEntry')
        self.entry_obs['textvariable'] = self.entry_obs_clear
        self.label_obs = Label(self.frame_obs, text= TITLE[7]+':')
        self.label_obs['bg'] = COLOR[2]
        self.label_obs['width'] = 50

        #
        #
        self.frame_obs.place(y=410, x=70)
        self.label_obs.place( x=-130)
        self.entry_obs.pack(fill='y', expand='True')
        #

        #Check bottons 
        #1
        self.entry_check1 = IntVar()
        self.checkbotton1 = Checkbutton(  self.frame_canva,
        text=TITLE[4], variable= self.entry_check1 )
        self.checkbotton1['bg'] = COLOR[2]
        self.checkbotton1.place(x =70, y=270)
        #2 
        self.entry_check2 = IntVar()
        self.checkbotton2 = Checkbutton(  self.frame_canva,
        text=TITLE[5], variable= self.entry_check2 )
        self.checkbotton2['bg'] = COLOR[2]
        self.checkbotton2.place(x =70, y=310)
        #3
        self.entry_check3 = IntVar()
        self.checkbotton3 = Checkbutton(  self.frame_canva,
        text=TITLE[6], variable= self.entry_check3 )
        self.checkbotton3['bg'] = COLOR[2]
        self.checkbotton3.place(x =70, y=350)
   
        #Button
        self.button_exit = Button(self.frame_canva)
        self.button_exit['text'] = EXTRAS[3]

        # USING FUNCTION disconnect() FROM THE SUPERCLASS  
        self.button_exit['command'] = self.exit
        self.button_exit['width'] = 10
        #
        self.button_exit.place(x=800, y=20)
        #
        #
        self.button_add = Button(  self.frame_canva)
        self.button_add['text'] = EXTRAS[1]
        self.button_add['width'] = 10
        
        # USING FUNCTION add() FROM THE SUPERCLASS  
        self.button_add['command'] = self.create_firstaba
        #
        self.button_add.place(y=500, x=700)
        #  
        #
        self.button_cancel = Button(self.frame_canva)
        self.button_cancel['text'] = EXTRAS[2]
        self.button_cancel['command'] = self.cancel
        self.button_cancel['width'] = 10
        #     
        self.button_cancel.place(y=500, x=800)
        #
                   
        self.mainloop = mainloop()
      

   #CLOSE THE SISTEM AND DISCONECT FROM THE DATABASE
    def exit(self):
        try:
            self.main_window.quit()
        except Exception as error:
            messagebox.showerror(error.__class__)
        else:
            self.disconnect()
    
    def add_to_db(self):
        self.add(self.entry_id.get(),self.entry_specie.get(), self.entry_city.get(),
                self.entry_date.get(), self.entry_check1.get(),self.entry_check2.get(),
                self.entry_check3.get(), self.entry_obs.get())
        self.cancel()

    #RESETA OS DADOS INSERIDOS
    def cancel(self):
        self.entry_id_clear.set(' ')
        self.entry_specie_clear.set(' ')
        self.entry_city_clear.set(' ')
        self.entry_date_clear.set(' ')
        self.entry_obs_clear.set(' ')
        self.entry_check1.set(0)
        self.entry_check2.set(0)
        self.entry_check3.set(0)

    def datas(self):
        self.cursor.execute('select * from individuo ORDER BY Id DESC')
         #retorna uma lista de tuplas com os resultados da consulta 
        return self.cursor.fetchall()
 
    
    def datas_exists(self):
        return True if len(self.datas()) > 0 else False
    

    def creat_aba(self, delete=False) :
    
        ##
        self.notebook = ttk.Notebook(self.main_window, height=600, width=1230)
            
        #Aba de navegação Interface
        self.main_aba = Frame(self.notebook)
        self.notebook.add(self.main_aba, text='Interface')
        self.notebook.place()

        #Aba de navegação Tabela 
        self.notebook_ = self.notebook
        self.table = Table(self.notebook_, self.datas()) #Retorna os dados p/ a classe Table, caso eles existam.
        self.notebook_.add(self.table.table_window, text='Tabela')          
        #
        self.notebook.place(y=10, x=0, relwidth=1)
        # 
        return self.main_aba 
      
  
    # Cria as abas de navegação após a inserção do primeiro registro 

    def create_firstaba(self) -> bool:
        self.add_to_db()
        # 
        if len(self.datas()) > 0:
            if self.opened is True:
                return False
            else:
                self.interface()


        






