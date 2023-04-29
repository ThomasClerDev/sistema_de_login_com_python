'''O sistema de login deve permitir que novos usuários sejam cadastrados, 
e que usuários existentes possam fazer o login.
O sistema deve alertar caso a senha e login não estejam certos.'''

resposta = input('[1] - Cadastrar novo usuário [2] - Fazer Login: ')

# armazenando os usuários existentes
usuarios = ['carol', 'Amanda', 'Jeff']
senhas = ['123456', 'abcdef', '123abcd']


# if condicao == condicao
if resposta == '1':
    # recebendo um usuário
    usuario_digitado = input('digite seu usuário: ')
    # O sistema não deve permitir que usuários duplicados sejam cadastrados;

    if usuario_digitado in usuarios:
        print('Usuário existente!')

    else:
        # recebendo uma senha
        senha_digitada = input('digite sua senha: ')

        # Caso não exista, cadastrar aquele usuário e senha
        usuarios.append(usuario_digitado)
        senhas.append(senha_digitada)

elif resposta == '2':
    # Permitir que usuários existentes possam fazer o login;

    # Pedir usuário
    usuario_digitado = input('Digite seu usuário: ')

    # pedir senha
    senha_digitada = input('Digite sua senha: ')
    # preciso verificar se a senha providenciada para aquele usuário é a mesma da lista

    encontrado = False

    for indice, usuario in enumerate(usuarios):
        if usuario_digitado == usuario and senha_digitada == senhas[indice]:
            print('Login feito com sucesso!')
            encontrado = True

        elif encontrado == False:
            # O sistema deve alertar caso a senha e login não estejam corretos.
            print('Usuário ou senha incorreto!')
else:
    print('Digite apenas 1 ou 2')
