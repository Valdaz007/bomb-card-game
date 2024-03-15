import random

class Pile:
    #? CONSTRUCTOR
    def __init__(self) -> None:
        self._pile = []
    
    def get(self) -> list:
        return self._pile

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



class Bomb(Pile):
    def __init__(self) -> None:
        self._deck = Pile()
        self._board = Pile()

        self.setDeck()
    
    def setDeck(self) -> None:      #? Set Deck of Cards Elements to Deck
        self._deck
        self._deck.add([j+i for i in 'DSHC' for j in 'A23456789TJQK'])
    
    def draw(self, count:int=1) -> list:        #? Remove a number of Cards from the Deck
        return self._deck.rmv(count=count)
    
    def discard(self, cards:list) -> None:      #? Add Cards discarded from Hand to the Board
        self._board.add(cards)