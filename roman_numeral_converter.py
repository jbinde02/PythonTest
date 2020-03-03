def roman_numeral_to_decimal():
    # Dictionary that contains the values of each Roman Numeral to 1000
    roman_numeral_dict = {'I': 1, 'IV': 4, 'V': 5,
                          'IX': 9, 'X': 10, 'XL': 40,
                          'L': 50, 'XC': 90, 'C': 100,
                          'CD': 400, 'D': 500, 'CM': 900,
                          'M': 1000}
    output = 0
    input_string = str(input("Input Roman Numeral... \n"))

    # Capitalizes the input
    if not input_string.isupper():
        input_string = input_string.upper()
        print(input_string)

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

    print(input_list)

    # Looks at each value in the input list, puts the key in the dictionary, and adds the value to the output.
    for c in input_list:
        output = output + roman_numeral_dict.get(c)
    print(output)


roman_numeral_to_decimal()
