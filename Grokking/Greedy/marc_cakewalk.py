# Source: https://www.hackerrank.com/challenges/marcs-cakewalk/problem

def marcsCakewalk(calorie):
    calorie.sort(reverse=True) # Sorting calories in descending order
    j = 0
    minimum_miles = 0
    while j < len(calorie):
        minimum_miles += (2 ** j) * calorie[j]
        j += 1
    return minimum_miles

if __name__ == '__main__':
    print (marcsCakewalk([1, 3, 2]))
    print (marcsCakewalk([7, 4, 9, 6]))
