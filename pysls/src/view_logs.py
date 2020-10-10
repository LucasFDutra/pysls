import boto3
import json
import os

def view_logs_local(project_name):
    config_cw_logs = {
        'service_name': 'logs',
        'aws_access_key_id': '123',
        'aws_secret_access_key': '123',
        'region_name': 'us-east-1',
        'endpoint_url': 'http://localhost:4566'
    }

    with open(os.path.join('.', project_name, 'src', 'serverless.yml'), 'r') as serverless:
        function_name = serverless.readline().replace('service:', '').replace('\n', '').strip()

    function_log_group_name = '/aws/lambda/'+function_name+'-dev-'+project_name

    cw_logs = boto3.client(**config_cw_logs)

    for log_group in cw_logs.describe_log_groups()['logGroups']:
        logGroupName = log_group['logGroupName']
        if (logGroupName == function_log_group_name):
            logStreams = cw_logs.describe_log_streams(logGroupName=logGroupName)['logStreams']
            for logStream in logStreams:
                logStreamName = logStream['logStreamName']
                logs = cw_logs.get_log_events(logGroupName=logGroupName, logStreamName=logStreamName)
                for log in logs['events']:
                    print('------------------------------------------------------------------')
                    print(log['message'])