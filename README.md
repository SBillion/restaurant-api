[![CircleCI](https://circleci.com/gh/SBillion/restaurant-api/tree/develop.svg?style=svg)](https://circleci.com/gh/SBillion/restaurant-api/tree/develop)

# Restaurant API



## Install

### Environment variables

Secret keys should not be in the settings file. To get this project work, you
have to create a **.env.** file at root project with following env variables defined
 ```dotenv
    DEBUG=True
    SECRET_KEY=put_your_secret_key_here
    DATABASE_URL=postgres://<username>:<password>@localhost:5432/<dbname>
``` 

### Database

Create a postgresql database and set its secrets in **.env** file

### Third packages
#### Using poetry

This project has a pyproject.tml file for poetry using. If you use [pyenv](https://github.com/pyenv/pyenv) to manage python versions, the version in .python-version file will be used

```shell script 
poetry install
```
#### Using pip

After creating your [virtualenv](https://virtualenv.pypa.io/en/latest/userguide/), activate it and install all required packages

```shell script
pip install -r requirements.txt
```

## Docker

Justo do 

```shell script
docker-compose up
```


### Lauch application

In the projet root and with your virtualenv activate

```shell script
python application.py runserver
```

#### Run tests

```shell script
python application.py tests
```


## What next ?

 - Add user and authentication to restrict usage of non readable endpoint
 - Add an API key system ?
 - Generate Swagger UI or ReDoc documentation using OpenAPI
 - Use tox
 - Deployment on a Saas platform or a private server if the tests passed




