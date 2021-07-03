from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo, cambiamos a puerto 8000 y activamos el debug para que el seridor este a la escucha.'

if __name__ == '__main__':    
    app.run(debug= True, port=8000) #cambiar de puerto 5000 al 8000 #debug True actualiza se pone a la escucha