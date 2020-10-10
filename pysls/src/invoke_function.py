import boto3
import json
import os

def invoke_function(project_name, event_path):
    config_client = {
        'service_name': 'lambda',
        'aws_access_key_id': '123',
        'aws_secret_access_key': '123',
        'region_name': 'us-east-1',
        'endpoint_url': 'http://localhost:4566'
    }

    client = boto3.client(**config_client)

    with open(os.path.join('.', project_name, 'src', 'serverless.yml'), 'r') as serverless:
        function_name = serverless.readline().replace('service:', '').replace('\n', '').strip()+'-dev-'+project_name

    if event_path == '':
        response = client.invoke(
            FunctionName=function_name
        )

    else:
        with open(event_path, 'rb') as event:
            response = client.invoke(
                FunctionName=function_name,
                Payload=event
            )
    print(json.loads(response['Payload'].read().decode("utf-8")))