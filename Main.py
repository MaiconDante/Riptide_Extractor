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

Application() 