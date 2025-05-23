class Player:
    def __init__(self, name: str, role: str, skill: int):
        valid_roles = ['Attacker', 'Midfielder', 'Defender']
        if role not in valid_roles:
            raise ValueError(f"Invalid role: {role}. Role must be one of {valid_roles}")
        if not isinstance(skill, int) or not (1 <= skill <= 100):
            raise ValueError(f"Invalid skill level: {skill}. Skill must be an integer between 1 and 100.")

        self.name = name
        self.role = role
        self.skill = skill

    def __str__(self):
        return f"Name: {self.name}, Role: {self.role}, Skill: {self.skill}"
