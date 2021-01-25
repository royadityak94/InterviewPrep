'''
    Source: https://www.youtube.com/watch?v=9mFaPhwsAb4
    Action: Convert integers to roman numerals
'''
from collections import OrderedDict

def convert_to_roman(num):
    # divisors = OrderedDict({1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
    #             50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'})
    # divisors = OrderedDict(reversed(list(divisors.items())))

    divisors = OrderedDict({1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC',
                            50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'})

    final_value = ''
    for key, value in divisors.items():
        if num >= key:
            final_value += int(num/key) * value
            num %= key
    return final_value

def main():
    #for num in range(1, 30):
    num = 532
    for num in range(1, 10):
        print ("Integer %d to roman numeral is %s" % (num, convert_to_roman(num)))

main()
