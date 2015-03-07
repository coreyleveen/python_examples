import random

class Deck(object):

    SUITS = ["C", "D", "H", "S"]
    RANKS = ["1", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "11", "12", "13"]

    def __init__(self):
        self.cards = []
        self._generate_card()
        self._shuffle_cards()

    def _generate_card(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = suit + rank
                self.cards.append(card)

    def _shuffle_cards(self):
        random.shuffle(self.cards)

    def draw_one_card(self):
        if self.cards:
            return self.cards.pop(0)

        return None

class Game(object):

    def __init__(self):
        self.deck = Deck()
        self.rounds_played = 0
        self.dealer_won = 0
        self.player_won = 0
        self.rounds_tied = 0

    def play_round(self):
        dealer_card = self.deck.draw_one_card()
        player_card = self.deck.draw_one_card()

        print("(dealer card: {}, player card: {})"\
            .format(dealer_card, player_card))

    def _resolve_result(self, dealer_card, player_card):
        result = "tie"
        if int(dealer_card[1:]) > int(player_card[1:]):
            result = "dealer"
        if int(player_card[1:]) > int(dealer_card[1:]):
            result = "player"
        return result

    def _log_results(self, result):
        self.rounds_played += 1
        if result == "player":
            self.player_won += 1
        elif result == "dealer":
            self.dealer_won += 1
        else:
            self.rounds_tied += 1

    def run(self):
        while True:
            if self.deck.cards:
                self.rounds_played += 1
                result = self.play_round()
                self._log_results(result)
            else:
                break
