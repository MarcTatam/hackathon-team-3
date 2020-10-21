""" Hackathon - Level 2 """

def longest_word(string):
    split_string = input_string.split(" ")
    temp_max_value = 0
    temp_max_word = 0
    for word in split_string:
        if len(word) > temp_max_value:
            temp_max_word = word
            temp_max_value = len(word)
    return temp_max_word

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return lorem
    print(longest_word("lorem ipsum, dolor sit amet"))




