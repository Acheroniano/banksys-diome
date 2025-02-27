import os  # Import the os module
import random  # Import the random module

# Sistema bancário em Python (Desafio de código da Dio.me)
# Autor: acheroniano@gmail.com
# Data: 2025-02-26

# Variáveis globais

bank_name = ""  # Add the bank_name variable
usuario = ""  # Add the usuario variable
saldo = 0.0  # Add the saldo variable
contador_de_saques = 0  # Add the contador_de_saques variable
contador_de_saques_maximo = 3  # Add the contador_de_saques_maximo variable
limite_de_saque = 500.0  # Add the limite_de_saque variable
configuracao_inicial_realizada = False  # Add the configuracao_inicial_realizada variable

# Variável do extrato
extrato = ""

opcao = 0  # Add the opcao variable


# Funções

def wait_for_key():
    """Waits for the user to press any key."""
    print("\n\n")
    if os.name == 'nt':
        os.system("pause")  # Windows
    else:
        input("Pressione qualquer tecla para continuar...")  # Linux/macOS


def clear_screen():  # Add the clear_screen function
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    global bank_name, opcao  # Access the global variable
    opcao = input('Digite a opção desejada: ')
    if opcao.isdigit():
        opcao = int(opcao)
        return opcao
    else:
        return 0


def configuracao_inicial():
    clear_screen()
    global extrato, configuracao_inicial_realizada, bank_name, usuario, saldo  # Access global variables
    if configuracao_inicial_realizada:
        print('Configuração inicial já realizada!')
        wait_for_key()
        return
    bank_name = input('Digite o nome do banco: ')
    usuario = input('Digite o nome do usuário: ')
    # saldo = random.randint(0, 10000) # Generate a random initial balance for the user
    saldo = random.randint(0, 10000)
    extrato = "banco: " + bank_name + "\n" + "usuario: " + usuario + "\n"
    extrato = f"Saldo inicial: R$ {saldo:.2f}\n==========================\n"
    print(
        f'\nOlá {usuario}!\n\nConfiguração inicial realizada com sucesso! Saldo atual: R$ {saldo:.2f}\n')
    wait_for_key()
    configuracao_inicial_realizada = True


def efetuar_saque():
    if not configuracao_inicial_realizada:
        print('Configuração inicial não foi realizada!')
        wait_for_key()
        return

    clear_screen()
    global extrato, contador_de_saques, saldo  # Access global variables
    if contador_de_saques >= contador_de_saques_maximo:
        print('Você atingiu o limite de saques diários!\n\n')
        wait_for_key()
        return
    print(
        f'\nOlá {usuario}!, Saldo atual: R$ {saldo:.2f}\n\nSaques realizados hoje: {contador_de_saques}\n')
    valor = float(input('Digite o valor do saque: (-) R$ '))
    if valor > saldo:
        print('Saldo insuficiente!\n\n')
        wait_for_key()
        return
    if valor > limite_de_saque:
        print(f'Valor máximo de saque diário é de R$ {limite_de_saque:.2f}\n\n')
        wait_for_key()
        return
    if valor <= 0:
        print('Valor de saque inválido!\n\n')
        wait_for_key()
        return
    saldo = saldo - valor
    extrato += f"Saque: (-) R$ {valor:.2f}\n==========================\nSaldo atual: R$ {saldo:.2f}\n==========================\n"
    print(f'Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}\n\n')
    wait_for_key()
    contador_de_saques += 1
    clear_screen()

def efetuar_deposito():
    global extrato, contador_de_saques, saldo  # Access global variables
    print(f'\nOlá {usuario}!, Saldo atual: R$ {saldo:.2f}\n\n')
    if not configuracao_inicial_realizada:
        print('Configuração inicial não foi realizada!')
        wait_for_key()
        return
    clear_screen()
    valor = float(input('Digite o valor do depósito: (+) R$ '))
    if valor <= 0:
        print('Valor de depósito inválido!\n\n')
        wait_for_key()
        return

    saldo = saldo + valor
    extrato += f"Depósito: (+) R$ {valor:.2f}\n==========================\nSaldo atual: R$ {saldo:.2f}\n==========================\n"
    print(f'Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}')
    wait_for_key()
    clear_screen()

def extrato_bancario():
    global extrato
    clear_screen()
    print("==================================================================")
    print("===================== Extrato Bancário ===========================")
    print("==================================================================")
    if extrato == "" or extrato == "Saldo inicial: R$ 0.00\n":
        print("\n\nNenhuma movimentação foi realizada.\n\n")
    else:
        print(extrato)
    print("===================================================================")
    wait_for_key()


def tela_inicial():
    clear_screen()
    print("===================================================================")
    print("== Sistema bancário em Python (Desafio de código da Dio.me) =======")
    print("===================================================================")

    if usuario != "" and bank_name != "":
        print(f"Banco: {bank_name} - \nUsuário: {usuario} - Saldo: R$ {saldo:.2f}")
    print("===================================================================")
    print("saques realizados hoje: ", contador_de_saques)
    print("===================================================================")
    print('1 - Configuração inicial')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Saldo')
    print('5 - Extrato')
    print('6 - Sair')


def mostrar_saldo():
    clear_screen()
    global saldo, bank_name, usuario  # Access global variable
    print("Banco : ", bank_name)
    print ("===========================")
    print(f'\nOlá {usuario}!, Saldo atual: R$ {saldo:.2f}\n\n')
    wait_for_key()


# Main loop

while True:
    tela_inicial()
    opcao = menu()

    if opcao == 1:
        configuracao_inicial()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        mostrar_saldo()
    elif opcao == 5:
        extrato_bancario()
    elif opcao == 6:
        clear_screen()
        if usuario != "" and bank_name != "":
            print("usuario : ", usuario)
            print("bank_name : ", bank_name)
            print(f"saldo : R$ {saldo:.2f}")
        print('===================================================================')
        print('Saindo do sistema...')
        print('Obrigado por utilizar o sistema bancário!')
        break
    else:
        print('\n\nOpção inválida!')
        wait_for_key()
        clear_screen()
        continue  # Continue the loop if the option is invalid

# End of the main loop
