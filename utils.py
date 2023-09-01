import random
import string

def generate_identifier(length=6):
    characters = string.ascii_letters
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def parse_and_format(results):
    click_data = []
    for record in results:
        ip = record[0]
        user_agent = record[1]
        latitude = record[2]
        longitude = record[3]
        timestamp = record[4]
        record = {"ip":ip, "user_agent":user_agent,"latitude":latitude,"longitude":longitude,"timestamp":timestamp}
        click_data.append(record)
    return click_data
