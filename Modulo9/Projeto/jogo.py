# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:18:20 2013

@author: i12168
"""

import Jogadores
import Objetos

from random import choice

NJOGADORES = 0
jogadores = []
objetosSaidos = []
objetosPorSair = []

for i in range (len(Jogadores.listajogador)):
    print Jogadores.listajogador.codigo[i]
    print Jogadores.listajogador.nome[i]
    
    
 
def num_jogadores():
    print ' +----------------+'    
    print ' | 1- 2 jogadores |'
    print ' | 2- 4 jogadores |'
    print ' +----------------+'
    print ' | 0- Sair        |'
    print ' +----------------+'
    
    op = raw_input ('Qual e a opçao que deseja? ')
    if op == '1':
        return 2
    elif op == '2':
        return 4
    


def encontraJogador(cod):
    for i in range(len(Jogadores.listajogador)):
        if Jogadores.listajogador[i].codigo == cod:
            print Jogadores.listajogador[i].nick
            return Jogadores.listajogador[i]



def escolherObjeto():
    for i in range(2):
        print choice(objetosPorSair)
    


def jogar():
  #  vitoria = False

   # while  not vitoria:
        escolherObjeto()
    
        
    
def start():
    global NJOGADORES
    global objetosPorSair    
    
    NJOGADORES = num_jogadores()
    
    objetosPorSair = Objetos.listaobjeto[:]
    
    #escolher jogadores
    for i in range(NJOGADORES):
        cod = input("Codigo do jogador --> ")
        j = encontraJogador(cod)
        jogadores.append(j)
        print "Jogador ", j.nick, "! Você é concorrente!"
        
    jogar()
    
    