from Pessoa import *
import os
def limpar(): os.system('clear')

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

y = 1
def mostrar():
    print("{:<4} {:<10} {:<7} {:<10} {:<7}"
          .format("N°","Nome","Idade","Cargo","Salário") )
    for x in cadastro:
        print("{:<4} {:<10} {:<7} {:<10} {:<7}"
              .format(y +1,
                      x.get_nome(),
                      x.get_idade(),
                      x.get_cargo(),
                      x.get_salario(),
                      ))
mostrar()

def questionar():
    confirma = int(input("Deseja alterar a lista? 1 - Sim ou 0 - Não: "))
    return confirma

confirma = questionar() 

while(confirma == 1):
    def alterar(x, opcao, valor):
        x = int(input("Digite o N° do funcionário: "))
        opcao = str(input("Digite a opção que deseja alterar: "))
        valor = str(input("Escreva o novo valor da opção: "))
        if(opcao == 0): cadastro[x].set_nome(valor)
        if(opcao == 0): cadastro[x].set_idade(valor)
        if(opcao == 0): cadastro[x].set_cargo(valor)
        if(opcao == 0): cadastro[x].set_salario(valor)
mostrar()



        

    
    
