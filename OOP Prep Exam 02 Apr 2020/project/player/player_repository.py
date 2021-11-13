class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player):
        if self.find(player.username):
            raise ValueError(f"Player {p.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player):
        if player == '':
            raise ValueError("Player cannot be an empty string!")
        if self.find(player):
            self.players.remove(self.find(player))
            self.count -= 1

    def find(self, username):
        for p in self.players:
            if p.username == username:
                return p
