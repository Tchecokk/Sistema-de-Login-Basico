import sqlite3
import time
import os
import bcrypt
import getpass

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

def criar_banco():
    os.system("cls")
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL)''')
    conexao.commit()

def tela_inicial():
    print("Olá bem vindo!")
    time.sleep(1)

    print(f"O que deseja fazer? \n 1) Fazer Login \n 2) Criar Conta")

    while True:
        escolha = input("Digite apenas numeros: ").strip()

        if escolha == "1":
            return 1
        elif escolha == "2":
            return 2
        else:
            print("O numero escolhido não está disponivel.")
            time.sleep(0.5)
    
    
def fazer_login():
    os.system("cls" if os.name == 'nt' else 'clear')
    time.sleep(0.5)
    print("Você escolheu: Fazer login")
    
    usuario_não_encontrado = 0

    while True:
        if usuario_não_encontrado == 6:
            print("Limite de tentativas de login excedido!")
            break
        
        login_usuario = input("Usuario: ")
        login_senha = getpass.getpass("Senha: ")
        time.sleep(1)

        login_senha_bytes = login_senha.encode('utf-8')
    
        cursor.execute("SELECT nome, senha FROM usuarios WHERE nome = ?", (login_usuario,))
        usuario_existe = cursor.fetchone()
    
        if usuario_existe:
            try:
                if bcrypt.checkpw(login_senha_bytes, usuario_existe[1]):
                    print(f"Login feito com sucesso, bem vindo {usuario_existe[0]}!")
                    break
                else:
                    print("Usuario ou senha incorretos.")
            except ValueError:
                print("Erro de segurança: Hash de senha inválido no banco de dados.")
        else:
            print("Usuario ou senha incorretos.")
            time.sleep(0.5)
            
            os.system("cls" if os.name == 'nt' else 'clear')
            usuario_não_encontrado += 1 

def criar_conta():
    os.system("cls" if os.name == 'nt' else 'clear')
    time.sleep(0.5)
    print("Você escolheu: Criar Conta")

    criar_usuario = input("Crie seu usuario: ")
    criar_senha = getpass.getpass("Crie sua senha: ")
    criar_senha_bytes = criar_senha.encode('utf-8')

    sal = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(criar_senha_bytes, sal)

    time.sleep(1)
    
    try:
        cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (criar_usuario, senha_hash))
        time.sleep(1)
        print("Conta criada com sucesso!")
        
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Já existe um usuario com esse nome.")

criar_banco()
verificador_de_escolha = tela_inicial() 

if verificador_de_escolha == 1:
    fazer_login()
elif verificador_de_escolha == 2:
    criar_conta()

conexao.close()