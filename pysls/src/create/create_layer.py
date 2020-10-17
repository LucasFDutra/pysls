import os
from pysls.utils.zip_files import zip_files
from pysls.utils.rmdir import rmdir

def create_layer(layer_name, python_version):
    if 'requirements.txt' in os.listdir('.'):
        os.system('pip install -r requirements.txt -t '+os.path.join('.','python','lib','python'+python_version,'site-packages'))
        zip_files(os.path.join('.', 'python'), layer_name)
        rmdir(os.path.join('.', 'python'))
    else:
        print('requirements.txt don\'t exist')