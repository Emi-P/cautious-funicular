from deck import Deck

class Game1v1:
    def __init__(self, teams, scorelimit: int):
        """
        Initialize the game with the 2 team instances.
        :param teams: List<Team>, list of team instances
        :param scorelimit: Int
        """
        self.teams = teams
        self.deck = Deck()
        self.scorelimit = scorelimit
        self.turn = 1 # 1 para team 1 , 2 para team 2
    
    def is_game_over(self):
        for team in self.teams:
            if team.score >= self.scorelimit:
                return True
        return False
    
    def play(self):
        while not self.is_game_over():
            self.deck.shuffle()
            self.turn = 1 if self.turn == 2 else 2

        print("El juego ha terminado.")
        for team in self.teams:
            print(f"Equipo {team.name} tiene {team.score} puntos.")