# End-to-end-Machine-Learning-Project-with-MLflow


## Workflows de mi proyecto
Este proyecto busca no solo m,ontar un proyecto completo de principio a fin si no que documentar los pasos y lka estrategias decidida apra su cosnstrucción. La forma de trabajar que usaremos será basada en la creación de Jupyter Notebooks en los que iremos escribiendo el código dee cada parte del proceso, incluyendo la preparación e inclusión inicial de los datos (ingestion), validación de tipos y formatos esperados para nuestros datos de entrenamineto y testeo (validation), transformación de los datos a formato de modelamiento (transformation), entrenamiento del modelo (model training) y por último evaluación del modelo (model evaluation). Luego de desarrollar el primer notebook iremos poblando lso datos, archivos y carpetas segun nuestro orden preliminar nos inidique (Estew busca sol oser una referencia de orden logico fe trabajo). Segmentaremos el desarrollo en fases que llamaremos las "stages" (1 a 6). Al ir avanzando  nuestros notebooks, iremos transpasando a nuestro pipeline cada .py que podremos ejecutar siguiendo las instrucciones definidas en nuestra configuración y el orden ede ejecución em nuestro main.py, bajo los parametros y requerimientos que definiremos (params.yaml & requirements.txt). Este es el orden de construcción completo que nos permitirá ir creando (build) el pipeline completo paso a paso. A medida que vayam,os completando cada fase volveremos al principio para asegurarnos de que sigamos este mismo orden a la hora de construir la siguiente fase (stages). Finalizaremos seteando nuestro MLOps haciendo uso de Dagshub para montar el proceso de Machine Learning con MLFlow y luego usando Github Actions, conectarlo ocn microservicio de ERC de Amazon Web Services.
### orden preliminar
1. Update config.yaml
2. Update schema.yaml ←ordenar columnas, atributos y composición de mis tablas
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components ←data properties para ingestion/validation/training/etc
7. Update the pipeline ←separaré mi pipeline en 2 para valid/train
8. Update the main.py
9. Update the app.py ←donde pondré toda las funcionalidades UI desde la cual ir integrando todo el proyecto



# cómo lo corremos?
### PASOS:

Clone the repository

```bash
https://github.com/Kokit0/End-to-End-MLP-with-MLFlow.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

### dagshub
[dagshub](https://dagshub.com/)

'''
MLFLOW_TRACKING_URI=https://dagshub.com/Kokit0/End-to-End-MLP-with-MLFlow.mlflow \
MLFLOW_TRACKING_USERNAME=Kokit0 \
MLFLOW_TRACKING_PASSWORD=1f4de8fcdefd1528df441f1fd62e0391a267d807 \
python script.py
'''

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Kokit0/End-to-End-MLP-with-MLFlow.mlflow

export MLFLOW_TRACKING_USERNAME=Kokit0 

export MLFLOW_TRACKING_PASSWORD=1f4de8fcdefd1528df441f1fd62e0391a267d807

```


## MLflow steps

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#opcional

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model