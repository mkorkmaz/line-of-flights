# -*- coding: utf-8 -*-

# author: mehmet@mkorkmaz.com

import yaml


def dict_isset_or(obj, indice, default_value):

    if indice in obj:
        return obj[indice]
    else:
        obj[indice] = default_value
        return obj[indice]


def read_yaml(file_name):
    with open(file_name, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(file_name)
            print("Configuration file error! Exiting...")
            exit()


def store_flight(config, es, flight):
    flight_data = dict()
    flight_data['aircraft_id'] = str(flight[0])
    flight_data['iata_identity'] = str(flight[13])
    flight_data['icao_identity'] = str(flight[16])
    flight_data['latitude'] = float(flight[1])
    flight_data['longitude'] = float(flight[2])
    flight_data['angle'] = int(flight[3])
    flight_data['altitude'] = int(flight[4])
    flight_data['speed'] = int(flight[5])
    flight_data['squawk_code'] = str(flight[6])
    flight_data['radar_id'] = str(flight[7])
    flight_data['aircraft'] = str(flight[8])
    flight_data['registration'] = str(flight[9])
    flight_data['last_update'] = int(flight[10])
    flight_data['departure'] = str(flight[11])
    flight_data['arrival'] = str(flight[12])
    flight_data['arrived'] = int(flight[14])
    flight_data['vspeed'] = int(flight[15])
    flight_data['reserved'] = str(flight[17])

    es.index(index=config['data_store']['index'], doc_type=config['data_store']['type'], body=flight_data)