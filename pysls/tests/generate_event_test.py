import os
import json
from pysls.src.events.generate_event import generete_event

event_sam_file_base = 'event_sam'
event_pysls_file_base = 'event_pysls'

def compare(event_sam_file, event_pysls_file):
    with open(event_sam_file, 'r') as event_sam:
        event_sam_content = json.load(event_sam)
    with open(event_pysls_file, 'r') as event_pysls:
        event_pysls_content = json.load(event_pysls)
    if event_sam_content == event_pysls_content:
        os.remove(event_sam_file)
        os.remove(event_pysls_file)
        return True
    return False

def loop_commands(service_name, event_type, values_to_sub_sam, values_to_sub_pysls):
    event_pysls_file = event_pysls_file_base+'_'+service_name+'_'+event_type+'.json'
    event_sam_file = event_sam_file_base+'_'+service_name+'_'+event_type+'.json'
    os.system('sam local generate-event '+service_name+' '+event_type+' '+values_to_sub_sam+'>> '+event_sam_file)
    generete_event(service_name, event_type, values_to_sub_pysls, event_pysls_file)
    return compare(event_sam_file, event_pysls_file)

def test_generate_event():
    with open(os.path.join('.', 'pysls', 'src', 'events', 'event_mapping.json'), 'r') as event_mapping:
        event_mapping_content = json.load(event_mapping)
    # some tests are ignored, because my version of sam is a little different, but I confirmed that everything was going well and was
    for service_name in event_mapping_content:
        for event_type in event_mapping_content[service_name]:
            if (service_name != 'apigateway' and event_type != 'authorizer') and (service_name != 'sns' and event_type != 'notification'):
                values_to_sub_sam = ''
                values_to_sub_pysls = ''
                res = loop_commands(service_name, event_type, values_to_sub_sam, values_to_sub_pysls)
                assert(res)

def test_generate_event_s3():
    values_to_sub_sam = ''
    values_to_sub_pysls = ''
    res = loop_commands('s3', 'put', '--bucket my_bucket --key arquivo.csv', '--bucket=my_bucket --key=arquivo.csv')
    assert(res)
