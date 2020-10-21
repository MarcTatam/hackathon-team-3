def most_characters(input_string: str)->str:
    split_string = input_string.split(" ")
    temp_max_value = 0
    temp_max_word = 0
    for word in split_string:
        if len(word) > temp_max_value:
            temp_max_word = word
            temp_max_value = len(word)
    return temp_max_word



