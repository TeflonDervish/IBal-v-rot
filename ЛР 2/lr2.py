import random
import string

def generate_password():
    
    q, p = 3, 0
    last = 12 - q - p
    
    russian_lowercase = "".join([chr(i) for i in range(ord('а'), ord('я') + 1)]) # 3 буквы
    russian_uppercase = "".join([chr(i) for i in range(ord('А'), ord('Я') + 1)]) # 0 буквы
    digits = string.digits
    

    all_characters = russian_lowercase + russian_uppercase + digits

    password = ''.join(random.choice(all_characters) for _ in range(3))
    password += ''.join(random.choice(all_characters) for _ in range(0))
    password += ''.join(random.choice(all_characters) for _ in range(9))

    return password


generated_password = generate_password()
print(generated_password)