# Imagem base do Python
FROM python:3.10-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar os arquivos de requisitos para o contêiner
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o projeto para dentro do contêiner
COPY . .

# Definir a variável de ambiente para o Django usar o modo de produção
ENV DJANGO_SETTINGS_MODULE=primeiraAula.settings

ENV DB_NAME=${DB_NAME}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_PORT=${DB_PORT}

RUN echo ${DB_NAME}
RUN echo ${DB_USER}
RUN echo ${DB_HOST}
RUN echo ${DB_PORT}
# Coletar arquivos estáticos durante o build
RUN python manage.py collectstatic --noinput

# Rodar as migrações durante o build (só funcionará se o banco de dados estiver acessível)
RUN python manage.py migrate --noinput

# Expor a porta que o contêiner vai usar
EXPOSE 8000

# Rodar o servidor Gunicorn para produção
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "primeiraAula.wsgi:application"]
