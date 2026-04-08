class Superhero:
    def __init__(self, name, weapon, color,power):
        self.name = name
        self.weapon = weapon
        self.color = color
        self.power = power


    def __str__(self):
        return f"{self.name} |weapon: {self.weapon} | color: {self.color} | power: {self.power}"

superhero_team = []

while True:
    name = input('Enter superhero name (or type \'stop\' to exit)')
    if name.lower() == 'stop':
        break

    weapon= input('weapon: ')
    color= input('color: ')
    power= input('power: ')
    new_hero = Superhero(name, weapon, color, power)
    superhero_team.append(new_hero)
    print(f'added {name} to the list')

print(f'List of {len(superhero_team)} superheros')
for superhero in superhero_team:
    print(superhero)
