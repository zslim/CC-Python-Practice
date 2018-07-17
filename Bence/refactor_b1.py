import random

while True:
    num_a = input("How many units attack: ")
    if int(num_a) == 1 or int(num_a) == 2 or int(num_a) == 3:
        break
    else:
        num_a = input("How many units attack: ")

while True:
    num_d = input("How many units defend: ")
    if int(num_d) == 1 or int(num_d) == 2:
        break
    else:
        num_d = input("How many units defend: ")

attack = []
defend = []

for x in range(int(num_a)):
    attack.append(random.randint(1, 6))
    
for x in range(int(num_d)):
    defend.append(random.randint(1, 6))

attack = sorted(attack, key=int, reverse=True)
defend = sorted(defend, key=int, reverse=True)

lost_att, lost_def = 0, 0

print("\n" + "Dice:")

if int(num_a) == 3:
    print("\t" + "Attacker: " + str(attack[0]) + "-" + str(attack[1]) + "-" + str(attack[2]))
elif int(num_a) == 2:
    print("\t" + "Attacker: " + str(attack[0]) + "-" + str(attack[1]))
elif int(num_a) == 1:
    print("\t" + "Attacker: " + str(attack[0]))

if int(num_d) == 2:
    print("\t" + "Defender: " + str(defend[0]) + "-" + str(defend[1]))
elif int(num_d) == 1:
    print("\t" + "Defender: " + str(defend[0]))

if attack[0] <= defend[0]:
    lost_att += 1
else:
    lost_def += 1

if attack[1] <= defend[1]:
    lost_att += 1
else:
    lost_def += 1

print("\n" + "Outcome:")
print("\t" + "Attacker: Lost", str(lost_att), "unit(s)")
print("\t" + "Defender: Lost", str(lost_def), "unit(s)")