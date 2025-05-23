import unittest
from player import Player

class TestPlayer(unittest.TestCase):

    def test_successful_player_creation(self):
        player = Player("TestPlayer", "Attacker", 85)
        self.assertEqual(player.name, "TestPlayer")
        self.assertEqual(player.role, "Attacker")
        self.assertEqual(player.skill, 85)

    def test_str_method(self):
        player = Player("TestPlayer", "Attacker", 85)
        self.assertEqual(str(player), "Name: TestPlayer, Role: Attacker, Skill: 85")

    def test_invalid_role(self):
        with self.assertRaisesRegex(ValueError, "Invalid role: Goalkeeper. Role must be one of \\['Attacker', 'Midfielder', 'Defender'\\]"):
            Player("TestPlayer", "Goalkeeper", 85)

    def test_invalid_skill_too_low(self):
        with self.assertRaisesRegex(ValueError, "Invalid skill level: 0. Skill must be an integer between 1 and 100."):
            Player("TestPlayer", "Defender", 0)
        with self.assertRaisesRegex(ValueError, "Invalid skill level: -10. Skill must be an integer between 1 and 100."):
            Player("TestPlayer", "Midfielder", -10)

    def test_invalid_skill_too_high(self):
        with self.assertRaisesRegex(ValueError, "Invalid skill level: 101. Skill must be an integer between 1 and 100."):
            Player("TestPlayer", "Attacker", 101)
        with self.assertRaisesRegex(ValueError, "Invalid skill level: 150. Skill must be an integer between 1 and 100."):
            Player("TestPlayer", "Defender", 150)

    def test_invalid_skill_not_an_integer(self):
        with self.assertRaisesRegex(ValueError, "Invalid skill level: high. Skill must be an integer between 1 and 100."):
            Player("TestPlayer", "Midfielder", "high")
        with self.assertRaisesRegex(ValueError, "Invalid skill level: 95.5. Skill must be an integer between 1 and 100."):
            Player("TestPlayer", "Attacker", 95.5)


if __name__ == '__main__':
    unittest.main()
