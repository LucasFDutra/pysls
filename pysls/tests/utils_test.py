from pysls.utils import copy_folder as cf
from pysls.utils import zip_files as zf
from pysls.utils import rmdir as rm
import os

source_folder = 'folder_to_make_tests'
destiny_folder = 'folder_to_make_tests_copy'

def test_copy_folder():
    os.mkdir(os.path.join('.', source_folder))
    os.mkdir(os.path.join('.', destiny_folder))
    os.mkdir(os.path.join('.', source_folder, 'folder1'))
    os.mkdir(os.path.join('.', source_folder, 'folder2'))

    open(os.path.join('.', source_folder, 'folder1', 'teste.py'), 'w').close()
    open(os.path.join('.', source_folder, 'folder2', 'teste.py'), 'w').close()
    open(os.path.join('.', source_folder, 'teste.py'), 'w').close()

    cf.copy_folder(os.path.join('.', source_folder), os.path.join('.', destiny_folder))

    dir_level_one_returned = os.listdir(os.path.join('.', destiny_folder))
    dir_level_one_expected = ['folder1', 'folder2', 'teste.py']
    dir_level_one_returned.sort()
    dir_level_one_expected.sort()

    dir_level_two_folder1_returned = os.listdir(os.path.join('.', destiny_folder, 'folder1'))
    dir_level_two_folder1_expected = ['teste.py']
    dir_level_two_folder1_returned.sort()
    dir_level_two_folder1_expected.sort()

    dir_level_two_folder2_returned = os.listdir(os.path.join('.', destiny_folder, 'folder2'))
    dir_level_two_folder2_expected = ['teste.py']
    dir_level_two_folder2_returned.sort()
    dir_level_two_folder2_expected.sort()

    assert(
        dir_level_one_returned == dir_level_one_expected and \
        dir_level_two_folder1_returned == dir_level_two_folder1_expected and \
        dir_level_two_folder2_returned == dir_level_two_folder2_expected
    )

def test_zip_files():
    a = zf.zip_files(source_folder, 'zip_file_test')
    zip_returned = os.listdir(os.path.join('.'))
    zip_expected = 'zip_file_test.zip'
    os.remove(os.path.join('.', 'zip_file_test.zip'))
    assert(zip_expected in zip_returned)

def test_rmdir():
    rm.rmdir(os.path.join('.', source_folder))
    rm.rmdir(os.path.join('.', destiny_folder))

    files_list = os.listdir('.')

    assert(
        source_folder not in files_list and \
        destiny_folder not in files_list
    )