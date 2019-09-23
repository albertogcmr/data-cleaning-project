# ETL Project

## Intro

Proyecto personal para el porfolio de analista de datos. Se procederá a realizar una ETL de un dataset muy complejo, sucio y poco estructurado. 

## Data source

Puedes descargarte el dataset de Kaggle de [aquí](https://www.kaggle.com/teajay/global-shark-attacks/version/1). 

## Files and folders

* main.py: Contiene el código que ejecuta nuestra ETL pipeline. 
* test.ipynb: Jupyter Notebook para hacer pruebas. 
* functions: carpeta que contiene los archivos con las funciones correspondientes a ETL y auxiliares. 
* input: directorio para almacenar el csv de entrada. 
* output: directorio para guardar el resultado. 
* shark-data: directorio que contiene un archivo con un listado de tipos de tiburones que se usa en la ETL. 

## Modules

Son necesarias varias librerías en este proyecto. Por ser tan pocas no se emplea `requirements.txt`: 
```python
import re
import pandas as pd
```

## Ejecución

Ejecuta la siguiente linea de comandos en la terminal de tu equipo: 

```console
$ python3 main.py
```
