# utf-8
# Домашка по day 01
# Сделать list из пяти сайтов
# обратиться к каждому в цикле не менее 100 раз

import requests
import time

sites = [
    'https://google.com',
    'https://yandex.ru',
    'https://mail.ru',
    'https://yahoo.com',
    'https://msn.com'
]

count = 100

for site in sites:
    result = {}
    times = {}
    for i in range(count):
        start_time = time.time()
        r = requests.get(site)
        delta_time = time.time() - start_time
        result[r.status_code] = result.setdefault(r.status_code, 0) + 1
        times[r.status_code] = times.setdefault(r.status_code, 0) + delta_time
    print(site, result, times)
