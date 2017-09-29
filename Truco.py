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

class Player:
    def __init__(self):
        self.hand = []
    def add_card_to_hand(self, carta):
        self.hand.append(carta)
        
j = Deck()
p = Player()
for i in j.cards:
    print(i)
print('---')
for i in j.get_three_cards():
    p.add_card_to_hand(i)
print(p.hand)
