# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:18:20 2013

@author: i12168
"""

import Jogadores
import Objetos

from random import choice
import operator

#penalizaçao caso a aposta seja superior ao preco
PENALIZACAO = 100

NJOGADORES = 0
jogadores = []
objetosSaidos = []
objetosPorSair = []

    
 
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
    global objetosPorSair
    for i in range(len(objetosPorSair)):
        return choice(objetosPorSair)
    

def atualizarJogadorJogosCompletos(cod, jc):
    for i in range(len(Jogadores.listajogador)):
        if Jogadores.listajogador[i].codigo == cod:
            Jogadores.listajogador[i] = Jogadores.listajogador[i]._replace(jogos_completos = jc)
            break
        
    # em teoria, existe sempre o Jogador
    
    
def atualizarJogadorVitorias(cod, vitorias):
    for i in range(len(Jogadores.listajogador)):
        if Jogadores.listajogador[i].codigo == cod:
            Jogadores.listajogador[i] = Jogadores.listajogador[i]._replace(vitorias = vitorias)
            break
            

def jogar(N, rondas):
    '''
        N: número de jogadores
    '''
    
    global objetosPorSair
    global objetosSaidos
    
    apostas = [0 for i in range(N)] 
    pontos =  [0 for i in range(N)] 
    
    for ronda in range(rondas):
    
        objeto = escolherObjeto()
        
        objetosSaidos.append(objeto)
        objetosPorSair.remove(objeto)
                
        print "OBJETO SAIDO", objeto.nome
        print "Vamos jogar ao Preço Certo!!!!"
        
        for jog in range(len(jogadores)):
            print jogadores[jog].nick, "é a sua vez", 
            apostas[jog] = raw_input("qual a sua aposta? ")
            dif = int(objeto.preco) - int(apostas[jog])
            if dif < 0:                
                pontos[jog] = pontos[jog] + PENALIZACAO
            else:
                pontos[jog] = pontos[jog] + dif
        
        
        print "Preço do ", objeto.nome, ": ", objeto.preco
        print "Pontuacao ao fim de ", ronda + 1, "rondas"
        print "="*50
        
        for jog in range(len(jogadores)):
            print jogadores[jog].nick, ": ", pontos[jog], "pontos"
                

    print "FIM DO JOGO!!!"
    print
    print "VENCEDOR DO JOGO"
    
    
    #SUPONDO QUE NAO HA EMPATE
    min_index, min_value = min(enumerate(pontos), key=operator.itemgetter(1))
    
    print jogadores[min_index].nick, " com ", min_value    
    
    
    #atualizar estatisticas
    for jog in range(len(jogadores)):
        jc = jogadores[jog].jogos_completos
        atualizarJogadorJogosCompletos(jogadores[jog].codigo, jc+1)
    
    atualizarJogadorVitorias(jogadores[min_index].codigo, jogadores[min_index].vitorias+1)
                        
    
    
        
            
    
def start():
    global objetosPorSair
    global jogadores
    
    n = num_jogadores()

    #escolher jogadores
    del jogadores[:]
    for i in range(n):
        cod = input("Codigo do jogador --> ")
        j = encontraJogador(cod)
        jogadores.append(j)
        print "Jogador ", j.nick, "! Você é concorrente!"
        

    terminar = False
    while not terminar:
    
        rondas = input ("Número de rondas")
        
        objetosPorSair = Objetos.listaobjeto[:]
        
        jogar(n, rondas)
    
        op = raw_input("Querem repetir o jogo? ")
        if op not in ['s', 'S']:
            terminar = True
        
        

    
    