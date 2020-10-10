import os

def rmdir(root_directory_name):
    for root, dirs, files in os.walk(root_directory_name, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(root_directory_name)