#!/usr/bin/python
# -*- coding: <encoding name> -*-

import requests
import json
from time import sleep as sleep

with open('grls.json', 'a', encoding='utf-8') as grls:
    try:
        url = "https://api.pharm-portal.ru/api/grls?perPage=500&page=1"
        next_page = requests.get(url).json()['next_page_url']
        last_page = requests.get(url).json()['last_page_url']
        grls.write('{\n')
    
        while next_page != 'None':
            if int(requests.get(next_page).headers['X-RateLimit-Remaining']) <= 1:
                requests.get(url)
                print('sleep')
                sleep(int(requests.get(next_page).headers['Retry-After']) + 2)
            url = next_page
            next_page = json.loads(requests.get(url).text)['next_page_url']
            data = json.loads(requests.get(url).text)['data']
            grls.write(data)
        grls.write('\n}')
    except KeyError:
        print(json.loads(requests.get(url).content), *requests.get(url).headers,\
              requests.get(next_page).headers['X-RateLimit-Remaining'], sep='\n')
