class Deck:
    def __init__(self, id):
            self.deck_id = id

    def get_DeckID(self) -> str:
        return self.deck_id

    def set_DeckID(self, id):
        self.deck_id = id

class Player:
    def __init__(self, uname:str):
        self.uname = uname
        self.pile = ''
    
    def set_Pile(self, pile:str):
        self.pile = pile