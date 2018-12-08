#!/usr/bin/env python

import yaml
import argparse
import os.path
import os
import sys
import datetime
import pytz
import json


# get name of input file from args

# get a free-form line of text
def get_text(prompt='-->', required=False):
    ret = ''
    while True:
        ret = input(prompt)
        if 0 < len(ret) or not required:
            return ret
    return ret

# get a selection from a list (with default)
def get_option(list, prompt='-->', default=None, required=False, list_style=True):
    iret = -1
    while True:
        items = ''
        for i in range(len(list)):
            if default and default == i+1:
                token = '*'
            else:
                if list_style:
                    token = ' '
                else:
                    token = ''
            if list_style:
                print(token, i+1, list[i])
            else:
                if i > 0:
                    items = items + '/'
                items = items + token + list[i]
        if not list_style:
            prompt = prompt.format(items)
        ret = input(prompt)
        if 0 == len(ret) and default:
            return list[default-1]
        if list_style:
            try:
                iret = int(ret)
            except:
                pass
            if iret < 1 or iret > 1+len(list):
                iret = -1
            else:
                return list[iret-1]
        else:
            if 0 < list.count(ret):
                return ret
    return list[iret-1]

def path_to_name(schema_path):
    return schema_path.replace('/', '')

def now_date():
    tz_aware = timezone.localize(datetime.datetime.now())
    return tz_aware.astimezone(pytz.utc).isoformat()

# ui_name, ui_address, ui_text, ui_date, ui_select, helper_uuid, helper_now_iso, helper_value
def sample_data(attr_name, data_type):
    if data_type == 'ui_name':
        return 'Name'
    elif data_type == 'ui_address':
        return 'Address'
    elif data_type == 'ui_text':
        return 'Text'
    elif data_type == 'ui_date':
        return now_date()
    elif data_type == 'ui_select':
        return 'Select'
    elif data_type == 'helper_uuid':
        return 'UUID'
    elif data_type == 'helper_now_iso':
        return now_date()
    elif data_type == 'helper_value':
        return 'Value'
    else:
        return 'Unknown type'

#Using a custom Dumper class to prevent changing the global state
class CustomDumper(yaml.Dumper):
    #Super neat hack to preserve the mapping key order. See https://stackoverflow.com/a/52621703/1497385
    def represent_dict_preserve_order(self, data):
        return self.represent_dict(data.items())    

CustomDumper.add_representer(dict, CustomDumper.represent_dict_preserve_order)

if 2 > len(sys.argv):
    print("usage:", sys.argv[0], "<input file>")
    sys.exit()

# for now, we are in PST time
timezone = pytz.timezone("America/Los_Angeles")

in_file = sys.argv[1]
in_dir = os.path.dirname(in_file)
out_services = in_dir + '/gen-services.yml'
out_routes = in_dir + '/gen-routes.yml'
out_data = in_dir + '/gen-data.json'

with open(in_file, 'r') as stream:
    try:
        schemas = yaml.load(stream) 
        #for schema in schemas:
        #    ok = 'N'
        #    while ok == 'N':
        #        print('Schema:', schema['name'], schema['version'])
        #        schema['description'] = get_text('  Enter Schema Description: ', True)
        #        schema['proof_request'] = get_text('  Enter Proof Request: ', False)
        #        for attr in schema['attributes'].keys():
        #            print('Enter values for', attr, schema['attributes'][attr]['required'])
        #            schema['attributes'][attr]['mapping'] = get_option(['name', 'address', 'attribute - text', 'attribute - datetime', 'value'], '  Select ' + attr + ' DATA type: ', 3, True, True)
        #            schema['attributes'][attr]['ui_type'] = get_option(['address', 'text', 'date', 'select', 'helper', 'value'], '  Select ' + attr + ' UI type: ', 2, True, True)
        #        print(schema)
        #        ok = get_option(['Y', 'N'], "Continue [{}]?", 1, True, False)
        #    y_schema = yaml.dump(schema, default_flow_style=False, Dumper=CustomDumper)
        #    print(y_schema)

        services = {}
        services['issuers'] = {}
        services['issuers']['myorg'] = {}
        services['issuers']['myorg']['credential_types'] = []
        routes = {}
        routes['forms'] = {}
        testdata = []
        for schema in schemas:
            # generate schema-level stuff for services.yml
            service = {}
            service['description'] = schema['description']
            service['schema'] = schema['name']
            service['issuer_url'] = schema['endpoint'] + schema['path']
            if 'proof_request' in schema:
                service['depends_on'] = []
                service['depends_on'].append(schema['proof_request'])
            if 'effective_date' in schema or 'revoked_date' in schema:
                service['credential'] = {}
                if 'effective_date' in schema:
                    service['credential']['effective_date'] = {}
                    service['credential']['effective_date']['input'] = schema['effective_date']
                    service['credential']['effective_date']['from'] = 'claim'
                if 'revoked_date' in schema:
                    service['credential']['revoked_date'] = {}
                    service['credential']['revoked_date']['input'] = schema['revoked_date']
                    service['credential']['revoked_date']['from'] = 'claim'
            service['topic'] = {}
            service['topic']['source_id'] = {}
            service['topic']['source_id']['input'] = schema['topic']
            service['topic']['source_id']['from'] = 'claim'
            service['topic']['type'] = {}
            service['topic']['type']['input'] = 'registration'
            service['topic']['type']['from'] = 'value'
            if 'cardinality' in schema:
                service['cardinality_fields'] = []
                service['cardinality_fields'].append(schema['cardinality'])

            # todo generate attribute-level stuff for services.yml
            service['mapping'] = []
            has_name = False
            has_address = False
            for attr in schema['attributes'].keys():
                model = {}
                if schema['attributes'][attr]['data_type'] == 'ui_name':
                    if not has_name:
                        model['model'] = 'name'
                        model['fields'] = {}
                        model['fields']['text'] = {}
                        model['fields']['text']['input'] = attr
                        model['fields']['text']['from'] = 'claim'
                        model['fields']['type'] = {}
                        model['fields']['type']['input'] = attr
                        model['fields']['type']['from'] = 'value'
                        service['mapping'].append(model)
                        has_name = True
                elif schema['attributes'][attr]['data_type'] == 'ui_address':
                    if not has_address:
                        model['model'] = 'address'
                        model['fields'] = {}
                        model['fields']['addressee'] = {}
                        model['fields']['addressee']['input'] = 'addressee'
                        model['fields']['addressee']['from'] = 'claim'
                        model['fields']['civic_address'] = {}
                        model['fields']['civic_address']['input'] = 'address_line_1'
                        model['fields']['civic_address']['from'] = 'claim'
                        model['fields']['city'] = {}
                        model['fields']['city']['input'] = 'city'
                        model['fields']['city']['from'] = 'claim'
                        model['fields']['province'] = {}
                        model['fields']['province']['input'] = 'province'
                        model['fields']['province']['from'] = 'claim'
                        model['fields']['postal_code'] = {}
                        model['fields']['postal_code']['input'] = 'postal_code'
                        model['fields']['postal_code']['from'] = 'claim'
                        model['fields']['country'] = {}
                        model['fields']['country']['input'] = 'country'
                        model['fields']['country']['from'] = 'claim'
                        service['mapping'].append(model)
                        has_address = True
                else:
                    model['model'] = 'attribute'
                    model['fields'] = {}
                    model['fields']['type'] = {}
                    model['fields']['type']['input'] = attr
                    model['fields']['type']['from'] = 'value'
                    if schema['attributes'][attr]['data_type'] == 'ui_date' or schema['attributes'][attr]['data_type'] == 'helper_now_iso':
                        model['fields']['format'] = {}
                        model['fields']['format']['input'] = 'datetime'
                        model['fields']['format']['from'] = 'value'
                    model['fields']['value'] = {}
                    model['fields']['value']['input'] = attr
                    model['fields']['value']['from'] = 'claim'
                    service['mapping'].append(model)

            services['issuers']['myorg']['credential_types'].append(service)

            # generate schema-level stuff for routes.yml
            form_name = path_to_name(schema['path'])
            routes['forms'][form_name] = {}
            routes['forms'][form_name]['path'] = schema['path']
            routes['forms'][form_name]['type'] = 'issue-credential'
            routes['forms'][form_name]['schema_name'] = schema['name']
            routes['forms'][form_name]['page_title'] = 'Title for ' + schema['name']
            routes['forms'][form_name]['title'] = 'Title for ' + schema['name']
            routes['forms'][form_name]['template'] = 'bcgov.index.html'
            routes['forms'][form_name]['description'] = schema['description']
            routes['forms'][form_name]['explanation'] = 'Use the form below to issue a Credential.'
            if 'proof_request' in schema:
                routes['forms'][form_name]['proof_request'] = {}
                routes['forms'][form_name]['proof_request']['id'] = schema['proof_request']
                routes['forms'][form_name]['proof_request']['connection_id'] = 'bctob'
            # optionally can serve javascript
            #js_includes:
            #  - src: js/bc_registries.js

            # generate attribute-level stuff for routes.yml
            routes['forms'][form_name]['fields'] = []
            has_address = False
            for attr in schema['attributes'].keys():
                if schema['attributes'][attr]['data_type'].startswith('ui_'):
                    field = {}
                    field['name'] = attr
                    field['label'] = attr
                    if schema['attributes'][attr]['data_type'] == 'ui_name':
                        field['type'] = 'text'
                    elif schema['attributes'][attr]['data_type'] == 'ui_address':
                        field['label'] = 'Mailing Address'
                        field['type'] = 'address'
                    elif schema['attributes'][attr]['data_type'] == 'ui_text':
                        field['type'] = 'text'
                    elif schema['attributes'][attr]['data_type'] == 'ui_date':
                        field['type'] = 'date'
                    elif schema['attributes'][attr]['data_type'] == 'ui_select':
                        field['type'] = 'select'
                        field['options'] = []
                        field['options'].append('todo-1')
                        field['options'].append('todo-2')
                        field['options'].append('todo-3')
                    else:
                        field['type'] = schema['attributes'][attr]['data_type']
                    field['required'] = schema['attributes'][attr]['required']
                    if schema['attributes'][attr]['data_type'] == 'ui_address' and not has_address:
                        routes['forms'][form_name]['fields'].append(field)
                        has_address = True
                    elif schema['attributes'][attr]['data_type'] != 'ui_address':
                        routes['forms'][form_name]['fields'].append(field)

            routes['forms'][form_name]['mappings'] = {}
            routes['forms'][form_name]['mappings']['attributes'] = []
            for attr in schema['attributes'].keys():
                if schema['attributes'][attr]['data_type'].startswith('helper_'):
                    attribute = {}
                    attribute['name'] = attr
                    if schema['attributes'][attr]['data_type'] == 'helper_value':
                        attribute['from'] = 'literal'
                        attribute['source'] = 'SomeValue'
                    else:
                        attribute['from'] = 'helper'
                        if schema['attributes'][attr]['data_type'] == 'helper_uuid':
                            attribute['source'] = 'uuid'
                        elif schema['attributes'][attr]['data_type'] == 'helper_now_iso':
                            attribute['source'] = 'now_iso'
                        else:
                            attribute['source'] = schema['attributes'][attr]['data_type']
                    routes['forms'][form_name]['mappings']['attributes'].append(attribute)

            datapacket = {}
            datapacket['schema'] = schema['name']
            datapacket['version'] = schema['version']
            datapacket['attributes'] = {}
            for attr in schema['attributes'].keys():
                datapacket['attributes'][attr] = sample_data(attr, schema['attributes'][attr]['data_type'])
            testdata.append(datapacket)

        #y_schemas = yaml.dump(schemas, default_flow_style=False, Dumper=CustomDumper)
        #print(y_schemas)

        #y_services = yaml.dump(services, default_flow_style=False, Dumper=CustomDumper)
        #print(y_services)
        print('Writing', out_services)
        with open(out_services, 'w') as outfile:
            yaml.dump(services, outfile, default_flow_style=False, Dumper=CustomDumper)
        
        #y_routes = yaml.dump(routes, default_flow_style=False, Dumper=CustomDumper)
        #print(y_routes)
        print('Writing', out_routes)
        with open(out_routes, 'w') as outfile:
            yaml.dump(routes, outfile, default_flow_style=False, Dumper=CustomDumper)

        print('Writing', out_data)
        with open(out_data, 'w') as outfile:
            outfile.write(json.dumps(testdata, indent=4, sort_keys=True))
    except yaml.YAMLError as exc:
        print(exc)

