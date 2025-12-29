from enum import Enum 

class Palo(Enum):
    ESPADA = 1
    ORO = 2
    COPA = 3
    BASTO = 4


"""
Valor de una carta en el sentido de 4 de copa < 5 de copa < 7 de oro < 1 de espada.
    Correponden a la siguiente lista:
    valor   -> Cartas asociadas al valor
    1       -> 4 de basto,copa,espada,oro 
    2       -> 5 de basto,copa,espada,oro
    3       -> 6 de basto,copa,espada,oro
    4       -> 7 de basto,copa
    5      -> 10 de basto,copa,espada,oro
    6      -> 11 de basto,copa,espada,oro
    7      -> 12 de basto,copa,espada,oro
    8     -> 1 de copa,oro
    9     -> 2 de basto,copa,espada,oro
    10     -> 3 de basto,copa,espada,oro
    11    -> 7 de oro
    12    -> 7 de espada
    13    -> 1 de basto
    14    -> 1 de espada
    establecido en este dict indexado por numero y palo como par
"""

values = {
    # 4
    (4, Palo.BASTO): 1,
    (4, Palo.COPA): 1,
    (4, Palo.ESPADA): 1,
    (4, Palo.ORO): 1,

    # 5
    (5, Palo.BASTO): 2,
    (5, Palo.COPA): 2,
    (5, Palo.ESPADA): 2,
    (5, Palo.ORO): 2,

    # 6
    (6, Palo.BASTO): 3,
    (6, Palo.COPA): 3,
    (6, Palo.ESPADA): 3,
    (6, Palo.ORO): 3,

    # 7 falso
    (7, Palo.BASTO): 4,
    (7, Palo.COPA): 4,

    # 10
    (10, Palo.BASTO): 5,
    (10, Palo.COPA): 5,
    (10, Palo.ESPADA): 5,
    (10, Palo.ORO): 5,

    # 11
    (11, Palo.BASTO): 6,
    (11, Palo.COPA): 6,
    (11, Palo.ESPADA): 6,
    (11, Palo.ORO): 6,

    # 12
    (12, Palo.BASTO): 7,
    (12, Palo.COPA): 7,
    (12, Palo.ESPADA): 7,
    (12, Palo.ORO): 7,

    # 1 falso
    (1, Palo.COPA): 8,
    (1, Palo.ORO): 8,

    # 2
    (2, Palo.BASTO): 9,
    (2, Palo.COPA): 9,
    (2, Palo.ESPADA): 9,
    (2, Palo.ORO): 9,

    # 3
    (3, Palo.BASTO): 10,
    (3, Palo.COPA): 10,
    (3, Palo.ESPADA): 10,
    (3, Palo.ORO): 10,

    # especiales
    (7, Palo.ORO): 11,
    (7, Palo.ESPADA): 12,
    (1, Palo.BASTO): 13,
    (1, Palo.ESPADA): 14,
}

    
class Card:
    def __init__(self, number: int, palo: Palo ):
        self.palo = palo
        self.number = number
    def __repr__(self):
        return f"{self.number} de {self.palo}"
        
    @property
    def value(self):
        return values[(self.number,self.palo)]

    def __lt__(self, other:"Card"):
        return self.value < other.value
    def __eq__(self, other:"Card"):
        return self.value == other.value
