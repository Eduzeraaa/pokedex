class Pokemon:
    def __init__(self, name, poke_type, hp, attack, defense, height, weight, speed):
        self.name = name
        self.poke_type = poke_type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.height = height
        self.weight = weight
        self.speed = speed

    def show_info(self):
        print(f'Name: {self.name}\nType: {self.poke_type}\nHP: {self.hp}\nAttack: {self.attack}\nDefense: {self.defense}\nSpeed: {self.speed}')
    
    def speech(self):
        pass
    
