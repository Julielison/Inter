import tkinter as tk
from tkinter import messagebox
from login import LoginWindow

def create_main_window():
    root = tk.Tk()
    root.title("Interpretador de Comandos")
    root.geometry("600x400")
    root.resizable(True, True)

    login_window = LoginWindow(root)
    login_window.pack()  # Corrigindo para exibir a janela de login

    root.mainloop()

if __name__ == "__main__":
    create_main_window()