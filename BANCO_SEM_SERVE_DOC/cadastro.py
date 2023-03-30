from pessoa import Pessoa

class Cadastro():

    __slots__ = ['_dicionario_pessoas']

    def __init__(self) -> None:

        """
        
        A função __init__ inicializa um objeto da classe Banco, que contém um dicionário vazio para armazenar as contas bancárias das pessoas cadastradas.

        Não recebe nenhum argumento além do self, que representa o próprio objeto instanciado.

        Atributos:

        _dicionario_pessoas: um dicionário vazio para armazenar as contas bancárias das pessoas cadastradas (dicionário)

        Retorno:

        Não há retorno nesta função.

        """

        self._dicionario_pessoas = {}

    def cadastrar(self,cpf,pessoa):

        """
        A função cadastrar recebe um CPF e um objeto do tipo Pessoa e adiciona uma nova entrada ao dicionário _dicionario_pessoas do objeto Banco, associando o CPF fornecido ao objeto Pessoa fornecido.

        Parâmetros:

         cpf: uma string que representa o CPF da pessoa a ser cadastrada (str)
        pessoa: um objeto do tipo Pessoa a ser cadastrado (objeto)

        Atributos:

        _dicionario_pessoas: um dicionário que armazena as contas bancárias das pessoas cadastradas (dicionário)

        Retorno:

        True se o CPF fornecido ainda não estiver associado a uma pessoa cadastrada e o objeto pessoa fornecido for do tipo Pessoa
        False se o CPF fornecido já estiver associado a uma pessoa cadastrada ou se o objeto pessoa fornecido não for do tipo Pessoa.
        
        """

        if cpf not in self._dicionario_pessoas.keys() and isinstance(pessoa,Pessoa):
            self._dicionario_pessoas[cpf] = pessoa
            return True
        else:
            return False

    def buscar(self,cpf):

        """
        A função buscar recebe um CPF e retorna o objeto do tipo Pessoa associado a esse CPF, se existir.

        Parâmetros:

        cpf: uma string que representa o CPF da pessoa a ser buscada (str)

        Atributos:

        _dicionario_pessoas: um dicionário que armazena as contas bancárias das pessoas cadastradas (dicionário)

        Retorno:

        O objeto do tipo Pessoa associado ao CPF fornecido, se existir
        None se o CPF fornecido não estiver associado a nenhuma pessoa cadastrada.



        """

        if cpf in self._dicionario_pessoas.keys():
            return self._dicionario_pessoas[cpf]
        else:
            return None