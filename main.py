from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def mensaje():
    return 'oli'

@app.get('/{nombre}/{codigo}')
def mensaje_n_c(nombre:str,codigo:int):
    return f'Bienvenido {nombre} su codigo es {codigo}'

@app.get('/uno')
def mensaje_edad(edad:int):
    return f'tu edad es {edad}'