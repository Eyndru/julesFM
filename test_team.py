import unittest
from team import Team
from player import Player

class TestTeam(unittest.TestCase):
    def setUp(self):
        self.p1 = Player("Attacker1", "Attacker", 80)
        self.p2 = Player("Midfielder1", "Midfielder", 75)
        self.p3 = Player("Defender1", "Defender", 70)
        self.p4 = Player("Attacker2", "Attacker", 85)
        self.p5 = Player("Midfielder2", "Midfielder", 72)
        self.sample_players = [self.p1, self.p2, self.p3, self.p4, self.p5]

    def test_team_creation_and_str(self):
        team = Team("Dragons", self.sample_players, "Balanced")
        self.assertEqual(team.name, "Dragons")
        self.assertEqual(team.players, self.sample_players)
        self.assertEqual(team.tactic, "Balanced")
        self.assertEqual(str(team), "Dragons")

        team2 = Team("Eagles", self.sample_players)
        self.assertEqual(team2.tactic, "")

    def test_set_tactic(self):
        team = Team("Lions", self.sample_players)
        team.set_tactic("Attacking")
        self.assertEqual(team.tactic, "Attacking")
        team.set_tactic("Defensive")
        self.assertEqual(team.tactic, "Defensive")
        team.set_tactic("Balanced")
        self.assertEqual(team.tactic, "Balanced")
        with self.assertRaises(ValueError):
            team.set_tactic("InvalidTactic")

    def test_calculate_tactical_strength_balanced(self):
        team = Team("Sharks", self.sample_players) # Tactic is "", should be like Balanced
        att, mid, defe = team.calculate_tactical_strength()
        # Expected: attack = 80+85=165, midfield = 75+72=147, defense = 70
        self.assertAlmostEqual(att, 165.0)
        self.assertAlmostEqual(mid, 147.0)
        self.assertAlmostEqual(defe, 70.0)

        team.set_tactic("Balanced")
        att, mid, defe = team.calculate_tactical_strength()
        self.assertAlmostEqual(att, 165.0)
        self.assertAlmostEqual(mid, 147.0)
        self.assertAlmostEqual(defe, 70.0)

    def test_calculate_tactical_strength_attacking(self):
        team = Team("Wolves", self.sample_players)
        team.set_tactic("Attacking")
        # Base strengths: attack_base = 165, midfield_base = 147, defense_base = 70
        # Expected: attack = 165 * 1.10 = 181.5, midfield = 147, defense = 70 * 0.95 = 66.5
        att, mid, defe = team.calculate_tactical_strength()
        self.assertAlmostEqual(att, 181.5)
        self.assertAlmostEqual(mid, 147.0)
        self.assertAlmostEqual(defe, 66.5)

    def test_calculate_tactical_strength_defensive(self):
        team = Team("Bears", self.sample_players)
        team.set_tactic("Defensive")
        # Base strengths: attack_base = 165, midfield_base = 147, defense_base = 70
        # Expected: attack = 165 * 0.95 = 156.75, midfield = 147, defense = 70 * 1.10 = 77
        att, mid, defe = team.calculate_tactical_strength()
        self.assertAlmostEqual(att, 156.75)
        self.assertAlmostEqual(mid, 147.0)
        self.assertAlmostEqual(defe, 77.0)

    def test_calculate_tactical_strength_non_negative(self):
        # Test with a player having skill 1 (lowest possible)
        p_low_def = Player("DefenderLow", "Defender", 1)
        # Create a team mostly with this low skill defender for that role
        players_low_def = [
            Player("Attacker", "Attacker", 50),
            Player("Midfielder", "Midfielder", 50),
            p_low_def, # The low skill defender
            Player("Attacker", "Attacker", 50),
            Player("Midfielder", "Midfielder", 50),
        ]
        team = Team("Minnows", players_low_def, "Attacking") # Attacking tactic reduces defense
        
        # Base defense for this team = 1. Modifier for Attacking = 0.95
        # Expected defense = 1 * 0.95 = 0.95
        _, _, defe = team.calculate_tactical_strength()
        self.assertAlmostEqual(defe, 0.95)

        # Test with a player having skill 0 (if Player class allowed it)
        # For now, Player skill is 1-100. The max(0, ...) in Team is for robustness.
        # This test case with skill 1 and attacking tactic confirms correct calculation
        # and that it doesn't go below 0 due to Player constraints.
        
        # If a player had 0 skill and was a defender, and tactic was attacking:
        # defense_strength = 0 * 0.95 = 0. Then max(0, 0) is 0.
        # This scenario is covered by the implementation's max(0, ...)
        # We can simulate this by setting a player's skill to 0 manually if needed for a specific test,
        # but that would be testing a state not normally allowed by Player.
        # The current implementation of calculate_tactical_strength correctly uses max(0, strength).

if __name__ == '__main__':
    unittest.main()
