alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        curLetter = alphabet.index(letter)
        encrypted_text +=alphabet[curLetter + shift_amount]

    return encrypted_text

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        currentLetter = alphabet.index(letter)
        decrypted_text += alphabet[currentLetter - shift_amount]

    return decrypted_text

def caesar(direction, text, shift):
    
    if direction == "encode":
        return encrypt(text, shift)
    elif direction == "decode":
        return decrypt(text, shift)
    else:
        return "Invalid direction"
    

# Loop until the user decides to quit
while True:
    direction = input("\nType 'encode' to encrypt, 'decode' to decrypt, or 'q' to quit: ").lower()
    if direction == 'q':
        print("Goodbye!")
        break

    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    shift = shift % 26  # Normalize shift
    
    result = caesar(direction, text, shift)
    print(f"Result: {result}")