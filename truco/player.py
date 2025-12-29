class Player:
    # Atributo de clase para tener id autoincremental
    _ID = 1
    
    def __init__(self, name: str, mano: list):
        self.id = Player.next_id; self.__class__._ID += 1
        self.name = name
        self.mano = mano