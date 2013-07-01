# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


JogadorReg = namedtuple("JogadorReg", "codigo, nome, nick,jogos_completos,vitorias,objetos_saidos")
listajogador = []


def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listajogador)):
        if listajogador[i].codigo == codigo:
            pos = i
            break
                            
    return pos

def inserir_jogador():
    codigo = input("Qual o codigo? ")

    pos = encontrar_posicao(codigo)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("Qual o nome? ")
    nick = raw_input('Qual e o nick? ')
    jogos_completos = 0
    vitorias = 0
    objetos_saidos = 0
    registo = JogadorReg(codigo, nome, nick,jogos_completos,vitorias,objetos_saidos)
    listajogador.append(registo)


def listar_jogador():
    print "Código  | ", 
    print "Nome    | ", 
    print "Nick    | ", 
    print "Jogos Completos | ", 
    print "Vitorias:  | "
    for i in range (len(listajogador)):
        print listajogador[i].codigo, " | ", 
        print listajogador[i].nome, " | ", 
        print listajogador[i].nick, " | ", 
        print listajogador[i].jogos_completos, " | ", 
        print listajogador[i].vitorias, " | "
        #print "Objetos ja saidos: ", listajogador[i].objetos_saidos

def eliminar_jogador():
    codigo = input ("Código do jogador a eliminar --> ")

    pos = encontrar_posicao(codigo)

    if pos == -1:
        print "Não existe aluno com esse código"
        return
    # TODO: Confirmar eliminação
    listajogador.pop(codigo)


    
def alterar_jogador():
    codigo = input ("Código do jogador a alterar --> ")
    
    pos = encontrar_posicao(codigo)

    if pos == -1:
        print "Não existe aluno com esse código"
        return

    # só altera o nome
    novo_nome = raw_input("Qual o nome? ")
    novo_nick= raw_input("Qual o nick? ")
    
    listajogador[codigo] = listajogador[codigo]._replace(nome=novo_nome,nick=novo_nick)



        

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










