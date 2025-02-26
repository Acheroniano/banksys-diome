print("Hello World!")
print("Oi, seja bem vindo ao curso de Python!")
print(1+10)
print(11+52+2533)
print(1.5 + 20 + 2.578)

print(True)
print(False)

age = 28
name = 'Robert Garcia'

print(f'o nome é = {name} e a idade é = {age}')

nome = input("Digite seu nome: ")

print(f"Olá, {nome}!")

input("Digite sua idade: ")

print("Operadores Aritiméticos")
print("Adição: 10 + 10 = ", 10 + 10)
print("Subtração: 10 - 10 = ", 10 - 10)
print("Multiplicação: 10 * 10 = ", 10 * 10)
print("Divisão: 10 / 10 = ", 10 / 10)
print("Exponenciação: 10 ** 10 = ", 10 ** 10)
print("Módulo: 10 % 10 = ", 10 % 10)
print("Divisão Inteira: 10 // 10 = ", 10 // 10)

print("Operadores de Comparação")
print("Igual: 10 == 10", 10 == 10)
print("Diferente: 10 != 10", 10 != 10)
print("Maior que: 10 > 10", 10 > 10)
print("Menor que: 10 < 10", 10 < 10)
print("Maior ou igual: 10 >= 10", 10 >= 10)
print("Menor ou igual: 10 <= 10", 10 <= 10)

print("Operadores Lógicos")
print("E: True and True = ", True and True)
print("OU: True or False = ", True or False)
print("NÃO: not True = ", not True)
print("NÃO: not False = ", not False)
print("E: True and False = ", True and False)

# Example of XOR operation
a = True
b = False
print("XOR: True ^ False = ", a ^ b)
print("XOR: True ^ True = ", a ^ a)
print("XOR: False ^ False = ", b ^ b)

print("Estruturas Condicionais")
idade = 18
if idade >= 18:
    print("Maior de Idade")
else:
    print("Menor de Idade")

print("Python has six bitwise operators that are used to perform operations on binary numbers:")
print("1. & (Bitwise AND)")
print("2. | (Bitwise OR)")  
print("3. ^ (Bitwise XOR)")
print("4. ~ (Bitwise NOT)") 
print("5. >> (Bitwise Right Shift)")
print("6. << (Bitwise Left Shift)")
print()
print("1. ** & (Bitwise AND)**: Sets each bit to 1 if both bits are 1.")
print("2. ** | (Bitwise OR)**: Sets each bit to 1 if either of the bits is 1.")
print("3. ** ^ (Bitwise XOR)**: Sets each bit to 1 if only one of the bits is 1.")
print("4. ** ~ (Bitwise NOT)**: Inverts all the bits.")
print("5. ** >> (Bitwise Right Shift)**: Shifts the bits to the right.")
print("6. ** << (Bitwise Left Shift)**: Shifts the bits to the left.")
print()
print("""1. ** & (Bitwise AND)**: Sets each bit to 1 if both bits are 1.\n
   - Example: 10 & 7 = 2\n
   - Truth Table:\n
     | Bit 1 | Bit 2 | Result |\n
     |-------|-------|--------|\n
     | 0     | 0     | 0      |\n
     | 0     | 1     | 0      |\n
     | 1     | 0     | 0      |\n
     | 1     | 1     | 1      |\n
""")


print("""2. ** | (Bitwise OR)**: Sets each bit to 1 if either of the bits is 1.\n
   - Example: 10 | 7 = 15\n
   - Truth Table:\n
     | Bit 1 | Bit 2 | Result |\n
     |-------|-------|--------|\n
     | 0     | 0     | 0      |\n
     | 0     | 1     | 1      |\n
     | 1     | 0     | 1      |\n
     | 1     | 1     | 1      |\n
""")

print("""3. ** ^ (Bitwise XOR)**: Sets each bit to 1 if only one of the bits is 1.\n
   - Example: 10 ^ 7 = 13\n
   - Truth Table:\n
     | Bit 1 | Bit 2 | Result |\n
     |-------|-------|--------|\n
     | 0     | 0     | 0      |\n
     | 0     | 1     | 1      |\n
     | 1     | 0     | 1      |\n
     | 1     | 1     | 0      |\n
""")

print("""4. ** ~ (Bitwise NOT)**: Inverts all the bits.\n
   - Example: `~10 = -11` (using two's complement)\n
   - Truth Table:\n
     | Bit | Result |\n
     |-----|--------|\n
     | 0   | 1      |\n
     | 1   | 0      |\n
""")


print("""5. ** >> (Bitwise Right Shift)**: Shifts the bits to the right \n
    and fills 0 on voids left as a result for unsigned integers,\n
    or copies the sign bit for signed integers.\n
   - Example: 10 >> 1 = 5\n
   - Effectively performs floor division by 2 raised\n
    to the power of the shift amount[1][2][3][4][5].\n
""")

print("""6. ** << (Bitwise Left Shift)**: Shifts the bits to the left \n
    and fills 0 on voids left as a result for unsigned integers,\n
    or copies the sign bit for signed integers.\n
   - Example: 10 << 1 = 20\n
   - Effectively performs multiplication by 2 raised to the power of the shift amount.\n
""")

print("""Bitwise operators are used to perform bitwise calculations on integers.\n"
      "The integers are first converted into binary and then operations are performed on bit by bit,\n"
      "hence the name bitwise operators.\n"
      "These operators are widely used in programming for performing calculations.\n"
      "These operators are similar to logical operators but are used to perform bitwise calculations.\n"
      "Bitwise operators are used to manipulate data at the bit level.\n
""")

print("Operadores de Atribuição")
print("""
x = 10\n
print(x)\n
x += 10\n
print(x)\n
x -= 10\n
print(x)\n
x *= 10\n
print(x)\n
x /= 10\n
print(x)\n
x %= 10\n
print(x)\n
x //= 10\n
print(x)\n
x **= 10\n
print(x)\n
x &= 10\n
print(x)\n
x |= 10\n
print(x)\n
x ^= 10\n
print(x)\n
x >>= 10\n
print(x)\n
x <<= 10\n
print(x)\n
""")
x = 10
print(x)
x += 10
print(x)
x -= 10
print(x)
x *= 10
print(x)
x /= 10
print(x)
x %= 10
print(x)
x //= 10
print(x)
x **= 10
print(x)
x = int(x)
x &= 10
print(x)
x |= 10
print(x)
x ^= 10
print(x)
x >>= 10
print(x)
x <<= 10
print(x)

print("Operadores de Identidade")
x = 10
y = 10
print(x is y)
print(x is not y)

print("Operadores de Associação")
x = [1, 2, 3]
print(1 in x)
print(4 in x)
print(1 not in x)
print(4 not in x)

print("Operadores de Membro")
x = [1, 2, 3]
print(1 in x)
print(4 in x)
print(1 not in x)
print(4 not in x)

nome = "Fabio Samuel dos Santos Canedo"

print("1a letra", nome[0])
print("10 primeiras letras", nome[:11])
print("da 11a letra até o final", nome[11:])
print("da letra 8 até a letra 11", nome[8:11])
print("pulando letras de 2 em 2", nome[::2])
print("inverte a string", nome[::-1])   # Inverte a string
print("inverte pulando de 2 em 2", nome[::-2])   # Inverte a string pulando de 2 em 2
print("cópia da string", nome[:])      # Copia a string

def exibir_mensagem():
    print("Olá, seja bem vindo ao curso de Python!")

exibir_mensagem()

nome = input("Digite seu nome: ")

def exibir_nome(nome):
    print(f"Olá, {nome}!")

exibir_nome(nome)

def calcular_total(numeros):
    return sum(numeros)

def retorna_ante_sucessor(numero):
    return numero - 1, numero + 1

print("Soma de 1,23,13,42 e 215:", calcular_total([1, 23, 13, 42, 215]))

print("Numero 25 :", retorna_ante_sucessor(25))


def salvar_carro(marca, modelo, ano, placa):
    # Salva o carro no banco de dados
    print(f"Carro inserido com sucesso! Marca: {marca}, Modelo: {modelo}, Ano: {ano}, Placa: {placa}")

salvar_carro("Fiat", "Uno", 2010, "ABC-1234")
salvar_carro(marca="Volkswagen", modelo="Fusca", ano=1990, placa="ABC-2354")
salvar_carro(**{"marca": "Chevrolet", "modelo": "Celta", "ano": 2005, "placa": "ABC-3456"})


def exibir_poema(data_extenso, *args, **kwargs):
    # *args é uma tupla (lista)
    # **kwargs é um dicionário

    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Terça-Feira, 25-02-2025", "Zen of Python", " */*/ life", "Beautiful is better than ugly.", autor="Tim Peters", ano=2004)

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Uno", 2010, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Flex")

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel, cor, km):
    print(modelo, ano, placa, marca, motor, combustivel, cor, km)

criar_carro(modelo="Uno", ano=2010, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Flex", cor="Vermelho", km=10000)


# Referenciando uma função como argumento de outra função (callback)

def func_somar(a, b):
    return a + b

def func_subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"Resultado: {a} + {b} = {resultado}")

exibir_resultado(10, 20, func_somar) # Resultado: 10 + 20 = 30
exibir_resultado(10, 20, func_subtrair) # Resultado: 10 - 20 = -10

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_bonus(500)
print(salario)

