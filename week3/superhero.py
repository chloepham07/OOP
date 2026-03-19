class Superhero:
    def __init__(self, name, weapon, color):
        self.name = name
        self.weapon = weapon
        self.color = color

    def __str__(self):
        return f"{self.name} | {self.weapon} | {self.color}"

superhero_A = Superhero('A','sword','red')
print(superhero_A)

superhero_B = Superhero('B','shield','green')
print(superhero_B)