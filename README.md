## **Hi there 👋**

# Docker containers and networks exercise 1

**This project is a part of COMP.SE.140 course at Tampere University, and its sole purpose is to indicate competence in using docker networks and containers in order to build an internetconnected services which exhange messages in 2 second intervals and are able to shutdown by themselves after 20 iterations after a STOP signal has been received.**


## DEMO

## Prerequisites
You should have [**Docker**](https://docker.io)  installed in your local machine and [**docker-compose**](https://docs.docker.com/compose/).



## Installation

Install  [**Docker**](https://docker.io) in your local machine and [**docker-compose**](https://docs.docker.com/compose/) if you don't have it already.

**Clone repository**
$ git clone -b exercise1 https://github.com/ipanagiotopoulos/devops_tampere.git

$ docker-compose up --build

#### wait a minute

$ docker-compose down
$ more logs/service1.log


## Usage

**Workspace** is located under **InternshipsApp** folder.

This stack contains two different containers

```version: '3.8'
services:
  django:
    image: django-service1
    container_name: yiannis_pana_django_devops
    build:
      dockerfile: ./application_django/Dockerfile
      context: .
    env_file:
      -  ./application_django/.env
    ports:
      - "7539:7539"
    volumes:
      - ./application_django/devops:/application_django
      - ./logs/service2.log://application_django/logs/service2.log
    networks:
        dev_ops_ex1:
          ipv4_address: 172.21.0.2
  nodejs:
    image: nodejs-service2
    container_name: yiannis_pana_nodejs_devops
    build:
      dockerfile: ./application_node_js/Dockerfile
      context: .
    env_file:
      -  ./application_node_js/.env
    ports:
      - "8000:8000"
    volumes:
      - ./application_node_js:/application_node_js
      - ./logs/service1.log:/application_node_js/logs/service1.log
    depends_on:
        - django
    networks:
       dev_ops_ex1:
          ipv4_address: 172.21.0.3
networks:
  dev_ops_ex1:
    name: devops_yiannis_pana_exercise_one
    ipam:
      config:
        - subnet: 172.21.0.0/16
          ip_range: 172.21.0.0/24
    external: false #internal network
volumes:
  static_volume: null
```

## yiannis_pana_django_devops 
**django-service1** is a service instance of a container which is  based on a python alpine image and it runs a web app which has been implemented in Django Web Framework(DRF and Django), aka service_2 which is receiving the HTTP requests made by  the **nodejs** service
- The source code is located under the **/application_django/devops/** folder and the script **init.sh** provides some helpful automations while deploying the app into the aforementioned container.
- Ensure that all **.env** fields are filled for the successfull run of the script and hence the service.
- Under the same folder there is a log folder which contains the logs and it has been mounted to the host machine filesystem via this volume  **/logs/service2.log://application_django/logs/service2.log**, and this was merely used for debugging reasons.
     
## yiannis_pana_nodejs_devops 
**nodejs** in a similar fashion is a service which has been implemented in Node.js and Express frameowrk, aka service_1 which sends requests to the service_2 every 2 seconds until it finally sends a STOP message which triggers the POST endpoint route of the Django application or **django**
service, where we sent a SIGINT signal in order to shut down our server via killing the running process which is run on **yiannis_pana_django_devops**
- The source code is located under the **/application_node_js/** folder
- Ensure that all **.env** fields are filled for the successfull run of the index.js which iniates the node.js server instance inside the container.
- Under the same folder there is a log folder which contains the logs and it has been mounted to the host machine filesystem via this volume  **/logs/service1.log://application_node)js/logs/service2.log**, and this was merely used for debugging reasons.

**After the shutdown of yiannis_pana_django_devops**, and the 20th iteration of logging  messages and sending HTTP requests the **yiannis_pana_nodejs_devops** docker service instance shuts down after the STOP signal has been sent to **service_1** via using **process.exit(0)** in the **app.listen() method

in **/application_node_js/index.js** file

Logs of both services can be found under the logs folder with their respective names **service1.log** and **service2.log**


