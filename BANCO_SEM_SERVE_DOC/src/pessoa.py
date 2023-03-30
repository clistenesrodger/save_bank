class Pessoa():

    __slots__ = ['_nome','_endereco','_cpf','_nascimento']

    def __init__(self,nome,endereco,cpf,nascimento):

        """
        A função __init__ é um método especial que é executado automaticamente ao criar um novo objeto do tipo Pessoa. 
        O objetivo desse método é inicializar os Parameters da classe com os valores fornecidos.

        Parameters:

        nome: uma string que representa o nome completo da pessoa (str)
        endereco: uma string que representa o endereço da pessoa (str)
        cpf: uma string que representa o CPF da pessoa (str)
        nascimento: um objeto do tipo datetime.date que representa a data de nascimento da pessoa (datetime.date)

        Parameters:

        _nome: uma string que representa o nome completo da pessoa (str)
        _endereco: uma string que representa o endereço da pessoa (str)
        _cpf: uma string que representa o CPF da pessoa (str)
        _nascimento: um objeto do tipo datetime.date que representa a data de nascimento da pessoa (datetime.date)
        
        """
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._nascimento = nascimento

    @property
    def nome(self):

        """
        A função nome é um método de acesso de propriedade que retorna o valor do atributo privado _nome de um objeto do tipo Pessoa.

        Returns:

        O valor do atributo privado _nome (str)
        """
        return self._nome

    @nome.setter
    def nome(self,n):
        """
        A função nome é um método de modificação de propriedade que atribui um novo valor ao atributo privado _nome de um objeto do tipo Pessoa.

        Parameters:

        n: uma string que representa o novo valor do nome da pessoa (str)
        """
        self._nome = n

    @property
    def endereco(self):

        """
        
        A função endereco é um método de acesso de propriedade que retorna o valor do atributo privado _endereco de um objeto do tipo Pessoa.

        Returns:

        O valor do atributo privado _endereco (str)

        """
        return self._endereco

    @endereco.setter
    def endereco(self,s):

        """
        A função endereco é um método de modificação de propriedade que atribui um novo valor ao atributo privado _endereco de um objeto do tipo Pessoa.

        Parameters:

        s: uma string que representa o novo valor do endereço da pessoa (str)
        
        """

        self._endereco = s

    @property
    def cpf(self):

        """
        A função cpf é um método de acesso de propriedade que retorna o valor do atributo privado _cpf de um objeto do tipo Pessoa.

        Returns:

        O valor do atributo privado _cpf (str)
        
        """

        return self._cpf

    @cpf.setter
    def cpf(self,c):

        """
        A função cpf é um método de modificação de propriedade que atribui um novo valor ao atributo privado _cpf de um objeto do tipo Pessoa.

        Parameters:

        c: uma string que representa o novo valor do CPF da pessoa (str)


        
        """
        self._cpf = c

    @property
    def nascimento(self):

        """
        A função nascimento é um método de acesso de propriedade que retorna o valor do atributo privado _nascimento de um objeto do tipo Pessoa.

        Returns:

        O valor do atributo privado _nascimento (str)
        
        """

        return self._nascimento

    @nascimento.setter
    def nascimento(self,n):

        """
        
        A função nascimento.setter é um método modificador de propriedade que define o valor do atributo privado _nascimento de um objeto do tipo Pessoa.

        Parameters:

        n (str): valor para ser atribuído ao atributo privado _nascimento

        Returns:

        Nenhum.



        """

        self._nascimento = n
