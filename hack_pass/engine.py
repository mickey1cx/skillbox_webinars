import requests

f_pass = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials'
                      '/10-million-password-list-top-1000000.txt')
passwords = f_pass.text.split()

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
digits = len(alphabet)
last_sym = alphabet[-1]

logins = ['admin', 'jack', 'cat']


def popular_password(state=None):

    if state is None:
        state = 0

    if state >= len(passwords) - 1:
        next_state = None
    else:
        next_state = state + 1
    return passwords[state], next_state


def simple_logins(state=None):

    if state is None:
        state = 0

    if state >= len(logins) - 1:
        next_state = None
    else:
        next_state = state + 1

    return logins[state], next_state


def dec_to_pass(num):

    password = ''
    temp = num
    while temp:
        c = temp // digits
        r = temp % digits
        password += alphabet[r]
        temp = c
    return password[::-1]


def brute_force(state=None):

    if state is None:
        state = 0, 0

    step, length = state

    password = dec_to_pass(step)
    if len(password) < length:
        password = '0' * (length - len(password)) + password

    if password.count(last_sym) == length:
        length += 1
        step = 0
    else:
        step += 1

    next_state = step, length

    return password, next_state