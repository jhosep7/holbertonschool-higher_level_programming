#!/usr/bin/python3
def roman_to_int(roman_string):
    Ans = 0
    i = 0
    Dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    while (i < len(roman_string)):
        N1 = Dict[roman_string[i]]
        if (i + 1 < len(roman_string)):
            N2 = Dict[roman_string[i + 1]]
            if (N1 >= N2):
                Ans = Ans + N1
                i = i + 1
            else:
                Ans = Ans + N2 -N1
                i = i + 2
        else:
            Ans = Ans + N1
            i = i + 1
    return Ans
