from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("TestHero", 3, 15.4, 4.5)

    def test_initialization(self):
        self.assertEqual("TestHero", self.hero.username)
        self.assertEqual(3, self.hero.level)
        self.assertEqual(15.4, self.hero.health)
        self.assertEqual(4.5, self.hero.damage)
        
    def test_battle_itself_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_if_not_enough_health_raises(self):
        self.hero.health = - 3
        enemy_hero = Hero("Enemy", 3, 10.5, 2.5)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. "
                         "You need to rest", str(ex.exception))

    def test_battle_if_enemy_not_enough_health_raises(self):
        enemy_hero = Hero("Enemy", 3, 0, 2.5)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight Enemy. "
                         "He needs to rest", str(ex.exception))

    def test_battle_if_hero_wins(self):
        enemy_hero = Hero("Enemy", 3, 10.5, 2.5)
        result = self.hero.battle(enemy_hero)
        self.assertEqual("You win", result)
        self.assertEqual(4, self.hero.level)
        self.assertEqual(12.9, self.hero.health)
        self.assertEqual(9.5, self.hero.damage)

    def test_battle_if_enemy_hero_wins(self):
        enemy_hero = Hero("Enemy", 5, 17.5, 2.5)
        result = self.hero.battle(enemy_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(6, enemy_hero.level)
        self.assertEqual(9, enemy_hero.health)
        self.assertEqual(7.5, enemy_hero.damage)

    def test_battle_if_draw(self):
        self.hero.health = 13.5
        enemy_hero = Hero("Enemy", 3, 13.5, 4.5)
        result = self.hero.battle(enemy_hero)
        self.assertEqual("Draw", result)
        
    def test_represent_hero(self):
        result = str(self.hero)
        self.assertEqual("Hero TestHero: 3 lvl\n"
                         "Health: 15.4\n"
                         "Damage: 4.5\n", result)


if __name__ == '__main__':
    main()
