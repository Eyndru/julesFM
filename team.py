import random
from player import Player # Assuming player.py is in the same directory

class Team:
    def __init__(self, name: str):
        """Initializes a Team with a name and an empty list of players."""
        self.name = name
        self.players = []
        self.tactic = None
        self.attack_strength = 0
        self.midfield_strength = 0
        self.defense_strength = 0
        self.tactics_list = ['Attacking', 'Balanced', 'Defensive']

    def add_player(self, player: Player):
        """Adds a Player object to the team's list of players."""
        if isinstance(player, Player):
            self.players.append(player)
        else:
            raise TypeError("Invalid player object. Please add a Player instance.")

    def set_tactic(self):
        """Randomly selects a tactic for the team."""
        self.tactic = random.choice(self.tactics_list)

    def calculate_tactical_strength(self):
        """
        Calculates the team's strength in attack, midfield, and defense based on players' skills and team tactic.
        Applies tactical multipliers:
            - Attacking: Attack x1.2, Midfield x1.0, Defense x0.8
            - Balanced:  Attack x1.0, Midfield x1.0, Defense x1.0
            - Defensive: Attack x0.8, Midfield x1.0, Defense x1.2
        """
        if not self.players:
            # No players, no strength
            self.attack_strength = 0
            self.midfield_strength = 0
            self.defense_strength = 0
            return

        base_attack = 0
        base_midfield = 0
        base_defense = 0

        for player in self.players:
            if player.role == 'Attacker':
                base_attack += player.skill
            elif player.role == 'Midfielder':
                base_midfield += player.skill
            elif player.role == 'Defender':
                base_defense += player.skill

        if self.tactic == 'Attacking':
            self.attack_strength = int(base_attack * 1.2)
            self.midfield_strength = int(base_midfield * 1.0)
            self.defense_strength = int(base_defense * 0.8)
        elif self.tactic == 'Balanced':
            self.attack_strength = int(base_attack * 1.0)
            self.midfield_strength = int(base_midfield * 1.0)
            self.defense_strength = int(base_defense * 1.0)
        elif self.tactic == 'Defensive':
            self.attack_strength = int(base_attack * 0.8)
            self.midfield_strength = int(base_midfield * 1.0)
            self.defense_strength = int(base_defense * 1.2)
        else:
            # Default to balanced if tactic not set or invalid, though set_tactic should prevent invalid
            self.attack_strength = int(base_attack * 1.0)
            self.midfield_strength = int(base_midfield * 1.0)
            self.defense_strength = int(base_defense * 1.0)

    def __str__(self):
        return (f"Team: {self.name}, Tactic: {self.tactic}, "
                f"Players: {len(self.players)}, "
                f"ATK: {self.attack_strength}, MID: {self.midfield_strength}, DEF: {self.defense_strength}")
