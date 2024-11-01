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
        root.mainloop()

Application() 