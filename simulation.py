import random
from team import Team # Assuming team.py is in the same directory

def simulate_clash(team1: Team, team2: Team):
    """
    Simulates a single tactical clash between two teams.

    Args:
        team1: The first Team object.
        team2: The second Team object.

    Returns:
        A tuple containing the scores for team1 and team2 (team1_score, team2_score).
    """
    if not isinstance(team1, Team) or not isinstance(team2, Team):
        raise TypeError("Both inputs must be Team objects.")

    # 1. Set tactics for both teams
    team1.set_tactic()
    team2.set_tactic()

    # 2. Calculate tactical strengths
    team1.calculate_tactical_strength()
    team2.calculate_tactical_strength()

    team1_score = 0.0
    team2_score = 0.0

    # 3. Determine zone winners with random variance
    variance = lambda: random.randint(-5, 5)

    # Team 1 Attack vs Team 2 Defense
    t1_attack_effective = team1.attack_strength + variance()
    t2_defense_effective = team2.defense_strength + variance()
    if t1_attack_effective > t2_defense_effective:
        team1_score += 1.0

    # Team 1 Midfield vs Team 2 Midfield
    t1_midfield_effective = team1.midfield_strength + variance()
    t2_midfield_effective = team2.midfield_strength + variance()
    if t1_midfield_effective > t2_midfield_effective:
        team1_score += 0.5
    elif t2_midfield_effective > t1_midfield_effective:
        team2_score += 0.5

    # Team 2 Attack vs Team 1 Defense
    t2_attack_effective = team2.attack_strength + variance()
    t1_defense_effective = team1.defense_strength + variance()
    if t2_attack_effective > t1_defense_effective:
        team2_score += 1.0
        
    return team1_score, team2_score
