# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


jogadorReg = namedtuple("jogadorReg", "id, nome,nick,jogos_completos,vitorias,objetos_saidos")
listajogador = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listajogador)):
        if listajogador[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_jogador():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("Qual o nome? ")
    nick= raw_input ('Qual e o nick ? ')
    
    registo = jogadorReg(cod, nome, nick, 0, 0, [])
    listajogador.append(registo)



def listar_jogador():
    for i in range (len(listajogador)):
        print "Código: ", listajogador[i].id
        print "Nome: ", listajogador[i].nome
        
  

def eliminar_jogador():
    cod = input ("Código do jogador a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe aluno com esse código"
        return

    # TODO: Confirmar eliminação
    listajogador.pop(pos)


    
def alterar_jogador():
    cod = input ("Código do jogador a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe jogador com esse código"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome? ")
    listajogador[pos] = listajogador[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.jogador()

        if op == '1':
            inserir_jogador()
        elif op =='2':
            listar_jogador()
        elif op == '3':
            alterar_jogador()
        elif op == '4':
            eliminar_jogador()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










