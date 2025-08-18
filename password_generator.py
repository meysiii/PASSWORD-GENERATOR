import random
import string

def generate_password(length=12):
    if length < 4:
        return "Length too short!"

    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Ensure password has at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 3)

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

# Example usage
length = int(input("Enter desired password length: "))
print("Generated Password:", generate_password(length))
