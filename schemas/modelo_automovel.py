#Última alteração: 06/07/2024 por: Ronaldo Ramos da Costa
#######################################################################
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from model.modelo_automovel import Modelo_Automovel

#######################################################################
#####     Definição dos schemas utilizados na API    ##################
#######################################################################

class Modelo_AutomovelSchema(BaseModel):
    """ Define como um novo modelo de automóvel a ser inserido, deve ser representado.
    """
    
    regiao_busca : str = "RJ, Zona Sul"
    categoria_modelo : str = "Carros"
    marca_modelo : str = "Fiat"
    tipo_modelo : str = "Hatch"
    tipo_cambio_modelo : str = "Automático"
    nome_modelo  : str = "Pulse"
    ano_desde_modelo : int = 2020
    ano_ate_modelo : int = 2024
    km_desde : int = 15000
    km_ate :int = 90000
    valor_desde_modelo : float = 20000
    valor_ate_modelo : float = 100000
    

class Modelo_AutomovelBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a pesquisa de uma busca, feita com base no nome do Modelo do automóvel.
    """
    nome_modelo  : str = "Pulse"
  

class ListagemModelo_AutomovelSchema(BaseModel):
    """ Define como uma listagem de buscas por modelos cadastradas, será retornada.
    """
    modelos_auto:List[Modelo_AutomovelSchema]


def apresenta_modelos(modelos_auto: List[Modelo_Automovel]):
    """ Retorna uma representação de uma busca por modelo, seguindo o schema definido em
        Modelo_AutomovelViewSchema.
    """
    result = []
    for modelo in modelos_auto:
        result.append({
            "marca_modelo" : modelo.marca_modelo,
            "nome_modelo": modelo.nome_modelo,           
            "categoria_modelo": modelo.categoria_modelo,
            "tipo_modelo": modelo.tipo_modelo,
            "tipo_cambio_modelo": modelo.tipo_cambio_modelo,
            "ano_desde_modelo": modelo.ano_desde_modelo,
            "ano_ate_modelo": modelo.ano_ate_modelo,
            "valor_desde_modelo": modelo.valor_desde_modelo,
            "valor_ate_modelo": modelo.valor_ate_modelo,
            "km_desde": modelo.km_desde,
            "km_ate": modelo.km_ate,
            "regiao_busca": modelo.regiao_busca,             
            "data_insercao": modelo.data_insercao
        })

    return {"modelos_auto": result}


class Modelo_AutomovelViewSchema(BaseModel):
    """ Define como uma 'busca por modelo', será retornada: modelo_auto
    """
    id_busca_modelo : int = 1
    regiao_busca : str = "RJ, Zona sul"
    categoria_modelo : str = "Carros"
    marca_modelo : str = "Fiat"
    tipo_modelo : str = "Hatch"
    tipo_cambio_modelo : str = "Automático"
    nome_modelo  : str = "Pulse"
    ano_desde_modelo : int = 2020
    ano_ate_modelo : int = 2024
    km_desde : int = 15000
    km_ate :int = 90000
    valor_desde_modelo : float = 20000
    valor_ate_modelo : float = 100000
      

class Modelo_AutomovelDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome_modelo: str
    

def apresenta_modelo_automovel(modelo_auto: Modelo_Automovel):
    """ Retorna uma representação do registro de uma busca por modelo de automóvel, seguindo o schema definido em
        Modelo_AutomovelViewSchema.
    """
    return {
        "marca_modelo": modelo_auto.marca_modelo,
        "id_busca_modelo": modelo_auto.id_busca_modelo,
        "nome_modelo": modelo_auto.nome_modelo,       
        "categoria_modelo": modelo_auto.categoria_modelo,
        "tipo_modelo": modelo_auto.tipo_modelo,
        "tipo_cambio_modelo": modelo_auto.tipo_cambio_modelo,
        "ano_desde_modelo": modelo_auto.ano_desde_modelo,
        "ano_ate_modelo": modelo_auto.ano_ate_modelo,
        "valor_desde_modelo": modelo_auto.valor_desde_modelo,
        "valor_ate_modelo": modelo_auto.valor_ate_modelo,
        "km_desde": modelo_auto.km_desde,
        "km_ate": modelo_auto.km_ate,
        "regiao_busca": modelo_auto.regiao_busca, 
        "data_insercao": modelo_auto.data_insercao
        }