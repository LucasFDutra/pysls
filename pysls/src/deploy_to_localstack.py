import os
from pysls.utils.copy_folder import copy_folder
from pysls.utils.rmdir import rmdir

def deploy_local(project_name):
    path_code_from = os.path.join(project_name, 'src')
    path_code_to = os.path.join('.', 'src_tmp')
    os.mkdir(path_code_to)
    copy_folder(path_code_from, path_code_to)
    os.system('cd '+ path_code_to +' && npm install --save-dev serverless-localstack')
    os.system('pip install -r requirements.txt -t '+path_code_to)
    os.system('cd '+ path_code_to +' && sls deploy')
    rmdir(path_code_to)