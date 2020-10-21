    """ Hackathon - Level 6 """

def cipher(string, x):
    true_key = key % 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext_list = []
    for character in cipher_text:
        if character == " ":
            plaintext_list.append(character)
        else:
            plaintext_list.append(alphabet[(alphabet.find(character) + true_key)% 26])
    return "".join(plaintext_list)

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return salve
    print(cipher('pxisb', 3))