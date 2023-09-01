import random
import string

def generate_identifier(length=6):
    characters = string.ascii_letters
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

if __name__ == "__main__":
    random_string = generate_identifier()
    print(random_string)

