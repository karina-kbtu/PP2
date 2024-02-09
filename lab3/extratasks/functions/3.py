def solve(numheads, numlegs):
    for numchickens in range(numheads + 1):
        numrabbits = numheads - numchickens
        totallegs = 2 * numchickens + 4 * numrabbits

        if totallegs == numlegs:
            return numchickens, numrabbits

    return None
print(solve())