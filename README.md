# Challenge para EGO
Vehicles REST API

Welcome to Vehicles REST API! An API project that runs in Docker ecosystem using [Django REST Framework](https://www.django-rest-framework.org/) about a car catalog with different features.

[![docker](https://img.shields.io/badge/docker-blue)](https://github.com/PyCQA/python)
[![language: python](https://img.shields.io/badge/lenguage-python-blue)](https://github.com/PyCQA/python)
[![framework: django](https://img.shields.io/badge/framework-django-darkgreen)](https://github.com/topics/python)
[![package: rest framework](https://img.shields.io/badge/djangorestframework-darkred)](https://github.com/encode/django-rest-framework)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

## Features

Some of the features that the project contains:

- Vehicle catalog with different category.
- User system with login to give limited access to other people.
- Django Admin to manage the models, categories and users in PostgreSQL database.

## Quick start

How to section with the steps to set up the project in your system.

<details><summary><b>Setting the project up</b></summary>

### Install dependencies

To run this project you need to install `Docker` and `Docker Compose`.

In [this article](https://support.netfoundry.io/hc/en-us/articles/360057865692-Installing-Docker-and-docker-compose-for-Ubuntu-20-04) are the details to install Docker and Docker Compose on a Linux machine. In case you want to install the tools on another platform or have any problems, you can read the official documentation of [Docker](https://docs.docker.com/get-docker/) and also that of [Docker Compose](https://docs.docker.com/compose/install/).

Continue with downloading the code when you have the dependencies installed and working.

### Download the code

To download the code, the best thing to do is to `fork` this project to your personal account by clicking on [this link](https://github.com/PabloMarelli/challenge-ego/fork). Once you have the fork to your account, download it from the terminal with this command (remember to put your username in the link):

```
git clone https://github.com/PabloMarelli/challenge-ego
```

> In case you don't have a Github account, or you don't want to fork, you can directly clone this repo with the command `git clone https://github.com/PabloMarelli/challenge-ego`.


### Initial project configuration

To run the application, you first need to download the database image with the `docker compose pull pgdb` command. Next, you need to compile the REST API service with the `docker compose build egochallenge-api` command (it may take a few minutes).

When the above processes finish, start the database service with the command `docker compose up -d pgdb` from the root of the project. With the database running, it is necessary to create the tables that the application needs to work with the command `docker compose run egochallenge-api python3 manage.py migrate`.

It is possible to load sample data to test the API as quickly as possible. The sample data is in the `.fixtures` directory. The command needed for load fixture is as follows (in the example, the `example_data.json` fixtures will be loaded):

```
docker compose run egochallenge-api python3 manage.py loaddata .fixtures/example_data.json
```

### Run the application

With the initial configurations done, now it's time to run the API service with the command `docker compose up egochallenge-api` (if you want to run the service in background, you can add the -d flag during execution). When the service starts, you can access the `Browsable API` from the browser by entering the [api root endpoint](http://localhost:8000/).

If you are able to access the `Browsable API`, it means that the application is running correctly.

</details>

## Documentation

In this section you will find the information to understand and configure the project.

<details><summary><b>See the details</b></summary>

### Main features

Below you can see the main features of the project:

* REST API fully explorable through the Django REST "Browsable API" and hyperlinks
* Application administration panel
* Customized Browsable API for each endpoint
* Extensive usage documentation

The feature related to each application is included in the [Applications](#applications) section.


### Django Configuration

In the file `./core/settings.py` you will find the general configuration of the Django project. Within this file, all kinds of Django configurations can be made, in which the following stand out:

* Selection and configuration of the database engine.
* Applications installed within the project.
* Time zone setting.
* Project debug configuration.
* Django REST Framework specific configuration.
* Template configuration.
* Directory configuration for static files.
* User model selection.
* User Authentication & Authorization.

For more information on all the possible configurations, you can access the official documentation at [this link](https://docs.djangoproject.com/en/3.2/topics/settings/).

### Browsable API

This application - by using Django REST Framework - has a functionality that makes the REST API browsable in HTML format. This feature is really an excellent functionality, as it enables you to explore, navigate, and discover the API without having to open any dedicated programs (such as Postman or other clients).

From the browsable API you can access to Home Endpoint, and navigate over the user registration, login, logout, password recovery and email confirmation flows. 

The usage flow related of each application is included in its [Applications](#applications) section.

### How to use the service API

The starting point of using the API is accessing its [root](http://localhost:8000) via a client or a browser. From there you can see some useful endpoints related to your custom applications endpoints.

**Applications flows**

The specific app endpoints are described in each section of [Applications](#applications).

### Using the admin site

The API service has an integrated administration panel that allows you to perform CRUD operations on each of registered applications models (tables).

To use the admin site you must create a superuser before. Execute the command `docker compose run egochallenge-api python3 manage.py createsuperuser`, enter your email and your password twice and then go to [admin endpoint](http://localhost:8000/admin) to login with your credentials.

Apart of the base sections, there are the custom applications, explained in the [Applications](#applications) section.

### Environment Variables

Some environment variables used by the database service, as well as the API service, are defined in the `.env` file. Necessary variables can be added/removed. In case you accidentally delete the values or the env file, below you can find some values that work correctly with the application.

```
SECRET_KEY = "django-insecure-fmkrrpn!s6uzxxask=wz4hshsby%e)-=9ms@nx%^3g7dz*ndh@"
DEBUG = True

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

It is **HIGHLY RECOMMENDED** that you change these variables if you want to use this application for productive purposes.

### Database manipulation

Django provides an excellent database manipulation without the need to use any external tools to perform the necessary operations.

If you want to make a simple backup of the database, execute the following command:

```
docker compose run egochallenge-api \
python3 manage.py dumpdata --indent 2 > .fixtures/db.json
```

If you want to make a backup of the database that can be used in a fresh database, execute the following command:

```
docker compose run egochallenge-api \
python3 manage.py dumpdata --indent 2 \
--exclude auth.permission --exclude contenttypes --exclude admin.logentry > .fixtures/db.json
```

To load the application data into a fresh database, run the following command to create the necessary tables:

```
docker compose run egochallenge-api python manage.py migrate
```

And then load data inside the tables:

```
docker compose run egochallenge-api python manage.py loaddata .fixtures/db.json
```


### Dir Structure

Folder structure for scalability. General folder contains:

```sh
├── [other files/folders]       # files/folders arount the Django project 
├── [project-root-folder]       # the root folder containing the Django app
|   ├── core                    # the main Django app folder
│   │   ├── __init__.py 
│   │   ├── admin.py            # base logic related to admin classes
│   │   ├── asgi.py             # autogenerated
│   │   ├── models.py           # base logic related to models
│   │   ├── permissions.py      # the main permissions the project has
│   │   ├── settings.py         # project settings
│   │   ├── urls.py             # main project url configurations
│   │   ├── views.py            # views related to the project, not to applications
│   │   └── wsgi.py             # autogenerated
|   ├── [apps(root-folder lvl)] # the django applications
|   |   [app1]                  # example app folder
│   │   [app2]                  # example app folder
|   ├── [integrations]          # integrations with third party services
|   ├── [templates]             # all the project templates should be in this dir
|   └── manage.py               # module to manage the project and common operations
```

Application folder structure:

```sh
├── application
│   ├── migrations          
│   ├── models              # package to store models separatelu
│   │   ├── __init__.py
│   │   └── model.py
│   ├── __init__.py         # autogenerated
│   ├── admin.py            # admin class definition and configuration
│   ├── apps.py             # required by Django
│   ├── permissions.py      # application level permissions
│   ├── serializers.py      # application level serializers
│   ├── urls.py             # application level url configuration
│   └── views.py            # views
```
</details>

## Applications 📚

In this section you will find information that will help you to have a greater context about each custom applications.

<details><summary><b>Read the apps info</b></summary>

### Catalog API

The catalog API manages vehicles and categories.

<details><summary><b>See all info related to Catalog API</b></summary>

#### Catalog Features

* Vehicles with different fields
* Categories

#### Prode sample data

The application comes with sample data ready to load at `.fixtures/example_data.json`. To load this data you have to execute the command `docker compose run egochallenge-api python3 manage.py migrate` and then, execute the command `docker compose run egochallenge-api python3 manage.py loaddata .fixtures/example_data.json` as explained in [Quick Start](#quick-start) section.

#### Using the Prode admin site

At first, it is necessary to create a superuser as described in the [Using the admin site](#using-the-admin-site) and then, login at the [admin endpoint](http://localhost:8000/admin). 

Inside the admin panel you can create different assesments, assign questions and options. From the left panel you can create all the entities that you consider necessary and the relationships between them.
#### Endpoints

Each endpoint is listed below, with its description and available methods.

* `/` - Shows a list with all the available resources of the application (GET)
* `catalog/vehicles/` - List all vehicles objects (GET)
* `catalog/vehicles/<int:pk>/` - Shows the detail of vehicle object (GET)
* `catalog/categories/` - List all categories objects (GET)
* `catalog/categories/<int:pk>/` - Shows the detail of categories object (GET)


Although the information of each endpoint is in the previous list, it is much better to navigate through the `Browsable API` that allows access to more information about each of the endpoints.

</details>

</details>

</details>



## Used technologies 🛠️

In this section you can see the most important technologies used.

<details><summary><b>See the complete list of technologies</b></summary><br>

* [Docker](https://www.docker.com/) - Ecosystem that allows the execution of software containers.
* [Docker Compose](https://docs.docker.com/compose/) - Tool that allows managing multiple Docker containers.
* [Python](https://www.python.org/) - Language in which the services are made.
* [Django](https://www.djangoproject.com/) - Popular Python framework for web application development.
* [Django REST Framework](https://www.django-rest-framework.org/) - Django-based framework for designing REST APIs.
* [PostgreSQL](https://www.postgresql.org/) - Database to query and store data.
* [Visual Studio Code](https://code.visualstudio.com/) - Popular multi-platform development IDE.

</details>