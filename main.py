from fastapi import FastAPI


app = FastAPI() # Estamos creando una instancia de FastApi
app.title = "Mi aplicaión con FastAPI"
app.version = "0.0.1"


@app.get('/', tags=['home']) # Creamos el EndPoint
def message():
    return "Hello world!"

# Para correr la aplicacion usamos el comando 'uvicorn main:app' y si queremos que se recargue automaticamente agregamos depues de app '--reload' y para asignarle un puerto '--port numero_del_puerto' y para que se pueda ver en toda la red '--host 0.0.0.0