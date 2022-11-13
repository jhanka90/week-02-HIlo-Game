from game.hilo import Hilo


class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[card]): A list of card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(1):
            card = Hilo()
            self.cards.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.
        Args:
            self (Director): An instance of Director.
        """
        draw_card = input("Draw another card? [y/n] ")
        self.is_playing = (draw_card == "y")
       
    def do_updates(self):
        """Updates the player's score.
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        for i in range(len(self.cards)):
            card = self.cards[i]
            card.draw()

     def do_outputs(self):
        """Displays the cards and the score. Also asks the player if they want to roll again. 
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return