
def one_login(login_generator, password_generator, query):
    login, next_login_state = login_generator()
    next_password_state = None
    while True:
        password, next_password_state = password_generator(next_password_state)
        if query(login, password):
            print('OK', login, password)
            break
        if next_password_state is None:
            break


def many_logins(
        login_generator,
        password_generator,
        query):

    complete = []

    next_password_state = None

    while True:

        password, next_password_state = password_generator(next_password_state)
        next_login_state = None

        while True:
            login, next_login_state = login_generator(next_login_state)
            if login not in complete and query(login, password):
                print('OK', login, password)
                complete.append(login)
                break
            if next_login_state is None:
                break

        if next_password_state is None:
            break

def many_logins_2(
        login_generator,
        password_generator,
        query):

    password_limit = 10000
    next_login_state = None

    while True:

        login, next_login_state = login_generator(next_login_state)
        next_password_state = None

        for i in range(password_limit):
            password, next_password_state = password_generator(next_password_state)
            if query(login, password):
                print('OK', login, password)
                break
            if next_password_state is None:
                break

        if next_login_state is None:
            break

