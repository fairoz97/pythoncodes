import random

#Returns coordinates after n steps of random walks
def random_walk(n):
    x = 0
    y = 0
    for i in range(n):
        direction = random.choice(['N', 'S', 'E', 'W'])
        if direction == 'N':
            y +=1
        elif direction == 'S':
            y -=1
        elif direction == 'E':
            x +=1
        else:
            x -=1
    return (x,y)    # x and y coordinates after taking n steps

number_of_walks = 1000

for walk_length in range(1,51):
    no_transport = 0
    for i in range(number_of_walks):
        walk = random_walk(walk_length)
        dist = abs(abs(walk[0]) + abs(walk[1]))
        if dist <= 4:
            no_transport +=1
    no_transport_percentage = no_transport / number_of_walks
    print("Walk Size:", walk_length, "// % of no transport: ", no_transport_percentage*100)
