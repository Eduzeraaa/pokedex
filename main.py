from pokemon import Pokemon


class Pikachu(Pokemon):
        def __init__ (self):
                super().__init__('Pikachu', 'Electric', 35, 40, 40, '0.4 m', '6 kg', 90)
        def speech(self):
            print("PIKACHU, PIKA PIKA ⚡")



class Charmander(Pokemon):
        def __init__ (self):
                super().__init__('Charmander', 'Fire', 39, 52, 43, '0.6 m', '8.5 kg', 65)
        def speech(self):
            print("CHARMANDER, WRAAAAH 🔥")



class Bulbasaur(Pokemon):
        def __init__ (self):
                super().__init__('Bulbasaur', 'Grass/Poison', 45, 49, 49, '0.7 m', '6.9 kg', 45)
        def speech(self):
            print("BULBASAUR, BULBA BULBA 🌿")

pokedex = [Pikachu(), Charmander(), Bulbasaur()]

i = int(input('Which Pokemon do you want to see?\n(0 - Any 1 - Pikachu, 2 - Charmander, 3 - Bulbasaur)\n'))
while i != 0:
        if 1 <= i <= len(pokedex):
                pokedex[i-1].show_info()
                pokedex[i-1].speech()
                print('------------------')
        else:
                print('Invalid option. Please try again.')
        i = int(input('Which Pokemon do you want to see?\n(0 - Any 1 - Pikachu, 2 - Charmander, 3 - Bulbasaur)\n'))
print('Exiting...')
