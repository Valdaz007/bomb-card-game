import random

class Pile:
    #? CONSTRUCTOR
    def __init__(self) -> None:
        self._pile = []
    
    def get(self) -> list:
        return self._pile
    
    def init(self, pile:list=[]) -> None:
        self._pile = pile

    def add(self, cards:list) -> None:      #? Add Element(s) to End of 
        for card in cards:
            self._pile.append(card)

    def rmv(self, pos:str='top', count:int=1) -> list:      #? Remove Element(s) from Pile either from the 'top' or 'bottom'
        if pos=='btm':
            return [self._pile.pop() for i in range(count)]     # Remove Element(s) at the End of the List
        else:
            return [self._pile.pop(0) for i in range(count)]    # Remove Element(s) at the Start of the List

    def shuffle(self) -> None:          #? Randomize Elements in Pile Order
        random.shuffle(self._pile)



class Bomb():
    def __init__(self) -> None:
        self._deck = Pile()
        self._board = Pile()

        self.setDeck()
    
    def getDeck(self) -> list:
        return self._deck
    
    def getBoard(self) -> list:
        return self._board

    def setDeck(self) -> None:      #? Set Deck of Cards Elements to Deck
        self._deck.init([j+i for i in 'DSHC' for j in 'A23456789TJQK'])

    def draw(self, count:int=1) -> list:        #? Remove a number of Cards from the Deck
        return self._deck.rmv(count=count)
    
    def discard(self, cards:list) -> None:      #? Add Cards discarded from Hand to the Board
        self._board.add(cards)

    def repileDeck(self) -> None:
        if len(self._deck) == 1:
            self._deck.add(self._board)
            self._board.init()


class Player:
    def __init__(self) -> None:
        self._hand = Pile()
    
    def getHand(self) -> list:
        return self._hand
    
    def setHand(self, hand:list) -> None:
        self._hand.init(hand)

    def pick(self, cards:list) -> None:
        self._hand.add(cards)
    
    def play(self, cardIndex:list) -> list:
        pass #Todo

