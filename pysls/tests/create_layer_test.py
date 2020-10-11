import pysls.src.create_lambda as clf
import pysls.src.create_layer as cl
from pysls.utils.rmdir import rmdir
import os
import time

def test_create_layer_no_req():
    lambda_name = 'lambda_test_layer_no_req'
    layer_test_name = 'numpy_no_req'
    clf.create_lambda(lambda_name, '3.8')

    cl.create_layer(layer_test_name, '3.8')
    files_list = os.listdir('.')

    rmdir(os.path.join('.', lambda_name))
    
    assert(layer_test_name+'.zip' not in files_list)

def test_create_layer_req():
    lambda_name = 'lambda_test_layer_req'
    layer_test_name = 'numpy_req'

    clf.create_lambda(lambda_name, '3.8')

    with open(os.path.join('.', 'requirements.txt'), 'w') as requirements:
        requirements.write('numpy')

    cl.create_layer(layer_test_name, '3.8')
    files_list = os.listdir('.')
    os.remove(os.path.join('.', layer_test_name+'.zip'))
    os.remove(os.path.join('.', 'requirements.txt'))

    rmdir(os.path.join('.', lambda_name))

    assert(layer_test_name+'.zip' in files_list)

