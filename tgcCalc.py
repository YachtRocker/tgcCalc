# Program to calculate golf clubs to use in the game "The Golf Club"
# Programmer:  Douglas Kohn
# To Do:
#	Convert over to a GUI
#	Add error handling
#	Give golfer more than one choice of club
#	Add rollout possibly
#       Add Putting Calc  -   DONE

import os

clubs = {   # distance, how much to open club, and club name
	245: (0, '3w'),
	225: (0, '5w'),
	207: (0, '3i'),
	198: (1, '3i'),
	182: (2, '3i'),
	162: (3, '3i'),
	147: (4, '3i'),
	195: (0, '4i'),
	183: (1, '4i'),
	166: (2, '4i'),
	146: (3, '4i'),
	131: (4, '4i'),
	181: (0, '5i'),
	167: (1, '5i'),
	149: (2, '5i'),
	130: (3, '5i'),
	115: (4, '5i'),
	170: (0, '6i'),
	153: (1, '6i'),
	134: (2, '6i'),
	114: (3, '6i'),
	101: (4, '6i'),
	158: (0, '7i'),
	139: (1, '7i'),
	120: (2, '7i'),
	100: (3, '7i'),
	87: (4, '7i'),
	145: (0, '8i'),
	125: (1, '8i'),
	106: (2, '8i'),
	87: (3, '8i'),
	75: (4, '8i'),
	132: (0, '9i'),
	112: (1, '9i'),
	93: (2, '9i'),
	76: (3, '9i'),
	64: (4, '9i'),
	120: (0, 'PW'),
	100: (1, 'PW'),
	82: (2, 'PW'),
	65: (3, 'PW'),
	54: (4, 'PW'),
	95: (0, 'SW'),
	80: (1, 'SW'),
	67: (2, 'SW'),
	55: (3, 'SW'),
	47: (4, 'SW'),
	75: (0, 'LW'),
	64: (1, 'LW'),
	54: (2, 'LW'),
	46: (3, 'LW'),
	39: (4, 'LW'),
}

# Function to calculate where to put the marker/distance for putting
def puttCalc(dist, elev):
    
    adjustedDistance = 0
    if elev > 0:
        adjustedElev = (elev * 1.5) + 2
        adjustedDistance = dist + adjustedElev
    elif elev < 0:
        adjustedElev = abs(elev) - 2
        adjustedDistance = dist - adjustedElev
    else:
        adjustedElev = 0

    print ""
    return adjustedDistance

# Functon which calculates distance adjustment for wind and elevation and selects a club recommendation.
def distCalculation(dist, wind, elev):
    adjDist = 0
    
    # Calc wind effect on ball, headwind*1.75, tailwind*0.75
    if wind > 0:
	wind = wind * 1.75
	adjDist = dist + wind
        print str(wind) + ' ' + str(adjDist)
    elif wind < 0:
	wind = abs(wind) * 0.75
	adjDist = dist - wind
        print str(wind) + ' ' + str(adjDist)
    else:
	adjDist = dist

    # Calc elevation effect on ball, divide by 3, add to distance if elevation is up, subtract from distance if elevation is down.
    if elev > 0:
	elev = elev / 3
	adjDist = adjDist + elev
        print str(elev) + ' ' + str(adjDist)
    elif elev < 0:
	elev = abs(elev) / 3
	adjDist = adjDist - elev
        print str(elev) + ' ' + str(adjDist)
    return adjDist

os.system('clear')

while True:
    choice = raw_input("Distance or Putting calculation( enter d or p): ")
    if choice.strip() == 'd':
	    distance = input('Enter Distance: ')
            print 'Enter 0 for no wind, negative number for tailwind, positive number for headwind.'
            wind = input('Enter Wind Speed: ')
	    elevation = input('Enter Elevation(negative for downward): ')
	    newdistance = distCalculation(distance, wind, elevation)
	
	    results = clubs[min(clubs, key=lambda x:abs(x-newdistance))]  # get the info from the dictionary, pick the number in the dict closest to newdistance

	    print " "
	    print "Use club " + str(results[1]) + " adjust up " + str(results[0])
	    print "Club distance is: " + str(min(clubs, key=lambda x:abs(x-newdistance))) + ", calculated distance is: " + str(newdistance)
	    print "Original distance is: " + str(distance)
	    print " "
    elif choice.strip() == 'p':
        puttDist = input('Enter distance from pin: ')
        puttElevDist = input('Enter elevaton of pin (negative for downhill): ')
        puttingAdjustment = puttCalc(puttDist, puttElevDist)
        print 'Set putting marker at ' + str(puttingAdjustment) + ' feet, and adjust for left/right movement.'
        print ''

    yesno = raw_input('continue(y/n): ')
	
    if yesno.strip() == 'y':
        print ""
        os.system('clear')
    else:
    	print "Goodbye."
        break

