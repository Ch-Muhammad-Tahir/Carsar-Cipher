

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']



direction = input("Type a 'encode' to encrypt, type 'decode' to decrypt:\n ")
text = input("Type Your Message:\n").lower()
sift = int(input("Type Your Shift:\n"))
sift =sift % 26
def encrypt(plain_text, shift_amount):
    cipher_text=""
    for letter in plain_text:
        position =alphabet.index(letter)
        new_position = position+shift_amount
        new_letter =alphabet[new_position]
        cipher_text+=new_letter

    print(f"The encoded text is: {cipher_text}")

def decrypt(cipher_text,cipher_siftAmount):
    decrypt_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - cipher_siftAmount
        new_letter = alphabet[new_position]
        decrypt_text += new_letter

    print(f"The Decode text is: {decrypt_text}")

if direction =='encode':
    encrypt(shift_amount=sift,plain_text=text)
elif direction=="decode":
    decrypt(cipher_text=text,cipher_siftAmount=sift)
else:
    print("Invalid Direction")