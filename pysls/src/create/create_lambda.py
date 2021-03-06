import os

def create_dir_structure(function_name):
    os.mkdir(os.path.join('.', function_name))
    os.mkdir(os.path.join('.', function_name, function_name))
    os.mkdir(os.path.join('.', function_name, function_name, 'src'))
    os.mkdir(os.path.join('.', function_name, function_name, 'tests'))
    os.mkdir(os.path.join('.', function_name, function_name, 'tests', 'integration'))
    os.mkdir(os.path.join('.', function_name, function_name, 'tests', 'unit'))
    os.mkdir(os.path.join('.', function_name, function_name, 'tests', 'utils'))
    os.mkdir(os.path.join('.', function_name, function_name, 'tests', 'utils', 'files'))
    os.mkdir(os.path.join('.', function_name, function_name, 'tests', 'utils', 'mocks'))

def create_main_files(function_name, python_version):
    open(os.path.join('.', function_name, 'requirements.txt'), 'w').close()
    open(os.path.join('.', function_name, function_name, '__init__.py'), 'w').close()

    with open(os.path.join('.', function_name, 'docker-compose.yml'), 'w') as dockerfile:
        dockerfile.write("version: '3'\n")
        dockerfile.write("services:\n")
        dockerfile.write("  localstack:\n")
        dockerfile.write("    image: localstack/localstack\n")
        dockerfile.write("    ports:\n")
        dockerfile.write("      - \"4566:4566\"\n")
        dockerfile.write("    environment:\n")
        dockerfile.write("      - SERVICES=s3,lambda,cloudformation,cloudwatch,sts,iam,dynamodb\n")
        dockerfile.write("      - LAMBDA_EXECUTOR=docker\n")
        dockerfile.write("      - DOCKER_HOST=unix:///var/run/docker.sock\n")
        dockerfile.write("    volumes:\n")
        dockerfile.write("      - \"/var/run/docker.sock:/var/run/docker.sock\"\n")

    with open(os.path.join('.', function_name, 'pyproject.toml'), 'w') as pyproject:
        pyproject.write("[tool.poetry]\n")
        pyproject.write("name = \""+function_name+"\"\n")
        pyproject.write("version = \"0.1.0\"\n")
        pyproject.write("description = \"\"\n")
        pyproject.write("authors = [\"YOUR NAME\"]\n")
        pyproject.write("\n")
        pyproject.write("[tool.poetry.dependencies]\n")
        pyproject.write("python = \"^"+python_version+"\"\n")
        pyproject.write("\n")
        pyproject.write("[tool.poetry.dev-dependencies]\n")
        pyproject.write("pytest = \"^5.2\"\n")
        pyproject.write("\n")
        pyproject.write("[build-system]\n")
        pyproject.write("requires = [\"poetry-core>=1.0.0\"]\n")
        pyproject.write("build-backend = \"poetry.core.masonry.api\"\n")

    with open(os.path.join('.', function_name, 'README.md'), 'w') as readme:
        readme.write('# OBJETIVO\n')
        readme.write('# COMO UTILIZAR\n')
        readme.write('## INSTALAÇÕES\n')
        readme.write('## COMO EXECUTAR\n')

    with open(os.path.join('.', function_name, '.gitignore'), 'w') as gitignore:
        gitignore.write("# Byte-compiled / optimized / DLL files\n")
        gitignore.write("__pycache__/\n")
        gitignore.write("*.py[cod]\n")
        gitignore.write("*$py.class\n")
        gitignore.write("\n")
        gitignore.write("# C extensions\n")
        gitignore.write("*.so\n")
        gitignore.write("\n")
        gitignore.write("# Distribution / packaging\n")
        gitignore.write(".Python\n")
        gitignore.write("build/\n")
        gitignore.write("develop-eggs/\n")
        gitignore.write("dist/\n")
        gitignore.write("downloads/\n")
        gitignore.write("eggs/\n")
        gitignore.write(".eggs/\n")
        gitignore.write("lib/\n")
        gitignore.write("lib64/\n")
        gitignore.write("parts/\n")
        gitignore.write("sdist/\n")
        gitignore.write("var/\n")
        gitignore.write("wheels/\n")
        gitignore.write("pip-wheel-metadata/\n")
        gitignore.write("share/python-wheels/\n")
        gitignore.write("*.egg-info/\n")
        gitignore.write(".installed.cfg\n")
        gitignore.write("*.egg\n")
        gitignore.write("MANIFEST\n")
        gitignore.write("\n")
        gitignore.write("# PyInstaller\n")
        gitignore.write("#  Usually these files are written by a python script from a template\n")
        gitignore.write("#  before PyInstaller builds the exe, so as to inject date/other infos into it.\n")
        gitignore.write("*.manifest\n")
        gitignore.write("*.spec\n")
        gitignore.write("\n")
        gitignore.write("# Installer logs\n")
        gitignore.write("pip-log.txt\n")
        gitignore.write("pip-delete-this-directory.txt\n")
        gitignore.write("\n")
        gitignore.write("# Unit test / coverage reports\n")
        gitignore.write("htmlcov/\n")
        gitignore.write(".tox/\n")
        gitignore.write(".nox/\n")
        gitignore.write(".coverage\n")
        gitignore.write(".coverage.*\n")
        gitignore.write(".cache\n")
        gitignore.write("nosetests.xml\n")
        gitignore.write("coverage.xml\n")
        gitignore.write("*.cover\n")
        gitignore.write("*.py,cover\n")
        gitignore.write(".hypothesis/\n")
        gitignore.write(".pytest_cache/\n")
        gitignore.write("\n")
        gitignore.write("# Translations\n")
        gitignore.write("*.mo\n")
        gitignore.write("*.pot\n")
        gitignore.write("\n")
        gitignore.write("# Django stuff:\n")
        gitignore.write("*.log\n")
        gitignore.write("local_settings.py\n")
        gitignore.write("db.sqlite3\n")
        gitignore.write("db.sqlite3-journal\n")
        gitignore.write("\n")
        gitignore.write("# Flask stuff:\n")
        gitignore.write("instance/\n")
        gitignore.write(".webassets-cache\n")
        gitignore.write("\n")
        gitignore.write("# Scrapy stuff:\n")
        gitignore.write(".scrapy\n")
        gitignore.write("\n")
        gitignore.write("# Sphinx documentation\n")
        gitignore.write("docs/_build/\n")
        gitignore.write("\n")
        gitignore.write("# PyBuilder\n")
        gitignore.write("target/\n")
        gitignore.write("\n")
        gitignore.write("# Jupyter Notebook\n")
        gitignore.write(".ipynb_checkpoints\n")
        gitignore.write("\n")
        gitignore.write("# IPython\n")
        gitignore.write("profile_default/\n")
        gitignore.write("ipython_config.py\n")
        gitignore.write("\n")
        gitignore.write("# pyenv\n")
        gitignore.write(".python-version\n")
        gitignore.write("\n")
        gitignore.write("# pipenv\n")
        gitignore.write("#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.\n")
        gitignore.write("#   However, in case of collaboration, if having platform-specific dependencies or dependencies\n")
        gitignore.write("#   having no cross-platform support, pipenv may install dependencies that don't work, or not\n")
        gitignore.write("#   install all needed dependencies.\n")
        gitignore.write("#Pipfile.lock\n")
        gitignore.write("\n")
        gitignore.write("# PEP 582; used by e.g. github.com/David-OConnor/pyflow\n")
        gitignore.write("__pypackages__/\n")
        gitignore.write("\n")
        gitignore.write("# Celery stuff\n")
        gitignore.write("celerybeat-schedule\n")
        gitignore.write("celerybeat.pid\n")
        gitignore.write("\n")
        gitignore.write("# SageMath parsed files\n")
        gitignore.write("*.sage.py\n")
        gitignore.write("\n")
        gitignore.write("# Environments\n")
        gitignore.write(".env\n")
        gitignore.write(".venv\n")
        gitignore.write("env/\n")
        gitignore.write("venv/\n")
        gitignore.write("ENV/\n")
        gitignore.write("env.bak/\n")
        gitignore.write("venv.bak/\n")
        gitignore.write("\n")
        gitignore.write("# Spyder project settings\n")
        gitignore.write(".spyderproject\n")
        gitignore.write(".spyproject\n")
        gitignore.write("\n")
        gitignore.write("# Rope project settings\n")
        gitignore.write(".ropeproject\n")
        gitignore.write("\n")
        gitignore.write("# mkdocs documentation\n")
        gitignore.write("/site\n")
        gitignore.write("\n")
        gitignore.write("# mypy\n")
        gitignore.write(".mypy_cache/\n")
        gitignore.write(".dmypy.json\n")
        gitignore.write("dmypy.json\n")
        gitignore.write("\n")
        gitignore.write("# Pyre type checker\n")
        gitignore.write(".pyre/\n")
        gitignore.write("\n")
        gitignore.write(".serverless/\n")
        gitignore.write("\n")
        gitignore.write("node_modules\n")
        gitignore.write("\n")
        gitignore.write("package-lock.json\n")
        gitignore.write("package.json\n")

def create_src_files(function_name, python_version):
    with open(os.path.join('.', function_name, function_name, 'src', 'lambda_function.py'), 'w') as lambda_function:
        lambda_function.write("import json\n")
        lambda_function.write("\n")
        lambda_function.write("def lambda_handler(event, context):\n")
        lambda_function.write("\n")
        lambda_function.write("    response = {\n")
        lambda_function.write("        \"statusCode\": 200,\n")
        lambda_function.write("        \"body\": json.dumps(event)\n")
        lambda_function.write("    }\n")
        lambda_function.write("\n")
        lambda_function.write("    return response\n")

    with open(os.path.join('.', function_name, function_name, 'src', 'serverless.yml'), 'w') as serverless:
        serverless.write("service: "+function_name.replace('_', '-')+"\n")
        serverless.write("# frameworkVersion: '2'\n")
        serverless.write("\n")
        serverless.write("# custom:\n")
        serverless.write("#   bucketName: my-bucket\n")
        serverless.write("\n")
        serverless.write("provider:\n")
        serverless.write("  name: aws\n")
        serverless.write("  runtime: python"+python_version+"\n")
        serverless.write("  region: us-east-1\n")
        serverless.write("#   iamRoleStatements:\n")
        serverless.write("#     - Effect: Allow\n")
        serverless.write("#       Action:\n")
        serverless.write("#         - s3:GetObject\n")
        serverless.write("#         - s3:PutObject\n")
        serverless.write("#       Resource: 'arn:aws:s3:::${self:custom.bucketName}/*'\n")
        serverless.write("\n")
        serverless.write("functions:\n")
        serverless.write("  "+function_name+":\n")
        serverless.write("    handler: lambda_function.lambda_handler\n")
        serverless.write("    # events:\n")
        serverless.write("    #   - x:\n")
        serverless.write("    #       bucket: ${self:custom.bucketName}\n")
        serverless.write("    #       event: s3:ObjectCreated:*\n")
        serverless.write("    #       rules:\n")
        serverless.write("    #         - prefix: uploads/\n")
        serverless.write("\n")
        serverless.write("plugins:\n")
        serverless.write("  - serverless-localstack\n")

def create_lambda(function_name, python_version):
    create_dir_structure(function_name)
    create_main_files(function_name, python_version)
    create_src_files(function_name, python_version)
