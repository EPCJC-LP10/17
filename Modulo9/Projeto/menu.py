# -*- coding: utf-8 -*-

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gestão de Jogadores"
    print "   2. Registar Presença (não implementado)"
    print 
    print "   0. Sair"
    print 

    op = raw_input("Opção: ")
    return op


def alunos():
    print
    print " *** Menu Jogadores **** "
    print
    print "1. Inserir novo Jogador"
    print "2. Listar todos Jogadores"
    print "3. Alterar dados de um Jogador"
    print "4. Eliminar Jogador"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op



if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"

