#Última alteração: 06/07/2024 por: Ronaldo Ramos da Costa
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importa os elementos definidos no modelo
from model.base import Base
from model.modelo_automovel import Modelo_Automovel

db_path = "database/"
# Verifica se o diretorio já existe ou se é preciso criar um novo.
if not os.path.exists(db_path):
   # Caso não exista, então cria o diretorio.
   os.makedirs(db_path)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url) 

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)
