from flask import Flask
from flaskext.mysql import MySQL



app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'horas_complementares'

mysql = MySQL(app)
@app.route('/')
def home():
    return 'Bem-vindo ao meu aplicativo!'

# Restante do código da aplicação

if __name__ == '__main__':
    app.run()