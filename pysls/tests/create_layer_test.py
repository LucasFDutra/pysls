import pysls.src.create_lambda as clf
import pysls.src.create_layer as cl
from pysls.utils.rmdir import rmdir
import os
import time

lambda_name = 'lambda_test_layer'
layer_test_name = 'numpy'

clf.create_lambda(lambda_name, '3.8')

def test_create_layer_no_req():
    cl.create_layer(layer_test_name, '3.8')
    files_list = os.listdir('.')
    assert(layer_test_name+'.zip' not in files_list)

def test_create_layer_req():
    with open(os.path.join('.', 'requirements.txt'), 'w') as requirements:
        requirements.write('numpy')

    cl.create_layer(layer_test_name, '3.8')
    files_list = os.listdir('.')
    os.remove(os.path.join('.', layer_test_name+'.zip'))
    os.remove(os.path.join('.', 'requirements.txt'))

    rmdir(os.path.join('.', lambda_name))

    assert(layer_test_name+'.zip' in files_list)

