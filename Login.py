def verifica_login(bd_usuarios):
    global usuario_confirmado, user
    user = input('\nDigite seu usuário: ')
    senha = input('\nDigite sua senha: ')
    print('')
    for usuario in bd_usuarios:
        nome_usuario = usuario.get('username')
        senha_usuario = usuario.get('password')
        if (user == nome_usuario and senha == senha_usuario):
            usuario_confirmado = True
            return usuario_confirmado