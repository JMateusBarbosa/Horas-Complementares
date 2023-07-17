from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email
from flask_mysqldb import MySQL
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)

# Configuração do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'horas_complementares'

mysql = MySQL(app)


class RegistrationForm(FlaskForm):
    Nome = StringField('Nome de usuário', validators=[InputRequired(), Length(min=4, max=20)])
    Email = StringField('E-mail', validators=[InputRequired(), Email(message='E-mail inválido'), Length(max=50)])
    Senha = PasswordField('Senha', validators=[InputRequired(), Length(min=8, max=80)])


@app.route('/')
def home():
    form = RegistrationForm()
    return render_template('register.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        Nome = form.Nome.data
        Email = form.Email.data
        Senha = form.Senha.data

        # Verificar se o nome de usuário já está cadastrado
        conn = mysql.connection
        cursor = conn.cursor()
        query = "SELECT * FROM Alunos WHERE Nome = %s"
        cursor.execute(query, (Nome,))
        result_username = cursor.fetchone()

        # Verificar se o e-mail já está cadastrado
        query = "SELECT * FROM Alunos WHERE Email = %s"
        cursor.execute(query, (Email,))
        result_email = cursor.fetchone()

        if result_username or result_email:
            # Nome de usuário ou e-mail já cadastrados, exibir mensagem de erro
            error_message = "Nome de usuário ou e-mail já existem"
            return render_template('register.html', form=form, error_message=error_message)
        else:
            # Inserir os dados do usuário no banco de dados
            query = "INSERT INTO Alunos (Nome, Email, Senha) VALUES (%s, %s, %s)"
            cursor.execute(query, (Nome, Email, Senha))
            conn.commit()
            cursor.close()
            conn.close()

            return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/database_check')
def database_check():
    try:
        conn = mysql.connection
        if conn:
            return "Conexão com o banco de dados estabelecida. Pronto para receber dados."
        else:
            return "Erro ao conectar ao banco de dados."
    except Exception as e:
        return f"Erro ao conectar ao banco de dados: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)
