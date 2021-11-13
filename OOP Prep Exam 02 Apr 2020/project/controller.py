from project.battle_field import BattleField
from project.player.player_repository import PlayerRepository
from project.card.card_repository import CardRepository
from project.player.beginner import Beginner
from project.player.advanced import Advanced
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type, username):
        player = eval(type)(username)
        self.player_repository.add(player)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type, name):
        card = eval(type)(name)
        self.card_repository.add(card)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username, card_name):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)

    def fight(self, attack_name, enemy_name):
        player_attack = self.player_repository.find(attack_name)
        player_enemy = self.player_repository.find(enemy_name)
        BattleField.fight(player_attack, player_enemy)
        return f"Attack user health {player_attack.health} - Enemy user health {player_enemy.health}"

    def report(self):
        result = []
        for user in self.player_repository.players:
            result.append(f"Username: {user.username} - Health: {user.health} - Cards {user.card_repository.count}")
            for card in user.card_repository.cards:
                result.append(f"### Card: {card.name} - Damage: {card.damage_points}")
        return '\n'.join(result)



