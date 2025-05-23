import unittest
import random
from player import Player
from team import Team
from simulation import simulate_clash

class TestSimulation(unittest.TestCase):

    def setUp(self):
        # Seed random for predictable "random" variance in tests if needed,
        # but for general outcome testing, it might not be strictly necessary.
        # random.seed(42) 
        
        self.team_alpha = Team("Alpha")
        self.team_beta = Team("Beta")

        # Populate Team Alpha
        self.team_alpha.add_player(Player("A_Att1", "Attacker", 80))
        self.team_alpha.add_player(Player("A_Mid1", "Midfielder", 70))
        self.team_alpha.add_player(Player("A_Def1", "Defender", 75))

        # Populate Team Beta
        self.team_beta.add_player(Player("B_Att1", "Attacker", 82))
        self.team_beta.add_player(Player("B_Mid1", "Midfielder", 68))
        self.team_beta.add_player(Player("B_Def1", "Defender", 73))

    def test_simulate_clash_basic_run(self):
        """Test that simulate_clash runs and returns scores."""
        score_alpha, score_beta = simulate_clash(self.team_alpha, self.team_beta)
        
        self.assertIsInstance(score_alpha, float)
        self.assertIsInstance(score_beta, float)
        
        # Check that tactics were set
        self.assertIsNotNone(self.team_alpha.tactic)
        self.assertIsNotNone(self.team_beta.tactic)
        
        # Check that strengths were calculated (will be non-zero if players exist)
        # These will change based on random tactic, so check they are not the initial zero.
        # This test assumes initial strengths are 0. If they can be something else, adjust.
        self.assertTrue(self.team_alpha.attack_strength != 0 or 
                        self.team_alpha.midfield_strength != 0 or 
                        self.team_alpha.defense_strength != 0)
        self.assertTrue(self.team_beta.attack_strength != 0 or 
                        self.team_beta.midfield_strength != 0 or 
                        self.team_beta.defense_strength != 0)

    def test_simulate_clash_input_type_validation(self):
        """Test that simulate_clash raises TypeError for invalid inputs."""
        with self.assertRaisesRegex(TypeError, "Both inputs must be Team objects."):
            simulate_clash(self.team_alpha, "not_a_team")
        with self.assertRaisesRegex(TypeError, "Both inputs must be Team objects."):
            simulate_clash("not_a_team", self.team_beta)
        with self.assertRaisesRegex(TypeError, "Both inputs must be Team objects."):
            simulate_clash(None, None)

    def test_simulate_clash_score_possibilities(self):
        """Run multiple simulations to check score patterns."""
        possible_scores_single_team = {0.0, 0.5, 1.0, 1.5} # Scores a team can get from winning zones
        # A team can win their attack zone (+1) and midfield (+0.5) = 1.5
        # A team can also concede a goal if the other team wins their attack zone.
        # So total scores can be 0, 0.5, 1.0, 1.5 (ignoring what the other team scores for a moment)
        # Max total score in a clash is 1 (for attack) + 0.5 (for mid) + 1 (for other team's attack) = 2.5
        # But we return (team1_score, team2_score)
        
        alpha_scores_seen = set()
        beta_scores_seen = set()
        
        for _ in range(200): # Run many times due to randomness
            # Reset strengths before each clash for consistent input conditions to simulate_clash
            # as simulate_clash modifies them.
            # This is important because set_tactic and calculate_tactical_strength are called inside simulate_clash.
            # Re-initialize teams or reset relevant attributes for a clean state if necessary,
            # or ensure setUp creates fresh objects for each test method if not already.
            # For this test, we'll re-run setup's player adding and strength calculation steps
            # to ensure each clash is independent of the last one's side effects on team objects.

            # Simplified reset: re-initialize teams for each iteration for true independence
            # This is a bit heavy but ensures no state leakage between simulations.
            # A lighter approach might be to reset tactic and strengths to None/0.
            current_team_alpha = Team("Alpha")
            current_team_alpha.add_player(Player("A_Att1", "Attacker", 80))
            current_team_alpha.add_player(Player("A_Mid1", "Midfielder", 70))
            current_team_alpha.add_player(Player("A_Def1", "Defender", 75))

            current_team_beta = Team("Beta")
            current_team_beta.add_player(Player("B_Att1", "Attacker", 82))
            current_team_beta.add_player(Player("B_Mid1", "Midfielder", 68))
            current_team_beta.add_player(Player("B_Def1", "Defender", 73))

            score_alpha, score_beta = simulate_clash(current_team_alpha, current_team_beta)
            alpha_scores_seen.add(score_alpha)
            beta_scores_seen.add(score_beta)

            # Check if scores are among possible values
            # Each point source: Team1 Attack (1), Midfield (0.5), Team2 Attack (1)
            # Team 1 can get: 0, 0.5, 1, 1.5
            # Team 2 can get: 0, 0.5, 1, 1.5
            self.assertIn(score_alpha, [0.0, 0.5, 1.0, 1.5])
            self.assertIn(score_beta, [0.0, 0.5, 1.0, 1.5])

if __name__ == '__main__':
    unittest.main()
