# -*- coding: utf-8 -*-

import menu
import Jogadores
import util
import Objetos
import jogo



# nome dos ficheiros
fxJogadores = "fxJogadores.dat"
fxObjetos = "fxObjetos.dat"

def ler_ficheiros():
    # adicionar todos ficheiros a ler
    Jogadores.listajogador = util.ler_ficheiro(fxJogadores)
    Objetos.listaobjeto = util.ler_ficheiro(fxObjetos)


def escrever_ficheiros():
    # adicionar todos ficheiros a guardar
    util.escrever_ficheiro(fxJogadores, Jogadores.listajogador)
    util.escrever_ficheiro(fxObjetos, Objetos.listaobjeto)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        Jogadores.gerir()
    elif op == '2':
        Objetos.gerir ()
    elif op == '3':
        jogo.start()
    elif op == '0':
        terminar = True


escrever_ficheiros()


