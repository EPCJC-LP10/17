# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 12:17:22 2013

@author: i12168
"""

from collections import namedtuple

import menu


objetoReg = namedtuple("objetoReg", "codigo,nome,marca,modelo,preco")
listaobjeto = []

def inserir_objeto():
    codigo = input("Qual o codigo? ")

    #if codigo >= 0:
    #    print "Código já existe"
    #    return

    #ler dados
    nome = raw_input("Qual o nome? ")
    marca = raw_input('Qual a marca? ')
    modelo= raw_input('Qual o modelo? ')
    preco= raw_input('Qual o preço? ')
    registo = objetoReg(codigo, nome,marca,modelo,preco)
    listaobjeto.append(registo)


def listar_objeto():
    for i in range (len(listaobjeto)):
        print "Código: ", listaobjeto[i].codigo
        print "Nome: ", listaobjeto[i].nome
        print "Marca: ", listaobjeto[i].marca
        print "Modelo: ", listaobjeto[i].modelo
        print "Preço: ", listaobjeto[i].preco
  

def eliminar_objeto():
    codigo = input ("Código do objeto a eliminar --> ")

    if codigo == -1:
        print "Não existe objeto com esse código"
        return

    # TODO: Confirmar eliminação
    listaobjeto.pop(codigo)


    
def alterar_objeto():
    codigo = input ("Código do objeto a alterar --> ")

    if codigo == -1:
        print "Não existe objeto com esse código"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome? ")
    novomarca = raw_input("Qual a marca? ")
    novomodelo= raw_input("Qual e o modelo? ")
    novopreco= raw_input('Qual e o preço?' )
    listaobjeto[codigo] = listaobjeto[codigo]._replace(nome=novonome,marca=novomarca,modelo=novomodelo,preco=novopreco)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.objetos()

        if op == '1':
            inserir_objeto()
        elif op =='2':
            listar_objeto()
        elif op == '3':
            alterar_objeto()
        elif op == '4':
            eliminar_objeto()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"