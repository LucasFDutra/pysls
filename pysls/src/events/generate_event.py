import json
import os
import base64
from urllib.parse import quote
import hashlib

def hash(hashing_scheme, value):
    if hashing_scheme == "md5":
        md5 = hashlib.md5()
        md5.update(value.encode("utf-8"))
        return md5.hexdigest()
    return value

def encode(encoding_scheme, value):
    if encoding_scheme == "url":
        return quote(value)
    if encoding_scheme == "base64":
        return base64.b64encode(value.encode("utf8")).decode("utf-8")
    return value

def generete_event(service_name, event_type, values_to_sub, event_file_name):
    this_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(this_folder, "event_mapping.json")

    with open(file_name, 'r') as event_mapping:
        event_mapping_content = json.load(event_mapping)
        event_type_content = event_mapping_content[service_name][event_type]
        tags_ = event_type_content['tags']
        tags = {}
        for key, value in tags_.items():
            tags[key] = hash(value.get('hashing'), encode(value.get('encoding'), value['default']))
            if value.get("children") is not None:
                children = value.get('children')
                children_key_name = [i for i in children][0]
                children = children.get(children_key_name)
                tags[children_key_name] = hash(children.get('hashing'), tags[key])

    file_name = os.path.join(this_folder, 'model_files', service_name, event_type_content['filename']+'.json')
    with open(file_name, 'r') as event_file:
        event_file_content = json.load(event_file)
        event_file_content = json.dumps(event_file_content)

    event_dict = {}
    for group in values_to_sub.split('--'):
        if (group != ''):
            [key, value] = group.strip().split('=')
            event_dict[key] = value
    event_dict = {**tags, **event_dict}

    for key, value in event_dict.items():
        event_file_content = event_file_content.replace("{{{"+key.replace('-', '_')+"}}}", value)

    with open(event_file_name, 'w')  as event:
        json.dump(json.loads(event_file_content), event, indent=4)
