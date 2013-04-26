def menu ():
    print '+--------------------------------+'
    print '|1- Inserir novo contacto        |'
    print '|2- Listar todos os contactos    |'
    print '|3- Pesquisar por nome           |'
    print '|4- Alterar dados de um contacto |'
    print '|5- Eliminar contacto            |'
    print '+--------------------------------+'
    print '|0- Terminar                     |'
    print '+--------------------------------+


def posicao_contacto (codigo):

        for pos in range (len(contactos)):
            if contactos[pos].codigo== codigo:
                return pos
    return -1 #nao encontrou

def inserir ():
    codigo= input ("Introduza o código: ")
    posicao = posicao_contacto(codigo)
    if posicao!= -1:
        print ("Código ja existente. \n")
        return
    #Ler os restantes dados do registo
    nome= raw_input ("Qual o nome do contacto ----> ")
    contacto= input ("Qual o numero do contacto ---> ")
    email= raw_input ("Qual o email do contacto ---> ")

    #Criar o novo registo
    novo_reg= contactos(nome, contacto, email)

    #adicionar a lista
    contactos.append(novo_registo)

def apresentar_registo(registo):
    print "Código", registo.codigo
    print "Nome", registo.nome
    print "email", registo.email


def listar_todos():
    if len(contactos) == 0:
        print "Nao existem contactos inseridos"

    for registo in contactos:
        apresentar_registo(registo)

#Outra maneira de fazer a listagem
def listar_todos_alternativa():
    if len (contactos) == 0:
        print "Nao existem contactos inseridos"
        return
    for i in range (len(contactos)):
        apresentar_registo (contactos[i])

def pesquisar ():
    codigo= int
        
