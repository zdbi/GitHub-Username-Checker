import requests

with open('wordlist.txt', 'r') as f:
    words = [line.strip() for line in f]

for word in words:
    response = requests.get(f'https://github.com/{word}')
    if response.status_code == 200:
        print(f'\033[31m{word} is taken\033[0m')
    else:
        print(f'\033[32m{word} is available\033[0m')