from pysls.src.create_lambda import create_dir_structure
from pysls.src.create_lambda import create_main_files
from pysls.src.create_lambda import create_src_files
from pysls.utils.rmdir import rmdir
import os

python_version = '3.8'

def test_create_dir_structure():
    project_test_name = 'lambda_test_dir_structure'

    create_dir_structure(project_test_name)
    dir_level_one_returned = os.listdir(os.path.join('.', project_test_name))
    dir_level_one_expected = [project_test_name]

    dir_level_two_returned = os.listdir(os.path.join('.', project_test_name, project_test_name))
    dir_level_two_expected = ['src', 'tests']
    dir_level_two_returned.sort()
    dir_level_two_expected.sort()

    dir_level_three_returned = os.listdir(os.path.join('.', project_test_name, project_test_name, 'tests'))
    dir_level_three_expected = ['integration', 'unit', 'utils']
    dir_level_three_returned.sort()
    dir_level_three_expected.sort()

    dir_level_four_returned = os.listdir(os.path.join('.', project_test_name, project_test_name, 'tests', 'utils'))
    dir_level_four_expected = ['files', 'mocks']
    dir_level_four_returned.sort()
    dir_level_four_expected.sort()

    rmdir(os.path.join('.', project_test_name))

    assert(
        dir_level_one_returned == dir_level_one_expected and \
        dir_level_two_returned == dir_level_two_expected and \
        dir_level_three_returned == dir_level_three_expected and \
        dir_level_four_returned == dir_level_four_expected
    )

def test_create_main_files():
    project_test_name = 'lambda_test_main_files'
    create_dir_structure(project_test_name)

    create_main_files(project_test_name, python_version)
    files_level_one_returned = [f for f in os.listdir(os.path.join('.', project_test_name)) if '.' in f]
    files_level_one_expected = ['requirements.txt', 'docker-compose.yml', 'pyproject.toml', 'README.md', '.gitignore', 'pysls_config.json']
    files_level_one_returned.sort()
    files_level_one_expected.sort()

    files_level_two_returned = [f for f in os.listdir(os.path.join('.', project_test_name, project_test_name)) if '.' in f]
    files_level_two_expected = ['__init__.py']
    files_level_two_returned.sort()
    files_level_two_expected.sort()

    rmdir(os.path.join('.', project_test_name))

    assert(
        files_level_one_returned == files_level_one_expected and \
        files_level_two_returned == files_level_two_expected
    )

def test_create_src_files():
    project_test_name = 'lambda_test_src_files'
    create_dir_structure(project_test_name)

    create_src_files(project_test_name, python_version)
    files_returned = [f for f in os.listdir(os.path.join('.', project_test_name, project_test_name, 'src')) if '.' in f]
    files_expected = ['lambda_function.py', 'serverless.yml']
    files_returned.sort()
    files_expected.sort()
    
    rmdir(os.path.join('.', project_test_name))

    assert(files_returned == files_expected)