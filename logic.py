from random import randint

import requests


class Pokemon:
    pokemons = {}

    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer

        self.pokemon_number = randint(1, 1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(30, 60)
        self.power = randint(10, 30)

        Pokemon.pokemons[pokemon_trainer] = self

    def attack(self, enemy):
        if isinstance(enemy, Wizard) and randint(1, 5) == 1:
            return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}, хп врага: {enemy.hp}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["sprites"][0]["front_default"]
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/versions/generation-i/red-and-blue/25.png"

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["forms"][0]["name"]
        else:
            return "Pikachu"

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона: {self.name}, его сила: {self.power}, его хп: {self.hp}"

    # Метод класса для получения картинки покемона
    def show_img(self):

        return self.img


class Wizard(Pokemon):
    pass


class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(1, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой: {super_power}"
