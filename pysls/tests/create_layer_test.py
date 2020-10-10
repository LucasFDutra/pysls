import pysls.src.create_layer as cl
from pysls.utils.rmdir import rmdir
import os

layer_test_name = 'numpy'

def test_create_layer():
    with open(os.path.join('.', 'requirements.txt'), 'w') as requirements:
        requirements.write('numpy')

    cl.create_layer(layer_test_name, '3.8')
    files_list = os.listdir('.')

    rmdir(os.path.join('.', layer_test_name))
    rmdir(os.path.join('.', 'requirements.txt'))

    assert(layer_test_name+'.zip' in files_list)

def test_create_layer():
    cl.create_layer(layer_test_name, '3.8')
    files_list = os.listdir('.')

    assert(layer_test_name+'.zip' not in files_list)

