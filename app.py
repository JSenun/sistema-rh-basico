from AtualizaDataBase import *
from Funcionario import Funcionario
from Login import *

# Funções "Gráficas" CMD
def cria_linha(separador, tamanho_linha=100):
    print(separador * tamanho_linha)

def cria_cabecalho(string):
    cria_linha('=')
    print(string.center(100))
    cria_linha('=')
    return

# Importando o "Banco de Dados" do arquivo JSON
banco_dados = le_arquivo_json('db.json')


# Separando as bases de usuários e colaboradores
db_usuarios = banco_dados.get('usuarios')
db_colaboradores_ativos = banco_dados.get('colaboradores_ativos')
db_colaboradores_inativos = banco_dados.get('colaboradores_inativos')

# Programa
fechar_programa = False
usuario_confirmado = False
tentativas_login = 3
while fechar_programa != True:
    if usuario_confirmado == True:
        print("\nAcesso Confirmado")
        fechar_programa = True
    elif  tentativas_login == 3 :
        cria_cabecalho('Sistema de Recursos Humanos - Five RH')
        print(f"\nFavor fazer login no sistema: ({tentativas_login} TENTATIVAS)")
        usuario_confirmado = verifica_login(db_usuarios)
        cria_linha('=')
        tentativas_login -= 1
    elif tentativas_login != 0 and tentativas_login != 3:
        print(f'\nLogin incorreto! Verificar usuário  e senha. TENTATIVAS RESTANTES: {tentativas_login}')
        usuario_confirmado = verifica_login(db_usuarios)
        cria_linha('=')
        tentativas_login -= 1
    else: 
        print("Acesso negado! Favor tentar novamente mais tarde")
        fechar_programa = True