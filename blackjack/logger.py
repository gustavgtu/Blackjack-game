class GameLogger:
    def __init__(self, filename="BlackjackHistory.txt"):
        self.filename = filename
        with open(self.filename, 'w') as f:
            f.write("=== Blackjack History ===\n")

    def log(self, bet, result, player, dealer):
        with open(self.filename, 'a') as f:
            f.write(f"\nResult: {result}\n")
            f.write(f"Bet: {bet.get_bet_amount()} | ")
            if result == "You won!":
                f.write(f"Won: {bet.payout_win()}\n")
            elif result == "Draw!":
                f.write(f"Returned: {bet.get_bet_amount()}\n")
            else:
                f.write(f"Lost: {bet.get_bet_amount()}\n")
            f.write(f"Player hand: {player.hand.cards} (Total: {player.hand.get_total()})\n")
            f.write(f"Dealer hand: {dealer.hand.cards} (Total: {dealer.hand.get_total()})\n")