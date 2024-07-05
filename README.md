# Minera Veículos na Web (OLX)

Este pequeno projeto faz parte da entrega do MVP da Disciplina **Desenvolvimento Full Stack Básico** 


## Situação Problema


Diversos sites na WEB, publicam ofertas de anuncios, que favorecem as pessoas que os encontram primeiro. Por exemplo na OLX e no LINKEDIN, as pessoas que encontram os anuncios assim que eles são publicados levam vantagens em relação a outras pessoas que chegam mais tarde à publicação. 

No caso da OLX, um anuncio de um automóvel publicado com preço a baixo do mercado e com baixa quilometragem, apresenta-se como uma ótima oportunidade. O problema é que para encontrar estes anuncios, precisamos ficar horas realizando inumeras pesquisas e ter a sorte de sermos um dos primeiros a encontrar o anuncio, logo após sua puboicação, pois na maioria das vezes quando visualizamos uma oportunidade, ela já foi encontrada por ootra pessoa e a oportunidade já foi alcançada por alguém. No caso do Linkedin, é a mesma coisa, anuncios de emprego chegam a ter mais de 800 candidados, e seguindo a mesma lógica, mas os recrutadore, só chegam a recrutar os primeiros inscritos, pois não conseguem e nem tem tempo para observar mais de 800 currículos. Ou seja, em Âmbos os casos, quem chega primeiro na oferta, leva uma grande vantagem para conseguir fechar um bom negócio. Mas como chegar primeiro nestas oportunidades? A idéia é desenvolver e validar a possibilidade de criar um serviço/mecanismo de busca de ofertas a partir de parâmetros pré cadastrados. 


##  Objetivo
O objetivo do projeto como um todo, é desenvolver e validar um mecanismo automatizado de buscas em sites na Web, a princípio no site da OLX, utilizando tecnologia 'web scraping', para encontrar em primeira mão, oportunidades interessantes que possam gerar valor para os usuários interessados. Neste MVP, o objetivo é realizar o cadastro do interesse por buscas que possam ser automatizadas futuramente utilizando tecnologias como 'selenium pyton', a partir de parâmetros previamente cadastrados em nosso MVP. 

##  Escopo do MVP
O MVP contempla apenas o cadastro de alguns parâmetros necessários para realizar uma busca automatizada de automóveis no site da OLX. Uma tela foi desenvolvida a partir de uma pesquisa manual realizada exclusivamente para Automóveis na região do Rio de Janeiro. 

O objetivo é futuramente utilizar os dados deste MVP para experimentar uma automatização via selenium, ou outra tecnologia mais adequada. Este mesmo raciocínio poderá dar inspiração para uma busca também em outros sites como o LINKEDIN, sempre objetivando chegar antecipadamente a oferta disponível

**Funcionalidades do Escopo do MVP**
O MVP permite cadastrar uma nova 'busca por modelo de automóvel', apresenta os modelos cadastrados,viabiliza pesquisa pelo nome do modelo e realiza exclusão de interesse de buscas a partir do nome do modelo de automóvel. Uma API foi desenvolvida e sua documentação exposta via OPEN API SWAGGER, e um front end utiliza os respectivos métodos para realizar as respectivas operações.

Futuramente seão desenvolvidas novas funcionalidades como: Automatização das Buscas, comunicação quando encontrar e tela de concura dos resultados encontrados.

---
## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.


## Utilizando o BackEnd
Após a instalação, as rotas e endpoints são disponibilizados na OpenAPI/Swagger para utilização de acordo com a documentação disponível no site.



