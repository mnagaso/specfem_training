# specfem_training

This github repository contains information for specfem's cheese training session 2021.
In this file, we explain how to open the jupyter lab with the pyspecfem's docker image.


## Install docker
Docker may be installed for Linux/Windows/OSX by following the docker's [official homepage](https://docs.docker.com/get-docker/)

## Install docker compose
Please check if docker-compose command is available on your terminal.  
[Here](https://docs.docker.com/compose/install/) you can find an instruction for installing it.  

## Launch preconfigured python/jupyter environment
0. Only for Windows/OSX user need to check if your Docker docker desctop application is started and engine is running.
1. Open a terminal window.
2. Clone this repository by the command `git clone https://github.com/mnagaso/specfem_training.git`
3. Enter this repository directory by `cd specfem_training`
4. Download and start docker image/container by the command `docker-compose up`
5. Access to localhost:8888 on your web browser.

If you find the error message like:
```
ERROR: for pyspecfem_docker_image_spec_1  Cannot start service spec: driver failed   programming  external connectivity on endpoint pyspecfem_docker_image_spec_1 (f1c7b06807902cff70e348dba40d38e0a957626432957a436b1032aebc9d3027):   
Error starting userland proxy: listen tcp4 0.0.0.0:8888: bind: address already in use

...
```
please open the docker-compose.yml file and modify the port number for the host side e.g.
```
      ports:
        - 8888:8888
```
to 
```
      ports:
        - 8889:8888
```
then when you will find an available port (which docker-compose up works), 
you can open jupyterlab by the address localhost:8889 or another port which you use in the docker-compose.yml file.


Please try `sudo docker-compose up` for the error
```
ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?

If it's at a non-standard location, specify the URL with the DOCKER_HOST environment variable. 
```


## Setup the directories on the cluster
Before starting a calculation, we need to prepare some directories on the cluster.
Please follow [this document](SETUP_CLUSTER.md).







