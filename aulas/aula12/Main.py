from Pessoa import *
import os
def limpar():
    os.system('cls')

limpar()

cadastro = []

def cadastrar():
    nome = str(input("Digite o nome da pessoa: "))
    idade = int(input("Digite a idade da pessoa: "))
    cargo = str(input("Digite o cargo da pessoa: "))
    salario = float(input("Digite o salário da pessoa: "))

    cadastro.append(Pessoa(nome,idade,cargo,salario))
    cadastrar_novamente = int(input("Deseja cadastrar mais alguém? 1 - Sim ou 0 - Não: "))
    if(cadastrar_novamente == 1):
        cadastrar()
    else:
        limpar()
        menu()
        

def mostrar():
    y = 0
    limpar()
    print("{:<4} {:<10} {:<7} {:<10} {:<7}"
          .format("N°","Nome","Idade","Cargo","Salário") )
    for x in cadastro:
        print("{:<4} {:<10} {:<7} {:<10} {:<7}"
              .format(y,
                      x.get_nome(),
                      x.get_idade(),
                      x.get_cargo(),
                      x.get_salario(),
                      ))
        y += 1
    menu()
        

def alterar():
    x = int(input("Digite o N° do funcionário: "))
    opcao = int(input("Digite a opção que deseja alterar: \n1 - Nome \n2 - Idade \n3 - Cargo \n4 - Salário \n"))
    valor = str(input("Escreva o novo valor da opção: "))
    if(opcao == 1): cadastro[x].set_nome(valor)
    elif(opcao == 2): cadastro[x].set_idade(valor)
    elif(opcao == 3): cadastro[x].set_cargo(valor)
    elif(opcao == 4): cadastro[x].set_salario(valor)
    else:
        print("Valor incorreto!")
    menu()

def remover():
    x = int(input("Digite o número do funcionário que deseja remover: "))
    res = int(input("Tem certeza que deseja remover o funcionário número?\n1 - Sim \n2 - Não\n"))
    if (res == 1):
        cadastro.pop(x)
        limpar()
        menu()
    else:
        print("Operação cancelada")
        menu()

def menu():
        x = int(input(("Escolha a ação que deseja fazer: \n1 - Cadastrar funcionário \n2 - Alterar tabela de funcionários \n3 - Remover funcionário \n4 - Mostrar tabela \n0 - Encerrar sessão\n")))
        if(x == 1): cadastrar()
        elif(x == 2): alterar()
        elif(x == 3): remover()
        elif(x == 4): mostrar()
        elif(x == 0): print("Sessão encerrada")
        else:
            limpar()
            print("Número inválido! Digite novamente")
            menu()
menu()  
