from fastapi import FastAPI, Response

from starlette.status import *

import random
from datetime import datetime

app = FastAPI()

@app.get("/")
def index():
    return {
        "data" : "Simple API for TE-INF 2025!"
    }

students = [
    'AMANDA SCHEIDT',
    'ANDRE DE CONTO NETO',
    'ANITA AMABILE DE BONA',
    'ARTHUR ALF VARELA',
    'AUGUSTO MACIEL FERREIRA',
    'DAVI BAZZANELLA KUHN',
    'EMANUELLE AMARAL SEBEN',
    'GABRIEL DE SOUSA DRACZESKI',
    'GUILHERME GAMA DA SILVA',
    'GUSTAVO DE OLIVEIRA TURCHETTO',
    'GUSTAVO ORNAGHI COUSSEAU',
    'HELIO BORSTMANN NETO',
    'JULIA BARCELOS ALMEIDA',
    'KAIO MANFRO DA SILVA',
    'LARA CANALI DE LIMA',
    'LETÍCIA GONÇALVES SKOREK',
    'MATEUS JUNGES DE SOUZA',
    'MAYSSON PICOLI',
    'MIGUEL FREITAS DA ROSA',
    'MIGUEL MOURA TERNES BAEZ',
    'PEDRO AUGUSTO BARTELLE',
    'VINICIUS DE OLIVEIRA REGNER',
    'YASMIM SACOL BITENCOURT',
    'YURI IVAN ALTHAUS',
    'YURI WITT KOVALEVICH',
]

@app.get("/student/")
def getStudentName():
    studentName = students[random.randint(0, len(students))]
    dt = datetime.now()

    return {
        'timestamp' : dt.strftime("%d-%m,%H:%M:%S"),
        'student_name' : studentName
    }

"""
rfidAccessControlTMP = {
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
"""

rfidAccessControl = {
    '7041231266' :      { "name": "Rafaela Oliveira", "access" : True },
    '271819227210' :    { "name": "Tiago Santos", "access" : True },
    '912033327170' :    { "name": "Carolina Silva", "access" : True },
    '3412924211104' :   { "name": "João Pereira", "access" : True },
    '59819027150' :     { "name": "Mariana Costa", "access" : True },
    '54160146141137' :  { "name": "Pedro Rodrigues", "access" : True },
    '17104427156' :     { "name": "Ana Martins", "access" : True },
    '219229927181' :    { "name": "Lucas Ferreira", "access" : True },
    '591173227117' :    { "name": "Beatriz Gomes", "access" : True },
    '13919919327150' :  { "name": "Gabriel Sousa", "access" : True },
    '25101952735' :     { "name": "Sofia Almeida", "access" : True },

    '5512514363250' :   { "name": "Miguel Ribeiro", "access" : False },
    '139791323397' :    { "name": "Laura Carvalho", "access" : False },
    '392504060201' :    { "name": "Matheus Fernandes", "access" : False },
    '29825521157' :     { "name": "Julia Nunes", "access" : False },
    '155137993380' :    { "name": "Guilherme Gonçalves", "access" : False },
    '210133712711' :    { "name": "Isabella Santos", "access" : False },
    '11912220459250' :  { "name": "Enzo Lima", "access" : False },
    '985514631216' :    { "name": "Giovanna Pereira", "access" : False },
    '199214363117' :    { "name": "Leonardo Oliveira", "access" : False },
    '1082143197124' :   { "name": "Valentina Silva", "access" : False },
    '1401962197143' :   { "name": "Daniel Rodrigues", "access" : False },
    '2315210760216' :   { "name": "Larissa Costa", "access" : False },
    '2475714263127' :   { "name": "Lucas Ferreira", "access" : False },
    '187793616192' :    { "name": "Clara Gomes", "access" : False },
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
        "id" : id,
        "name" : accessData["name"],
        "access" : accessData["access"]
        
    }
