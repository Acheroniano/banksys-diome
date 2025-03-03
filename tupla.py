# Tupla em Python

# Tupla é uma coleção de objetos que não pode ser alterada 
# (imutável). Tuplas são definidas por parênteses e vírgulas.

frutas = ("laranja", "pera", "uva", "maçã",)
letras = tuple("python")

numeros = tuple([1, 2, 3, 4])
print(frutas)
print(letras)
print(numeros)

pais = ("Brasil",)

print(pais)

print (frutas[0]) # laranja
print (frutas[2]) # uva
print (frutas[-1]) # maçã
print (frutas[1:3]) # ('pera', 'uva')
print (frutas[:2]) # ('laranja', 'pera')    
print (frutas[2:]) # ('uva', 'maçã')
print (frutas[::2]) # ('laranja', 'uva')
print (frutas[::-1]) # ('maçã', 'uva', 'pera', 'laranja')
print (frutas.index("uva")) # 2
print (frutas.count("uva")) # 1

# frutas[0] = "banana" # TypeError: 'tuple' object does not support item assignment

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0][0]) # 1
print(matriz[1][1]) # 3
print(matriz[2][2]) # c
print(matriz[-1][-1]) # c
print(matriz[0]) # (1, 'a', 2)
print(matriz[1]) # ('b', 3, 4)
print(matriz[2]) # (6, 5, 'c')

# listas são mutáveis e tuplas são imutáveis
# listas são definidas por colchetes e tuplas por parênteses

carros = ["gol"]    # lista
carros = ("gol",)    # tupla
carros = tuple(["gol"])    # tupla
carros = ["gol",]    # lista
carros = tuple("gol")    # tupla
carros = tuple(["gol",])    # tupla
carros = tuple("gol", )    # tupla

# Conjuntos

set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4})
set("abacaxi") # {"b", "a", "c", "x", "i"}
set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}

linguagens = {"python", "java", "python"}
print(linguagens) # {'python', 'java'}

paises = sorted(set(["brasil", "argentina", "brasil", "chile", "argentina", "quenia"])
                
print(paises) # ['argentina', 'brasil', 'chile', 'quenia']

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto_c = conjunto_a.union(conjunto_b) # {1, 2, 3, 4, 5}
conjunto_a.issubset(conjunto_b) # True
conjunto_b.issuperset(conjunto_a) # True    
conjunto_a.intersection(conjunto_b) # {1, 2, 3}
conjunto_a.difference(conjunto_b) # {}  
conjunto_b.difference(conjunto_a) # {4, 5}
conjunto_a.symmetric_difference(conjunto_b) # {4, 5}    
conjunto_a.add(4) # {1, 2, 3, 4}
conjunto_a.remove(4) # {1, 2, 3}
conjunto_a.discard(4) # {1, 2, 3}
conjunto_a.pop() # 1    
conjunto_a.clear() # {}
conjunto_a.update() # {1, 2, 3, 4, 5}
conjunto_a.update([6, 7]) # {1, 2, 3, 4, 5, 6, 7}
conjunto_a.update({8, 9}) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
conjunto_a.isdisjoint(conjunto_b) # False
conjunto_a.discart(4) # {1, 2, 3, 5, 6, 7, 8, 9}
conjunto_a.pop() # 
print(conjunto_a) # {1, 2, 5, 6, 7, 8, 9}
  

# Dicionários
