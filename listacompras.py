tentativa = 0
while True:
    usuario = input("Digite seu usário: ")
    senha = input("Digite sua senha: ")
    
    listaInicial = []
    historicoLista = []
    
    
    if usuario == 'João' and senha == '1607joao':
        
        print(f"Olá, {usuario}! Seja bem vindo.")
        while True:
            print('Escolha a opção que deseja: ')
            print("""
                  [01] Criar lista 
                  [02] Adicionar item
                  [03] Remover item
                  [04] Verificar Histórico 
                  [05] Ver lista 
                  [06] Sair
                  """)
            escolha = int(input('Digite sua escolha '))
            
            match escolha:
            
                case 1:
                    nomeLista = input("Dê um nome para sua lista de hoje: ")
                   
                case 2:
                    nomeProduto = input('informe o nome do produto ')
                    listaInicial.append(nomeProduto)
                    historicoLista.append(f' + {nomeProduto} ')
                    
                    
                    
                case 3:
                    produtoRet = input('Digite o nome do produto que você deseja retirar ')
                    if produtoRet in listaInicial:
                        listaInicial.remove(produtoRet)
                        historicoLista.append( f'- {produtoRet}')
                
                    else:
                        print('Produto não identificado ')
                        
                case 4:
                    print('Seu histórico de alterações: ')
                    print(historicoLista)
                
                case 5:
                    print(f"Lista '{nomeLista}'")
                    print(listaInicial)
                    
                case 6:
                    print("Saindo... Obrigado pela preferência.")
                    break
                
                case _:
                    print('Valor não encontrado ')
            break 
    else:
        print('Senha ou usuário incorreto. Tente novamente')
        tentativa += 1
        if tentativa == 3:
            print('Você atingiu o limite de tentativas. Tente novamente amanha!')
            break