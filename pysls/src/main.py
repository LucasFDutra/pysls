import sys
import re
import os
from platform import python_version
from pysls.src.create.create_lambda import create_lambda
from pysls.src.create.create_layer import create_layer
from pysls.src.localstack.view_logs import view_logs_local
from pysls.src.localstack.deploy_to_localstack import deploy_local
from pysls.src.localstack.invoke_function import invoke_function
from pysls.src.events.generate_event import generete_event

import json

def fct_pysls_config():
    with open(os.path.join('.', 'pysls_config.json'), 'r') as pysls_config:
        config = json.load(pysls_config)
    return config

# --create_function=function_name
def fct_create_function(function_name, py_version):
    create_lambda(function_name, py_version)

# --create_layer=layer_name
def fct_create_layer(layer_name, py_version):
    create_layer(layer_name, py_version)

# --view_logs=function_name
def fct_view_logs(function_name, service_name):
    view_logs_local(function_name, service_name)

# --deploy_local
def fct_deploy(function_name):
    deploy_local(function_name)

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
    print('## --deploy ------------------------------ send function and dependencies to localstack                                ##')
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