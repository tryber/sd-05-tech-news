FROM mongo:latest
RUN mkdir technews
COPY --from=python:latest . .
WORKDIR /technews
COPY . .
# Instalando as dependências
RUN apt-get update && apt-get install -y \
    python3-venv
RUN python3 -m venv .venv && \
    python3 -m pip install -r dev-requirements.txt

# Para rodar o container:
# docker run -it --name=technews -v $PWD/tech_news:/technews/tech_news lizzardmedeiros/technews bash
# > mongod --fork --logpath /var/log/mongod.log