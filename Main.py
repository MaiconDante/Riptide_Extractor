# Importando bibliotecas do projeto
import customtkinter as ctk
from tkinter import PhotoImage, filedialog
from time import strftime
from pytubefix import YouTube
from threading import Thread
import os

# Variável root recebendo comando CTk que faz aparecer a janela
root = ctk.CTk()

# Criando a Classe da aplicação onde receberá todas execuções
class Application():
    def __init__(self):  # Construtor que recebe as propriedades do aplicativo
        self.root = root
        self.screen()
        self.appearance()
        self.frames_screen_up()
        self.frames_screen_down()
        self.buttons()
        self.clock()
        self.result()
        root.mainloop()

    # Função com todas caracteristicas da janela que foi configurada
    def screen(self):
        self.root.title("| Riptide Extractor Link |") # Titulo da janela do aplicativo
        self.widthscreen = 800 # Tamanho da largura da tela do aplicativo 
        self.heightscreen = 500 # Tamanho da altura da tela do aplicativo

        self.width_system = root.winfo_screenwidth() # Variavel recebendo informação da largura da resolução de tela do usuário
        self.height_system = root.winfo_screenheight() # Variavel recebendo informação da altura da resolução de tela do usuário
        
        self.posx = self.width_system/2-self.widthscreen/2 # Cálculo da posição x para deixar o aplicativo centralizado na tela do usuário
        self.posy = self.height_system/2-self.heightscreen/2 # Cálculo da posição y para deixar o aplicativo centralizado na tela do usuário
        self.root.geometry("%dx%d+%d+%d" % (self.widthscreen, self.heightscreen, self.posx, self.posy)) # Exibindo tela aplicativo na proporção calculada
        self.root.resizable(False, False) # Configuração para deixar tela redimensionável
        self.root.maxsize(width=800, height=500) # Configuração para colocar o máximo que o aplicativo pode redimensionar
        self.root.minsize(width=600, height=400) # Configuração para colocar o mínimo que o aplicativo pode redimensionar
    
    # Função que seta a cor do tema do aplicativo se escuro, claro ou do sistema
    def appearance(self):
        self.root._set_appearance_mode("system")

    # Função que realiza criação do frame parte de cima do aplicativo definindo conteudo que irá compor dentro
    def frames_screen_up(self):
        self.frameup = ctk.CTkFrame(self.root,
                                    fg_color="#ffc1a6",
                                    bg_color="#d66a04",
                                    corner_radius=50,
                                    border_width=10)
        self.frameup.place(relx=0.01,
                           rely=0.01,
                           relwidth=0.98,
                           relheight=0.4)
        self.img = PhotoImage(file="./Riptide_Extractor/riptidelogo.png")
        self.label_logo = ctk.CTkLabel(self.frameup,
                                       width=50,
                                       height=50,
                                       image=self.img,
                                       text="")
        self.label_logo.place(relx=0.043,
                              rely=0.19,
                              relwidth=0.28,
                              relheight=0.75)
        self.label_name_app = ctk.CTkLabel(self.frameup,
                                           text="| RIPTIDE EXTRACTOR LINK |",
                                           text_color="black", font=("Arial", 12),
                                           fg_color="#f55e07")
        self.label_name_app.place(relx=0.54,
                                  rely=0.15,
                                  relwidth=0.22,
                                  relheight=0.1)
        self.text_box = ctk.CTkTextbox(self.frameup,
                                       width=200,
                                       height=200,
                                       border_color="#f55e07",
                                       corner_radius=20,
                                       text_color="#f55e07",
                                       border_width=2)
        self.text_box.place(relx=0.41,
                            rely=0.3,
                            relwidth=0.48,
                            relheight=0.6)
        self.text_box.insert("2.2", "         | Extração de conteúdo do video do YOUTUBE |\n\n       | EXTRAIR somente o audio, gerando arquivo MP3 |\n\n       | EXTRAIR o video completo gerando arquivo MP4 |")
        self.text_box.configure(state="disabled") # Aqui desabilita a possibilidade de editar no textbox

    # Função que realiza criação do frame parte de baixo do aplicativo definindo conteudo que irá compor dentro
    def frames_screen_down(self):
        self.framedown = ctk.CTkFrame(self.root,
                                      fg_color="#ffc1a6",
                                      bg_color="#d66a04",
                                      corner_radius=50)
        self.framedown.place(relx=0.01,
                             rely=0.41,
                             relwidth=0.98,
                             relheight=0.57)
        self.label_link = ctk.CTkLabel(self.framedown,
                                       width=20, height=20,
                                       text="LINK",
                                       font=("Arial Black", 18),
                                       corner_radius=40, fg_color="#f55e07")
        self.label_link.place(relx=0.1,
                              rely=0.2,
                              relwidth=0.2,
                              relheight=0.15)
        self.box_link = ctk.CTkEntry(self.framedown,
                                     width=50,
                                     height=50,
                                     corner_radius=10,
                                     fg_color="#f5ac82",
                                     text_color="gray")
        self.box_link.place(relx=0.31,
                            rely=0.2,
                            relwidth=0.6,
                            relheight=0.15)
        self.box_link.insert(0, "Digite ou Cole aqui o seu link aqui !!!")
        self.box_link.bind("<FocusIn>", self.on_entry_click)
        self.box_link.bind("<FocusOut>", self.on_focusout)

    def on_entry_click(self, event):
        if self.box_link.get() == "Digite ou Cole aqui o seu link aqui !!!":
            self.box_link.delete(0, "end") 
            self.box_link.configure(text_color="gray") 

    def on_focusout(self, event):
        if self.box_link.get() == "":
            self.box_link.insert(0, "Digite ou Cole aqui o seu link aqui !!!")
            self.box_link.configure(text_color="gray")  
            
    def buttons(self):
        self.btn_mp3 = ctk.CTkButton(self.framedown,
                                     text="GERAR |MP3|",
                                     font=("Arial Black", 12),
                                     width=50, height=50,
                                     corner_radius=50,
                                     fg_color="#992002",
                                     hover_color="#04026b",
                                     command="")
        self.btn_mp3.place(relx=0.31,
                           rely=0.5,
                           relwidth=0.2,
                           relheight=0.15)
        
        self.btn_mp4 = ctk.CTkButton(self.framedown,
                                     text="GERAR |MP4|",
                                     font=("Arial Black", 12),
                                     width=50,
                                     height=50,
                                     corner_radius=50,
                                     fg_color="#992002",
                                     hover_color="#04026b",
                                     command="")
        self.btn_mp4.place(relx=0.53,
                           rely=0.5,
                           relwidth=0.2,
                           relheight=0.15)
        
        self.btn_cancel = ctk.CTkButton(self.framedown,
                                    text="FECHAR",
                                    font=("Arial Black", 12),
                                    width=50,
                                    height=50,
                                    corner_radius=50,
                                    fg_color="#992002",
                                    hover_color="#04026b",
                                    command=self.root.destroy)  # Fechar a janela
        self.btn_cancel.place(relx=0.15,
                           rely=0.51,
                           relwidth=0.13,
                           relheight=0.15)
    
    def clock(self):
        def time():
            string = strftime("%H: %M: %S %p")
            self.clock_lbl.configure(text=string)
            self.clock_lbl.after(500, time)
            
        self.clock_lbl = ctk.CTkLabel(self.framedown,
                                      font=("ds-digital", 15, "bold"),
                                      fg_color="transparent",
                                      text_color="#521205")
        self.clock_lbl.place(relx=0.75,
                             rely=0.5,
                             relwidth=0.15,
                             relheight=0.15)
        time()   
    
    def result(self):
        self.label_info = ctk.CTkLabel(self.framedown,
                                       text="O seu vídeo será convertido... | ESCOLHA E CLIQUE |",
                                       text_color="black", font=("Arial", 18, "bold"),
                                       fg_color="#ff7f4d",
                                       corner_radius=50)
        self.label_info.place(relx=0.12,
                              rely=0.75,
                              relwidth=0.75,
                              relheight=0.15)

Application() 