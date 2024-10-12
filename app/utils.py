import random
import string
from requests import post
from os import getenv

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

def get_client_ip(request):
    # Try to get the client IP from CF-Connecting-IP header if you are using cloudflare proxy
    client_ip = request.headers.get('CF-Connecting-IP', None)
    
    # If CF-Connecting-IP is not present, fall back to X-Forwarded-For
    if client_ip is None:
        x_forwarded_for = request.headers.get('X-Forwarded-For', None)
        if x_forwarded_for is not None:
            # X-Forwarded-For can contain a comma-separated list of IPs; take the first one
            client_ip = x_forwarded_for.split(',')[0].strip()
    
    # If both headers are missing, use the default remote address
    if client_ip is None:
        client_ip = request.remote_addr
    
    return client_ip

def is_malicious(url):
    api_key = getenv("SAFE_BROWSING_TOKEN",default="Undefined")
    SAFE_BROWSING_URL = f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}'
    
    payload = {
        "client": {
            "clientId": "clickstat",
            "clientVersion": "1.5.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }

    response = post(SAFE_BROWSING_URL, json=payload)
    result = response.json()
    print(result,response.headers)

    if 'matches' in result:
        return True
    else:
        return False

