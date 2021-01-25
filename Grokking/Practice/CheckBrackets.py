
def main():
    openingBrackets = '({['
    closingBrackets = ')}]'
    matchingPairs = {}
    for idx, char in enumerate(closingBrackets):
    	matchingPairs[char] = openingBrackets[idx]
    print (matchingPairs)

main()
