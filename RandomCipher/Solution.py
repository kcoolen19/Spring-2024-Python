import random
# An outline for problem two is given here:
# Given the english alphabet and the random module let us create a random encryption/decryption scheme
chr(97) # 97 is the char equivalent of 'a'
alphabet = []

# TODO: Create a list of lower case alphabet characters, and store this in alphabet. Recall chr(97) returns a, chr(98) returns b,.....
alphabet = [chr(i) for i in range(97,123)]

# TODO: Copy the list above (use list.copy()) and shuffle the contents to create a mapping of letters to ciphertext
ciphertext = alphabet.copy()
random.shuffle(ciphertext)

#TODO: Create a list of tuples in mapping below, where the first tuple element is the letter in the alphabet, and the second tuple element
# is the associated shuffled character
mapping = []
for i in range(len(alphabet)):
    mapping.append((alphabet[i], ciphertext[i]))

# Create a Decryption Dictionary for decoding using the second tuple element as a key, and the value as the first tuple
decryption_dict = {}
for i in range(len(ciphertext)):
    decryption_dict[ciphertext[i]] = alphabet[i]

msg = "i want to say something secret"

# Encrypt the message
cipher = ''
for character in msg:
    encrypted_char = character
    for tuple_pair in mapping:
        if character == tuple_pair[0]:
            encrypted_char = tuple_pair[1]
    cipher += encrypted_char


# Decrypt the message
decrypted_msg = ''
for character in cipher:
    if character in decryption_dict:
      decrypted_msg += decryption_dict[character]
    else:
      decrypted_msg += character


print("Encrypted message is:", cipher)
print("Decrypted message is:", decrypted_msg)
