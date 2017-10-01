# -*- coding: cp1252 -*-
import random

class Carta:

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
        self.power = self.card_power()

    def __str__(self): #fun��o para impress�o do objeto
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
        return str(valor) + ' de ' + str(naipe) + 'Poder dela � de ' + str(self.power)

    def card_power(self): #fun��o para ter o valor que a carta vale
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
        
class Hand:
    
    def __init__(self):
        self.hand = [] #Lista de cartas na m�o
        self.point = 1 #Pontos da m�o
        self.rodada = 1 #Flag para contar o numero de rodadas
        
    def add_card(self, carta): #Fun��o para adicionar a carta na m�o
        self.hand.append(carta)

class partida:

    def vitory_verify(self, player):
        flag = False
        for i in player.hands: #percorrer as m�os dos jogadores
            cont = 0
            for j in i: #Percorrer uma m�o em especifica
                cont+= i.point
            if cont>=12:
                flag = True
                break
        return flag

class Rodada:
    def win(self, vira, cardp1, cardp2, cardp3, cardp4):
        manilha = self.get_manilha(vira)
        value = max(cardp1.power, cardp2.power, cardp3.power, cardp4.power)
        retorno = []
        if (cardp1.valor != manilha.valor) and (cardp2.valor != manilha.valor) and (cardp3.valor != manilha.valor) and (cardp4.valor != manilha.valor):
            if cardp1.power == value:
                retorno.append(cardp1)
            if cardp2.power == value:
                retorno.append(cardp2)
            if cardp3.power == value:
                retorno.append(cardp3)
            if cardp4.power == value:
                retorno.append(cardp4)
        #Fazer um else p qnd alguem jogar alguma manilha            
        return retorno
            
    def get_manilha(self, vira):        
        manilha = vira.valor+1
        if manilha > 13:
            manilha = manilha - 13
        manilha = Carta(manilha, 1)
        return manilha
    

#Area de testes    
j = Deck()
p = Player()
hand = Hand()
p.add_hand_for_player(hand)
for i in j.cards:
    print(i)
print('---')
for i in j.get_three_cards():
    p.add_card_to_hand(i)
print(p.hands[0])
print(p.hands[0].hand[1]) 
print('-------')
r = Rodada()
a = r.win(j.cards[0],j.cards[1],j.cards[2],j.cards[3],j.cards[4])
for i in a:
    print(i)
