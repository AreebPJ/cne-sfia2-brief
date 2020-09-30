# QAC SFIA2 Project

## Getting Started 

The application is a Flask application running in **2 micro-services** (*frontend* and *backend*).
The application works by:
1. The frontend service making a GET request to the backend service. 
2. The backend service using a database connection to query the database and return a result.
3. The frontend service serving up a simple HTML (`index.html`) to display the result.

The objective is to effeciently deploy this application. This will involve utilizing several concepts including:
* Continuous Integration
* Containerisation
* Configuration Management
* Cloud Solutions
* Infrastructure Management
* Orchestration 
## Requirements 
There are a minimum set of requirements that were added during the duration of the project. The requirements are:
* A Jira board with full expansion on tasks needed to complete the project.
* A record of any issues or risks that you faced creating the project.
* The application must be deployed using containerisation and orchestration tools.
* The application must be tested through the CI pipeline.
* The project must make use of two managed Database Servers: 1 for Testing and 1 for Production.
* If a change is made to the code base, Webhooks should be used so that Jenkins recreates and redeploys the changed application.
* The infrastructure for the project should be configured using an infrastructure management tool (Infrastructure as Code).
* As part of the project, you need to create an Ansible Playbook that will provision the environment that your CI Server needs to run.
* The project must make use of a reverse proxy to make your application accessible to the user.

## Aproach 
The steps taken to acomplish the project were as follows:
1. Get the app running with docker and docker compose.
 * This involved creating Dockerfiles to build images for the frontend, backend and database.
 * Creating a yaml file to build the images and deploy the app
2. Jenkins
 * Deploy Jenkins on another VM
 * Create a pipeline job that will ssh onto the deploy VM, build the images and deploy the app.
 * Another jenkins job for the test VM that test the backend and frontend service before deploying it. 
