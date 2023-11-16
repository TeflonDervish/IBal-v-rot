import random
import string

def generate_password(length=8):
    length = max(length, 6)
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits

    all_characters = lowercase_letters + uppercase_letters + digits

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password


generated_password = generate_password(2)
print(generated_password)