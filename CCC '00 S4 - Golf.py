# credits to tyler tian; this is me taking notes.
import sys

# stop program from breaking on last case
sys.setrecursionlimit(5280)

from math import isnan

# getting initial input
dist = int(input())
num_clubs = int(input())

# initiailization of array holding club lengths
clubs = [None for i in range(num_clubs)]

# filling the array
for i in range(num_clubs):
    clubs[i] = (int(input()))

known = {}
def fewest_strokes(distance, clubs):
    if distance == 0:
        return 0

    if distance in known:
        # if you know the # of shots to clear the remaining distance
        return known[distance]
    
    # if no match found then further break up the problem

    # in any sorting filter, your highest possible value is infinity
    fewest = float("inf")
    
    # iterate through the distances each club covers
    for club in clubs:
        if club == distance:
            # If the club can bridge the distance it needs to cover
            return 1

        elif club > distance:
            # If the club hits further than the distance then no point trying
            continue
    
        # recurse for a new distance given you've already hit this shot
        result = fewest_strokes(distance - club, clubs)

        # if the result is not nan (a result was found)
        if not isnan(result):
            if result < fewest:
                fewest = result

    # if the fewest hasn't changed, assign nan
    # this means there were no viable results in this recursion
    if fewest == float("inf"):
        fewest = float("nan")

    # at this distance, you can get to the hole in fewest shots + your current shot
    known[distance] = fewest + 1
    return fewest + 1

# initial recursion call
result = fewest_strokes(dist, clubs)

# if nan (no results were viable)
if isnan(result):
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in {} strokes.".format(result))