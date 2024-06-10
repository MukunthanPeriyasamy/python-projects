alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_number):
    encode = ""
    for index in plain_text:
        if index in alphabet:
            position = alphabet.index(index)
            shift_number = shift_number % 26
            new_position = position + shift_number
            new_letter = alphabet[new_position]
            encode += new_letter
        else:
            encode+= index
    print(f"The encoded text is {encode}")


def decrypt(plain_text, shift_number):
    decode = ""
    for index in plain_text:
        if index in alphabet:
            position = alphabet.index(index)
            shift_number = shift_number % 26
            new_position = position - shift_number
            new_letter = alphabet[new_position]
            decode += new_letter
        else:
            decode += index
    print(f"The decoded text is {decode}")


if direction == "encode":
    encrypt(plain_text=text, shift_number=shift)
else:
    decrypt(plain_text=text, shift_number=shift)
