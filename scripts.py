import os

def run_tests():
    os.rename('requirements.txt', 'requirements_tmp.txt')
    os.system('pytest --cov=./pysls --cov-report=xml')
    os.rename('requirements_tmp.txt', 'requirements.txt')

if __name__ == "__main__":
    run_tests()