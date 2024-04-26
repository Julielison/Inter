import tkinter as tk
from tkinter import messagebox
import dataBaser

class LoginError(Exception):
    """Exceção personalizada para erros de login."""
    def __init__(self, message):
        super().__init__(message)

class LoginWindow(tk.Frame):
    """Classe para a janela de login."""
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.label_username = tk.Label(self, text="Usuário:")
        self.label_username.pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        self.label_password = tk.Label(self, text="Senha:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        self.button_frame = tk.Frame(self)
        self.button_frame.pack()

        self.button_login = tk.Button(self.button_frame, text="Entrar", command=self.login)
        self.button_login.pack(side=tk.LEFT, padx=5, pady=5)

        self.button_open_signup = tk.Button(self.button_frame, text="Cadastrar", command=self.open_signup_window)
        self.button_open_signup.pack(side=tk.LEFT, padx=5, pady=5)

    def login(self):
        """Função para realizar o login."""
        user = self.entry_username.get()
        password = self.entry_password.get()

        dataBaser.cursor.execute("""
        SELECT User, Password FROM Users
        WHERE User = ? and Password = ?          
        """, (user, password))
        print("Selecionou")
        try: 
            if dataBaser.cursor.fetchone() is None:
                raise LoginError("Usuário ou senha incorretos.")
            else:
                messagebox.showinfo(title="Login", message="Login bem-sucedido!")
        except LoginError as le:
            messagebox.showerror(title="Login", message=str(le))

    def open_signup_window(self):
        """Função para abrir a janela de cadastro."""
        signup_window = SignupWindow(self.master)

class SignupWindow(tk.Toplevel):
    """Classe para a janela de cadastro."""
    def __init__(self, master):
        super().__init__(master)
        self.title("Cadastro de Usuário")
        self.geometry("400x300")  

        self.label_username = tk.Label(self, text="Usuário:")
        self.label_username.pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        self.label_password = tk.Label(self, text="Senha:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        self.button_create_account = tk.Button(self, text="Criar Conta", command=self.register_user)
        self.button_create_account.pack()

    def register_user(self):
        """Função para registrar um novo usuário."""
        user = self.entry_username.get()
        password = self.entry_password.get()

        if not user or not password:
            messagebox.showerror(title="Register Error", message="Preencha Todos os Campos!!")
            return

        dataBaser.cursor.execute("""
        INSERT INTO Users(User, Password) VALUES(?, ?)
        """, (user, password))
        dataBaser.conn.commit()
        messagebox.showinfo(title="Register Info", message="Registro Realizado com Sucesso")
        
        self.destroy()