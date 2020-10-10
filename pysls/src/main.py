import sys
import re
import os
from platform import python_version
from pysls.src.create_lambda import create_lambda
from pysls.src.create_layer import create_layer
from pysls.src.view_logs import view_logs_local
from pysls.src.deploy_to_localstack import deploy_local
from pysls.src.invoke_function import invoke_function

# pysls
# --create_function=project_name
def fct_create_function(project_name, py_version):
    create_lambda(project_name, py_version)

# --create_layer=layer_name
def fct_create_layer(layer_name, py_version):
    create_layer(layer_name, py_version)

# --view_logs=project_name
def fct_view_logs(project_name):
    view_logs_local(project_name)

# --deploy_local
def fct_deploy(project_name):
    deploy_local(project_name)

#--invoke
def fct_invoke_function(project_name, event_path):
    invoke_function(project_name, event_path)

# --help
def fct_help():
    print('###===================================================================================================================###')
    print('## --create_function=project_name -------- create directories and files structure to develop lambda function in python ##')
    print('## --create_layer=layer_name ------------- build a zip with dependencies on requirements.txt in the layer structure    ##')
    print('## --logs -------------------------------- view logs by function                                                       ##')
    print('## --deploy ------------------------------ send function and dependencies to localstack                                ##')
    print('## --invoke=event_file_path -------------- invoke function inside localstack                                           ##')
    print('###===================================================================================================================###')

def main():
    py_version = python_version()[0:3]
    arg = sys.argv[1]

    if ('--help' in arg):
        fct_help()
    elif ('--create_function' in arg):
        project_name = arg.replace('--create_function=', '')
        project_name = re.sub('(\W+)', '_', project_name)
        fct_create_function(project_name, py_version)

    elif ('--create_layer' in arg):
        layer_name = arg.replace('--create_layer=', '')
        fct_create_layer(layer_name, py_version)

    elif ('--logs' in arg):
        with open(os.path.join('.', 'pyproject.toml'), 'r') as pyproject:
            pyproject.readline()
            project_name = pyproject.readline().replace('name = ', '').replace('\n', '').replace('"', '')
        fct_view_logs(project_name)

    elif ('--deploy' in arg):
        with open(os.path.join('.', 'pyproject.toml'), 'r') as pyproject:
            pyproject.readline()
            project_name = pyproject.readline().replace('name = ', '').replace('\n', '').replace('"', '')
        fct_deploy(project_name)
    
    elif ('--invoke' in arg):
        event_path = arg.replace('--invoke=', '')
        with open(os.path.join('.', 'pyproject.toml'), 'r') as pyproject:
            pyproject.readline()
            project_name = pyproject.readline().replace('name = ', '').replace('\n', '').replace('"', '')
        fct_invoke_function(project_name, event_path)

if __name__ == "__main__":
    main()