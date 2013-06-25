# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 12:17:22 2013

@author: i12168
"""

from collections import namedtuple

import menu


objetoReg = namedtuple("objetoReg", "id, nome,marca,modelo,preco")
listaobjeto = []



def encontrar_objeto(codigo):
    pos = -1
    for i in range (len(listaobjeto)):
        if listaobjeto[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_objeto():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("Qual o nome? ")
    marca = raw_input('Qual a marca? ')
    modelo= raw_input('Qual o modelo')
    preco= raw_input('Qual o preço)
    registo = objetoReg(cod, nome,marca,modelo,preco)
    listaobjeto.append(registo)



def listar_objeto():
    for i in range (len(listaobjeto)):
        print "Código: ", listaobjeto[i].id
        print "Nome: ", listaobjeto[i].nome
        
  

def eliminar_objeto():
    cod = input ("Código do objeto a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe objeto com esse código"
        return

    # TODO: Confirmar eliminação
    listaobjeto.pop(pos)


    
def alterar_objeto():
    cod = input ("Código do objeto a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe objeto com esse código"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome? ")
    listaobjeto[pos] = listaobjeto[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.objeto()

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