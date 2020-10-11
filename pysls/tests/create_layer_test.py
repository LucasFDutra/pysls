from pysls.src.create_lambda import create_lambda
from pysls.src.create_layer import create_layer
from pysls.utils.rmdir import rmdir
import os
import time

python_version = '3.8'

def test_create_layer_no_req():
    lambda_name = 'lambda_test_layer_no_req'
    layer_test_name = 'numpy_no_req'
    create_lambda(lambda_name, python_version)

    create_layer(layer_test_name, python_version)
    files_list = os.listdir('.')

    rmdir(os.path.join('.', lambda_name))
    
    assert(layer_test_name+'.zip' not in files_list)

def test_create_layer_req():
    lambda_name = 'lambda_test_layer_req'
    layer_test_name = 'numpy_req'

    create_lambda(lambda_name, python_version)

    with open(os.path.join('.', 'requirements.txt'), 'w') as requirements:
        requirements.write('numpy')

    create_layer(layer_test_name, python_version)
    files_list = os.listdir('.')
    os.remove(os.path.join('.', layer_test_name+'.zip'))
    os.remove(os.path.join('.', 'requirements.txt'))

    rmdir(os.path.join('.', lambda_name))

    assert(layer_test_name+'.zip' in files_list)

