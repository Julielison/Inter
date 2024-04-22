# import subprocess

# def executar_processo_como_usuario_existente(usuario, comando):
#     # Comando para executar o processo como o usuário existente usando runas
#     comando_executar_como_usuario = f'runas /user:{usuario} "{comando}"'

#     # Executar o processo como o usuário existente
#     subprocess.run(comando_executar_como_usuario, shell=True)

# # Exemplo de uso
# executar_processo_como_usuario_existente('fulano', 'powershell.exe')

from argon2 import PasswordHasher

from argon2 import PasswordHasher

def encrypt_password(password):
    # Criar um objeto PasswordHasher
    ph = PasswordHasher()

    # Criptografar a senha
    hashed_password = ph.hash(password)

    # Pegar apenas a parte da senha (o hash)
    hash_only = hashed_password.split('$', 3)[3]

    return hash_only

# Senha a ser criptografada
senha = "minha_senha"

# Criptografar a senha e pegar apenas a parte do hash
senha_criptografada = encrypt_password(senha)

# Imprimir apenas a parte do hash
print("Apenas a parte do hash:", senha_criptografada)
