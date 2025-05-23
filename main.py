from player import Player
from team import Team
from simulation import simulate_clash
import random

def create_sample_team(team_name: str, num_attackers: int, num_midfielders: int, num_defenders: int) -> Team:
    """Helper function to create a team with a specified number of players in each role."""
    team = Team(team_name)
    
    # Create Attackers
    for i in range(num_attackers):
        skill = random.randint(60, 90) # Random skill between 60 and 90
        team.add_player(Player(f"{team_name}_Att{i+1}", "Attacker", skill))
        
    # Create Midfielders
    for i in range(num_midfielders):
        skill = random.randint(60, 90)
        team.add_player(Player(f"{team_name}_Mid{i+1}", "Midfielder", skill))
        
    # Create Defenders
    for i in range(num_defenders):
        skill = random.randint(60, 90)
        team.add_player(Player(f"{team_name}_Def{i+1}", "Defender", skill))
        
    return team

if __name__ == "__main__":
    # For reproducibility of the output, uncomment the line below
    # random.seed(42) 

    # 1. Create two sample teams with 5 players each
    # Team Alpha: 2 Attackers, 2 Midfielders, 1 Defender
    team_alpha = create_sample_team("Team Alpha", 2, 2, 1)
    
    # Team Beta: 2 Attackers, 2 Midfielders, 1 Defender
    team_beta = create_sample_team("Team Beta", 2, 2, 1)

    # Print team compositions (optional, for verification)
    print(f"{team_alpha.name} Players:")
    for player in team_alpha.players:
        print(f"- {player.name} ({player.role}, Skill: {player.skill})")
    
    print(f"\n{team_beta.name} Players:")
    for player in team_beta.players:
        print(f"- {player.name} ({player.role}, Skill: {player.skill})")
    print("\n" + "="*30 + "\n")

    # 2. Simulate a clash
    # simulate_clash sets tactics and calculates strengths internally
    score_alpha, score_beta = simulate_clash(team_alpha, team_beta)

    # 3. Print the results
    print(f"Clash Simulation Results:")
    print(f"-> {team_alpha.name} chose tactic: {team_alpha.tactic}")
    print(f"-> {team_beta.name} chose tactic: {team_beta.tactic}")
    print(f"\n--- Scores ---")
    print(f"{team_alpha.name} scored: {score_alpha}")
    print(f"{team_beta.name} scored: {score_beta}")
    
    print("\n" + "="*30 + "\n")
    
    # Optional: Print detailed strengths after clash
    # print(f"{team_alpha.name} Strengths: ATK {team_alpha.attack_strength}, MID {team_alpha.midfield_strength}, DEF {team_alpha.defense_strength}")
    # print(f"{team_beta.name} Strengths: ATK {team_beta.attack_strength}, MID {team_beta.midfield_strength}, DEF {team_beta.defense_strength}")
