#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Este módulo implementa um CRUD de contatos em um banco de dados SQLite.

@author: Ricardo
"""
import sys
import sqlite3
import os

banco = os.path.join("contatos/", "contatos.db")

def criaTabela():
    """
    Cria a tabela contatos no banco de dados contatos.db
    """
    conn = sqlite3.connect(banco)
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE contatos (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            salario REAL
            )
            """)
        print("Tabela criada")
    except sqlite3.Error as e:
        print("Erro ao criar tabela: ", e)
    finally:
        if conn:
            conn.close()
    return

def cadastrar():
    """
    Cadastra um novo registro na tabela contatos.

    Solicita ao usuário o nome, idade e salário do contato a ser cadastrado.
    """
    print("Cadastrar")
    nome = input("Entre com o nome (str): ")
    idade = int(input("Entre com a idade (int): "))
    salario = float(input("Entre com o salário (float): "))
    conn = sqlite3.connect(banco)
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contatos (nome, idade, salario) VALUES (?,?,?)",
        (nome, idade, salario))
        conn.commit()
        print("Dados inseridos com sucesso")
    except sqlite3.Error as e:
        print("Erro ao inserir dados")
    finally:
        if conn:
            conn.close()
    return

def editar():
    """
    Edita um registro na tabela contatos a partir do id do registro.

    Solicita ao usuário o id do registro a ser editado, e os novos dados.
    """
    print("Editar")
    idReg = int(input("Entre com o id do registro a ser editado: "))
    nome = input("Entre com o nome (str): ")
    idade = int(input("Entre com a idade (int): "))
    salario = float(input("Entre com o salário (float): "))
    conn = sqlite3.connect(banco)
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE contatos SET nome=?, idade=?, salario=? WHERE id=?", (nome, idade, salario, idReg))
        conn.commit()
        print("Registro editado")
    except sqlite3.Error as e:
        print("Erro ao editar registro")
    finally:
        if conn:
            conn.close()
    return

def apagar():
    """
    Apaga um registro na tabela contatos a partir do id do registro.

    Solicita ao usuário o id do registro a ser apagado.
    """
    print("Apagar")
    idReg = int(input("Entre com o id do registro a ser apagado: "))
    conn = sqlite3.connect(banco)
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contatos WHERE id=?", (idReg,))
        conn.commit()
        print("Registro %d apagado" % idReg)
    except sqlite3.Error as e:
        print("Erro ao apagar registro")
    finally:
        if conn:
            conn.close()
    return

def listar():
    """
    Lista todos os registros da tabela contatos.
    """

    print("Listar")
    conn = sqlite3.connect(banco)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contatos")
        for linha in cursor.fetchall():
            print(linha)
    except sqlite3.Error as e:
        print("Erro ao acessar registro")
    finally:
        if conn:
            conn.close()

def sair():
    """
    Encerra a execução do programa.
    """
    print("Terminado")
    sys.exit()
    return

def main():
    """
    Função principal do programa.

    Verifica se o banco de dados existe, se não existir cria o banco e a tabela.
    Exibe o menu de opções e chama a função correspondente à opção escolhida.
    """
    
    if not os.path.exists(banco):
        criaTabela()
    else:
        print("Não foi necessário criar a tabela")
    
    switcher = {
    'A': cadastrar,
    'B': editar,
    'C': apagar,
    'D': listar,
    'Z': sair,
    }
    
    while True:
        print("(A) Cadastrar contato\n(B) Editar contato\n(C) Apagar contato\n(D) Listar contato\n(Z) Terminar")
        opcao = input("Entre com a opção: ").upper()
        switcher.get(opcao, lambda: print("Opção inválida"))()


if __name__ == "__main__":
    main()
