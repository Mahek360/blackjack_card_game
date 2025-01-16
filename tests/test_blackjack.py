import unittest
import sys
sys.path.insert(0, './src')  # Add the 'src' directory to the Python path
from blackjack_main import *

"""
 Unit tests based on the scenarios in the technical test document provided.
"""

class TestBlackjackGame(unittest.TestCase):

    """Set up initial game state for testing."""
    def setUp(self):        
        global player_score, dealer_score, deck, blackjack_status
        player_score = []
        dealer_score = []
        deck = []
        blackjack_status = {"dealer": "no", "player": "no"}
        # Call shuffle method to set up a fresh deck
        shuffle()

    """Tests that the player and dealer are dealt two cards each."""
    def test_initial_hand(self):        
        self.assertEqual(len(player_score), 2, "Player should have 2 cards")
        self.assertEqual(len(dealer_score), 2, "Dealer should have 2 cards")

    """Tests that hitting adds a card to the player's hand and updates score."""
    def test_hit_functionality(self):
        initial_score = sum(player_score)
        player_hit()
        self.assertEqual(len(player_score), 3, "Player should have 3 cards after hitting")
        self.assertGreater(sum(player_score), initial_score, "Player's score should increase after hitting")

    """Tests that standing ends the game and the player's score is evaluated."""
    def test_stand_functionality(self):
        initial_score = sum(player_score)
        stand()
        self.assertEqual(len(player_score), 2, "Player should still have 2 cards after standing")
        self.assertEqual(sum(player_score), initial_score, "Player's score should remain the same after standing")

    """Tests that if the score is 21 or less, the hand is valid."""
    def test_valid_hand_when_21_or_less(self):
        player_score = [10, 5, 6]  # Example hand
        self.assertTrue(stand(), "Player should have a valid hand with 21 or less")

    """Tests that if the score is 22 or more, the player is bust."""
    def test_bust_when_22_or_more(self):
        player_score = [10, 10, 3]  # Example hand
        self.assertFalse(stand(), "Player should be bust with score over 21")

    """Tests that a King and Ace results in a score of 21."""
    def test_king_and_ace_is_21(self):
        player_score = [10, 11]  # King (10) + Ace (11)
        self.assertEqual(sum(player_score), 21, "King and Ace should give a score of 21")

    """Tests that a King, Queen, and Ace results in a score of 21."""
    def test_king_queen_ace_is_21(self):
        player_score = [10, 10, 11]  # King (10) + Queen (10) + Ace (11)
        self.assertEqual(sum(player_score), 21, "King, Queen, and Ace should give a score of 21")

    """Tests that a 9, Ace, and Ace results in a score of 21."""
    def test_nine_ace_ace_is_21(self):
        player_score = [9, 11, 11]  # 9 + Ace (11) + Ace (11)
        self.assertEqual(sum(player_score), 21, "9, Ace, and Ace should give a score of 21")

    """Tests that the deck has 52 cards and cards are not duplicated."""
    def test_deck_integrity(self):
        self.assertEqual(len(deck), 52, "Deck should have 52 cards at the start")

if __name__ == '__main__':
    unittest.main()
