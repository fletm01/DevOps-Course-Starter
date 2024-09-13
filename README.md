# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Setting up Mongo DB Database

This To Do app uses Mongo DB for stroing the To Do items. You'll need to set up:

* A Mongo DB Account and Database
* Provide a connection string for connecting to said database

When you have done this you will then need to update the `.env` file to include your Mongo DB details.


## Running the App Locally

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running The Test Suite
To run the tests for the codebase run the following command:
```
poetry run pytest
```
Please Note: Make sure you have installed `pytest` by running `poetry add pytest` before running the tests 

If instead you'd like to run your tests via Docker, please run the following:
```
$ docker build --target test --tag todo-app:test .
$ docker run todo-app:test
```

## Building and Running the App via Docker

To build the container for local development:
```bash
docker build --target development --tag todo-app:dev .
```

To run the container for local development:
```bash
docker run --publish 8000:5000 -it --env-file .env --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:dev 
```
For the production container, the build and run commands are:
```bash
docker build --target production --tag todo-app:prod .
docker run --publish 8000:5000 -it --env-file .env todo-app:prod
```

## Diagrams
Architecture Diagrams can be found in the `Diagrams` sub folder. They were built using [app.diagram.net] (app.diagrams.net) (you can use the `.draw.io` file to edit these diagrams) 

## Azure Hosting
The container image that is deployed to Azure is hosted on Docker Hub https://hub.docker.com/repository/docker/fletm01/todo-app/general

The To Do app website is hosted at https://mikestodo-app.azurewebsites.net/

To update the website you will need to run the following commands to build and push the container image:

```bash
docker build --tag fletm01/todo-app --target production .
docker push fletm01/todo-app
```

Next youll need to make a POST request to the webhook list provided on the App Service (under the Deployment Centre tab). This will trigger Azure to pull the updated image from Docker Hub.

## Data Encryption

To do items are stored in a Cosmos DB Database (using a MongoDB API). Data is encrypted at rest by default.

https://learn.microsoft.com/en-us/azure/cosmos-db/database-encryption-at-rest

The app service is hosted over HTTPS (enforced, i.e. HTTP redirects to HTTPS). Similarly TLS is enabled for connecting to the MongoDB CosmosDB database.
