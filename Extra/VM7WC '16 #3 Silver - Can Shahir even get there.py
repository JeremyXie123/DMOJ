# initial settings
num_houses, num_roads, shahir_house, date_house = [int(i) for i in input().split()]

shahir_house -= 1 # zero based
date_house -= 1 # zero based

#initializing an empty adjacency list
adj_list = [[] for i in range(num_houses)]

# reading the following n lines
for i in range(num_roads):
    line_data = input().split() 
    house_a = int(line_data[0]) - 1 # casting strings to integers
    house_b = int(line_data[1]) - 1 # casting strings to integers
    adj_list[house_a].append(house_b) # connection between house a and b
    adj_list[house_b].append(house_a) # connection between house b and a

from queue import Queue
to_visit = Queue()
to_visit.put(shahir_house) # visit shahir's house
visitted = set([shahir_house]) # visitted shahir's house

found = False

while not to_visit.empty(): # while there is still items to search through
    next_house = to_visit.get() # next items on tovisit gets visitted
    if next_house == date_house: # if the date house is found
        found = True
        break

    for house in adj_list[next_house]: # connected houses through roads
        if house not in visitted: # if you haven't visitted the house
            to_visit.put(house) # you will visit this later
            visitted.add(house) # you will visit this again, so prevent a duplicate call (optimization)

if found:
    print("GO SHAHIR!")
else:
    print("NO SHAHIR!")