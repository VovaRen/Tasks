import random


class Animals:

    def __init__(self, kind, name, age, awake):
        self.kind = kind
        self.age = age
        self.awake = awake
        self.name = name

    def age_info(self):
        return f'{self.name} the {self.kind}, he is {self.age} years old!'

    def awake_info(self):
        return f'{self.name} is asleep!' if self.awake == 'sleeping' else ''

    def eat_info(self):
        if self.awake != 'sleeping':
            return random.choice([f'{self.name} is eating!', ''])


animal_1 = Animals('cat', 'Tom', 5, 'sleeping')


class wolf(Animals):
    def __init__(self, kind, name, age, awake, color=None):
        super().__init__(kind, name, age, awake)
        self.color = color

    def color_info(self):
        return f'He is {self.color} color'

    def attack_info(self):
        return f'{self.name} can attack!' if super().eat_info() == '' else 'You can relax!'


animal_2 = wolf('wolf', 'Akela', 5, 'unsleeping', 'black')

print(animal_2.attack_info())
print(animal_2.age_info())

# def test(a: str) -> str:
#     return a
