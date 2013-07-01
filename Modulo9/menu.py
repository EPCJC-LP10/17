# -*- coding: utf-8 -*-

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gestão de jogador"
    print "   2. Gestao de objetos"
    print "   3. Jogar" 
    print 
    print "   0. Sair"
    print 

    op = raw_input("Opção: ")
    return op


def jogadores():
    print
    print " *** Menu Alunos **** "
    print
    print "1. Inserir novo jogador"
    print "2. Listar todos jogadores"
    print "3. Pesquisar jogador"
    print "4. Alterar dados de um jogador"
    print "5. Eliminar jogador"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op



if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"

