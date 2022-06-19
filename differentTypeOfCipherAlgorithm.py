# Transposition Cipher
import pyperclip


def main():
    myMessage = 'Transposition Cipher'
    myKey = 10
    ciphertext = encryptMessage(myKey, myMessage)

    print("Cipher Text is")
    print(ciphertext + '|')
    pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key
    return ''.join(ciphertext)


if __name__ == '__main__':
    main()

# Substitution Cipher
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'
plaintext = "Hey, this is really fun!"


def makeKey(alphabet):
    alphabet = list(alphabet)
    random.shuffle(alphabet)
    return ''.join(alphabet)


def encrypt(plaintext, key, alphabet):
    keyMap = dict(zip(alphabet, key))
    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)


def decrypt(cipher, key, alphabet):
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(), c) for c in cipher)


cipher = encrypt(plaintext, key, alphabet)

print(plaintext)
print(cipher)
print(decrypt(cipher, key, alphabet))


#Monoalphabetic cipher
key_dict = {
    'a': 'm',
    'b': 'n',
    'c': 'b',
    'd': 'v',
    'e': 'c',
    'f': 'x',
    'g': 'z',
    'h': 'a',
    'i': 's',
    'j': 'd',
    'k': 'f',
    'l': 'g',
    'm': 'h',
    'n': 'j',
    'o': 'k',
    'p': 'l',
    'q': 'p',
    'r': 'o',
    's': 'i',
    't': 'u',
    'u': 'y',
    'v': 't',
    'w': 'r',
    'x': 'e',
    'y': 'w',
    'z': 'q',
    ' ': ' ',
}


def get_key(value):
    for key, val in key_dict.items():
        if (val == value):
            return key


def monoalphabetic_encrypt(word):
    c = ''
    for i in word:
        i = key_dict[i]
        c += i
    return c


def monoalphabetic_decrypt(word):
    c = ''
    for i in word:
        i = get_key(i)
        c += i
    return c


encryptText = monoalphabetic_encrypt("monoalphabetic cipher")
print(encryptText)
print(monoalphabetic_decrypt(encryptText))