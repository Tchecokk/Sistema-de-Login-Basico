import sqlite3
import os
import time

os.system('cls' or 'clear')

conexao = sqlite3.connect('banco.db')
comando = conexao.cursor()

comando.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT UNIQUE NOT NULL, senha INTEGER NOT NULL)")
conexao.commit()

while True:
    try:
        print("Deseja fazer o que? \n 1. Fazer Login \n 2. Criar Conta")
        escolha = int(input(""))
        break
    except ValueError:
        print("Por favor escolha um dos numeros")

if escolha == 1:
    login = True
    criar_conta = False
if escolha == 2:
    criar_conta = True
    login = False

while criar_conta == True:
    try:
        print("Crie uma conta")
        nome = input("Qual seu nome? ")
        time.sleep(0.5)
        senha = int(input("Qual sua senha? "))
        
        comando.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
        conexao.commit()
        print("Usuário inserido com sucesso!")
        print("Lista Finalizada")
        time.sleep(1)
        break  
    except ValueError:
        print("Erro na escrita! Por favor, insira um número para a senha e tente novamente.")
        time.sleep(1)
    except sqlite3.IntegrityError:
        print("Este nome de usuário já está em uso. Tente outro.")
    finally:
        comando.execute("SELECT nome, senha FROM usuarios")
    usuarios = comando.fetchall()

    for usuario in usuarios:
        nome_usuario, senha_usuario = usuario
        print(f"Nome: {nome_usuario}, Senha: {senha_usuario}")

while login == True:
    print("Login")
    
    log_nome = input("Digite sua nome: ")
    log_senha= int(input("Digite sua senha: "))

    comando.execute("SELECT nome FROM usuarios WHERE nome = ? AND senha = ?", (log_nome, log_senha))
    usuario_encontrado = comando.fetchone()

    if usuario_encontrado:
        print(f"Login bem-sucedido! Bem-vindo, {usuario_encontrado[0]}.")
        break
    else:
        print("Nome de usuário ou senha inválidos.")
conexao.close()