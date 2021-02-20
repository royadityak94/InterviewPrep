'''
Given a word, write a function to generate all of its unique generalized abbreviations.
Generalized abbreviation of a word can be generated by replacing each substring of the word by the count of characters in the substring. Take the example of “ab” which has four substrings: “”, “a”, “b”, and “ab”. After replacing these substrings in the actual word by the count of characters we get all the generalized abbreviations: “ab”, “1b”, “a1”, and “2”.
'ab' => [“”, “a”, “b”, “ab”] => [“ab”, “1b”, “a1”,  “2”]
"BAT" => "BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"
'''
# O(n * 2^N) time | O(n * 2^N) space
def generate_gen_abbrev(string):
    resultant = []
    generate_gen_abbrev_rec(string, [], 0, 0, resultant)
    return resultant

def generate_gen_abbrev_rec(string, abvWord, currIdx, count, resultant):
    if currIdx == len(string):
        print ("Got: ", abvWord)
        if count:
            abvWord += str(count),
        resultant += ''.join(abvWord),
    else:
        generate_gen_abbrev_rec(string, abvWord[:], currIdx+1, count+1, resultant)

        if count:
            abvWord += str(count),
        newWord = abvWord + [string[currIdx]]
        print ("\t Sending New: ", newWord)
        generate_gen_abbrev_rec(string, newWord, currIdx+1, 0, resultant)

def main():
    print("Generalized abbreviation are: " + str(generate_gen_abbrev("BAT")))
    #print("Generalized abbreviation are: " + str(generate_gen_abbrev("code")))

main()

# ['3', '2T', '1A1', '1AT', 'B2', 'B1T', 'BA1', 'BAT']
# ['4', '3e', '2d1', '2de', '1o2', '1o1e', '1od1', '1ode', 'c3', 'c2e', 'c1d1', 'c1de', 'co2', 'co1e', 'cod1', 'code']
#
