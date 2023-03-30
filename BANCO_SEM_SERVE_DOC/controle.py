from PyQt5 import uic,QtWidgets
import mysql.connector
import datetime


def verifica_login():

    """
     é utilizada para verificar se um usuário está cadastrado em um banco de dados e se as informações de login e senha digitadas são válidas.

    Parâmetros:

    Nenhum

    Retorno:

    Nenhum

    Argumentos:

    Nenhum

    Atributos globais:

    "global_cpf": Variável global utilizada para armazenar o CPF do usuário logado.
    """

    

    global global_cpf
    tela_login.label_5.setText("")
    login_lido = tela_login.lineEdit.text()
    senha_lida = tela_login.lineEdit_2.text()
    cpf = tela_login.lineEdit_3.text()

    if cpf not in ' !@#*+-_=''"\|/' and login_lido not in ' !@#*+-_=''"\|/' and senha_lida not in ' !@#*+-_=''"\|/':
        global_cpf = cpf

        con = mysql.connector.connect(host='localhost',database='mono_banco',user='root',password='rodger090')
        cursor = con.cursor()
        comando = f"select * from conta where cpf_key= {global_cpf}"
        cursor.execute(comando)
        resultado = cursor.fetchall()

        if ( resultado != [] ):

            if ((resultado[0][3] == login_lido) and (resultado[0][4] == senha_lida)):
                menu_de_operacoes.show()
                tela_login.close()
                tela_login.lineEdit.setText("")
                tela_login.lineEdit_2.setText("")
                tela_login.lineEdit_3.setText("")
            else:
                tela_login.label_5.setText("dados de login ou senha incorretos!")
        else:
            tela_login.label_5.setText("CPF não cadastrado!")
    else:
        tela_login.label_5.setText("há campos em branco!")

    

def cadastro():
    
    """
    A função "cadastro" é utilizada para exibir a tela de cadastro de um novo usuário.

    Parâmetros:

    Nenhum

    Retorno:

    Nenhum

    Argumentos:

    Nenhum

    Atributos globais:

    Nenhum

    """

    tela_login.lineEdit.setText("")
    tela_login.lineEdit_2.setText("")
    tela_login.lineEdit_3.setText("")
    cadastramento.show()
    tela_login.hide() 
    cadastramento.pushButton.clicked.connect(finalizar_cad)
    cadastramento.pushButton_3.clicked.connect(voltar_4)
    cadastramento.pushButton_2.clicked.connect(sair_4)

def finalizar_cad():

    """
    é responsável por finalizar o cadastro de um novo usuário no sistema. Ela recebe informações do novo usuário preenchidas na interface gráfica de cadastro e as insere no banco de dados.

    Argumentos:

    Não possui argumentos.

    Comportamento:

    Recupera as informações do novo usuário preenchidas na interface gráfica de cadastro;
    Conecta ao banco de dados usando as credenciais fornecidas;
    Executa as instruções SQL para inserir as informações do novo usuário nas tabelas "pessoa", "conta" e "operacoes";
    Exibe mensagem na interface gráfica indicando o sucesso ou falha na operação.

    Retorno:

    Não possui retorno.


    """
    
    nome = cadastramento.lineEdit.text()
    endereco = cadastramento.lineEdit_2.text()
    cpf = cadastramento.lineEdit_3.text()
    nascimento = cadastramento.lineEdit_4.text()
    numero = cadastramento.lineEdit_5.text()
    limite = cadastramento.lineEdit_6.text()
    login = cadastramento.lineEdit_7.text()
    senha = cadastramento.lineEdit_8.text()

    con = mysql.connector.connect(host='localhost',database='mono_banco',user='root',password='rodger090')
    cursor1 = con.cursor()
    cursor2 = con.cursor()
    cursor3 = con.cursor()
    comando1 = "INSERT INTO pessoa (cpf_key, nome, endereco,nascimento) values ( %s,%s,%s,%s )"
    comando2 = "INSERT INTO conta (cpf_key,numero,limite,login,senha) values (%s,%s,%s,%s,%s)"
    comando3 = "INSERT INTO operacoes (cpf_key,extrato,historico,saldo) values ( %s,%s,%s,%s )"
    
    
    if con.is_connected():
        db_info = con.get_server_info()
        print('Conectado ao servidor MySQL versão ',db_info)
        cursor = con.cursor()
        cursor.execute('select database();')
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ",linha)


        if nome not in ' !@#*+-_=''"\|/' and endereco not in ' !@#*+-_=''"\|/' and cpf not in ' !@#*+-_=''"\|/' and nascimento not in ' !@#*+-_=''"\|/' and numero not in ' !@#*+-_=''"\|/' and limite not in ' !@#*+-_=''"\|/' and login not in ' !@#*+-_=''"\|/' and senha not in ' !@#*+-_=''"\|/':

            str1 = ''
            saldo = 0.00
            data = datetime.datetime.today()
            data2 = str(data)
            #data3 = re.search(r"\d{4}-\d{2}-\d{2}-",data).group
            data2 = 'abertura de conta: ' + data2
            cursor1.execute(comando1,(cpf,nome,endereco,nascimento))
            cursor2.execute(comando2,(cpf,numero,limite,login,senha))
            cursor3.execute(comando3,(cpf,str1,data2,saldo))
            con.commit()

            cadastramento.label_10.setText("cadastro feito com sucesso")
            cadastramento.lineEdit.setText("")
            cadastramento.lineEdit_2.setText("")
            cadastramento.lineEdit_3.setText("")
            cadastramento.lineEdit_4.setText("")
            cadastramento.lineEdit_5.setText("")
            cadastramento.lineEdit_6.setText("")
            cadastramento.lineEdit_7.setText("")
            cadastramento.lineEdit_8.setText("")
        else:
            cadastramento.label_10.setText(" Há campos em branco")

    else:
        print('deu ruim')

 

def depositar():

    """
    A função depositar() exibe a tela de depósito e define as funções a serem executadas quando os botões são pressionados.
    Quando o botão "Voltar" é pressionado, a função voltar_2() é chamada para retornar ao menu de operações. Quando o botão "Confirmar" é pressionado,
    a função confirma_deposito() é chamada para realizar o depósito. Quando o botão "Sair" é pressionado, a função sair_2() é chamada para fechar o programa.
    """

    deposita.show()
    menu_de_operacoes.close() #
    deposita.pushButton.clicked.connect(voltar_2)
    deposita.pushButton_2.clicked.connect(confirma_deposito)
    deposita.pushButton_3.clicked.connect(sair_2)

def confirma_deposito():

    """
    Confirma o depósito na conta do usuário.

    A função se conecta ao banco de dados do sistema e faz uma consulta para obter as informações da conta do usuário. 
    Em seguida, verifica se o valor informado para o depósito é válido e atualiza o saldo e o histórico da conta com as informações do depósito realizado.

    Args:
    Nenhum.

    Returns:
    Nenhum.
    """
    con = mysql.connector.connect(host='localhost',database='mono_banco',user='root',password='rodger090')
    cursor = con.cursor()
    comando1 = f"select * from operacoes where cpf_key= {global_cpf}"
    cursor.execute(comando1)
    resultado = cursor.fetchall()


    string = (deposita.lineEdit.text())
    if string not in ' !!!!@#*+-_=''"\|/':
        valor = float(string)
        if (valor < 0):
            deposita.label_4.setText("valor inválido")
        else:
            deposita.label_4.setText("deposito feito com sucesso")
            deposita.lineEdit.setText("")
            comando2 = f"UPDATE operacoes SET saldo = {resultado[0][3] + valor} where cpf_key= {global_cpf}"
            mod = resultado[0][2] + "\n deposito: " + string
            comando3 = f"UPDATE operacoes SET historico = (%s) where cpf_key= (%s)"
            print(comando2)
            print(comando3)
            
            cursor.execute(comando2)
            cursor.execute(comando3,(mod,global_cpf))
            con.commit()
    else:
        deposita.label_4.setText('preencha o campo do valor')

    print(resultado[0][3])




def sacar():
    """
    A função sacar() exibe a janela de saque (saque) e conecta seus botões de ação a outras funções. 
    Quando o botão "Voltar" é clicado, a função voltar_3() é chamada. Quando o botão "Confirmar" é clicado, a função confirma_sacar() é chamada. 
    E quando o botão "Sair" é clicado, a função sair_3() é chamada.

    """
    saque.show()
    menu_de_operacoes.close() #
    saque.pushButton.clicked.connect(voltar_3)
    saque.pushButton_2.clicked.connect(confirma_sacar)
    saque.pushButton_3.clicked.connect(sair_3)

def confirma_sacar():

    """
    A função confirma_sacar() recebe os valores informados pelo usuário para realizar uma operação de saque em sua conta bancária, 
    verifica se a senha informada é correta, se o valor do saque é maior que zero e se o saldo é suficiente para realizar a operação. 
    Em caso positivo, atualiza o saldo na tabela de operações e registra a operação de saque no histórico.

    Parâmetros:

    Não possui parâmetros.

    Retorno:

    Não possui retorno.

    """

    saque.label_5.setText('')
    string = saque.lineEdit.text()
    senha = saque.lineEdit_2.text()

    con = mysql.connector.connect(host='localhost',database='mono_banco',user='root',password='rodger090')
    cursor = con.cursor()
    comando1 = f"select * from conta where cpf_key= {global_cpf}"
    comando2 = f"select * from operacoes where cpf_key= {global_cpf}"
    cursor.execute(comando1)
    resultado1 = cursor.fetchall()
    cursor.execute(comando2)
    resultado2 = cursor.fetchall()

    if string not in ' !@#*+-_=''"\|/' and senha not in ' !@#*+-_=''"\|/':
        valor = float(string)
        if (resultado1[0][3] == senha):
            if resultado2[0][3] >= valor and valor > 0:
                    saque.label_5.setText('saque feito com sucesso')
                    saque.lineEdit.setText("")
                    saque.lineEdit_2.setText("")
                    comando3 = f"UPDATE operacoes SET saldo = {resultado2[0][3] - valor} where cpf_key= {global_cpf}"
                    mod = resultado2[0][2] + "\n saque: " + string
                    comando4 = f"UPDATE operacoes SET historico = (%s) where cpf_key= (%s)"
                    cursor.execute(comando3)
                    cursor.execute(comando4,(mod,global_cpf))
                    con.commit()
            else:
                    saque.label_5.setText('saldo insuficiente')
        else:
                saque.label_5.setText('senha incorreta')  
    else:
        saque.label_5.setText('preencha os campos vazios')
   



def transfere():

    """
    Esta função exibe a tela de transferência de uma conta para outra e conecta os botões "Voltar", "Confirmar" e "Sair" com as funções correspondentes.

    Argumentos:

    Nenhum.

    Retorno:

    Nenhum.

    """
    
    transferencia.show()
    menu_de_operacoes.close() #
    transferencia.pushButton.clicked.connect(voltar_5)
    transferencia.pushButton_2.clicked.connect(confirma_transferir)
    transferencia.pushButton_3.clicked.connect(sair_5)

def confirma_transferir():

    """
    Essa função "confirma_transferir()" é responsável por confirmar a transferência de um valor entre duas contas cadastradas no banco.

    Parâmetros:

    nenhum

    Retorno:

    nenhum

    Exceções:

    nenhum

    """

    string = (transferencia.lineEdit.text())
    beneficiado = transferencia.lineEdit_2.text()
    senha = transferencia.lineEdit_3.text()

    con = mysql.connector.connect(host='localhost',database='mono_banco',user='root',password='rodger090')
    cursor = con.cursor()
    comando1 = f"select * from conta where cpf_key= {global_cpf}"
    comando2 = f"select * from operacoes where cpf_key= {global_cpf}"
    comando3 = f"select * from operacoes where cpf_key= {beneficiado}"
    cursor.execute(comando1)
    resultado1 = cursor.fetchall()
    cursor.execute(comando2)
    resultado2 = cursor.fetchall()
    cursor.execute(comando3)
    resultado3 = cursor.fetchall()

    if string not in ' !@#*+-_=''"\|/' and beneficiado not in ' !@#*+-_=''"\|/' and senha not in ' !@#*+-_=''"\|/':
        valor = float(string)
       
        if resultado1[0][4] == senha:
            if (resultado2[0][3] >= valor and valor > 0):
                transferencia.label_6.setText("transferencia realizada com sucesso")
                
                comando4 = f"UPDATE operacoes SET saldo = (%s) where cpf_key= (%s)"
                comando5 = f"UPDATE operacoes SET saldo = (%s) where cpf_key= (%s)"
                comando6 = f"UPDATE operacoes SET historico = (%s) where cpf_key= (%s)"
                comando7 = f"UPDATE operacoes SET historico = (%s) where cpf_key= (%s)"
                mod = resultado2[0][2] + "\n saque: " + string # conta principal
                mod2 = resultado3[0][2] + "\n deposito: " + string # conta do beneficiado
                cursor.execute(comando4,(resultado2[0][3] - valor,global_cpf))
                cursor.execute(comando5,(resultado3[0][3] + valor,beneficiado))
                cursor.execute(comando6,(mod,global_cpf))
                cursor.execute(comando7,(mod2,beneficiado))
                con.commit()
                
            else:
                transferencia.label_6.setText("saldo insuficiente")
        else:
                transferencia.label_6.setText("senha incorreta")
    else:
        transferencia.label_6.setText('preencha os campos vazios')

    


def consultar_extrato():

    """
    Essa função é responsável por exibir a tela de consulta de extrato bancário, onde o usuário pode visualizar todas as operações realizadas em sua conta. A função também conecta os botões presentes na tela às funções correspondentes.

    Parâmetros:

    Nenhum parâmetro é recebido pela função.

    Retorno:

    Nenhum valor é retornado pela função.

    """
    menu_de_operacoes.close() 
    extrato_tela.show()
    extrato_tela.pushButton.clicked.connect(voltar_6)
    extrato_tela.pushButton_2.clicked.connect(confirma_extrato)
    extrato_tela.pushButton_3.clicked.connect(sair_6)

def confirma_extrato():
    extrato_tela.listWidget.clear()
    con = mysql.connector.connect(host='localhost',database='mono_banco',user='root',password='rodger090')
    cursor = con.cursor()
    comando = f"select * from operacoes where cpf_key= {global_cpf}"
    cursor.execute(comando)
    resultado = cursor.fetchall()
    extratoui = str(resultado[0][3])
    extrato_tela.listWidget.addItem(extratoui)

    
    

#operações historico

def consultar_historico():

    """
    A função consultar_historico exibe a tela de histórico de operações e conecta seus botões "Voltar", 
    "Confirmar" e "Sair" às respectivas funções voltar_7(), confirma_historico() e sair_7().

    Não há parâmetros de entrada para essa função e nenhum valor de saída.

    """
    historico_tela.show()
    menu_de_operacoes.close() #
    historico_tela.pushButton.clicked.connect(voltar_7)
    historico_tela.pushButton_2.clicked.connect(confirma_historico)
    historico_tela.pushButton_3.clicked.connect(sair_7)

def confirma_historico():

    """
    Função: confirma_historico()

    Descrição: Esta função busca as operações registradas no banco de dados para um determinado CPF e exibe essas informações em uma lista na tela.

    Parâmetros:

    Nenhum parâmetro é passado explicitamente na chamada da função. A variável global_cpf é utilizada para determinar qual é o CPF que deve ser buscado no banco de dados.

    Retorno:

    Nenhum valor é retornado explicitamente pela função.

    """

    historico_tela.listWidget.clear()
    con = mysql.connector.connect(host='localhost',database='mono_banco',user='root',password='rodger090')
    cursor = con.cursor()
    comando1 = f"select * from operacoes where cpf_key= {global_cpf}"
    cursor.execute(comando1)
    resultado = cursor.fetchall()
    historico_tela.listWidget.addItem(resultado[0][2])




def voltar_1():
    """
    
    essa função realiza a abertuta da tela_login() e oculta a tela menu_de_operacoes

    """
    menu_de_operacoes.hide()
    tela_login.show()

def sair_1():
    """
    fecha a tela menu de operacoes

    """
    menu_de_operacoes.close()


def voltar_2():
    """
    
    aqui a tela deposita é ocultada e a tela menu_de_operacoes é aberta , e a tela deposita é limpa.

    """
    deposita.hide() 
    menu_de_operacoes.show()
    deposita.lineEdit.setText('')
    
def sair_2():
    """
    aqui a tela deposita é fechada
    
    """
    deposita.close()


def voltar_3():

    """
    aqui a tela saque é ocultada, o menu_de_operacoes é aberta, e o saque.lineEdit é limpo

    """
    saque.hide()  
    menu_de_operacoes.show()
    saque.lineEdit.setText('')
    saque.lineEdit_2.setText('')
    
def sair_3():

    """
    a tela de saque é fechada

    """
    saque.close()

def voltar_4():
    """
    aqui a tela de cadastramento é limpa, a tela de cadastramento é fechada enquanto a tela_login é aberta.

    """
    cadastramento.label_10.setText("")
    cadastramento.hide() 
    tela_login.show()
    cadastramento.lineEdit.setText("")
    cadastramento.lineEdit_2.setText("")
    cadastramento.lineEdit_3.setText("")
    cadastramento.lineEdit_4.setText("")
    cadastramento.lineEdit_5.setText("")
    cadastramento.lineEdit_6.setText("")
    cadastramento.lineEdit_7.setText("")
    cadastramento.lineEdit_8.setText("")
def sair_4():
    """
    a tela de cadastramento é fechada.
    """
    cadastramento.close()

def voltar_5():

    """
    aqui a tela de transferencia é ocultada e limpa,enquanto a tela  de menu_de_operacoes é aberta.

    """
    transferencia.hide() 
    menu_de_operacoes.show()
    transferencia.lineEdit.setText("")
    transferencia.lineEdit_2.setText("")
    transferencia.lineEdit_3.setText("")
    
def sair_5():

    """
    tela de transferencia é fechada

    """

    transferencia.close()

def voltar_6():

    """
    a tela de extrato é fechada e limpa, enquanto a tela menu_de_opetacoes é aberta.
    """
    extrato_tela.listWidget.clear()
    menu_de_operacoes.show() #
    extrato_tela.hide() #
    

def sair_6():
    """
    a tela extrato é fechada.

    """
    extrato_tela.close()

def voltar_7():

    """
    a tela de historico é ocultada e limpa, enquanto a tela de menu_de_operacoes é aberta.

    """
    historico_tela.listWidget.clear()
    menu_de_operacoes.show() 
    historico_tela.hide()

def sair_7():
    """
    
    a tela de historico é fechada.

    """
    historico_tela.close()

app = QtWidgets.QApplication([])




tela_login = uic.loadUi("login.ui")
cadastramento = uic.loadUi("cadastramento.ui")
menu_de_operacoes = uic.loadUi("menu_de_operacoes.ui")
deposita = uic.loadUi("depositar.ui")
saque = uic.loadUi("saque.ui")
transferencia = uic.loadUi("transferencia.ui")
extrato_tela = uic.loadUi("extrato.ui")
historico_tela = uic.loadUi("historico.ui")


tela_login.pushButton.clicked.connect(verifica_login)
tela_login.pushButton_2.clicked.connect(cadastro)
menu_de_operacoes.pushButton_6.clicked.connect(voltar_1)
menu_de_operacoes.pushButton_7.clicked.connect(sair_1)
menu_de_operacoes.pushButton.clicked.connect(depositar)
menu_de_operacoes.pushButton_2.clicked.connect(sacar)
menu_de_operacoes.pushButton_3.clicked.connect(transfere)
menu_de_operacoes.pushButton_4.clicked.connect(consultar_extrato)
menu_de_operacoes.pushButton_5.clicked.connect(consultar_historico)

"""botoes da tela depositar"""

tela_login.show()
app.exec()
