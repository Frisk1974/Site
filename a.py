import random

# Classe para habilidades
class Skill:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def level_up(self):
        self.level += 1
        print(f"Habilidade '{self.name}' aumentou para o nível {self.level}!")

# Classe para o jogador
class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.skills = []
        self.inventory = Inventory()
        self.location = "vilarejo"

    def learn_skill(self, skill_name):
        skill = Skill(skill_name)
        self.skills.append(skill)
        print(f"{self.name} aprendeu a habilidade '{skill_name}'!")

    def upgrade_skill(self, skill_name):
        for skill in self.skills:
            if skill.name == skill_name:
                skill.level_up()
                break
        else:
            print("Habilidade não encontrada.")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} ganhou {amount} de experiência!")
        if self.experience >= 100:  # Exemplo de limite para subir de nível
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        print(f"{self.name} subiu para o nível {self.level}!")

    def move(self, location):
        self.location = location
        print(f"{self.name} se moveu para {location}.")

# Classe para o inventário
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Item '{item}' adicionado ao inventário.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Item '{item}' removido do inventário.")
        else:
            print("Item não encontrado no inventário.")

    def show_inventory(self):
        print("Inventário:", self.items)

# Classe para inimigos
class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} recebeu {damage} de dano. Saúde restante: {self.health}")

# Classe para batalhas
class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        print(f"Iniciando batalha entre {self.player.name} e {self.enemy.name}!")
        while self.player.level > 0 and self.enemy.health > 0:
            damage = 10  # Exemplo de dano
            self.enemy.take_damage(damage)
            if self.enemy.health <= 0:
                print(f"{self.enemy.name} foi derrotado!")
                self.player.gain_experience(50)
                break
            self.player.gain_experience(10)  # Exemplo de ganho de experiência
            print(f"{self.player.name} ataca {self.enemy.name}!")

# Classe para missões
class Quest:
    def __init__(self, title, description, reward):
        self.title = title
        self.description = description
        self.reward = reward
        self.completed = False

    def complete_quest(self):
        self.completed = True
        print(f"Missão '{self.title}' completada! Recompensa: {self.reward}")

# Classe para clima
class Weather:
    def __init__(self):
        self.conditions = ["ensolarado", "nublado", "chuva", "neve"]
        self.current_condition = random.choice(self.conditions)

    def change_weather(self):
        self.current_condition = random.choice(self.conditions)
        print(f"O clima mudou para: {self.current_condition}")

    def apply_weather_effects(self):
        if self.current_condition == "chuva":
            print("A visibilidade está reduzida devido à chuva.")
        elif self.current_condition == "neve":
            print("A movimentação está mais lenta por causa da neve.")

# Classe para loja
class Shop:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, price):
        self.inventory[item] = price

    def sell_item(self, item, player_inventory):
        if item in self.inventory:
            price = self.inventory[item]
            player_inventory.remove_item (item)
            print(f"Item '{item}' vendido por {price} moedas.")
        else:
            print("Item não disponível na loja.")

# Criação de um jogador
player = Player("João")

# Sistema de inventário
inventory = player.inventory
inventory.add_item("poção de cura")

# Criação de um inimigo
enemy = Enemy("Goblin", 30)

# Iniciar batalha
battle = Battle(player, enemy)
battle.start_battle()

# Criar uma missão
quest = Quest("Missão 1", "Complete a missão 1", "100 moedas")

# Completar a missão
quest.complete_quest()

# Criar clima e mudar
weather = Weather()
weather.change_weather()

# Mostrar inventário
inventory.show_inventory() 
# Adicionar mais itens ao inventário
inventory.add_item("espada")
inventory.add_item("armadura")

# Tentar vender um item na loja
shop = Shop()
shop.add_item("espada", 100)
shop.add_item("armadura", 200)

# Vender a espada
shop.sell_item("espada", inventory)

# Mostrar o inventário após a venda
inventory.show_inventory()

# Aprender uma nova habilidade
player.learn_skill("magia")

# Atualizar uma habilidade
player.upgrade_skill("magia")

# Mover o jogador para uma nova localização
player.move("floresta")

# Aplicar efeitos do clima
weather.apply_weather_effects()
# Adicionar mais funcionalidades ao RPG
# Sistema de eventos aleatórios
class RandomEvent:
    def __init__(self):
        self.events = [
            "Você encontrou um tesouro!",
            "Um inimigo apareceu!",
            "Você encontrou um viajante que oferece ajuda.",
            "Uma tempestade se aproxima."
        ]

    def trigger_event(self):
        event = random.choice(self.events)
        print(event)

# Exemplo de uso do sistema de eventos aleatórios
random_event = RandomEvent()
random_event.trigger_event()

# Sistema de habilidades especiais
class SpecialSkill(Skill):
    def __init__(self, name, level=1, cooldown=0):
        super().__init__(name, level)
        self.cooldown = cooldown
        self.is_on_cooldown = False

    def use_skill(self):
        if not self.is_on_cooldown:
            print(f"{self.name} foi usado!")
            self.is_on_cooldown = True
            # Lógica para cooldown
        else:
            print(f"{self.name} está em cooldown!")

# Exemplo de habilidade especial
fireball = SpecialSkill("Fireball", cooldown=3)
fireball.use_skill()

# Sistema de crafting
class Crafting:
    def __init__(self):
        self.recipes = {
            "espada de ferro": ["ferro", "ferro", "couro"],
            "poção de cura": ["erva", "água"]
        }

    def craft_item(self, item, inventory):
        if item in self.recipes:
            required_items = self.recipes[item]
            if all(inventory.items.count(i) >= required_items.count(i) for i in required_items):
                for i in required_items:
                    inventory.remove_item(i)
                inventory.add_item(item)
                print(f"{item} foi criado com sucesso!")
            else:
                print("Itens insuficientes para criar o item.")
        else:
            print("Receita não encontrada.")

# Exemplo de uso do sistema de crafting
crafting = Crafting()
inventory.add_item("ferro")
inventory.add_item("ferro")
inventory.add_item("couro")
crafting.craft_item("espada de ferro", inventory)

# Sistema de habilidades de combate
class CombatSkill(SpecialSkill):
    def __init__(self, name, damage, level=1, cooldown=0):
        super().__init__(name, level, cooldown)
        self.damage = damage

    def use_skill(self, enemy):
        if not self.is_on_cooldown:
            enemy.take_damage(self.damage)
            self.is_on_cooldown = True
            print(f"{self.name} causou {self.damage} de dano!")
        else:
            print(f"{self.name} está em cooldown!")

# Exemplo de habilidade de combate
sword_slash = CombatSkill("Sword Slash", damage=15)
sword_slash.use_skill(enemy)

# Finalizando o jogo
print("Obrigado por jogar!")