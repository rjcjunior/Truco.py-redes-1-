# -*- coding: cp1252 -*-
import random

class Carta:

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
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
        return str(valor) + ' de ' + str(naipe)

class Deck:
    def __init__(self):
        self.cards = []
        self.start_deck()

    def start_deck(self):
        for i in range (1,5):
            for j in range(1,14):
                carta = Carta(j,i)
                self.cards.append(carta)
        random.shuffle(self.cards)
    
    def get_three_cards(self):
        retorno = []
        for i in range(0,3):
            retorno.append(self.cards[i])
            self.cards.remove(self.cards[i])
        return retorno

    def get_vira(self):
        retorno = self.cards[0]
        self.cards.remove(self.cards[0])
        return retorno

class Player:
    def __init__(self):
        self.hands = []
    def add_hand_for_player(self, hand):
        self.hands.append(hand)
    def add_card_to_hand(self, carta):
        i = 0
        while (True):
            if self.hands[i].rodada > 3:
                i+=1
            else:
                break
        self.hands[i].add_card(carta)
        
class Hand:
    
    def __init__(self):
        self.hand = []
        self.point = 1
        self.rodada = 1
        
    def add_card(self, carta):
        self.hand.append(carta)
    
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
