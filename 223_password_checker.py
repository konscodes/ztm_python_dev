from sys import argv
import requests
import hashlib

hash_list = []

def get_hash(password):
    global hash_list
    password = password.encode('utf-8')
    hash = hashlib.sha1(password).hexdigest()
    hash_list.append(hash.upper())


def query(hash):
    query = requests.get('https://api.pwnedpasswords.com/range/' + hash[:5])
    if query.status_code != 200:
        raise RuntimeError(f'Error fetching: {query.status_code}')
    text = query.text.split()
    data = {}
    for item in text:
        key, value = item.split(sep=':')
        data[key] = value
    return data


def main(args):
    global hash_list
    if len(args) == 0:
        raise RuntimeError('No password provided?')
    
    for password in args:
        get_hash(password)

    for hash in hash_list:
        data = query(hash)
        match = data.get(hash[5:])
        if match is not None:
            print(f'Match found: {match} times')
        else: print(match)


main(argv[1:])