import requests

import logic
import engine
import queries

logic.many_logins_2(login_generator=engine.simple_logins,
                password_generator=engine.popular_password,
                query=queries.request_local)

