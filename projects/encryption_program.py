import string
import random

chars = list(" " + string.ascii_letters + string.digits + string.punctuation)
key = chars.copy()

def genrate_key():
    random.shuffle(key)

def encrypt(plain_text):
    cypher_text = ""
    for letter in plain_text:
        cypher_text += key[chars.index(letter)]
    print(f"Encrypted message: {cypher_text}")

def decrypt(cipher_text):
    plain_text = ""
    for letter in cipher_text:
        plain_text += chars[key.index(letter)]
    print(f"Decrypted message: {plain_text}")

def main():
    genrate_key()
    while True:
        print("1. Generate New Key")
        print("2. Encrypt")
        print("3. Decrypt")
        print("4. Exit")
        
        choice = int(input("Enter your choice (1-4): "))
        match choice:
            case 1:
                genrate_key()
            case 2:
                plain_text = input("Enter the text to encrypt: ")
                encrypt(plain_text)
            case 3:
                cipher_text = input("Enter the text to decrypt: ")
                decrypt(cipher_text)
            case 4:
                break
            case _:
                print("Invalid choice! Try again.")
                continue

    print("Thanks for using this program!")
    
if __name__ == "__main__":
    main()