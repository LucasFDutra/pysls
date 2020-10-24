import boto3
import os
from pysls.utils.copy_folder import copy_folder
from pysls.utils.rmdir import rmdir
from pysls.utils.zip_files import zip_files

def update_local(service_name, function_name):
    project_dir = os.getcwd()
    path_code_from = os.path.join(function_name, 'src')
    path_code_to = os.path.join('.', 'src_tmp')
    os.mkdir(path_code_to)
    copy_folder(path_code_from, path_code_to)
    os.system('pip3 install -r requirements.txt -t '+path_code_to)
    os.chdir(path_code_to)
    zip_files('.', 'lambda_function')
    os.chdir(project_dir)

    config_client = {
        'service_name': 'lambda',
        'aws_access_key_id': '123',
        'aws_secret_access_key': '123',
        'region_name': 'us-east-1',
        'endpoint_url': 'http://localhost:4566'
    }

    client = boto3.client(**config_client)
    
    function_name_in_localstack = service_name+'-dev-'+function_name

    with open(os.path.join(path_code_to, 'lambda_function.zip'), 'rb') as f:
        response = client.update_function_code(
            FunctionName=function_name_in_localstack,
            ZipFile=f.read(),
        )

    rmdir(path_code_to)

    print('Stack update finished')
