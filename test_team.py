import unittest
from player import Player
from team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Attacker1", "Attacker", 80)
        self.player2 = Player("Midfielder1", "Midfielder", 70)
        self.player3 = Player("Defender1", "Defender", 75)
        self.team = Team("Test Lions")
        self.team.add_player(self.player1)
        self.team.add_player(self.player2)
        self.team.add_player(self.player3)

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Test Lions")
        self.assertEqual(len(self.team.players), 3)

    def test_add_player(self):
        player4 = Player("Attacker2", "Attacker", 85)
        self.team.add_player(player4)
        self.assertEqual(len(self.team.players), 4)
        with self.assertRaises(TypeError):
            self.team.add_player("Not a Player")

    def test_set_tactic(self):
        self.team.set_tactic()
        self.assertIn(self.team.tactic, ['Attacking', 'Balanced', 'Defensive'])

    def test_calculate_tactical_strength_no_tactic(self):
        # Should default to balanced or apply no multipliers if tactic is None
        self.team.tactic = None # Explicitly set to None
        self.team.calculate_tactical_strength()
        self.assertEqual(self.team.attack_strength, 80) # 80 * 1.0
        self.assertEqual(self.team.midfield_strength, 70) # 70 * 1.0
        self.assertEqual(self.team.defense_strength, 75) # 75 * 1.0

    def test_calculate_tactical_strength_attacking(self):
        self.team.tactic = 'Attacking'
        self.team.calculate_tactical_strength()
        self.assertEqual(self.team.attack_strength, int(80 * 1.2)) # 96
        self.assertEqual(self.team.midfield_strength, int(70 * 1.0)) # 70
        self.assertEqual(self.team.defense_strength, int(75 * 0.8)) # 60

    def test_calculate_tactical_strength_balanced(self):
        self.team.tactic = 'Balanced'
        self.team.calculate_tactical_strength()
        self.assertEqual(self.team.attack_strength, int(80 * 1.0)) # 80
        self.assertEqual(self.team.midfield_strength, int(70 * 1.0)) # 70
        self.assertEqual(self.team.defense_strength, int(75 * 1.0)) # 75

    def test_calculate_tactical_strength_defensive(self):
        self.team.tactic = 'Defensive'
        self.team.calculate_tactical_strength()
        self.assertEqual(self.team.attack_strength, int(80 * 0.8)) # 64
        self.assertEqual(self.team.midfield_strength, int(70 * 1.0)) # 70
        self.assertEqual(self.team.defense_strength, int(75 * 1.2)) # 90
        
    def test_calculate_tactical_strength_no_players(self):
        empty_team = Team("Empty Eagles")
        empty_team.set_tactic() # Set some tactic
        empty_team.calculate_tactical_strength()
        self.assertEqual(empty_team.attack_strength, 0)
        self.assertEqual(empty_team.midfield_strength, 0)
        self.assertEqual(empty_team.defense_strength, 0)

if __name__ == '__main__':
    unittest.main()
