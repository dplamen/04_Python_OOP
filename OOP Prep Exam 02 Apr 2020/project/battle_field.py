class BattleField:

    def fight(self, attacker, enemy):
        players = [attacker, enemy]
        for player in players:
            if player.is_dead:
                raise ValueError("Player is dead!")

        for player in players:
            if player.__class__.__name__ == 'Beginner':
                player.health += 40
                for card in player.card_repository.cards:
                    card.damage_points += 30

        for player in players:
            for card in player.card_repository.cards:
                player.health += card.health_points

        for card in attacker.card_repository.cards:
            if enemy.is_dead:
                return
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            if attacker.is_dead:
                return
            attacker.take_damage(card.damage_points)