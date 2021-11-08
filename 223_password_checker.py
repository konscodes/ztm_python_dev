from sys import argv
import requests
import hashlib

hash_list = []
for password in argv[1:]:
    password = password.encode('utf-8')
    print(type(password))
    hash = hashlib.sha1(password).hexdigest()
    hash_list.append(hash.upper())

print(hash_list)

for given_hash in hash_list:
    query = requests.get('https://api.pwnedpasswords.com/range/' + given_hash[:5])
    print(query.status_code)
    data_list = query.text.split()
    data_dict = {}
    for item in data_list:
        key, value = item.split(sep=':')
        data_dict[key] = value

    print(data_dict)