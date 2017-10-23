# -*- coding: cp1252 -*-
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

    def __str__(self): #Fun��o para impress�o do objeto
        valor = self.valor
        naipe = self.naipe
        if valor <=13  and valor>0:
            if valor == 1:
                valor = '�s'
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

    def set_visibilidade(self, visibilidade): #Fun��o para definir a visibilidade
        self.visibilidade = visibilidade
        if self.visibilidade == False:
            self.power = 0
        
    def card_power(self): #Fun��o para ter o valor que a carta vale
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

    def start_deck(self): #Inicia o deck e j� o embaralha
        for i in range (1,5):
            for j in range(1,14):
                carta = Carta(j,i)
                self.cards.append(carta)
        random.shuffle(self.cards)
    
    def get_three_cards(self): #Fun��o para retirar e retornar 3 cartas do baralho
        retorno = []
        for i in range(0,3):
            retorno.append(self.cards[i])
            self.cards.remove(self.cards[i])
        return retorno

    def get_vira(self): #Fun��o para tirar uma carta do baralho e retornar ela, usar para tirar a carta vira
        retorno = self.cards[0]
        self.cards.remove(self.cards[0])
        return retorno
    
class Player:
    def __init__(self):
        self.hands = [] #Jogador tem um array de m�os, pq cada 3 rodadas, precisaremos de uma nova m�o

    def add_hand_for_player(self, hand): #Fun��o para adicionar a m�o ao jogador
        self.hands.append(hand) 

    def add_card_to_hand(self, carta): #Fun��o para adicionar a carta na m�o atual do jogador
        i = 0
        while (True): #Se a m�o for menor ou igual a rodada 3, adiciona a carta. Caso n�o seja pula p proxima pq essa j� fechou a qnt maxima de rodadas
            if self.hands[i].rodada > 3:
                i+=1
            else:
                break
        self.hands[i].add_card(carta)
        
    def remove_card_to_hand(self, posicao): #Retornar e retirar uma carta da m�o de acordo com sua posi��o(1,12)
        i = 0
        posicao -=1
        while (True): #Se a m�o for menor ou igual a rodada 3, remove a carta. Caso n�o seja pula p proxima pq essa j� fechou a qnt maxima de rodadas
            if self.hands[i].rodada > 3:
                i+=1
            else:
                break
        return self.hands[i].hand.pop(posicao)

    def __str__(self): # Fun��o para imprimir m�o atual
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
        self.hand = [] #Lista de cartas na m�o
        self.point = 0 #Pontos da m�o
        self.rodada = 0 #Flag para contar o numero de rodadas
        
    def add_card(self, carta): #Fun��o para adicionar a carta na m�o
        self.hand.append(carta)
        
    def __str__(self): #Fun��o para impress�o do objeto
        string = ''
        for i in self.hand:
            string += str(i) + '\n'
        return string
    __repr__ = __str__


def vitory_verify(player):
    flag = False
    for i in player.hands: #Percorrer as m�os dos jogadores
        cont = 0
        for j in i: #Percorrer uma m�o em especifica
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
            
        
def get_manilha(vira):   #Fun��o para retornar a manilha     
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
    

#Fun��o para realizar a leitura correta das mensagens recebidas.
def ler_msg(bytesRecebidos,data):
    qtdArmazenada = bytesRecebidos #quantidade de bytes j� recebidos por aquela conex�o  
    qtdRecebida = len(data) # contar quantidades de bytes (atual msgs_antigas+msg_nova)

    data = data.decode() # passando mensagem em bytes para string
    
    msgEsperada = data[(qtdArmazenada-1):] #corta a string a partir da quantidade ja recebida at� o final
    return msgEsperada
                
    
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(4)


listaconexoes = []
flag = False #Flag para verificar se pode n�o pode come�ar
flag1 = False #Flag para iniciar a variavel de game
contRodada = 0 #contador para verificar n�mero de rodas

#msg = 'variavel pra troca de mensagens' #variavel para controlar troca de mensagens 

while 1:         
     print ('Aguardando conexao...')
     connectionSocket, addr = serverSocket.accept()
     print ('Nova conexao recebida!')
     listaconexoes.append(connectionSocket)


     ###VERIFICANDO SE H� 4 CONEX�ES PARA INICIAR O JOGO 
     if (len(listaconexoes) < 4):
         x = '0'
         mensagem= x.encode('utf-8')
         listaconexoes[(len(listaconexoes)-1)].send(mensagem)
     else:
         x = '1'
         mensagem = x.encode('utf-8')
         listaconexoes[(len(listaconexoes)-1)].send(mensagem)
         flag = True
         
     print ('Status da autoriza��o 1 para sim e 0 para n�o: ',mensagem) #informando status do servidor
    # print ('Respotas do cliente: ', listaconexoes[(len(listaconexoes))].recv(1024)) #se poss�vel tentar fazer o servidor ouvir o clientes (n�o est� funcionando ainda)
         
     if (flag):
        if (flag1 != True):
            game  = Game() #Iniciar o jogo
            flag1 = True
            print ('Todos os jogadores online. Servidor pronto para gerenciar o jogo')
        while True: #Um loop para repetir todo o jogo, evitando fazer a nova conex�o e criar um jogo novo
            if (contRodada%3 == 0): #controla cria��o de m�o a cada 3 rodadas
                for i in range (0,4):                
                    h = Hand()
                    game.jogadores[i].add_hand_for_player(h) #criando m�o para cada jogador          
            for jogador in game.jogadores:
                for carta in game.deck.get_three_cards():
                    jogador.add_card_to_hand(carta)
            for i in range(0,4):#Enviar m�o para o jogador            
               listaconexoes[i].send((game.jogadores[i].__str__()).encode('utf-8'))
            print('------------')
            time.sleep(1) #Delay para enviar o VIra  
            vira = game.deck.get_vira() #Definir o vira
            for i in range(0,4): #Receber confirma��o de envio para o vira
                listaconexoes[i].send((vira.__str__()).encode('utf-8'))
            escolhasRodada = [] #Uma variavel para armazenar as escolhas da rodada
            flag_escolha = False #Saber se ele escolheu truco ou n�o
            for i in range(0,4): #Coletar cartas
                escolha = listaconexoes[i].recv(1024)
                #Dps tem de fazer o envio da carta para os demais jogadores !!!!
                escolha = escolha.decode("utf-8") 
                if escolha != '2':
                    cartaescolhida = int(escolha[0]) #Pegar a posicao escolhida
                    cartaescolhida = game.jogadores[i].remove_card_to_hand(cartaescolhida)#Pegar a carta na posi��o escolhida
                    visibilidadeEscolhida = int(escolha[1])
                    if visibilidadeEscolhida == 1:
                        cartaescolhida.visibilidade = False
                        cartaescolhida.power = 0 #Falando q o poder dela � 0 
                    escolhasRodada.append(cartaescolhida)
                    
            if flag_escolha: #N�o escolheu truco          !!!Tem de fazer se escolher truco
                ganhador = win(vira, escolhasRodada[0], escolhasRodada[1], escolhasRodada[2],escolhasRodada[3])
                if ganhador == 1: #Dupla 1 ganhou
                    game.jogadores[0].hand.point += 1 # Os jogadores 1 e 3 v�o ganhar um pto na m�o, isso vai servir para controlar os ptos dos jogadores
                    game.jogadores[2].hand.point += 1                
                elif ganhador ==2: #Dupla 2 ganhou
                    game.jogadores[1].hand.point += 1 # Os jogadores 2 e 4 v�o ganhar um pto na m�o, isso vai servir para controlar os ptos dos jogadores
                    game.jogadores[3].hand.point += 1                                   
                else: #Empate
                    for i in range(0,4):
                        game.jogadores[i].hand.point += 1
                for i in range(0,4): # Incrementar o numero de rodadas na m�o
                    game.jogadores[i].hand.rodadas += 1
                contRodada += 1
                if vitory_verify(game.jogadores[0]) or vitory_verify(game.jogadores[2]):
                    #Enviar algo avisando que a dupla 1 ganhou o truco !!!!
                    for conexao in listaconexoes: #Fechar conexao
                        conex�o.shutdown()
                        conex�o.close()
                    break
                if vitory_verify(game.jogadores[1]) or vitory_verify(game.jogadores[3]):
                    #Enviar algo avisando que a dupla 2 ganhou o truco !!!!
                    for conexao in listaconexoes: #Fechar conexao
                        conex�o.shutdown()
                        conex�o.close()
                    break
                

                '''S� um lembrete para eu n�o esquecer:
                    tratar escolhas( N�o pode escolher opcoes n�o permitidas)
                    Enviar as cartas escolhidas para os jogadores
                    Enviar a dupla ganhadora para os jogadores
                '''
