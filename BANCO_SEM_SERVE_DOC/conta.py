import datetime
class Conta:

    """
    Inicializa um objeto Conta com os dados fornecidos.

    :param numero: número da conta.
    :type numero: int
    :param pessoa: nome do titular da conta.
    :type pessoa: str
    :param limite: limite de crédito da conta.
    :type limite: float
    :param login: login para acesso à conta.
    :type login: str
    :param senha: senha para acesso à conta.
    :type senha: str

    """

    def __init__(self,numero,pessoa,limite,login,senha):
        self.numero = numero
        self.pessoa = pessoa
        self.saldo = 0
        self.limite = limite
        self.login = login
        self.senha = senha
        self.historico = Historico()

    def deposito(self,valor):
        """
        Essa função é um método de uma classe de conta bancária que adiciona um valor de depósito ao saldo da conta e registra a transação no histórico de transações da conta bancária. A função realiza as seguintes tarefas:

        Parâmetros:

        valor (float): o valor do depósito a ser adicionado ao saldo da conta bancária.

        Retorno:

        A função retorna True se o valor do depósito for maior que zero e o depósito for bem-sucedido. Caso contrário, retorna False.
        
        """
        if valor > 0:
            self.saldo += valor
            self.historico.transacoes.append(f"deposito de {valor}")
            return True
        else:
            return False

    def sacar(self,valor):

        """
        Essa função é um método de uma classe de conta bancária que adiciona um valor de depósito ao saldo da conta 
        e registra a transação no histórico de transações da conta bancária.

        Parâmetros:

        valor (float): o valor do depósito a ser adicionado ao saldo da conta bancária.

        Retorno:

        A função retorna True se o valor do depósito for maior que zero e o depósito for bem-sucedido. Caso contrário, retorna False.
        

        """

        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f"saque de {valor}")
            return True
            
    def transfere(self,destino,valor):

        """
        Essa função é um método de uma classe de conta bancária que realiza uma transação de saque na conta, 
        subtraindo o valor especificado do saldo da conta e registrando a transação no histórico de transações da conta bancária. 

        Argumentos:

        valor (float): o valor do saque a ser subtraído do saldo da conta bancária.

        Retorno:

        A função retorna True se o valor do saque for menor ou igual ao saldo da conta bancária e a transação de saque for bem-sucedida. 
        Caso contrário, retorna False.

        """

        retirou = self.sacar(valor)
        if (retirou == False):
            return False
        else:
            destino.deposito(valor)
            self.historico.transacoes.append(f"transferência de {valor} para conta {destino.numero}")
            return True

    def extrato(self):
        self.historico.transacoes.append(f"tirou extrato - saldo de {self.saldo}")
        return f"numero: {self.numero}\nsaldo:{self.saldo}"
        
class Historico:

    def __init__(self):

        """
        A função __init__ inicializa um objeto da classe Historico, que contém informações sobre a data de abertura da conta e uma lista vazia de transações.

        Não recebe nenhum argumento além do self, que representa o próprio objeto instanciado.

        Atributos:

        data_abertura: a data e hora em que a instância do objeto foi criada (objeto do tipo datetime.datetime)
        transacoes: uma lista vazia de transações realizadas na conta (lista)

        Retorno:

        Não há retorno nesta função.

        """

        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    
    def imprime(self):
        """
        essa função retorna a data de abertura e transações de uma conta

        """
        #print(f"data abertura: {self.data_abertura}")
        #print("transações: ")
        #for t in self.transacoes:
            #print("-", t)
  
        return f"data de abertura: {self.data_abertura}\ntransações: {self.transacoes}"
                   

