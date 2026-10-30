# Caesar Cipher: Encryption and Decryption

# Message ko encrypt karne ka function
def encrypt(message, key):
    result = ""

    # Message ke har character ko check karo
    for ch in message:

        # Check karo ki character alphabet hai ya nahi
        if ch.isalpha():

            # Uppercase ke liye A aur lowercase ke liye a base hoga
            base = ord('A') if ch.isupper() else ord('a')

            # Letter ko key ke according aage shift karo
            # % 26 se Z ke baad dobara A se start hoga
            new_char = chr((ord(ch) - base + key) % 26 + base)

            # Naya character result mein add karo
            result += new_char

        else:
            # Space, number aur symbols ko same rakho
            result += ch-
    return result


# Message ko decrypt karne ka function
def decrypt(message, key):

    # Original message pane ke liye letters ko peeche shift karo
    return encrypt(message, -key)


# Program ka title print karo
print("Caesar Cipher Encryption and Decryption")

# User se message input lo
message = input("Enter your message: ")

# User se shift key input lo
key = int(input("Enter shift key (0-25): "))

# Message ko encrypt karo
encrypted = encrypt(message, key)

# Encrypted message ko decrypt karo
decrypted = decrypt(encrypted, key)

# Original, encrypted aur decrypted messages display karo
print("\nOriginal Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
