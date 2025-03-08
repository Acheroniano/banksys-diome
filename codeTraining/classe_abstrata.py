# classe_abstrata.py (Comentários e explicações em PT-BR por um Dev Júnior)

from abc import ABC, abstractmethod

# Importação das classes ABC e abstractmethod do módulo abc (Abstract Base Classes).
#   - from abc import ABC, abstractmethod: Importa as classes necessárias para definir classes abstratas.
#       - ABC: Classe base para criar classes abstratas.
#       - abstractmethod: Decorador para métodos abstratos.


class ControleRemoto(ABC):
    # Classe ControleRemoto: Define uma classe abstrata ControleRemoto.  
    # Uma classe abstrata não pode ser instanciada diretamente; serve como modelo para outras classes.
    # - class ControleRemoto(ABC): Define a classe "ControleRemoto" que herda de "ABC" 
    # (Abstract Base Class), tornando-a abstrata.

    @abstractmethod
    def ligar(self):
        pass
    # Método abstrato ligar:  Define um método que *deve* ser implementado pelas subclasses.
    #   - @abstractmethod: Este decorador indica que o método é abstrato.  
    #   Subclasses obrigatoriamente devem implementá-lo.
    #   - def ligar(self):  A definição do método, que não faz nada (pass).

    @abstractmethod
    def desligar(self):
        pass
    # Método abstrato desligar: Similar ao método ligar, 
    #   este método também é abstrato e deve ser implementado pelas subclasses.
    #   - @abstractmethod: Decorador indicando que o método é abstrato.
    #   - def desligar(self): Definição vazia do método.

    @property
    @abstractmethod
    def marca(self):
        pass
    # Propriedade abstrata marca: Define uma propriedade (getter) 
    #   abstrata que deve ser implementada pelas subclasses. Propriedades usam o decorador @property.
    #   - @property: Decorador que transforma o método em uma propriedade.
    #   - @abstractmethod: Decorador indicando que o método é abstrato.
    #   - def marca(self): Definição vazia da propriedade.


class ControleTV(ControleRemoto):
    # Classe ControleTV: Classe concreta que herda de ControleRemoto e implementa seus métodos abstratos.  Classes concretas podem ser instanciadas.
    #   - class ControleTV(ControleRemoto): Define a classe "ControleTV", que herda de "ControleRemoto".

    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")
    # Implementação do método ligar para ControleTV.
    #   - def ligar(self): Define o método "ligar" para a classe "ControleTV".
    #       - print("Ligando a TV..."): Imprime uma mensagem na tela.
    #       - print("Ligada!"): Imprime uma mensagem indicando que a TV está ligada.

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")
    # Implementação do método desligar para ControleTV.
    #   - def desligar(self): Define o método "desligar" para a classe "ControleTV".
    #       - print("Desligando a TV..."): Imprime uma mensagem na tela.
    #       - print("Desligada!"): Imprime uma mensagem indicando que a TV está desligada.

    @property
    def marca(self):
        return "LG"
    # Implementação da propriedade marca para ControleTV.
    #   - @property: Decorador que define como uma propriedade.
    #   - def marca(self): Define a propriedade "marca" para retornar "LG".


class ControleArCondicionado(ControleRemoto):
    # Classe ControleArCondicionado: Outra classe concreta herdando de ControleRemoto, 
    # com sua própria implementação dos métodos abstratos.
    # - class ControleArCondicionado(ControleRemoto): Define a classe "ControleArCondicionado",
    # herdando de "ControleRemoto".

    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")
    # Implementação do método ligar para ControleArCondicionado.
    #   - def ligar(self): Define o método "ligar" para a classe "ControleArCondicionado".
    #       - print("Ligando o Ar Condicionado..."): Imprime uma mensagem.
    #       - print("Ligado!"): Imprime uma mensagem indicando que o ar condicionado está ligado.

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")
    # Implementação do método desligar para ControleArCondicionado.
    #   - def desligar(self): Define o método "desligar" para a classe "ControleArCondicionado".
    #       - print("Desligando o Ar Condicionado..."): Imprime uma mensagem.
    #       - print("Desligado!"): Imprime uma mensagem indicando que o ar condicionado está desligado.

    @property
    def marca(self):
        return "Samsung"
    # Implementação da propriedade marca para ControleArCondicionado.
    #   - @property: Decorador para definir como uma propriedade.
    #   - def marca(self): Define a propriedade "marca" para retornar "Samsung".


controle = ControleTV()
# Criação de um objeto ControleTV.
#   - controle = ControleTV(): Cria uma instância da classe "ControleTV" e a atribui à variável "controle".

controle.ligar()
# Chamada do método ligar do objeto controle.
#   - controle.ligar(): Chama o método "ligar" da instância "controle".

controle.desligar()
# Chamada do método desligar do objeto controle.
#   - controle.desligar(): Chama o método "desligar" da instância "controle".

print(controle.marca)
# Imprime a marca do controle.
#   - print(controle.marca): Imprime o valor retornado pela propriedade "marca" da instância "controle".


controle = ControleArCondicionado()
# Criação de um objeto ControleArCondicionado.
#   - controle = ControleArCondicionado(): Cria uma instância da classe "ControleArCondicionado".

controle.ligar()
# Chamada do método ligar.
#   - controle.ligar(): Chama o método "ligar" da instância "controle".

controle.desligar()
# Chamada do método desligar.
#   - controle.desligar(): Chama o método "desligar" da instância "controle".

print(controle.marca)
# Imprime a marca.
#   - print(controle.marca): Imprime o valor retornado pela propriedade "marca" da instância "controle".

