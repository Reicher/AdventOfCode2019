# Day 1

print 'Day 1'

def simpleFuelCalc( mass ):
    fuel = mass / 3
    fuel -= 2
    return fuel

def advFuelCalc( mass, total = 0 ):
    fuel = simpleFuelCalc( mass )
    if fuel <= 0:
        return total
    else:
        total += fuel
        return advFuelCalc(fuel, total)
    
sum = 0
with open('input.txt', 'r') as fp:
    for line in fp:
        mass = int( line )
        fuel = advFuelCalc( mass )
        print str( mass ) + " mass = " + str( fuel ) + " fuel."
        sum += fuel

print "Total fuel needed: " + str( sum )
