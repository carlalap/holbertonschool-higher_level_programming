#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    result = 0
    previous_value = 0

    for num in roman_string:
        curr_value = roman_values.get(num, 0)

        if curr_value > previous_value:
            result += curr_value - 2 * previous_value
        else:
            result += curr_value
        previous_value = curr_value
    return result
