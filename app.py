from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Endpoint principal que retorna uma mensagem de sucesso.
    Isso confirma que a aplicação está no ar.
    """
    return "<h1>Docker está funcionando!</h1><p>Sua aplicação Flask foi iniciada com sucesso dentro do contêiner.</p>"

# Opcional: Um endpoint de 'health check' é uma boa prática
@app.route('/health')
def health_check():
    """
    Endpoint simples para verificar a saúde da aplicação.
    """
    return {"status": "ok"}, 200