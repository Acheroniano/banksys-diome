# Cria um dicionário com informações de uma pessoa
pessoa = {"nome": "João", "idade": 39, "cidade": "São Paulo"}

# Cria outro dicionário usando a função dict()
pessoa2 = dict(nome="Maria", idade=25, cidade="Rio de Janeiro")

# Adiciona um novo elemento ao dicionário pessoa2
pessoa2["telefone"] = "999-888-777"

# Imprime o valor associado à chave "nome" no dicionário pessoa
print(pessoa["nome"]) # João

# Imprime o valor associado à chave "idade" no dicionário pessoa2
print(pessoa2["idade"]) # 25

# Imprime todo o dicionário pessoa2
print(pessoa2) # {'nome': 'Maria', 'idade': 25, 'cidade': 'Rio de Janeiro', 'telefone': '999-888-777'}

# Imprime todas as chaves do dicionário pessoa2
print(pessoa2.keys()) # ['nome', 'idade', 'cidade', 'telefone']

# Imprime todos os valores do dicionário pessoa2
print(pessoa2.values()) # ['Maria', 25, 'Rio de Janeiro', '999-888-777']

# Imprime todos os pares chave-valor do dicionário pessoa2
print(pessoa2.items()) # [('nome', 'Maria'), ('idade', 25), ('cidade', 'Rio de Janeiro'), ('telefone', '999-888-777')]

# Obtém o valor associado à chave "nome" no dicionário pessoa2
print(pessoa2.get("nome")) # Maria

# Obtém o valor associado à chave "telefone" no dicionário pessoa2
print(pessoa2.get("telefone")) # 999-888-777

# Tenta obter o valor associado à chave "email" no dicionário pessoa2, retorna None se não existir
print(pessoa2.get("email")) # None

# Tenta obter o valor associado à chave "email" no dicionário pessoa2, retorna "Não existe" se não existir
print(pessoa2.get("email", "Não existe")) # Não existe

# Remove o elemento com a chave "idade" do dicionário pessoa2 e retorna seu valor
print(pessoa2.pop("idade")) # 25

# Imprime o dicionário pessoa2 após a remoção da chave "idade"
print(pessoa2) # {'nome': 'Maria', 'cidade': 'Rio de Janeiro', 'telefone': '999-888-777'}

# Remove e retorna o último par chave-valor do dicionário pessoa2
print(pessoa2.popitem()) # ('telefone', '999-888-777')

# Imprime o dicionário pessoa2 após a remoção do último par chave-valor
print(pessoa2) # {'nome': 'Maria', 'cidade': 'Rio de Janeiro'}

# Remove todos os elementos do dicionário pessoa2
pessoa2.clear()

# Imprime o dicionário pessoa2 após a remoção de todos os elementos
print(pessoa2) # {}

# Imprime o número de elementos no dicionário pessoa
print(len(pessoa)) # 3

# Verifica se a chave "nome" está presente no dicionário pessoa
print("nome" in pessoa) # True

# Verifica se a chave "email" não está presente no dicionário pessoa
print("email" not in pessoa) # True

# Verifica se a chave "email" está presente no dicionário pessoa
print("email" in pessoa) # False

# Verifica se a chave "idade" está presente no dicionário pessoa
print("idade" in pessoa) # True

# Verifica se o valor "João" está presente no dicionário pessoa
print("João" in pessoa.values()) # True

# Verifica se o valor "Maria" está presente no dicionário pessoa
print("Maria" in pessoa.values()) # False

# Verifica se o valor "João" está presente no dicionário pessoa2
print("João" in pessoa2.values()) # False

# Verifica se o valor "Maria" está presente no dicionário pessoa2
print("Maria" in pessoa2.values()) # False

# Itera sobre as chaves do dicionário pessoa
for chave in pessoa:
    # Imprime a chave atual
    print(chave) # nome, idade, cidade
    
    # Imprime o valor associado à chave atual no dicionário pessoa
    print(pessoa[chave]) # João, 39, São Paulo
    
    # Tenta imprimir o valor associado à chave atual no dicionário pessoa2
    #print(pessoa2[chave]) # Maria, Rio de Janeiro, Não existe
    
    # Usa o método get() para obter o valor associado à chave atual no dicionário pessoa2
    print(pessoa2.get(chave)) # Maria, Rio de Janeiro, None

contatosx= dict()
contatosx.clear()

# Cria um dicionário de contatos, onde cada chave é um email e o valor é outro dicionário com informações da pessoa
contatosx = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "999-888-777"},
    "fssc00@gmail.com": {"nome": "Fabio Canedo", "telefone": "999-888-77725"},
    "chappie@hotmail.com": {"nome": "Charles Pie", "telefone": "999-215488"},
    "karineportugal@gmail.com": {"nome": "Karine", "telefone": "458487-777"},
    "melanie@uol.com.br": {"nome": "Melanie O.", "telefone": "487899-777"},
}


# Obtém o telefone associado ao email "fssc00@gmail.com"
telefonex = contatosx["fssc00@gmail.com"]["telefone"]
print(telefonex) # 999-888-77725

# Obtém o valor associado à chave "a" no dicionário "extra" dentro do contato "melanie@uol.com.br"
extra = contatosx["melanie@uol.com.br"]
print(extra) # 1

copia_contatos = contatosx.copy()
print(copia_contatos) # {'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '999-888-777'},   

dict.fromkeys(["nome", "telefone"]) # {'nome': None, 'telefone': None}

dict.fromkeys(["nome", "telefone"], "vazio") # {'nome': 'vazio', 'telefone': 'vazio'}

print(contatosx.get("chave")) # None

contatosx.get("chave")  
contatosx.get("chave", {}) # {}
contatosx.get("guilherme@gmail.com", {}) # {'nome': 'Guilherme', 'telefone': '999-888-777'}

contato = {"pessoa1": "João", "telefone": "999-888-777",
           "pessoa2": "Maria", "telefone": "9499-888-777778",          
           "pessoa3": "José", "telefone": "999-32888-777778",
           "pessoa4": "Ana", "telefone": "999-3888-777778",
           "pessoa5": "Carlos", "telefone": "999-334888-777778",
           }

print(contato) # {'pessoa1': 'João', 'telefone': '999-888-777', 'pessoa2': 'Maria', 'telefone': '9499-888-777778', 'pessoa3': 'José', 'telefone': '999-32888-777778', 'pessoa4': 'Ana', 'telefone': '999-3888-777778', 'pessoa5': 'Carlos', 'telefone': '999-334888-777778'}    

contato.setdefault("idade", 30)
print(contato)  # {'pessoa1': 'João', 'telefone': '999-888-777', 'pessoa2': 'Maria', 'telefone': '9499-888-777778', 'pessoa3': 'José', 'telefone': '999-32888-777778', 'pessoa4': 'Ana', 'telefone': '999-3888-777778', 'pessoa5': 'Carlos', 'telefone': '999-334888-777778', 'idade': 30}

contato.update({"pessoa5": "Carlos", "telefone": "999-888-777", "idade": 30})
print(contato) 

del contato["pessoa5"]
print(contato)

