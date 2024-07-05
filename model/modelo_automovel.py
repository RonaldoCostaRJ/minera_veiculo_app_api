#Última alteração: 06/07/2024 por: Ronaldo Ramos da Costa
#######################################################################
#importa os tipos de dados que serão utilizados
from sqlalchemy import Column, String, Integer, DateTime,Float

from datetime import datetime
from typing import Union

from  model import Base

##clase base que é utilizada para representar as informações de uma busca por um modelo de automóvel via webscrapping.
class Modelo_Automovel(Base):
    __tablename__ = 'modelo_automovel'    
    id_busca_modelo = Column("id_busca_modelo", Integer, primary_key=True)
    marca_modelo = Column(String(25))
    nome_modelo = Column(String(50), unique=True )     
    categoria_modelo = Column(String(30))
    tipo_modelo = Column(String(20))
    tipo_cambio_modelo = Column(String(15))
    ano_desde_modelo = Column( Integer)
    ano_ate_modelo = Column( Integer)
    valor_desde_modelo = Column(Float)
    valor_ate_modelo = Column(Float)
    km_desde = Column(Integer)
    km_ate = Column(Integer)
    regiao_busca = Column(String(50))
    data_insercao = Column(DateTime)
    ##################################################################################################################

    def __init__(self, marca_modelo_in:str, nome_modelo_in:str, categoria_modelo_in:str, tipo_modelo_in:str,tipo_cambio_modelo_in:str,
                ano_desde_modelo_in: int, ano_ate_modelo_in: int, valor_desde_modelo_in: float, valor_ate_modelo_in: float, km_desde_in:int, km_ate_in: int, regiao_busca_in:str, data_insercao_in:Union[DateTime, None] = None):
        """
        Cria um Modelo_Automovel

        Argumentos:            
            marca_modelo: nome da marca do modelo de automóvel a ser pesquisado. Exemplo: Fiat / VolksWagen / Renault / Chevrolet / Ford
            nome_modelo: nome do modelo de automóvel. Exemplo: Palio / Gol / Fusca / Pulse/ Uno / Corola
            categoria_modelo: Detalhe da categoria de Automóvel. Exemplo: Carros / Caminhões / Ônibus 
            tipo_modelo: Detalhe do tipo de Automóvel quanto ao porte e utilidade. Exemplo: Hatch / SUV / Sedã / Pick-up / Conversível / Caminhão Leve / Buggy / Van/Utilitário. 
            tipo_cambio_modelo: Detalhe do câmbio. Exemplo: Automático / Manual / Semi-Automático / Automatizado.
            ano_desde_modelo: Indica o ano inicial de fabricação que interessa na busca. Em conjunto com o ano_ate_modelo, forma um range do período de busca: Exemplo: 2019 --> (2019 a 2022)
            ano_ate_modelo: Indica o ano final de fabricação que interessa na busca. Em conjunto com o ano_desde_modelo, forma um range do período de busca: Exemplo: 2022 --> (2019 a 2022)
            valor_desde_modelo: valor inicial do intervalo que interessa na busca
            valor_desde_modelo: valor final do intervalo que interessa na busca
            km desde: km inicial do intervalor que interessa na busca. 5000 a 20000 (carros novos)
            km ate: km final do intervalo que interessa na busca 5000 a 20000 (carros novos)
            regial busca: região do RIo de Janeiro que interessa na busca. Ex: Zona sul / Zona norte
            data de inserção da busca. Define a data de inclusão da busca no sistema.
            
        """
        # Inicialização dos dados durante a instanciação da classe.
        self.marca_modelo = marca_modelo_in
        self.nome_modelo = nome_modelo_in        
        self.categoria_modelo = categoria_modelo_in
        self.tipo_modelo = tipo_modelo_in
        self.tipo_cambio_modelo = tipo_cambio_modelo_in
        self.ano_desde_modelo = ano_desde_modelo_in
        self.ano_ate_modelo = ano_ate_modelo_in
        self.valor_desde_modelo = valor_desde_modelo_in
        self.valor_ate_modelo = valor_ate_modelo_in
        self.km_desde = km_desde_in
        self.km_ate = km_ate_in
        self.regiao_busca = regiao_busca_in
       
        # Caso a data de inserção não seja informada, será registrado a data exata da inserção no banco.
        if data_insercao_in:
            self.data_insercao = data_insercao_in
        else: 
            self.data_insercao = datetime.now()
