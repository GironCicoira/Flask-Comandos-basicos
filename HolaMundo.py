from flask import Flask

app = Flask(__name__)#nuevo objeto,

@app.route('/')#wrap o un decorador
def index(): #funcion
    return 'Hola Mundo' #regresar  un string

app.run() #Ejecutar el servidor