from Pessoa import *
import os
def limpar():
    os.system('clear')

limpar()



def pergunta():
    res = int(input("Deseja cadastrar uma nova pessoa? 1 - Sim ou 0 - Não: "))
    return res

cadastro = []

res = pergunta()
while(res == 1):
    nome = str(input("Digite o nome da pessoa: "))
    idade = int(input("Digite a idade da pessoa: "))
    cargo = str(input("Digite o cargo da pessoa: "))
    salario = float(input("Digite o salário da pessoa: "))

    cadastro.append(Pessoa(nome,idade,cargo,salario))
    res = pergunta()

def mostrar():
    y = 0
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
        mostrar()



def questionar():
    confirma = int(input("Deseja alterar a lista? 1 - Sim ou 0 - Não: "))
    return confirma

confirma = questionar()

while(confirma == 1):
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
            alterar()
            mostrar()

def excluir():
     apagar = int(input("Deseja excluir um funcionário da lista? \n1 - Sim \n2- Não\n"))
     return apagar

apagar = excluir()

while(apagar == 1):
        def remover():
            x = int(input("Digite o número do funcionário que deseja remover: "))
            res = int(input("Tem certeza que deseja remover o funcionário número?\n1 - Sim \n2 - Não\n"))
            if (res == 1):
                cadastro.pop(x)
                remover()
                mostrar()

def menu():
        x = int(input(("Escolha a ação que deseja fazer: \n1 - Cadastrar funcionário \n2 - Alterar tabela de funcionários \n3 - Remover funcionário \n4 - Mostrar tabela\n")))
        if(x == 1): pergunta()
        elif(x == 2): questionar()
        elif(x == 3): remover()
        elif(x == 4): mostrar()
        else:
            print("Número inválido! Sessão encerrada")
menu()