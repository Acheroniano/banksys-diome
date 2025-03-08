# poo.py (Refatorado por um Dev Júnior - Comentado em Português BR)

# Vamos começar definindo a classe Bicicleta.
# Uma classe é como um "molde" para criar objetos.
class Bicicleta:
    # O método __init__ é o "construtor" da classe.
    # Ele é executado quando criamos um novo objeto Bicicleta.
    def __init__(self, cor, modelo, ano, valor):
        # "self" é uma referência ao próprio objeto que está sendo criado.
        # Aqui, estamos definindo os "atributos" (características) da bicicleta.
        self.cor = cor  # Atributo para armazenar a cor da bicicleta.
        self.modelo = modelo  # Atributo para o modelo da bicicleta.
        self.ano = ano  # Atributo para o ano de fabricação.
        self.valor = valor  # Atributo para o valor da bicicleta.

    # Método para simular o som da buzina.
    def buzinar(self):
        print('plim plim')  # Imprime o som da buzina.

    # Método para simular a parada da bicicleta.
    def parar(self):
        print('parando bicicleta...')  # Mensagem indicando que a bicicleta está parando.
        print('bicicleta parada!!!')  # Mensagem de confirmação que a bicicleta parou.

    # Método para simular a bicicleta em movimento.
    def correr(self):
        print('vrummmmmmm...')  # Imprime o som da bicicleta correndo.

    # O método __str__ é usado para criar uma representação em string do objeto.
    # Ele é chamado quando usamos print(objeto).
    def __str__(self):
        # Criamos uma string que descreve a bicicleta, mostrando seus atributos.
        # Por exemplo: Bicicleta: cor = vermelha, modelo = caloi, ano = 2022, valor = 600
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

# Criando uma classe chamada Pessoa
class Pessoa:
    # O método __init__ é o construtor da classe Pessoa.
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Criando o método apresentar
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando um objeto da classe Pessoa
fabio = Pessoa("Fábio", 30)
fabio.apresentar()

# Criando uma instancia da classe Bicicleta chamada Bike1
Bike1 = Bicicleta('vermelha', 'caloi', 2022, 600)

# Executando os métodos de Bike1
Bike1.buzinar()
Bike1.parar()
Bike1.correr()

# imprimindo os atributos de Bike1
print(Bike1.cor, Bike1.modelo, Bike1.ano, Bike1.valor)

# Criando uma nova bicicleta Bike2
Bike2 = Bicicleta('verde', 'monark', 2000, 189)
Bike2.buzinar()
print("1")
Bike2.buzinar()
print(Bike2.cor)
print(Bike1) # imprime os atributos de Bike1.

# Aqui começamos a parte de Herança (Inheritance).
# Herança permite que uma classe "herde" características de outra.

# Criando uma classe chamada A
class A:
    pass  # "pass" significa que a classe está vazia por enquanto.

# A classe B herda da classe A.
class B(A):  # B é uma "subclasse" de A. A é a "superclasse".
    pass

# A classe C herda da classe B.
class C(B):  # C é uma "subclasse" de B, que é uma subclasse de A.
    pass

# Herança Simples (Simple Inheritance)

# Vamos criar uma classe chamada Veiculo.
# Ela será a "classe pai" ou "superclasse".
class Veiculo:
    # Construtor da classe Veiculo
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor  # Cor do veículo.
        self.placa = placa  # Placa do veículo.
        self.numero_rodas = numero_rodas  # Número de rodas do veículo.

    # Método para simular ligar o motor.
    def ligar_motor(self):
        print('ligando motor...')  # Mensagem de que o motor está ligando.

    # Representação do objeto em string.
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

# A classe Motocicleta "herda" da classe Veiculo.
# Isso significa que ela terá todos os atributos e métodos de Veiculo.
class Motocicleta(Veiculo):
    pass  # Não adicionamos nada novo aqui, ela só herda.

# A classe Carro também herda de Veiculo.
class Carro(Veiculo):
    pass  # Também só herda.

# A classe Caminhao herda de Veiculo e adiciona novas características.
class Caminhao(Veiculo):
    # Aqui, o caminhão tem o seu proprio construtor, que extende o construtor da classe Veiculo.
    def __init__(self, cor, placa, numero_rodas, carregado):
        # "super()" chama o construtor da superclasse (Veiculo).
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado  # Atributo para indicar se o caminhão está carregado.

    # Método para verificar se o caminhão está carregado.
    def esta_carregado(self):
        # Imprime "Sim" ou "Não" dependendo do valor de self.carregado.
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

# Criando objetos das classes Motocicleta, Carro e Caminhao.
moto = Motocicleta('preta', 'abc-1234', 2)  # Criando uma motocicleta.
print(moto)  # Imprime as informações da motocicleta.
moto.ligar_motor()  # Chama o método ligar_motor da motocicleta.

carro = Carro('branca', 'xde-0098', 4)  # Criando um carro.
print(carro)  # Imprime as informações do carro.
carro.ligar_motor()  # Chama o método ligar_motor do carro.

Caminhao = Caminhao('roxa', 'gfe-8712', 8, True)  # Criando um caminhão.
print(Caminhao)  # Imprime as informações do caminhão.
Caminhao.ligar_motor()  # Chama o método ligar_motor do caminhão.
Caminhao.esta_carregado()  # Chama o método esta_carregado do caminhão.

# Herança Múltipla (Multiple Inheritance)
# Uma classe pode herdar de múltiplas classes ao mesmo tempo.

# Classe base Animal
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

# Classe Mamifero, que herda de Animal
class Mamifero(Animal):
    # Utiliza **kw para suportar argumentos nomeados na classe Animal.
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw) # Utiliza **kw para passar os argumentos para a superclasse.

# Classe Ave, que também herda de Animal
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

# Classes que herdam de Mamifero
class cachorro(Mamifero):
    pass

class gato(Mamifero):
    pass

class leao(Mamifero):
    pass

# Classe que herda de Mamifero e Ave (herança múltipla)
class ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        # .__mro__ e .mro() mostram a ordem de resolução de métodos.
        print(ornitorrinco.__mro__) #mostra as classes pais em ordem.
        print(ornitorrinco.mro()) #idem.
        # Estamos invocando os construtores das superclasses, passando cada um para sua respectiva classe pai.
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

# Criando instancias.
gato = gato(nro_patas=4, cor_pelo='preto')
print(gato)

ornitorrinco = ornitorrinco(nro_patas=4, cor_pelo='laranja', cor_bico='preto')
print(ornitorrinco)

# --- Exemplos de Superclass e Subclass (Reiterando o Conceito) ---
class Superclass:
    # Atributos e métodos da Superclasse
    pass

class Subclass(Superclass):
    # Atributos e métodos da Subclasse
    # Pode sobrescrever métodos da Superclasse
    pass

#--- outro exemplo de super e sub class ---
class Superclass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        print("Method from Superclass")

class Subclass(Superclass):
    def __init__(self, value, other_value):
        # Chamando o construtor da Superclasse usando super()
        super().__init__(value)
        self.other_value = other_value

    def my_method(self):
        # Chamando o método da Superclasse usando super()
        super().my_method()
        print("Method from Subclass")

# --- Exemplo de Bicicleta e MountainBike (Revisando Herança e Sobrescrita) ---
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('plim plim')

    def parar(self):
        print('parando bicicleta...')
        print('bicicleta parada!!!')

    def correr(self):
        print('vrummmmmmm...')

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class MountainBike(Bicicleta):  # MountainBike herda de Bicicleta
    def __init__(self, cor, modelo, ano, valor, suspension_type):
        super().__init__(cor, modelo, ano, valor)  # Chama o __init__ da classe Bicicleta
        self.suspension_type = suspension_type  # Novo atributo específico da MountainBike

    def jump(self):  # Novo método específico da MountainBike
        print("Jumping over obstacles!")

    def correr(self):  # Sobrescrita do método correr
        print("Vrummmm Vrummm... on uneven terrain!")

# --- Exemplo de uso da MountainBike ---
my_mountain_bike = MountainBike("black", "FullSus", 2023, 1200, "Full")
my_mountain_bike.buzinar()  # Herdado de Bicicleta
my_mountain_bike.parar()  # Herdado de Bicicleta
my_mountain_bike.jump()  # Método único da MountainBike
my_mountain_bike.correr()  # Método sobrescrito (comportamento diferente)
print(my_mountain_bike)


