def caesar_cipher(cipher_text:str, key: int)->str:
    true_key = key % 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext_list = []
    for character in cipher_text:
        if character == " ":
            plaintext_list.append(character)
        else:
            plaintext_list.append(alphabet[(alphabet.find(character) + true_key)% 26])
    return "".join(plaintext_list)