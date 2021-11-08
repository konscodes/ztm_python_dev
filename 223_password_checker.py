from sys import argv
import requests
import hashlib

hash_list = []

def get_hash(password):
    global hash_list
    password = password.encode('utf-8')
    print(type(password))
    hash = hashlib.sha1(password).hexdigest()
    hash_list.append(hash.upper())


def query(hash):
    query = requests.get('https://api.pwnedpasswords.com/range/' + hash[:5])
    print(query.status_code)
    text = query.text.split()
    data = {}
    for item in text:
        key, value = item.split(sep=':')
        data[key] = value
    return data


for password in argv[1:]:
    get_hash(password)

for hash in hash_list:
    data = query(hash)
    print(data)
