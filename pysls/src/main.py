import sys
import re
import os
from platform import python_version
from pysls.src.create.create_lambda import create_lambda
from pysls.src.create.create_layer import create_layer
from pysls.src.localstack.view_logs import view_logs_local
from pysls.src.localstack.deploy_to_localstack import deploy_local
from pysls.src.localstack.update_to_localstack import update_local
from pysls.src.localstack.invoke_function import invoke_function
from pysls.src.events.generate_event import generete_event

import json
import yaml

def find_serverless():
    file_paths = [] 
    for root, directories, files in os.walk('.'): 
        for filename in files: 
            filepath = os.path.join(root, filename) 
            if (filename == 'serverless.yml'):
                return filepath, True
    return '', False

def fct_pysls_config():
    serverless_path, state = find_serverless()

    if (state):
        with open(serverless_path, 'r') as serverless:
            serverless_content = yaml.safe_load(serverless)

        config = {
            'service': serverless_content['service'],
            'function_name': list(serverless_content['functions'].keys())[0]
        }
        return config
    else:
        print('serverless.yml not found')
        exit()

# --create_function=function_name
def fct_create_function(function_name, py_version):
    create_lambda(function_name, py_version)

# --create_layer=layer_name
def fct_create_layer(layer_name, py_version):
    create_layer(layer_name, py_version)

# --logs
def fct_view_logs(function_name, service_name):
    view_logs_local(function_name, service_name)

# --deploy
def fct_deploy(function_name):
    deploy_local(function_name)

# --update
def fct_update(service_name, function_name):
    update_local(service_name, function_name)

#--invoke
def fct_invoke_function(function_name, service_name, event_path):
    invoke_function(function_name, service_name, event_path)

#--generete event
def fct_generete_event(service_name, event_type, values_to_sub, event_file_name):
    generete_event(service_name, event_type, values_to_sub, event_file_name)

# --help
def fct_help():
    print('###===================================================================================================================###')
    print('## --create_function=function_name ------- create directories and files structure to develop lambda function in python ##')
    print('## --create_layer=layer_name ------------- build a zip with dependencies on requirements.txt in the layer structure    ##')
    print('## --logs -------------------------------- view logs by function                                                       ##')
    print('## --deploy ------------------------------ mount function structure in localstack                                      ##')
    print('## --update ------------------------------ send just the function and dependencies to localstack                       ##')
    print('## --generete_event ---------------------- crete a event file                                                          ##')
    print('## --invoke=event_file_path -------------- invoke function inside localstack                                           ##')
    print('###===================================================================================================================###')

def main():
    py_version = python_version()[0:3]
    arg = sys.argv[1]

    if ('--help' in arg):
        fct_help()
    elif ('--create_function' in arg):
        function_name = arg.replace('--create_function=', '')
        function_name = re.sub('(\W+)', '_', function_name)
        fct_create_function(function_name, py_version)

    elif ('--create_layer' in arg):
        layer_name = arg.replace('--create_layer=', '')
        fct_create_layer(layer_name, py_version)

    elif ('--logs' in arg):
        config = fct_pysls_config()
        function_name = config['function_name']
        service_name = config['service']
        fct_view_logs(function_name, service_name)

    elif ('--deploy' in arg):
        config = fct_pysls_config()
        function_name = config['function_name']
        fct_deploy(function_name)

    elif ('--update' in arg):
        config = fct_pysls_config()
        function_name = config['function_name']
        service_name = config['service']
        fct_update(service_name, function_name)

    elif ('--invoke' in arg):
        event_path = arg.replace('--invoke=', '')
        event_path = event_path.replace('--invoke', '')
        config = fct_pysls_config()
        function_name = config['function_name']
        service_name = config['service']
        fct_invoke_function(function_name, service_name, event_path)

    elif ('--generate_event' in arg):
        service_name = ''
        event_type = ''
        values_to_sub = ''
        event_file_name = 'event.json'
        for arg_ in sys.argv[2:]:
            if ('--service=' in arg_):
                service_name = arg_.replace('--service=', '')
            elif ('--event_type=' in arg_):
                event_type = arg_.replace('--event_type=', '')
            elif ('--filename=' in arg_):
                event_file_name = arg_.replace('--filename=', '')
            else:
                values_to_sub += arg_
            
        fct_generete_event(service_name, event_type, values_to_sub, event_file_name)

    else:
        print('command not found')


if __name__ == "__main__":
    main()