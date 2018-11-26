#!/usr/bin/env python

import yaml

with open("config/schemas-meta.yml", 'r') as stream:
    try:
        meta = yaml.load(stream) 
        print(meta)
    except yaml.YAMLError as exc:
        print(exc)

