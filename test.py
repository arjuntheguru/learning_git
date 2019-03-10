import random

temp1 = []
temp2 = []
temp3 = []
while len(temp1) != 3:
    rand = random.randint(1,8)
    while rand not in temp1:
        temp1.append(rand)

while len(temp2) != 3:
    rand = random.randint(1,8)
    while rand not in temp2 and rand not in temp1:
        temp2.append(rand)

while len(temp3) != 2:
    rand = random.randint(1,8)
    while rand not in temp2 and rand not in temp1 and rand not in temp3:
        temp3.append(rand)

temp3.append('')
matrix=[temp1,temp2,temp3]

    

