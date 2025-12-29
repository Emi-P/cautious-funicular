from deck import Deck

class Game1v1:
    def __init__(self, team1, team2, scorelimit: int):
        """
        Initialize the game with the 2 team instances.
        :param teams: List<Team>, list of team instances
        :param scorelimit: Int
        """
        self.team1 =  team1
        self.team1 =  team1
        
        self.deck = Deck()
        self.scorelimit = scorelimit
        self.turn = 1    # 1 para team 1 , 2 para team 2, corresponde a quien es mano
        self.playing = 1 # A quien esta por poner una carta en la ronda
        self.table = [  [],
                        []
                    ]
    
    def is_game_over(self):
        for team in self.teams:
            if team.score >= self.scorelimit:
                return True
        return False
    
    def play(self):
        while not self.is_game_over():
            # refrescar mazo
            # juegan la ronda
            while 
            # suman puntos
            # chequea si
            

            
            