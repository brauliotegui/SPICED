class Player:
    '''
    The class Player is a blueprint for a poker player.

    Parameter
    -------

    name: Name of the player
    stack_size: Amount of chips the player currently has
    '''

    buy_in = 1000
    limit = 100

    def __init__(self, name, maximum_bet):
        self.name = name
        self.__maximum_bet = maximum_bet
        self.stack_size = self.buy_in
        self.current_bet = 0

    def raise_bet(self):
        self.current_bet += self.__maximum_bet
        self.stack_size -= self.__maximum_bet
        return self.current_bet

    def get_stack_size(self):
        print(self.stack_size)

    def vocalize_max_bet(self):
        return f'The maximum I am allowed to bet is {self.__maximum_bet}'

    @classmethod
    def increase_limit(cls, increase):
        cls.limit = cls.limit + increase

    @staticmethod
    def conversion_to_dollar():
        return 'One chip is worth 3 dollars'

    def __repr__(self):
        return f'Player {self.name} is betting {self.current_bet} and his stack size is {self.stack_size}'
