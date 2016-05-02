#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import os
import time
import requests
from elasticsearch import Elasticsearch
import my_functions

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config = my_functions.read_yaml(BASE_DIR + '/config.ini')

ES = Elasticsearch([
    {'host': config['data_store']['es_server']}
])

headers = {'User-Agent': config['flightradar24']['user_agent']}

if config['flightradar24']['service']=='by_code':
    flights_endpoint = str(config['flightradar24']['endpoint_live'] + '?airline=!' +
                           config['flightradar24']['airline_live_data']) + '&_' + \
                       str(int(time.mktime(time.localtime())*1000))
    flights_endpoint = flights_endpoint.rstrip()
    flights_request = requests.get(flights_endpoint, headers=headers)
else:

    balancer_request = requests.get(config['flightradar24']['balancer_config'], headers=headers)
    balancer_url = list(balancer_request.json().keys())[0]
    flights_endpoint = str('https://' + balancer_url + config['flightradar24']['endpoint'] + '&bounds=' +
                           config['flightradar24']['bounds']['world'])
    flights_endpoint = flights_endpoint.rstrip()
    flights_request = requests.get(flights_endpoint, headers=headers)
try:
    flights_data = flights_request.json()

    for key, flight in flights_data.items():
        if key == 'stats':
            continue
        if type(flight) is list:
            if config['flightradar24']['airline'] == 'ALL':
                my_functions.store_flight(config, ES, flight)
            else:
                if config['flightradar24']['airline'] in flight[13]:
                    my_functions.store_flight(config, ES, flight)
except:
    print("Oops, response is not json")
