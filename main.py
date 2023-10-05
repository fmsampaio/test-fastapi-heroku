from fastapi import FastAPI, Response

from starlette.status import *

import random
from datetime import datetime

app = FastAPI()

@app.get("/")
def index():
    return {
        "data" : "Simple FastAPI app for Heroku deployment (updated)!"
    }

students = [
    'ANA CAROLINA DA SILVA',
    'ANTÔNIO BERTHES PASTORI',
    'ARTHUR COLOGNESE BUSETTI',
    'DAVI VALÉRIO MACEDO',
    'DIEGO NATAN DA SILVA',
    'DIOGO CERENTINI',
    'EDUARDO ERNESTO PICCOLI',
    'EDUARDO STEIN GUIZZO',
    'ENZO DANIEL ZARDO',
    'FELIPE MÁRCIO FURLAN MAINARDO CARDOSO',
    'GABRIEL LOVATO VIANNA',
    'GRAZIELE LOPES DE SOUZA',
    'GUILHERME PASQUAL DE TONI',
    'GUSTAVO DE CESERO VIEIRA',
    'IURY RIBEIRO IANOSKI',
    'JOSÉ HENRIQUE NOAL',
    'KARINA MARQUES BIANCHI',
    'LÚCIO MARIO SILVESTRIN',
    'MATEUS MATANA',
    'MATEUS ROCHA BATTÚ',
    'MIKAEL FERNANDES MOREIRA',
    'MURILO BOEIRA DUTRA',
    'NICOLAS SARAIVA',
    'PIETRO DE OLIVEIRA BORTOLINI',
    'SAMIRA MARQUES',
    'SANDERSON GUGGIANA PINARELO',
    'VICTOR AUGUSTO MESNEROVICZ',
    'VITHÓRIA SOSNOSKI MATOS',
]

@app.get("/student/")
def getStudentName():
    studentName = students[random.randint(0, len(students))]
    dt = datetime.now()

    return {
        'timestamp' : dt.strftime("%d-%m,%H:%M:%S"),
        'student_name' : studentName
    }


rfidAccessControl = {
    "0000000000" : { "name": "Rafaela Oliveira", "access" : True },
    "1111111111" : { "name": "Tiago Santos", "access" : True },
    "2222222222" : { "name": "Carolina Silva", "access" : True },
    "3333333333" : { "name": "João Pereira", "access" : True },
    "4444444444" : { "name": "Mariana Costa", "access" : True },
    "5555555555" : { "name": "Pedro Rodrigues", "access" : False },
    "6666666666" : { "name": "Ana Martins", "access" : False },
    "7777777777" : { "name": "Lucas Ferreira", "access" : False },
    "8888888888" : { "name": "Beatriz Gomes", "access" : False },
    "9999999999" : { "name": "Gabriel Sousa", "access" : False },
}

@app.get("/access/{id}")
def getAccessData(id : str, response: Response):
    if id not in rfidAccessControl:
        response.status_code = HTTP_404_NOT_FOUND
        return {
            "details" : "ID not found",
        }
    
    accessData = rfidAccessControl.get(id)
    response.status_code = HTTP_200_OK
    return {
        "details" : "Success",
        "data" : {
            "id" : id,
            "name" : accessData["name"],
            "access" : accessData["access"]
        }
    }
