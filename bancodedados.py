import sqlite3
import os
import time

os.system('cls' or 'clear')

conexao = sqlite3.connect('banco.db')
comando = conexao.cursor()

comando.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)")
conexao.commit()

while True:
    try:
        nome = input("Qual seu nome? ")
        time.sleep(0.5)
        idade = int(input("Qual sua idade? "))
        
        comando.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
        conexao.commit()
        print("Usuário inserido com sucesso!")
        time.sleep(1)
        break  
    except ValueError:
        print("Erro na escrita! Por favor, insira um número para a idade e tente novamente.")
        time.sleep(1)

comando.execute("SELECT nome, idade FROM usuarios")
usuarios = comando.fetchall()

for usuario in usuarios:
    nome_usuario, idade_usuario = usuario
    print(f"Nome: {nome_usuario}, Idade: {idade_usuario}")

print("Lista Finalizada")
conexao.close()