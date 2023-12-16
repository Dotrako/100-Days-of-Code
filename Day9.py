direction = input("Please choose 'decode' to encrypt the code or 'encode' to crypt the code").lower
text = input("Please enter the message you wanna encrypt").lower()
shift = int(input("please enter the shift number of your letters"))   


# ceaser cipher program
def encryption(plain_text, shift_amount):
    import string 
    alphabet = list(string.ascii_lowercase)
    
    coded_message = ""  
    for char in plain_text:
        position = alphabet.index(char)
        char = alphabet[(position + shift_amount) % 26]
        coded_message += char
    print(f"The encripted message is {coded_message}")
encryption(plain_text = text, shift_amount = shift)


#caepher decoded program
def decryption(cipher_text, shift):    
    import string 
    alphabet = list(string.ascii_lowercase)

    decoded_message = ""
    for char in message2:
        position = alphabet.index(char)
        char = alphabet[(position - shift)%26]
        decoded_message += char
    print(f"The decodede message is {decoded_message}")
decryption(cipher_text = text, shift_amount = shift)

if direction == "encode":
    encryption(plain_text = text, shift_amount = shift)
elif direction == "decode":
    decryption(cipher_text = text, shift_amount = shift)