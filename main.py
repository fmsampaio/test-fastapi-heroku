from fastapi import FastAPI

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

