import random
from collections import OrderedDict
import sys
def baseline(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def current_implementations(num):
    mapper = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
            100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    final_value = ''
    for key in list(mapper)[::-1]:
        if num >= key:
            final_value += int(num/key) * mapper[key]
            num %= key
    return final_value

def main():
    for cnt in range(100):
        num = random.randint(1, 100001)
        val1, val2 = baseline(num), current_implementations(num)
        if val1 != val2:
            print ("Integer %d to roman numeral is %s %s" % (num, val1, val2))
            sys.exit(-5)
    print ("Evaluated: ", cnt)
main()
