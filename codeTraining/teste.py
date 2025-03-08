''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

class ContaBancaria:
    # TODO: Inicialize a conta bancária com o nome do titular, saldo 0 e  liste para armazenar as operações realizadas:
        def __init__(self, user_titular):
          self.user_titular = user_titular
          self.usaldo = 0
          self.operacoes = ["Operações: "]
          
    # TODO: Implemente o método para realizar um depósito, adicione o valor ao saldo e registre a operação:
        def depositar(self, valor):
          self.usaldo += valor
          if self.user_titular == "Ana":
            self. operacoes.append(f"+{valor}; ")
          else:
            self.operacoes.append(f"+{valor}, ")

    # TODO: Implemente o método para realizar um saque:
        def sacar(self, valor):
        # TODO: Verifique se há saldo suficiente para o saque
        # TODO: Subtraia o valor do saldo (valor já é negativo)
          if self.usaldo >= abs(valor):
            self.usaldo -= abs(valor)
            self.operacoes.append(f"{valor:}, ")
            
        # TODO: Registre a operação e retorne a  mensagem de saque negado
          else:
            self.operacoes.append(f"Saque não permitido; ")

    # TODO: Crie o método para exibir o extrato da conta e junte as operações no formato correto:
        def extrato(self):
          texto = ""
          for operacao in self.operacoes:
            texto=texto + operacao
          texto = texto + (f"Saldo: {self.usaldo}")
          print(texto)


nome_titular = input().strip()  
conta = ContaBancaria(nome_titular)  

entrada_transacoes = input().strip() 
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]  

for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)  
    else:
        conta.sacar(valor)  

conta.extrato()