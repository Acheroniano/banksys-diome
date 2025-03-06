# This program demonstrates various Python concepts including:
# - Basic print statements
# - Variable assignments
# - Input from the user
# - Arithmetic, comparison, and logical operators
# - Conditional statements
# - Bitwise operators
# - Identity and membership operators
# - String slicing
# - Functions with different argument types
# - Global variables

# Print a simple greeting message to the console
print("Hello World!")

# Print a greeting message in Portuguese
print("Oi, seja bem vindo ao curso de Python!")

# Print the result of adding 1 and 10
print(1+10)

# Print the sum of multiple integers
print(11+52+2533)

# Print the sum of floating-point numbers
print(1.5 + 20 + 2.578)

# Print boolean values True and False
print(True)
print(False)

# Assign an integer value to the variable 'age'
age = 28

# Assign a string value to the variable 'name'
name = 'Robert Garcia'

# Print a formatted string that includes the values of 'name' and 'age'
print(f'o nome é = {name} e a idade é = {age}')

# Prompt the user to enter their name and store it in the 'nome' variable
nome = input("Digite seu nome: ")

# Print a greeting message that includes the user's name
print(f"Olá, {nome}!")

# Prompt the user to enter their age (the input is not stored in a variable)
input("Digite sua idade: ")

# Print a header for the arithmetic operators section
print("Operadores Aritiméticos")

# Demonstrate addition
print("Adição: 10 + 10 = ", 10 + 10)

# Demonstrate subtraction
print("Subtração: 10 - 10 = ", 10 - 10)

# Demonstrate multiplication
print("Multiplicação: 10 * 10 = ", 10 * 10)

# Demonstrate division
print("Divisão: 10 / 10 = ", 10 / 10)

# Demonstrate exponentiation
print("Exponenciação: 10 ** 10 = ", 10 ** 10)

# Demonstrate the modulo operator
print("Módulo: 10 % 10 = ", 10 % 10)

# Demonstrate integer division
print("Divisão Inteira: 10 // 10 = ", 10 // 10)

# Print a header for the comparison operators section
print("Operadores de Comparação")

# Demonstrate the equality operator
print("Igual: 10 == 10", 10 == 10)

# Demonstrate the inequality operator
print("Diferente: 10 != 10", 10 != 10)

# Demonstrate the greater than operator
print("Maior que: 10 > 10", 10 > 10)

# Demonstrate the less than operator
print("Menor que: 10 < 10", 10 < 10)

# Demonstrate the greater than or equal to operator
print("Maior ou igual: 10 >= 10", 10 >= 10)

# Demonstrate the less than or equal to operator
print("Menor ou igual: 10 <= 10", 10 <= 10)

# Print a header for the logical operators section
print("Operadores Lógicos")

# Demonstrate the 'and' operator
print("E: True and True = ", True and True)

# Demonstrate the 'or' operator
print("OU: True or False = ", True or False)

# Demonstrate the 'not' operator
print("NÃO: not True = ", not True)

# Demonstrate the 'not' operator with False
print("NÃO: not False = ", not False)

# Demonstrate the 'and' operator with True and False
print("E: True and False = ", True and False)

# Example of XOR operation
a = True
b = False

# Demonstrate XOR with True and False
print("XOR: True ^ False = ", a ^ b)

# Demonstrate XOR with True and True
print("XOR: True ^ True = ", a ^ a)

# Demonstrate XOR with False and False
print("XOR: False ^ False = ", b ^ b)

# Print a header for the conditional structures section
print("Estruturas Condicionais")

# Initialize the 'idade' variable with the value 18
idade = 18

# Check if 'idade' is greater than or equal to 18
if idade >= 18:
    # If true, print "Maior de Idade" (Adult)
    print("Maior de Idade")
else:
    # If false, print "Menor de Idade" (Minor)
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

# Print the first letter of the string
print("1a letra", nome[0])

# Print the first 10 letters of the string
print("10 primeiras letras", nome[:11])

# Print from the 11th letter to the end of the string
print("da 11a letra até o final", nome[11:])

# Print from the 8th letter to the 11th letter
print("da letra 8 até a letra 11", nome[8:11])

# Print the string skipping letters 2 by 2
print("pulando letras de 2 em 2", nome[::2])

# Invert the string
print("inverte a string", nome[::-1])   # Inverte a string

# Invert the string skipping letters 2 by 2
print("inverte pulando de 2 em 2", nome[::-2])   # Inverte a string pulando de 2 em 2

# Copy the string
print("cópia da string", nome[:])      # Copia a string

# Define a function that prints a greeting message
def exibir_mensagem():
    print("Olá, seja bem vindo ao curso de Python!")

# Call the function to display the greeting message
exibir_mensagem()

# Prompt the user to enter their name
nome = input("Digite seu nome: ")

# Define a function that displays a greeting message with the user's name
def exibir_nome(nome):
    print(f"Olá, {nome}!")

# Call the function to display the greeting message with the user's name
exibir_nome(nome)

# Define a function that calculates the sum of a list of numbers
def calcular_total(numeros):
    return sum(numeros)

# Define a function that returns the predecessor and successor of a number
def retorna_ante_sucessor(numero):
    return numero - 1, numero + 1

# Print the sum of a list of numbers
print("Soma de 1,23,13,42 e 215:", calcular_total([1, 23, 13, 42, 215]))

# Print the predecessor and successor of a number
print("Numero 25 :", retorna_ante_sucessor(25))

# Define a function that saves a car to the database
def salvar_carro(marca, modelo, ano, placa):
    # Salva o carro no banco de dados
    print(f"Carro inserido com sucesso! Marca: {marca}, Modelo: {modelo}, Ano: {ano}, Placa: {placa}")

# Call the function to save a car
salvar_carro("Fiat", "Uno", 2010, "ABC-1234")

# Call the function to save a car with keyword arguments
salvar_carro(marca="Volkswagen", modelo="Fusca", ano=1990, placa="ABC-2354")

# Call the function to save a car with a dictionary
salvar_carro(**{"marca": "Chevrolet", "modelo": "Celta", "ano": 2005, "placa": "ABC-3456"})

# Define a function that displays a poem
def exibir_poema(data_extenso, *args, **kwargs):
    # *args é uma tupla (lista)
    # **kwargs é um dicionário

    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

# Call the function to display a poem
exibir_poema("Terça-Feira, 25-02-2025", "Zen of Python", " */*/ life", "Beautiful is better than ugly.", autor="Tim Peters", ano=2004)

# Define a function that creates a car
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Call the function to create a car
criar_carro("Uno", 2010, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Flex")

# Define a function that creates a car with keyword arguments
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel, cor, km):
    print(modelo, ano, placa, marca, motor, combustivel, cor, km)

# Call the function to create a car with keyword arguments
criar_carro(modelo="Uno", ano=2010, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Flex", cor="Vermelho", km=10000)

# Referenciando uma função como argumento de outra função (callback)

# Define a function that adds two numbers
def func_somar(a, b):
    return a + b

# Define a function that subtracts two numbers
def func_subtrair(a, b):
    return a - b

# Define a function that displays the result of a function
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"Resultado: {a} + {b} = {resultado}")

# Call the function to display the result of the sum function
exibir_resultado(10, 20, func_somar) # Resultado: 10 + 20 = 30

# Call the function to display the result of the subtract function
exibir_resultado(10, 20, func_subtrair) # Resultado: 10 - 20 = -10

# Define a global variable
salario = 2000

# Define a function that adds a bonus to the global variable
def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

# Call the function to add a bonus to the global variable
salario_bonus(500)

# Print the value of the global variable
print(salario)

