<a href="https://codecov.io/gh/LucasFDutra/pysls">
  <img src="https://codecov.io/gh/LucasFDutra/pysls/branch/master/graph/badge.svg" />
</a>

# OBJETIVO
Facilitar a criação de um projeto aws lambda em python. Criando a estrutura de diretórios, possibilitando o deploy dentro do [localstack](https://github.com/localstack/localstack), invocação da função de dentro do container, visualização dos logs da função e a criação de zips que serão utilizados para construção dos layers.

> NOTA: Para os usuários de Windows a sua função e layers pode apresentar alguns problemas devido as dependências com binários em C. Pois os binários em linux são diferentes dos de windows, logo a lambda não conseguirá entender. Por isso recomendo (assim como a documentação da aws) que você utilize um container para desenvolvimento ou o WSL.

# REQUISITOS

Caso deseje utilizar o localstack para seus testes, será necessário instalar o docker. E para a função de deploy no localstack é necessário utilizar o serverless framework, logo também é necessário instalar o node. 

- [docker](https://docs.docker.com/get-docker/)
- [node](https://nodejs.org/en/)
- [serverless](https://www.serverless.com/framework/docs/getting-started/)

# COMO INSTALAR
Para instalar a aplicação é bem simples, basta digitar o comando:

```sh
$ pip install pysls
```

# COMO UTILIZAR
Uma vez que o pacote esteja instalado, você pode rodar ele via linha de comando. Os comandos são os seguintes:

---
## CRIAR ESTRUTURA DE ARQUIVOS

```sh
$ pysls --create_function=project_name
```

A estrutura de arquivos é dada da seguinte forma:

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

- `docker-compose.yml`: Contém uma estrutura pré montada do localstack;
- `lambda_test/src/lambda_function.py`: O arquivo onde a função lambda deve ficar, e qualquer outro arquivo pertencente a função lambda deve ficar contido dentro da pasta src;
- `lambda_test/src/serverless.yml`: Configurações para o serverless framework (já contendo o plugin para o localstack);
- `tests`: Pasta reservada a criar seus testes;
- `pyproject.toml`: Esse arquivo serve para quem quer utilizar o poetry como gerenciador de pacotes, porém o pysls também precisa dele para recuperar informações;
- `requirements.txt`: É desse arquivo que o pysls irá utilizar para criar seu layer e buildar a aplicação para colocá-la no localstack.

> OBS.: A versão free do localstack não permite a utilização de layers, mas é possível enviar os códigos das libs dentro do pacote da lambda.

---
## MONTAR O ZIP DO LAYER

```sh
$ pysls --create_layer=layer_name
```

Esse comando irá rodar o pip apontando como destino do pacote uma pasta `./python/lib/python+python_version/site-packages`, depois de baixar todos os arquivos nessa pasta, ela será zipada, e depois apagada.

---
## ENVIAR PARA O LOCALSTACK

```sh
$ pysls --deploy
```

Esse comando irá copiar a sua pasta src para uma pasta `./scr_tmp`, depois disso um comando npm é executado adicionando assim o plugin serverless-localstack. Após instalar o plugin, serão adicionados a pasta todos os pacotes que estão dentro do arquivo `requirements.txt`. O script roda o comando de deploy do serverless framework, e envia tudo para o localstack. Em seguida a pasta `./scr_tmp` é excluída.

> OBS.: O localstack precisa estar ativo, caso não esteja, basta executar o comando: `$ docker-compose -up`.

---
## VER LOGS DE DENTRO DO LOCALSTACK

```sh
$ pysls --logs
```

Esse comando busca de dentro do arquivo `pyproject.toml` o nome do projeto, e de dentro do arquivo `lambda_test/src/serverless.yml` o nome parcial da função dentro da lambda no localstack. O nome completo é montado da seguinte forma `/aws/lambda/<function_name_in_serverless>-dev-<project_name_in_pyproject>`. Com o nome completo da função, é possível olhar nos grupos de logs do cloud watch e buscar por tudo que for relacionado somente a essa função.

---
## EXECUTAR A FUNÇÃO COM BASE EM UM EVENTO

```sh
$ pysls --invoke=event_file_path
```

Também faz o processo de montar o nome da função. E por meio da SDK do python a função é invocada passando o arquivo de evento como parâmetro. E exibe o retorno da lambda.

Também é possível não enviar nenhum arquivo de evento, no caso basta executar o comando `$ pysls --invoke`.

> OBS.: Para criar esse arquivo, recomendo dar uma olhada na documentação do [SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html) na parte em que ele é utilizado para gerar esse arquivo

# COMO CONTRIBUIR

- Abra uma issue com sua ideia para discutirmos
- Depois faça um fork e mande seu pull request (por favor, não mande pull requests muito grandes).

# IDEIAS FUTURAS

- [] Gerar os arquivos de eventos pela própria ferramenta;
- [] Não depender do Serveless Framework para montar a função e suas dependências e enviar a mesma para dentro do localstack;
- [] Adicionar novas ideias futuras kkk