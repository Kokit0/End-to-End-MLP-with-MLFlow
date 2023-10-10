# End-to-End Machine Learning Proyecto de Implementación Continua CICD y MLOps con MLflow


## Descripción General

Bienvenido a este proyecto de implementación continua y MLOps con MLflow. Este proyecto se enfoca en proporcionar una guía detallada sobre cómo construir un proyecto de Machine Learning de extremo a extremo, desde la ingesta de datos hasta la implementación de modelos en producción.

Aquí, no solo nos centraremos en el producto final, sino que también documentaremos cuidadosamente cada paso del proceso y las estrategias utilizadas para su construcción. Nuestro enfoque se basa en el uso de Jupyter Notebooks para escribir y organizar el código de cada fase del proyecto.

### Objetivo del Proyecto

Este proyecto no solo busca la implementación de un producto de extremo a extremo, sino que también tiene como objetivo documentar cada paso y estrategia utilizada en su construcción. Utilizaremos Jupyter Notebooks como nuestra base de trabajo, donde escribiremos el código para cada fase del proceso. El proyecto abarca desde la preparación inicial de los datos (ingestión) hasta la validación de tipos y formatos, la transformación de datos para su uso en modelos (transformación), el entrenamiento del modelo (entrenamiento) y finalmente, la evaluación del modelo (evaluación).

- Preparación inicial de los datos: Ingestión de datos y transformación de formatos.
- Validación de tipos y formatos esperados en los datos de entrenamiento y prueba.
- Transformación de los datos para su uso en modelos de Machine Learning.
- Entrenamiento de modelos y evaluación del rendimiento.
- Creación de un flujo de trabajo de implementación continua (MLOps) con MLflow.
- Integración con GitHub Actions y servicios de microservicios en la Nube de Amazon Web Services (AWS).

## Estructura del Proyecto

A medida que avanzamos en el proyecto, llenamos los datos, archivos y carpetas de acuerdo con un orden predefinido que sigue una lógica clara. Cada etapa del proyecto se denomina "stages" (etapas) y se numeran del 1 al 6 para mantener un seguimiento estructurado. Al completar cada etapa, migraremos el código a un pipeline, que se ejecuta siguiendo las instrucciones definidas en nuestra configuración y el orden especificado en el archivo main.py. Utilizamos un archivo de configuración (params.yaml) y un archivo de requisitos (requirements.txt) para establecer los parámetros y requisitos mínimos del proyecto. Por supuesto estos son solo los necesarios que definí para alcanzar un proceso fluido y sencillo. De querer agregar mas modelos se deberá actualizar este proceedimiento acorde a los intereses que ustedes tengan.

## Construyendo el Pipeline

Este proceso de construcción sigue un orden específico y nos permite desarrollar el pipeline completo paso a paso. Conforme avanzamos en cada fase, volvemos al inicio para garantizar que sigamos el mismo orden al construir la siguiente etapa. Al final, completaremos nuestra implementación continua (MLOps) utilizando Dagshub para orquestar el flujo de trabajo de Machine Learning con MLFlow. Luego, integramos el proyecto con las acciones de GitHub, conectándolo con los servicios de microservicio en la Nube de Amazon Web Services (AWS).


Este proyecto es ideal para aquellos que desean aprender cómo desarrollar y desplegar proyectos de Machine Learning de manera efectiva, siguiendo las mejores prácticas de MLOps y la implementación continua, de forma simple.


## Estructura del Proyecto

### Fases del Proyecto

1. Actualizar `config.yaml`
2. Actualizar `schema.yaml` (ordenar columnas y definir atributos)
3. Actualizar `params.yaml`
4. Definir la entidad
5. Configurar el administrador de configuraciones en `src/config`
6. Definir los componentes (propiedades de datos para ingestión, validación, entrenamiento, etc.)
7. Crear el pipeline (dividido en ingestión y entrenamiento)
8. Configurar `main.py`
9. Crear la aplicación web `app.py` (integración de todas las funcionalidades)


## Partamos por acá:
### Pasos para Ejecutar el Proyecto

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Kokit0/End-to-End-MLP-with-MLFlow.git
   ```

2. Crear un entorno de conda después de abrir el repositorio:

   ```bash
   conda create -n mlproj python=3.8 -y
   ```

3. Activar el entorno:

   ```bash
   conda activate mlproj
   ```

4. Instalar los requisitos:

   ```bash
   pip install -r requirements.txt
   ```

5. Ejecutar la aplicación:

   ```bash
   python app.py
   ```

6. Acceder a través de tu localhost y puerto.

## Integración de Dagshub

[Dagshub](https://dagshub.com/) es una parte integral de nuestro proceso de desarrollo. Utiliza el siguiente comando para exportar variables de entorno antes de ejecutar scripts:

dagshub
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

## Implementación de AWS-CICD-Deployment con GitHub Actions

Este proyecto incluye la implementación de AWS utilizando GitHub Actions. Aquí te explicamos cómo configurar y utilizar servicios de AWS para tu proyecto.

### Paso 1: Inicio de Sesión en la Consola de AWS

Inicia sesión en la consola de AWS.

### Paso 2: Creación de un Usuario IAM para la Implementación

1. Crea un usuario IAM para gestionar la implementación.

2. Asigna permisos específicos al usuario, incluyendo acceso a EC2 y ECR. 

```
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

```

### Paso 3: Creación de un Repositorio ECR

3. Crea un repositorio ECR para almacenar y gestionar las imágenes de Docker del proyecto. Guarda la URI del repositorio.

```
#ECR repo to store/save docker image
- Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj
```

### Paso 4: Creación de una Máquina EC2

4. Crea una instancia EC2 con un sistema operativo Ubuntu.

5. Instala Docker en la instancia EC2 para gestionar las imágenes de Docker.

Open EC2 and Install docker in EC2 Machine:
	
```
	#opcional

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
```

### Paso 5: Configuración de EC2 como Runner Autogestionado

5. Configura EC2 como runner autogestionado de GitHub
```
#self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one
``` 

### Paso 6: Configuración de Secretos en GitHub

6. En la configuración de tu repositorio de GitHub, agrega los siguientes secretos:

``` 
- `AWS_ACCESS_KEY_ID`: ID de acceso de AWS
- `AWS_SECRET_ACCESS_KEY`: Clave de acceso secreta de AWS
- `AWS_REGION`: Región de AWS (ejemplo: us-east-1)
- `AWS_ECR_LOGIN_URI`: URI de inicio de sesión de ECR (ejemplo: 566373416292.dkr.ecr.ap-south-1.amazonaws.com)
- `ECR_REPOSITORY_NAME`: Nombre de tu repositorio ECR (ejemplo: simple-app)
``` 

## Pasos de MLflow

Puedes ejecutar MLflow utilizando el siguiente comando:

```bash
mlflow ui
```
#### Notas sobre MLflow

Este proyecto utiliza MLflow para el rastreo y gestión de experimentos de Machine Learning. MLflow es una herramienta de producción que permite rastrear, registrar y etiquetar todos los experimentos y modelos. Puedes aprender más sobre MLflow en su [documentación](https://mlflow.org/docs/latest/index.html).

## Lista de Herramientas Principales

A continuación, se presenta una lista resumida de las herramientas clave utilizadas en este proyecto:

- [Jupyter Notebooks](https://jupyter.org/)
- [Conda](https://docs.conda.io/en/latest/)
- [MLflow](https://mlflow.org/)
- [Dagshub](https://dagshub.com/)
- [AWS (Amazon Web Services)](https://aws.amazon.com/)
- [GitHub Actions](https://github.com/features/actions)
- [Docker](https://www.docker.com/)


## Contribuciones

Si deseas contribuir a este proyecto, no dudes en crear una solicitud de extracción o informame sobre problemas que estes teniendo. 
¡Estaré feliz de discutir inquetudes e implementarle mejoras!

_____

## Agradecimientos
- a @KrishNaik por enseñarme Dagshub!