import random

class Pile:
    #? CONSTRUCTOR
    def __init__(self) -> None:
        self._pile = []
    

    def get(self) -> list:
        return self._pile


    def add(self, cards:list) -> None:
        for card in cards:
            self._pile.append(card)


    def rmv(self, pos:str='top', count:int=1) -> list:
        if pos=='btm':
            return [self._pile.pop() for i in range(count)]
        else:
            return [self._pile.pop(0) for i in range(count)]
        

    def shuffle(self) -> None:
        random.shuffle(self._pile)