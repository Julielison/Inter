import tkinter as tk
from testes.database_crud import *

# Pega o nome do usuário
def get_name_user():
    username = entry.get()
    print('guardou')
#  
    # Instancia uma conexão com o banco de dados
    data = Database()

    # Checa se o nome de usuário já existe 
    #if data.check_username(username):
    #     pass


# Cria uma instância da classe Tk para representar a janela principal
root = tk.Tk()

# Define o título da janela
#teste
root.title("Interpretador de Comandos")

# Define o tamanho da janela
root.geometry("600x400")

# Permitir redimensionamento tanto na largura quanto na altura
root.resizable(True, True)

# Título do input
label = tk.Label(root, text="Digite seu nome de usuário:")
label.pack()

# Cria um campo de entrada
entry = tk.Entry(root)
entry.pack()

# Cria um botão para obter o texto inserido
botao = tk.Button(root, text="Iniciar", command=get_name_user)
botao.pack()

root.bind('<Return>', lambda event=None: get_name_user())


# Inicia o loop principal da interface gráfica
root.mainloop()