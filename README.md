# Project 3

## Introduction

https://drive.google.com/file/d/1-nuFWMe03rDLtOUY7ulSeFHac03QLYOQ/view?usp=sharing

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

![Project 2 Trello](https://user-images.githubusercontent.com/101715806/170137324-7c90b8b9-3efd-493f-8973-a49471bbee1f.PNG)


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


## Docker 

Docker is used to containerise the apis within the application and push them up to docker as images. This was done by creating a dockerfile within each of the apis.


![docker images](https://user-images.githubusercontent.com/101715806/170139380-e735d53b-c862-4bad-966a-1ed48d20638f.PNG)




 ## Docker Swarm and Ansible 
 
Docker swarm was used within the project across different VMS to configure the docker manager and worker being used as an orchstration tool to deploy the app
 
 Ansible was used along docker with an inventory.yaml and a playbook.yaml to set up roles for the VM's
 
 ## Nginx
 
 Nginx is used as a load balancer spreading traffic to the application across different servers, increasing the application speed and its potential for scalability
 
 ## Testing
 
 Testing was carried out on all the apis within the application to make sure the app is working as intended and any bugs or issues with the code can be ironed out to improve the apps strength. Below are images of all the test on my apis.
 
 ![pytest api1](https://user-images.githubusercontent.com/101715806/170138168-6a555200-71c6-4777-84d4-85f56ba0c945.PNG)
![pytest api2](https://user-images.githubusercontent.com/101715806/170138183-9e9b3753-bac1-420a-b997-554bb3db3cb2.PNG)
![pytest api3](https://user-images.githubusercontent.com/101715806/170138193-b5b32f7b-ef31-4776-a34e-d217aef8b783.PNG)
![pytest api4](https://user-images.githubusercontent.com/101715806/170138196-05ab67da-b446-4ef4-a54f-28b8053a3c26.PNG)

 
 ## Feature branch model
 
 ![Feature branch model](https://user-images.githubusercontent.com/101715806/170137425-853c65aa-0966-4e54-a57f-b07759043010.PNG)


I used the feature branch model thorughout the project for different parts of the project, using a dev branch as the worker branch and branches off of that which were worked on, this allowed me to track progress and not push any mistakes straight onto the main branch
 
 
## Future improvements

Implent Jenkins properly so it could automate testing and deploy the application

Implent nginx to spread traffic across different VM's
