import random
class Card:
    def __init__(self, rank, suit, faceUp = True):
        self.rank = rank
        self.suit = suit
        self.faceUp = faceUp

    def print_card(self):
        symbols = {"hearts" : "♥", "diamonds" : "♦", "spades" :"♠", "clubs" : "♣"}
        if self.faceUp:
            return f'{self.rank} {symbols[self.suit]}'
        else:
            return "??"

    def flip(self):
        self.faceUp = not self.faceUp

class Deck:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.cards = []

        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["hearts", "diamonds", "spades", "clubs"]
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def topCard(self):
        return self.cards.pop()
    
    def deal(self, p):
        card = self.topCard()
        p.hand.add_card(card)

class Hand: 
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def show_card(self):
        for card in self.cards:
            print(card.print_card())

    def compareTo(self, other):
        return self.value - other.value
    
    def get_hand_string(self):
        return " ".join([card.print_card() for card in self.cards])
    
class Player:
    def __init__(self, name, chips, isinPlay = True):
        self.name = name
        self.chips = chips
        self.bets = 0
        self.hand = Hand()
        self.isinPlay = isinPlay

    def bet(self, amount):
        actual_amount = min(amount, self.chips)
        self.chips -= actual_amount
        self.bets += actual_amount
        return actual_amount

    def fold(self):
        self.isinPlay = False
        print(f"{self.name} folds.")

    def check(self):
        print (f"{self.name} checks")

    def call(self , amount):
        self.chips -= amount
        self.bets += amount

    def raise_bet(self, amount): 
        self.bet(amount)

    def clear(self):
        self.hand = Hand()
        self.isinPlay = True
        self.bets = 0

class HumanPlayer(Player):
    def act(self, current_highest_bet):
        amount_to_call = current_highest_bet - self.bets
        print(f"\n{self.name}'s turn. Chips: {self.chips} | To Call: {amount_to_call}")
        print(f"Your hand: {self.hand.get_hand_string()}")
        
        while True:
            action = input("Choose action (fold, check, call, raise): ").lower().strip()
            
            if action == 'fold':
                self.fold()
                return 0
            elif action == 'check':
                if amount_to_call > 0:
                    print("You cannot check, you must call the bet or fold.")
                else:
                    print(f"{self.name} checks.")
                    return 0
            elif action == 'call':
                if amount_to_call == 0:
                    print("Nothing to call, checking instead.")
                    return 0
                print(f"{self.name} calls {amount_to_call}.")
                return self.bet(amount_to_call)
            elif action == 'raise':
                try:
                    raise_amt = int(input("How much to raise? "))
                    total_bet = amount_to_call + raise_amt
                    print(f"{self.name} raises by {raise_amt}.")
                    return self.bet(total_bet)
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Invalid input.")

class ComputerPlayer(Player):
    def act(self, current_highest_bet):
        amount_to_call = current_highest_bet - self.bets
        print(f"\n{self.name}'s turn. Chips: {self.chips}")
        
        if amount_to_call > 0:
            if amount_to_call > self.chips * 0.5: 
                self.fold()
                return 0
            else:
                print(f"{self.name} calls {amount_to_call}.")
                return self.bet(amount_to_call)
        else:
            print(f"{self.name} checks.")
            return 0
            
class PokerGame: 
    def __init__(self, players):
        self.players = players
        self.currentPlayer = 0
        self.deck = Deck()
        self.round = 1
        self.community_cards = []

    def get_active_players(self):
        return [p for p in self.players if p.isinPlay]
    
    def print_board(self):
        print("\n" + "="*30)
        print(f"POT: {self.pot}")
        if self.community_cards:
            board = " ".join([c.print_card() for c in self.community_cards])
            print(f"BOARD: {board}")
        print("="*30)

    def betting_round(self):
        current_highest_bet = 0
        players_acted = 0
        active_players = self.get_active_players()
        
        while players_acted < len(active_players):            
            for player in active_players:
                if not player.isinPlay:
                    continue
                    
                added_to_pot = player.act(current_highest_bet)
                self.pot += added_to_pot
                
                if player.bets > current_highest_bet:
                    current_highest_bet = player.bets
                    players_acted = 1 
                else:
                    players_acted += 1

                if len(self.get_active_players()) == 1:
                    return 

    def deal_community_cards(self, count):
        for _ in range(count):
            self.community_cards.append(self.deck.topCard())

    def playRound(self):
        print(f"\n\n{'*'*10} STARTING ROUND {self.round} {'*'*10}")
        self.deck.reset() 
        self.deck.shuffle()
        self.pot = 0
        self.community_cards = []
        
        for player in self.players:
            if player.isinPlay:
                self.deck.deal(player)
                self.deck.deal(player)
                
        print("\n PRE-FLOP ")
        self.print_board()
        self.betting_round()
        
        if len(self.get_active_players()) > 1:
            print("\nTHE FLOP ")
            self.deal_community_cards(3)
            self.print_board()
            self.betting_round()

        if len(self.get_active_players()) > 1:
            print("\n THE TURN ")
            self.deal_community_cards(1)
            self.print_board()
            self.betting_round()

        if len(self.get_active_players()) > 1:
            print("\nTHE RIVER ")
            self.deal_community_cards(1)
            self.print_board()
            self.betting_round()

        print("\nSHOWDOWN ")
        active = self.get_active_players()

        if len(active) == 0:
            print("No players remaining.")
            return

        elif len(active) == 1:
            winner = active[0]
            print(f"{winner.name} wins {self.pot} chips! (Everyone else folded)")

        else:
            self.print_board()
            for p in active:
                print(f"{p.name} shows: {p.hand.get_hand_string()}")
            winner = active[0]
            print(f"{winner.name} wins {self.pot} chips!")
            
        winner.chips += self.pot
        
        for player in self.players:
            player.clear()
            
        self.round += 1

pl1 = HumanPlayer('You', 1000)
pl2 = ComputerPlayer('Bot Bob', 1000)
pl3 = ComputerPlayer('Bot Alice', 1000)

game = PokerGame([pl1, pl2, pl3])

game.playRound()
