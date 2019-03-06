from bottle import Bottle, run

app = Bottle()

msg = '''
<center><h1>Minha página web</h1></center>
<p>Python é uma linguagem fácil de aprender, você escreve pouco e é bem didática. O curso de Python lhe fornecerá a base necessária para você programar nessa linguagem fantástica!<p>
<center><a href="/curso_python">Clique aqui para acessar o curso</a></center>
'''

@app.route('/')
def index():
	return msg

@app.route('/curso_python')
def curso():
	return '<center><h1>Bem-vindo(a) ao Curso de Python</h1></center>\
			<center><a href="/">Voltar a página principal</a></center>'

run(app, host='localhost', port=8080)