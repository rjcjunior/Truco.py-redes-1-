import random
from socket import *
from sys import *
import time


class Carta:

    def __init__(self, valor, naipe, visibilidade=True):
        self.valor = valor
        self.naipe = naipe
        self.power = self.card_power()
        self.set_visibilidade(visibilidade)

    def __str__(self): #Função para impressão do objeto
        valor = self.valor
        naipe = self.naipe
        if valor <=13  and valor>0:
            if valor == 1:
                valor = 'Ás'
            elif valor == 11:
                valor = 'Dama'
            elif valor == 12:
               valor = 'Valete'
            elif valor == 13:
                valor = 'Rei'
        else:
            return 'Valor invalido'
        if naipe > 0 and naipe <= 4:
            if naipe == 1:
                naipe = 'Ouros'
            if naipe == 2:
                naipe = 'Espadas'
            if naipe == 3:
                naipe = 'Copas'
            if naipe == 4:
                naipe = 'Paus'
        else:
            return 'Naipe invalido'
        return str(valor) + ' de ' + str(naipe) + ', O poder dela eh de ' + str(self.power)

    def set_visibilidade(self, visibilidade): #Função para definir a visibilidade
        self.visibilidade = visibilidade
        if self.visibilidade == False:
            self.power = 0
        
    def card_power(self): #Função para ter o valor que a carta vale
        if self.valor == 4:
            return 1
        elif self.valor == 5:
            return 2
        elif self.valor == 6:
            return 3
        elif self.valor == 7:
            return 4
        elif self.valor == 8:
            return 5
        elif self.valor == 9:
            return 6
        elif self.valor == 10:
            return 7
        elif self.valor == 11:
            return 8
        elif self.valor == 12:
            return 9
        elif self.valor == 13:
            return 10
        elif self.valor == 1:
            return 11
        elif self.valor == 2:
            return 12
        elif self.valor == 3:
            return 13
    __repr__ = __str__
        

class Deck:
    def __init__(self):
        self.cards = [] #Deck tem um array de cartas
        self.start_deck() 

    def start_deck(self): #Inicia o deck e já o embaralha
        for i in range (1,5):
            for j in range(1,14):
                carta = Carta(j,i)
                self.cards.append(carta)
        random.shuffle(self.cards)
    
    def get_three_cards(self): #Função para retirar e retornar 3 cartas do baralho
        retorno = []
        for i in range(0,3):
            retorno.append(self.cards[i])
            self.cards.remove(self.cards[i])
        return retorno

    def get_vira(self): #Função para tirar uma carta do baralho e retornar ela, usar para tirar a carta vira
        retorno = self.cards[0]
        self.cards.remove(self.cards[0])
        return retorno
    
class Player:
    def __init__(self):
        self.hands = [] #Jogador tem um array de mãos, pq cada 3 rodadas, precisaremos de uma nova mão

    def add_hand_for_player(self, hand): #Função para adicionar a mão ao jogador
        self.hands.append(hand) 

    def add_card_to_hand(self, carta): #Função para adicionar a carta na mão atual do jogador
        i = 0
        while (True): #Se a mão for menor ou igual a rodada 3, adiciona a carta. Caso não seja pula p proxima pq essa já fechou a qnt maxima de rodadas
            if self.hands[i].rodada > 3:
                i+=1
            else:
                break
        self.hands[i].add_card(carta)
        
    def remove_card_to_hand(self, posicao): #Retornar e retirar uma carta da mão de acordo com sua posição(1,12)
        i = 0
        posicao -=1
        while (True): #Se a mão for menor ou igual a rodada 3, remove a carta. Caso não seja pula p proxima pq essa já fechou a qnt maxima de rodadas
            if self.hands[i].rodada > 3:
                i+=1
            else:
                break
        return self.hands[i].hand.pop(posicao)

    def __str__(self): # Função para imprimir mão atual
        i = 0
        while (True):
            if self.hands[i].rodada > 3:
                i+=1
            else:
                break
        string = (self.hands[i].hand.__str__())
        return string
    __repr__ = __str__
        
class Hand:
    
    def __init__(self):
        self.hand = [] #Lista de cartas na mão
        self.point = 0 #Pontos da mão
        self.rodada = 0 #Flag para contar o numero de rodadas
        
    def add_card(self, carta): #Função para adicionar a carta na mão
        self.hand.append(carta)
        
    def __str__(self): #Função para impressão do objeto
        string = ''
        for i in self.hand:
            string += str(i) + '\n'
        return string
    __repr__ = __str__


def vitory_verify(player):
    flag = False
    for i in player.hands: #Percorrer as mãos dos jogadores
        cont = 0
        for j in i: #Percorrer uma mão em especifica
            cont+= i.point
        if cont>=12:
            flag = True
            break
    return flag

def win(vira, cardp1, cardp2, cardp3, cardp4):
    manilha = get_manilha(vira)
    cartas = [cardp1.power, cardp2.power, cardp3.power, cardp4.power]
    value = max(cartas)
    if not(manilha.power in cartas):

        if cartas.count(value) == 1:
            if cardp1.power == value:
                return 1 #Dupla 1 ganhou 
            elif cardp2.power == value:
                return 2 #Dupla 2 ganhou
            elif cardp3.power == value:
                return 1 #Dupla 1 ganhou
            else:
                return 2 #Dupla 2 ganhou
        elif cartas.count(value) > 2:
            return 0 #Empate
        else:
            if (cardp1.power == cardp2.power == value) or \
               (cardp1.power == cardp4.power == value) or \
               (cardp2.power == cardp3.power == value) or \
               (cardp3.power == cardp4.power == value):
                    return 0 #Empate    
            elif cardp1.power == cardp3.power == value:
                return 1 #Dupla 1 ganhou
            else:
                return 2 #Dupla 2 ganhou
    else:
        if cartas.count(manilha.power) == 1:
            if cardp1.power == manilha.power:
                return 1 #Dupla 1 ganhou 
            elif cardp2.power == manilha.power:
                return 2 #Dupla 2 ganhou
            elif cardp3.power == manilha.power:
                return 1 #Dupla 1 ganhou
            else:
                return 2 #Dupla 2 ganhou
        else:
            if (cardp1.power == cardp2.power == manilha.power):
                if cardp1.naipe > cardp2.naipe:
                    return 1 #Dupla 1 ganhou
                else:
                    return 2 #Dupla 2 ganhou
            if (cardp1.power == cardp4.power == manilha.power):
                if cardp1.naipe > cardp4.naipe:
                    return 1 #Dupla 1 ganhou
                else:
                    return 2 #Dupla 2 ganhou
            if (cardp2.power == cardp3.power == manilha.power):
                if cardp2.naipe > cardp3.naipe:
                    return 1 #Dupla 1 ganhou
                else:
                    return 2 #Dupla 2 ganhou
            if (cardp3.power == cardp4.power == manilha.power):
                if cardp3.naipe > cardp4.naipe:
                    return 1 #Dupla 1 ganhou
                else:
                    return 2 #Dupla 2 ganhou
            elif cardp1.power == cardp3.power == manilha.power:
                return 1 #Dupla 1 ganhou
            else:
                return 2 #Dupla 2 ganhou
            
        
def get_manilha(vira):   #Função para retornar a manilha     
    manilha = vira.valor+1
    if manilha > 13:
        manilha = manilha - 13
    manilha = Carta(manilha, 1)
    return manilha
    


class Game: #Classe para iniciar o jogo

    def __init__(self):
        self.deck = Deck()
        self.jogadores = []
        for i in range(0,4):
            aux = Player()
            self.jogadores.append(aux)
    

#Função para realizar a leitura correta das mensagens recebidas.
def ler_msg(bytesRecebidos,data):
    qtdArmazenada = bytesRecebidos #quantidade de bytes já recebidos por aquela conexão  
    qtdRecebida = len(data) # contar quantidades de bytes (atual msgs_antigas+msg_nova)

    data = data.decode() # passando mensagem em bytes para string
    
    msgEsperada = data[(qtdArmazenada-1):] #corta a string a partir da quantidade ja recebida até o final
    return msgEsperada
                
    
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(4)


listaconexoes = []
flag = False #Flag para verificar se pode não pode começar
flag1 = False #Flag para iniciar a variavel de game
contRodada = 0 #contador para verificar número de rodas

#msg = 'variavel pra troca de mensagens' #variavel para controlar troca de mensagens 

while 1:         
     print ('Aguardando conexao...')
     connectionSocket, addr = serverSocket.accept()
     print ('Nova conexao recebida!')
     listaconexoes.append(connectionSocket)


     ###VERIFICANDO SE HÁ 4 CONEXÕES PARA INICIAR O JOGO 
     if (len(listaconexoes) < 4):
         x = '0'
         mensagem= x.encode('utf-8')
         listaconexoes[(len(listaconexoes)-1)].send(mensagem)
     else:
         x = '1'
         mensagem = x.encode('utf-8')
         listaconexoes[(len(listaconexoes)-1)].send(mensagem)
         flag = True
         
     print ('Status da autorização 1 para sim e 0 para não: ',mensagem) #informando status do servidor
    # print ('Respotas do cliente: ', listaconexoes[(len(listaconexoes))].recv(1024)) #se possível tentar fazer o servidor ouvir o clientes (não está funcionando ainda)
         
     if (flag):
        if (flag1 != True):
            game  = Game() #Iniciar o jogo
            flag1 = True
            print ('Todos os jogadores online. Servidor pronto para gerenciar o jogo')
        while True: #Um loop para repetir todo o jogo, evitando fazer a nova conexão e criar um jogo novo
            if (contRodada%3 == 0): #controla criação de mão a cada 3 rodadas
                for i in range (0,4):                
                    h = Hand()
                    game.jogadores[i].add_hand_for_player(h) #criando mão para cada jogador          
            for jogador in game.jogadores:
                for carta in game.deck.get_three_cards():
                    jogador.add_card_to_hand(carta)
            for i in range(0,4):#Enviar mão para o jogador            
               listaconexoes[i].send((game.jogadores[i].__str__()).encode('utf-8'))
            print('------------')
            time.sleep(1) #Delay para enviar o VIra  
            vira = game.deck.get_vira() #Definir o vira
            for i in range(0,4): #Receber confirmação de envio para o vira
                listaconexoes[i].send((vira.__str__()).encode('utf-8'))
            escolhasRodada = [] #Uma variavel para armazenar as escolhas da rodada
            flag_escolha = False #Saber se ele escolheu truco ou não
            position_player = 0 #Pegar a posicao do jogador, vai servir para descobrir quem pediu o vira
            for i in range(0,4): #Coletar cartas
                escolha = listaconexoes[i].recv(1024)
                escolha = escolha.decode("utf-8")
                if escolha != '2':
                    cartaescolhida = int(escolha[0]) #Pegar a posicao escolhida
                    cartaescolhida = game.jogadores[i].remove_card_to_hand(cartaescolhida)#Pegar a carta na posição escolhida
                    for j in range(0,4): #Envio de cartas para todos os outros jogadores AINDA NÃO TESTEI ISSO!!!!!!!
                        if (i != j): #Enviar para todos menos para o jogador atual
                            msg_envio = "O Jogador " + str(i) + " jogou a carta " + cartaescolhida.__str__() 
                            listaconexoes[i].send((msg_envio).encode('utf-8'))
                    visibilidadeEscolhida = int(escolha[1])
                    if visibilidadeEscolhida == 1:
                        cartaescolhida.visibilidade = False
                        cartaescolhida.power = 0 #Falando q o poder dela é 0 
                    escolhasRodada.append(cartaescolhida)
                else:
                    flag_escolha = True
                    break #Sai do for
                position_player +=1
                    
            if flag_escolha: #Não escolheu truco          !!!Tem de fazer se escolher truco
                ganhador = win(vira, escolhasRodada[0], escolhasRodada[1], escolhasRodada[2],escolhasRodada[3])
                if ganhador == 1: #Dupla 1 ganhou
                    game.jogadores[0].hand.point += 1 # Os jogadores 1 e 3 vão ganhar um pto na mão, isso vai servir para controlar os ptos dos jogadores
                    game.jogadores[2].hand.point += 1
                    for i in range(0,4):
                          listaconexoes[i].send("A dupla 1 ganhou essa rodada".encode('utf-8'))
                elif ganhador ==2: #Dupla 2 ganhou
                    game.jogadores[1].hand.point += 1 # Os jogadores 2 e 4 vão ganhar um pto na mão, isso vai servir para controlar os ptos dos jogadores
                    game.jogadores[3].hand.point += 1                                   
                    for i in range(0,4):
                          listaconexoes[i].send("A dupla 2 ganhou essa rodada".encode('utf-8'))
                else: #Empate
                    for i in range(0,4):
                        game.jogadores[i].hand.point += 1 
                    for i in range(0,4):
                          listaconexoes[i].send("Rolou um empate".encode('utf-8'))
                for i in range(0,4): # Incrementar o numero de rodadas na mão
                    game.jogadores[i].hand.rodadas += 1
                contRodada += 1
                if vitory_verify(game.jogadores[0]) or vitory_verify(game.jogadores[2]):

                    for conexao in listaconexoes: #Fechar conexao
                        conexao.send("A dupla 1 ganhou o truco".encode('utf-8'))
                        conexao.shutdown()
                        conexao.close()
                    break
                if vitory_verify(game.jogadores[1]) or vitory_verify(game.jogadores[3]):
                    for conexao in listaconexoes: #Fechar conexao
                        conexao.send("A dupla 2 ganhou o truco".encode('utf-8'))
                        conexao.shutdown()
                        conexao.close()
                    break
'''            else: #Se escolher o truco
                # Enviar Chamada de truco para os jogadores
                for i in range (0,4):
                    if  (i!= position_player) and (i != position_player + 2 or i != position_player - 2):
                        listaconexoes[i].send("truco".encode('utf-8')) #Enviar mensagem avisando que alguem solicitou truco
                    if (i == position_player + 2 or i == position_player - 2):
                        listaconexoes[i].send("truco1".encode('utf-8')) #Enviar mensagem avisando que o parceiro pediu truco
                aceitou = False
                fugiu = False
                retruco = False
                for i in range(0,4)
                    if  (i!= position_player) and (i != position_player + 2 or i != position_player - 2): 
                        resposta_truco = listaconexoes[i].recv(1024)
                    if resposta_truco = "aceitar":
                        break #Pegou a primeira resposta e saiu do loop
                        #A especificação não diz o q acontece qnd um cara da dupla aceita o truco e o outro tenta fugir, então estou considenrando que a primeira resposta é a q vale
                    elif resposta_truco = "fugir":
                        break #Pegou a primeira resposta e saiu do loop
                    elif resposta_truco = "proximo_decide": #Como estou considerando a primeira resposta como a valida, inseri algo para caso o primeiro não queira decidir, deixando a resposta para o proximo
                        if i==3:
                            resposta_truco ==" fugir" # Se o cara, mesmo sendo o ultimo  a escolher, não quiser tomar a decisão. Então consideramos q a dupla fugiu do truco
                    else: #Retrucou
                        break # retrucou

                # caso aceite, 3x os pontos da mão
                # caso fuja, distribuir pontos para a dupla que pediu o truco
                # Tratar retruco, se pedir
                
'''
