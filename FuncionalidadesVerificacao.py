def verifica_login(bd_usuarios):
    usuario_invalido = []
    usuario_valido = [False]

    user = input('\nDigite seu usuário: ')
    senha = input('\nDigite sua senha: ')
    print('')
    for usuario in bd_usuarios:
        nome_usuario = usuario.get('username')
        senha_usuario = usuario.get('password')
        if (user == nome_usuario and senha == senha_usuario):
            usuario_valido = [True, nome_usuario]
        else:
            usuario_invalido = [False]
    
    if usuario_valido[0] == True:
        return usuario_valido
    else:
        return usuario_invalido
    

def verifica_credencial(nome_usuario,bd_usuarios):
    for usuario in bd_usuarios:
        if nome_usuario == usuario.get('username'):
            dados_usuario = usuario
            break
    
    if dados_usuario['credencial'] == 'administrador':
        print("O usuario é administrador")
    elif dados_usuario['credencial'] == 'gerente':
        print("O usuario é gerente")
    else:
        print("O usuario é assistente")