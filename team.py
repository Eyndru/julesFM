from player import Player

class Team:
    def __init__(self, name: str, players: list[Player], tactic: str = ""):
        self.name = name
        self.players = players
        self.tactic = tactic

    def __str__(self) -> str:
        return self.name

    def set_tactic(self, chosen_tactic: str):
        valid_tactics = ['Attacking', 'Balanced', 'Defensive']
        if chosen_tactic in valid_tactics:
            self.tactic = chosen_tactic
        else:
            raise ValueError(f"Invalid tactic chosen. Must be one of {valid_tactics}")

    def calculate_tactical_strength(self):
        attack_strength = 0.0
        midfield_strength = 0.0
        defense_strength = 0.0

        for player in self.players:
            if player.role == 'Attacker':
                attack_strength += player.skill
            elif player.role == 'Midfielder':
                midfield_strength += player.skill
            elif player.role == 'Defender':
                defense_strength += player.skill

        if self.tactic == 'Attacking':
            attack_strength *= 1.10
            defense_strength *= 0.95
        elif self.tactic == 'Defensive':
            defense_strength *= 1.10
            attack_strength *= 0.95

        attack_strength = max(0, attack_strength)
        midfield_strength = max(0, midfield_strength)
        defense_strength = max(0, defense_strength)

        return attack_strength, midfield_strength, defense_strength
