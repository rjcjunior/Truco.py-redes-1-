# -*- coding: cp1252 -*-
import random

class Carta:

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
        self.power = self.card_power()

    def __str__(self): #função para impressão do objeto
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
        return str(valor) + ' de ' + str(naipe) + 'Poder dela é de ' + str(self.power)

    def card_power(self): #função para ter o valor que a carta vale
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
        
class Hand:
    
    def __init__(self):
        self.hand = [] #Lista de cartas na mão
        self.point = 1 #Pontos da mão
        self.rodada = 1 #Flag para contar o numero de rodadas
        
    def add_card(self, carta): #Função para adicionar a carta na mão
        self.hand.append(carta)


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
print(p.hands[0].hand[1]
)
