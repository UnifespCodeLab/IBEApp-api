FROM python:3.12-slim as base

# Define variáveis de ambiente úteis
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py \
    PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM base as debug

COPY requirements-dev.txt .
RUN pip install --no-cache-dir --user -r requirements-dev.txt

COPY . .

# Expõe a porta do Flask e do debugger
EXPOSE 5000
EXPOSE 5678

# Comando para rodar a aplicação com o debugger esperando um cliente se conectar
CMD ["python", "-m", "debugpy", "--wait-for-client", "--listen", "0.0.0.0:5678", "-m", "flask", "run", "--host=0.0.0.0", "--no-reload"]


FROM base as prod

# Copia o código da aplicação para a imagem final
COPY . .

EXPOSE 5000

CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "app:app"]