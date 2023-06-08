print('-'*80)
print('UNIFOR'.center(80))
print('-'*80)
print('Bem-vindo ao sistema de seleção de filmes BibCine!'.center(80))
print('-'*80)

# Dados de exemplo para o login
usuarios = {
    'usuario1': 'senha1',
    'usuario2': 'senha2',
    'usuario3': 'senha3'
}

administradores = {
    'admin': 'admin123'
}

# Lista de filmes disponíveis
filmes = [
    'Creed 2',
    'Super Mario',
    'Velozes e Furiosos 10',
    'Pequena Sereia',
    'Guardiões da Galáxia: vol.3'
]

# Variável para armazenar os votos
votos = {filme: 0 for filme in filmes}

# Variável para armazenar os usuários que já votaram
usuarios_votaram = []


# Função para cadastrar um novo usuário
def cadastrar_usuario():
    # Solicitar informações do usuário
    nome = input("Digite seu nome: ")
    usuario = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")

    # Adicionar o novo usuário ao dicionário de usuários
    usuarios[usuario] = senha
    print("Cadastro realizado com sucesso!".center(40))
    print("'"*40)

# Função para realizar o login
def fazer_login():
    usuario = input('Usuário: ')
    senha = input('Senha: ')

    if usuario in usuarios and senha == usuarios.get(usuario):
        print("_"*30)
        print('Login bem-sucedido!'.center(30))
        # Armazenar os dados de login no arquivo
        with open('logins.txt', 'a') as arquivo:
            arquivo.write(f'Usuário: {usuario}\n')
        return usuario
    
    elif usuario in administradores and senha == administradores.get(usuario):
        print("."*36)
        print('Login de administrador bem-sucedido!')
        menu_administrador()  # Chama a função do menu do administrador
        return None
    
    else:
        escolha5 = int(input('Usuário ou senha incorretos. Tente novamente. Ou aperte 5 para retornar ao menu: '))
        if escolha5 == 5:
            return None

# Função para escolher filmes
def escolher_filmes():
    print('\nLista de filmes disponíveis:')
    for i, filme in enumerate(filmes, start=1):
        print(f'{i}. {filme}')

    escolhas = []
    while True:
        escolha = input('\nDigite o número do filme que deseja adicionar (ou "sair" para sair): '.center(80))
        print("_"*80)
        
        if escolha.lower() == 'sair':
            break
        
        try:
            escolha_num = int(escolha)
            if escolha_num < 1 or escolha_num > len(filmes):
                print('Escolha inválida. Tente novamente.')
            elif filmes[escolha_num - 1] in escolhas:
                print('Filme já escolhido. Tente novamente.')
            else:
                escolhas.append(filmes[escolha_num - 1])
                print(f'Filme "{filmes[escolha_num - 1]}" adicionado à sua lista de escolhas.')
                break  # Encerra o loop após a primeira escolha
        except ValueError:
            print('Escolha inválida. Tente novamente.')

    return escolhas
def sugestao_filmes():
    while True:
      sugestao = input("Nos conte algum filme que você gostaria de assistir no Bibcine: ")
      decisao = int(input("Para voltar ao menu digite 1, para dar outra sugestão digite 2: "))

      with open('sugestao.txt', 'a') as arquivo:
              arquivo.write(f'Sugestão: {sugestao}\n')

      if decisao == 1:
        break
      elif decisao == 2:
        continue

def menu_administrador():
    while True:
        print("1 - Adicionar Filme")
        print("9 - Voltar")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            adicionar_filme()
        elif opcao == 9:
            break
        
def adicionar_filme():
    filme = input("Digite o nome do filme que deseja adicionar: ")
    filmes.append(filme)
    votos[filme] = 0
    print(f'O filme "{filme}" foi adicionado à lista de filmes.')
                

def menu():
    votacao_realizada = False
    while True:
        print("1 - Cadastro")
        print("2 - Fazer Login")
        print("3 - Dê sugestões de filmes para o BibCine.")
        print("9 - Sair")
        opcao = int(input("Digite o número da opção desejada: "))
        
        if opcao == 9:
            break
        elif opcao == 3:
            sugestao_filmes()
        elif opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            usuario = fazer_login()
            if usuario:
                # Verificar se o usuário já votou
                if usuario in usuarios_votaram:
                    print('Você já votou. Apenas um voto é permitido por usuário.')
                else:
                    escolhas = escolher_filmes()
                    for filme in escolhas:
                        votos[filme] += 1
                    votacao_realizada = True
                    usuarios_votaram.append(usuario)
        
                    

            else:
                print("É necessário fazer login para escolher filmes.")

    if votacao_realizada:
        # Exibir resultado da votação
        print('-' * 80)
        print('Resultado da votação:')
        for filme, votos_filme in votos.items():
            print(f'{filme}: {votos_filme} votos')

        # Encontrar a maior quantidade de votos
        maior_votos = max(votos.values())

        # Encontrar os filmes com a maior quantidade de votos
        filmes_mais_votados = [filme for filme, votos_filme in votos.items() if votos_filme == maior_votos]

        print('_' * 50)
        print('Os filmes mais votados:')
        for filme in filmes_mais_votados:
            print(filme)

menu()
print('_'*50)
print('Obrigado por utilizar nosso sistema!')