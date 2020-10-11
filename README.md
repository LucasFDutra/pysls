<a href="https://codecov.io/gh/LucasFDutra/pysls">
  <img src="https://codecov.io/gh/LucasFDutra/pysls/branch/master/graph/badge.svg" />
</a>

# OBJECTIVE
To facilitate the build of aws lambda projects in python. Building a directory structure, enabling deployment within the [localstack](https://github.com/localstack/localstack), invoke the function inside the container, view functions logs and create zip files to use for building layers.

> NOTE.: If you use Windows, you may want to use Docker or WSL to build layers and build dependency packages, because some dependencies have C binaries. And the binaries on Linux are different from Windows, and lambda runs on Linux.

# REQUIREMENTS

If you want to use localstack to run your tests, you need to install the docker. And to use the deploy function into the localstack, you will need the serverless framework too, so you will also need to install the node.

- [docker](https://docs.docker.com/get-docker/)
- [node](https://nodejs.org/en/)
- [serverless](https://www.serverless.com/framework/docs/getting-started/)

# HOW TO INSTALL
To install the application, just run the command below:

```sh
$ pip install pysls
```

# HOW TO USE
Once the package is installed, you can run it via the command line. The commands are as follows:

---
## CREATE FILE STRUCTURE

```sh
$ pysls --create_function=project_name
```
The files structure is as follows:

```sh
├── docker-compose.yml
├── lambda_test
│   ├── __init__.py
│   ├── src
│   │   ├── lambda_function.py
│   │   └── serverless.yml
│   └── tests
│       ├── integration
│       ├── unit
│       └── utils
│           ├── files
│           └── mocks
├── pyproject.toml
├── README.md
└── requirements.txt
```

- `docker-compose.yml`: Contains a pre-assembled localstack structure;
- `lambda_test/src/lambda_function.py`: This file contains the main function code, and any other files must exist within the src folder;
- `lambda_test/src/serverless.yml`: Contains serverless framework settings (the localstack plugin is already included);
- `tests`: Folder reserved for your tests;
- `pyproject.toml`: This file is for those who want to use poetry as package manager, but pysls also needs it to retrieve information;
- `requirements.txt`: pysls uses this file to create a layer and to build  a lambda function package to send to localstack.

> OBS.: With the free version of localstack is not possible to use layers, but it is possible to send the code from the libraries together with the lambda code package.

---
## ASSEMBLING THE LAYER ZIP FILE

```sh
$ pysls --create_layer=layer_name
```

This command will run the pip pointing to the folder `./python/lib/python+python_version/site-packages` as the final directory to place the library files, and after that it will compress the folder and delete it

---
## SEND TO LOCALSTACK

```sh
$ pysls --deploy
```

This command will copy the `src` folder to `./src_tmp`, and after that it will run a npm command to add the `serverless-localstack` plugin. After that, it will add to the folder the libraries files that are listed in the file `requirements.txt`. The script will execute the deploy command into the localstack based on the deploy command of serverless framework. After all this, the folder `./src_tmp` will be deleted.

> OBS.: The localstack must be active, if not, run the commando: `$ docker-compose -up`.

---
## VIEW LOGS INSIDE THE LOCALSTACK

```sh
$ pysls --logs
```

This command searches for the project name within `pyproject.toml` and the partial name of the lambda function within `lambda_test/src/serverless.yml`. The full name is constructed as follows: `/aws/lambda/<function_name_in_serverless>-dev-<project_name_in_pyproject>`. With the full name, it is possible to view all logs related to the function.

---
## EXECUTE THE FUNCTION BASED ON AN EVENT

```sh
$ pysls --invoke=event_file_path
```

Perform the same process to assemble the function name. And use the python SDK to invoke lambda by passing the event file as a parameter. And then it shows the lambda's response.

It is possible not to send any files, in this case run the command `$ pysls --invoke`.

> OBS.: To create this file, I recommend consulting the [SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html) documentation, with SAM it is possible to create this event file.

# HOW TO CONTRIBUTE

- Open an issue with your idea to discuss;
- Then fork and send your pull request (please do not send too large pull requests).

# FUTURE IDEAS

- [ ] Create your own settings file;
- [ ] Generate the event files by the tool itself;
- [ ] Do not depend on the Serveless Framework to build the function and its dependencies and send it to the localstack;
- [ ] Add new future ideas kkk