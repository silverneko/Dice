import random

def roll(dice):
    dice = dice.split('+')
    points = 0
    for die in dice:
        die.replace('D', 'd')
        if die.count('d'):
            die = die.split('d')
            if not die[0]:
                times = 1
            else:
                times = int(die[0])
            faces = int(die[1])
            for _ in range(times):
                points += 1 + random.randrange(faces)
        else:
            points += int(die)
    return points
