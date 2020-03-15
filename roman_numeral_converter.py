def roman_numeral_to_decimal(input_string):
    # Dictionary that contains the values of each Roman Numeral to 1000
    roman_numeral_dict = {'I': 1, 'IV': 4, 'V': 5,
                          'IX': 9, 'X': 10, 'XL': 40,
                          'L': 50, 'XC': 90, 'C': 100,
                          'CD': 400, 'D': 500, 'CM': 900,
                          'M': 1000}
    output = 0

    # Capitalizes the input
    if not input_string.isupper():
        input_string = input_string.upper()

    # Turns input into list
    input_list = list(input_string)

    # Enumerates the list. If there is a element in front of the current character and has a greater value than the
    # current character, combine the two and place the new string in the current index. Removes the old two elements
    # which are in front.
    for index, c in enumerate(input_list):
        if index + 1 < len(input_list) \
                and roman_numeral_dict.get(input_list[index]) < roman_numeral_dict.get(input_list[index + 1]):
            input_list.insert(index, input_list[index] + input_list[index + 1])
            input_list.remove(input_list[index + 1])
            input_list.remove(input_list[index + 1])

    # Looks at each value in the input list, puts the key in the dictionary, and adds the value to the output.
    for c in input_list:
        output = output + roman_numeral_dict.get(c)
    return output


def decimal_to_roman_numeral(input_int):
    output = ""

    # Looks at the input which is a int. Divides it by each Roman Numerals respected value. If the Roman Numerals value
    # can go into the input once or more, it will execute the if statement. The if statement will do a floor division
    # using the Roman Numeral value. The result will determine how many of the Roman Numeral to add to the output.
    # It will then modify the input, taking away what was added and then continue down the ifs until done.
    if input_int / 1000 >= 1:
        times = input_int // 1000
        input_int -= 1000 * times
        output += 'M' * times

    if input_int / 900 >= 1:
        times = input_int // 900
        input_int -= 900 * times
        output += 'CM' * times

    if input_int / 500 >= 1:
        times = input_int // 500
        input_int -= 500 * times
        output += 'D' * times

    if input_int / 400 >= 1:
        times = input_int // 400
        input_int -= 400 * times
        output += 'CD' * times

    if input_int / 100 >= 1:
        times = input_int // 100
        input_int -= 100 * times
        output += 'C' * times

    if input_int / 90 >= 1:
        times = input_int // 90
        input_int -= 90 * times
        output += 'XC' * times

    if input_int / 50 >= 1:
        times = input_int // 50
        input_int -= 50 * times
        output += 'L' * times

    if input_int / 40 >= 1:
        times = input_int // 40
        input_int -= 40 * times
        output += 'XL' * times

    if input_int / 10 >= 1:
        times = input_int // 10
        input_int -= 10 * times
        output += 'X' * times

    if input_int / 9 >= 1:
        times = input_int // 9
        input_int -= 9 * times
        output += 'IX' * times

    if input_int / 5 >= 1:
        times = input_int // 5
        input_int -= 5 * times
        output += 'V' * times

    if input_int / 4 >= 1:
        times = input_int // 4
        input_int -= 4 * times
        output += 'IV' * times

    if input_int / 1 >= 1:
        times = input_int // 1
        input_int -= 1 * times
        output += 'I' * times

    return output
