# Project 3

## Introduction

This project aimed to create an application composed of at least 4 services that work together

## Proposal

In order to meet the requirements for the project i began planning my sprint to ensure i could make an application which used a CI/CD pipeline

My idea was to create a Gladiator generator giving you a random weapon and skill with it, these 2 then gave you your chance of survival

Front end - Creates you with the results of the randomised outcomes

api1 - Gave a randon weapon

api2 - Creates a random skill number between 1-10 for that weapon

api3 - Returns a chance of survival based on the weapon and how good it is and whether you will survive.

## Archetecture

### Risk assesment
![Project 2 Risk assesment](https://user-images.githubusercontent.com/101715806/169771334-d6f7ac4d-7ddd-464c-af93-ce116c7d29a0.PNG)


Here is my risk assesment for the project with dates ive updated regulary to monitor the potential risks my project faces and ones that i might encounter throughout the project

## Trello Board
![Project 2 Trello](https://user-images.githubusercontent.com/101715806/169771715-50554012-5ce5-436a-9d5d-b77bec306967.PNG)

A trello board was used thorughout the sprint to track progression thorugh the project to see which jobs were complete and which were still in progess, to further improve this trello board i would colour co ordinated the tasks to make it more user friendly and to see priority of tasks

Ci Pipeline
![Project 2 CI](https://user-images.githubusercontent.com/101715806/169772170-1f7159a6-8d5c-4f95-8e48-425edd80f309.PNG)

Here is the CI piplene layout for the project displaying the way all the services used interact with eachother and the progession of code thorughout the application

## Infrastrcuture

## Jenkins

Jenkins uses the following command to build and push docker images

pipeline {
    agent any
    
    stages {
        stage('Clone Repo') {
            steps {
                script{
                    if(fileExists('/home/jenkins/.jenkins/workspace/Project2/Project3')){
                        sh 'cd Project3 && git pull'
                    }
                    else{
                        sh 'git clone https://github.com/EthanWright98/Project3'
                    }
                }
            }
        }
        stage('Installs'){
            steps {
                sh 'pip3 install -r Project3/api1/application/requirements.txt' 
            }
        }
        stage('Build & Push'){
            steps{
                sh 'cd Project3 && sudo docker-compose build'
                sh 'cd Project3 && sudo docker-compose push'
                
            }
        }
        stage('Deploy'){
            steps{
                sh 'cd Project3 && sudo docker-compose up -d'
            }
        }
    }
}

 ## Docker Swarm and Ansible 
 
 Docker swarm was used within the project across different VMS to configure the docker manager and worker being used as an orchstration tool to deploy the app
 
 Ansible was used along docker with an inventory.yaml and a playbook.yaml to set up roles for the VM's
 
 ## Nginx
 
 Nginx is used as a load balancer spreading traffic to the application across different servers, increasing the application speed and its potential for scalability
 
## Future improvements

Implement full testing into the app allowing for secuirity and robustness

Implent Jenkins properly so it could automate testing and deploy the application
