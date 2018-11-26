#!/usr/bin/env python

import yaml

with open("config/schemas-meta.yml", 'r') as stream:
    try:
        schemas = yaml.load(stream) 
        print(schemas)
        for schema in schemas:
            print(schema['name'])
            print(schema['version'])
            print(schema['description'])
            for attr in schema['attributes'].keys():
                print(' ', attr)
                print(' ', schema['attributes'][attr]['required'])
    except yaml.YAMLError as exc:
        print(exc)

