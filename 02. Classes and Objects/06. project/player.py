class Player:

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f'Skill {skill_name} added to the collection of the player {self.name}'
        return "Skill already added"

    def player_info(self):
        result = []
        result.append(f'Name: {self.name}')
        result.append(f'Guild: {self.guild}')
        result.append(f'HP: {self.hp}')
        result.append(f'MP: {self.mp}')
        if self.skills:
            for skill, mana in self.skills.items():
                result.append(f'==={skill} - {mana}')
        return '\n'.join(result) + '\n'
