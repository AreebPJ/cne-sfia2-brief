# QAC SFIA2 Project

## Application

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

## Getting Started
The initial setup involved creating the dockerfiles for the application. There after the yaml files for docker-compose were created.  
The steps taken to automate the testing and deployment of the application were as follows:
1. Terraform was used to spin up the instances on AWS. 
One EC2 instance to be configured with jenkins and one for testing.
Two RDS instances. One for testing and one for deployment.
After the instances have been spun up terraform outputs the public DNS for the instance to be configured for jenkins.

2. Ansible was used to configure an EC2 instance with jenkins. 
After terraform successfully spins up the instances it outputs a public DNS. This was pasted into the ansible inventory file. The public key configuration was automated as a pem key was added whilst creating the EC2 instances. The ansible playbook installs java and jenkins. 

3. After running the ansible playbook ssh access was configured from the jenkins VM to the test VM by generating a key pair in the jenkins instance and pasting it into the authorized keys file of the test VM. This is for the jenkins pipeline job to be able to ssh into the test vm and run commands

4. RDS instances for production and testing were accessed and the tables and data were inserted.  

5. To accomplish the testing the jenkins EC2 instance was accessed. Jenkins was setup and the pipeline jobs for testing had been created. The jenkins pipeline job for the testing configures the test instance by installing all the relevant applications, builds the image and executes the tests. 

6. The production VM was on GCP. Kubernetes was used on a Google cloud cluster. This VM had been configured before hand and then the pipeline job deploys the app by connecting to the GCP VM.  



 

