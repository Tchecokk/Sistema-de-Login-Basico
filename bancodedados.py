import sqlite3
import time
import os

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
    global verificador_de_escolha
    print("Olá bem vindo!")
    time.sleep(1)

    print(f"O que deseja fazer? \n 1) Fazer Login \n 2) Criar Conta")
    escolha = input("Digite apenas numeros: ")

    while True:
        if escolha == "1":
            verificador_de_escolha = 1
            break
        elif escolha == "2":
            verificador_de_escolha = 2
            break
        else:
            print("O numero escolhido não está disponivel.")
            time.sleep(0.5)
    
    
def fazer_login():
    os.system("cls")
    time.sleep(0.5)
    print("Você escolheu: Fazer login")
    
    usuario_não_encontrado = 0

    while True:
        if usuario_não_encontrado == 6:
            print("Limite de tentativas de login excedido!")
            break
        
        login_usuario = input("Usuario: ")
        login_senha = input("Senha: ")
        time.sleep(1)
    
        cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ? ", (login_usuario, login_senha))
        usuario_existe = cursor.fetchone()
    
        if usuario_existe:
            print(f"Login feito com sucesso, bem vindo {usuario_existe[0]}!")
            break
        else:
            print("Usuario ou senha incorretos.")
            time.sleep(0.5)
            
            os.system('cls')
            usuario_não_encontrado += 1

    conexao.close()

def criar_conta():
    os.system("cls")
    time.sleep(0.5)
    print("Você escolheu: Criar Conta")

    criar_usuario = input("Crie seu usuario: ")
    criar_senha = input("Crie sua senha: ")
    time.sleep(1)
    
    try:
        cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (criar_usuario, criar_senha))
        time.sleep(1)
        print("Conta criada com sucesso!")
        
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Já existe um usuario com esse nome.")
    finally:
        conexao.close()

criar_banco()
tela_inicial()

if verificador_de_escolha == 1:
    fazer_login()
if verificador_de_escolha == 2:
    criar_conta()