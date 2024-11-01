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
     

Application() 