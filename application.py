import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

def get_db_connection():
    conexao = sqlite3.connect('blog.db')
    conexao.row_factory = sqlite3.Row
    return conexao

def get_post(post_id):
    conexao = get_db_connection()
    post = conexao.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conexao.close()
    if post is None:
        abort(404)
    return post

@app.route("/")
def index():
    conexao = get_db_connection()
    posts = conexao.execute('SELECT * FROM posts').fetchall()
    conexao.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/adicionar', methods=('GET', 'POST'))
def adicionar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        frase = request.form['frase']
        link_imagem = request.form['link_imagem']
        conteudo = request.form['conteudo']

        conexao = get_db_connection()
        conexao.execute('INSERT INTO posts (titulo, conteudo, frase, link_imagem, autor) VALUES (?, ?, ?, ?, ?)', (titulo, conteudo, frase, link_imagem, autor))
        conexao.commit()
        conexao.close()
        return redirect(url_for('index'))
            
    return render_template('adicionar.html')   