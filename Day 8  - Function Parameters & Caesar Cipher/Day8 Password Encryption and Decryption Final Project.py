import string 
from Day 8 Art Module import logo
print(logo)

# Get user input for the type of operation ('encode' or 'decode')
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# Get user input for the text to be processed
text = input("Type your message:\n").lower()

# Get user input for the shift amount
shift = int(input("Type the shift number:\n"))   

def ceaser(direction, text, shift):    

    #Encoding function
    def encryption(plain_text, shift_amount):
        alphabet = list(string.ascii_lowercase)
        
        coded_message = ""  
        for char in plain_text:
            position = alphabet.index(char)
            char = alphabet[(position + shift_amount) % 26]
            coded_message += char
        print(f"Your encripted message is {coded_message}")
    encryption(plain_text = text, shift_amount = shift)

    #Decoding function
    def decryption(cipher_text, shift_amount):    
        import string 
        alphabet = list(string.ascii_lowercase)

        decoded_message = ""
        for char in cipher_text:
            position = alphabet.index(char)
            char = alphabet[(position - shift) % 26]
            decoded_message += char
        print(f"Your decoded message is {decoded_message}")
    decryption(cipher_text = text, shift_amount = shift)

# Call the main ceaser function with user inputs
ceaser(direction = direction, text = text, shift = shift) 