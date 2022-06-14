#encrypt cypher text
def cipher_encrypt(plain_text, key):
    encrypted = ""
    for c in plain_text:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + key) % 26 + ord('A')
            encrypted += chr(c_shifted)

        elif c.islower():
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            encrypted += chr(c_shifted)

        elif c.isdigit():
            encrypted += str((int(c) + key) % 10)

        else:
            encrypted += c

    return encrypted


#Brute force to decrypt cypher text
def cipher_decrypt_lower(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og

        elif c.isupper():
            c_index = ord(c) - ord('A')
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og

        elif c.isdigit():
            decrypted += str((int(c) - key) % 10)

        else:
            decrypted += c

    return decrypted


plain_text = "mate, the adventure ride in canberra was so much fun, we were so drunk we ended up calling"
ciphertext = cipher_encrypt(plain_text, 4)
print("Plain text message:\n", plain_text)
print("Encrypted ciphertext:\n", ciphertext)
for i in range(0, 26):
    plain_text = cipher_decrypt_lower(ciphertext, i)
    print("For key {}, decrypted text: {}".format(i, plain_text))


#breaking a substitution cipher
print(ciphertext)
stored_letters = {}

for char in ciphertext:
    if char not in stored_letters:
        stored_letters[char] = 1
    else:
        stored_letters[char] += 1

print(stored_letters)
attempt = ciphertext.replace("e", "A")
attempt = attempt.replace("i", "E")
attempt = attempt.replace("a", "W")
attempt = attempt.replace("v", "R")
attempt = attempt.replace("r", "N")
attempt = attempt.replace("m", "I")
attempt = attempt.replace("s", "O")
attempt = attempt.replace("w", "S")
attempt = attempt.replace("h", "D")
attempt = attempt.replace("y", "U")
attempt = attempt.replace("o", "K")
attempt = attempt.replace("t", "P")
attempt = attempt.replace("z", "V")
attempt = attempt.replace("x", "T")
attempt = attempt.replace("q", "M")
attempt = attempt.replace("l", "H")
attempt = attempt.replace("g", "C")
attempt = attempt.replace("j", "F")
attempt = attempt.replace("p", "L")
attempt = attempt.replace("k", "G")
attempt = attempt.replace("f", "B")
print(attempt)