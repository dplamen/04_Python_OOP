from project import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'
        if player.guild == 'Unaffiliated':
            player.guild = self.name
            self.players.append(player)
            return f'Welcome player {player.name} to the guild {player.guild}'
        return f'Player {player.name} is in another guild.'

    def kick_player(self, player_name):
        if self.players:
            for player in self.players:
                if player.name == player_name:
                    player.guild = 'Unaffiliated'
                    self.players.remove(player)
                    return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        result = []
        result.append(f'Guild: {self.name}')
        for player in self.players:
            result.append(player.player_info())
        return '\n'.join(result)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())


