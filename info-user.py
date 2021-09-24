import robloxpy as rblx
import time

requisitar = True
message_welcome = '''
 
                  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
                  █---╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗--█
                  █---║║║╠─║─║─║║║║║╠─--█
                  █---╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝--█
                  █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█


            !Welcome To Script Info-User: Roblox!
                    Created by: Aoki-x
               Siga: UCHIHALAW777 no Roblox!
    Obs.: Esse Script mostra apenas informações básicas.\n'''

while requisitar:
    print(message_welcome)

    print('1- Informações sobre um Usuario.\n2- Informações sobre um jogo(Não pega mais).')
    choice = int(input('Opção->: '))

    if choice == 1:
        try:
            name = input('Digite o nome do Usuario->: ')
            userId = rblx.User.External.GetID(name) # Pega o ID atraves do nome e passa para a variavel "userId"
            creationDate = rblx.User.External.CreationDate(userId) # Mostra a data de criação do perfil
            exUsername = rblx.User.External.UsernameHistory(userId) # Retorna o historico de nomes anteriores em uma lista
            isOnline = rblx.User.External.IsOnline(userId) # Verifica se está online
            rapRobux = rblx.User.External.GetRAP(userId) # Retorna a riqueza em itens limitados
            userDescription = rblx.User.External.GetDescription(userId) # Retorna a descrição do perfil

            print(f'USUARIO: {name}\nID: {userId}\nDATA DE CRIAÇÃO: {creationDate}\nNOMES ANTERIORES: {exUsername}\nONLINE: {isOnline}\nRAP(Riqueza em itens limitados): {rapRobux}\nDESCRIÇÃO: {userDescription}')
        except:
            print('Ocorreu um erro inesperado, tente digitar o nome certo.\nEm 3 segundos você ira retornar ao menu!')
            time.sleep(3)
            continue
        runAgain = str(input('\nEssas são as informações.\ninfelizmente não posso fazer mais opções. Eu teria que ter seu cookie(dados), e isso seria falta de privacidade.\nQuer retornar?:'))
        if runAgain == 'sim' or runAgain == 'Sim' or runAgain == 'S':
            continue
        elif runAgain == 'Não' or runAgain == 'não' or runAgain == 'N':
            print('Te vejo na proxima! Fique atento ao mu perfil no GitHub!')
            break
        else:
            print('Não entendemos oque você falou, então iremos tirar você a força.\nAté a proxima!\nAss: Aoki-x')
            break
    if choice == 2:
        try:
            gameId = int(input('Digite o ID do jogo->: '))
            playersOn = rblx.Game.External.GetCurrentUniversePlayers(gameId)
            gameLikes = rblx.Game.External.GetUniverseLikes(gameId)
            gameDeslikes = rblx.Game.External.GetUniverseDislikes(gameId)
            favourites = rblx.Game.External.GetUniverseFavourites(gameId)
            gameVisits = rblx.Game.External.GetUniverseVisits(gameId)
            print(f'PLAYERS ON NESSE EXATO MOMENTO: {playersOn}\nLIKES: {gameLikes}\nDESLIKES: {gameDeslikes}\nFAVORITADO: {favourites} VEZES\nVISITAS: {gameVisits}')
        except:
            print('Ocorreu um erro inesperado, tente colocar o ID certo.\nEm 3 segundos você ira retornar ao menu!')
            time.sleep(3)
            continue