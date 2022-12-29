#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    if not roman_string:
        return 0
    elif not isinstance(roman_string, str):
        return 0
    else:
        result = 0
        for a, b in zip(roman_string, roman_string[1:]):
            if roman_num[a] < roman_num[b]:
                result -= roman_num[a]
            else:
                result += roman_num[a]
        return result + roman_num[roman_string[-1]]
