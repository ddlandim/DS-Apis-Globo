# Desafio: Desenvolvedor Backend - Produtos de dados
Autor : Douglas Diniz Landim  
Email : douglas.diniz.landim@accenture.com
# Documento do desafio técnico:

![DesafioTecnico_ProdutoDados.pdf](/DesafioTecnico_ProdutoDados.pdf)

# Informação de Fornecedor do Projeto
 - Razão Social: Accenture do Brasil
 - CNPJ: 
 - Código de Serviço: 
 - Responsável Geral: 
 - Departamento Fornecedor de Serviço: AGBG
 - Líder Direto: Alexandre Coutinho, alexandre.l.coutinho@accenture.com

# Informações Gerais

Este projeto consiste no desenvolvimento de um script de proprocessamento de dados, com 2 conjuntos históricos de dados de entrada, que realiza estimativas de audiência através deste conjunto calculando para cada registro a mediana dos 4 ultimos registros de audiencia média. O conjunto final é armazenado em memória por uma API que fornece as estimativas através de requisições.

## Envolvidos na elaboração e Requisição

| Nome |  Área | E-mail | Responsável por |  
|:-----|:---:|:----| :-----: | 
|Júlio Vieira Ferreira|Application Development|j.vieira.ferreira@accenture.com|Contato com o cliente e solicitação do desafio|
|Douglas Diniz Landim|Data & A.I|douglas.diniz.landim@accenture.com|Desenvolvedor envolvido no desafio|

## Objetivos da API

 - Preprocessamento e calculo:  
  Preprocessar o conjunto de dados de historico de audiência e estimar uma audiencia com a mediana de audiencia para cada registro com um intervalo dos 4 dias anteriores, filtrando a data, local da transmissão e programa transmitido.
 - Preprocessamento:  
   Carregar o conjunto de dados com o tempo disponível de anuncios.
 - Preprocessamento:  
   Unir os 2 conjuntos de dados
 - Rota API /get_program:  
   Fornecer os dados de audiencia estimada e tempo disponível para anuncio de um programa, através de uma requisição REST-API, com os parâmetros de data do programa, local de transmissão, e código do programa. 
- Rota API /get_period:  
   Fornecer os dados de audiencia estimada e tempo disponível para anuncio de uma lista de programas, através de uma requisição REST-API, com os parâmetros de data de inicio e fim em um intervalo temporal no conjunto de dados.

## Criticidade
- Media: Caso esta API falhe, processos de b.i e modelos estimativos podem ser bloqueados. 

- Prioritária: A API deve esta sempre ativa e disponível, o pro=e

# Requisitos
Requisitos necessários para o desenvolvimento e execução da API.
## Requisitos Funcionais

- P1:  
  Fornecer em arquivo .csv, conjunto de dados de historico de audiencias para o calculo de estimativas de audiencias através da mediana de datas anteriores.
- P2:  
  Fornecer em arquivo .csv, conjunto de dados de historico de tempo disponível para anuncios congruentes na data, local de transmissão e código do programa dos dados fornecidos no conjunto historico de audiencias.

## Requisitos de ambiente:
 - E1:  
  Miniconda 3 compatível com Python 3.8.5
  - E2:  
  Gerenciador de pacotes NPM
## Informações para Requisição

![Swagger : Especificações da API em OPENAPI 3.0](/specs_api/specs_api.yaml)

A API em execução tem as seguintes 2 rotas de requisição.
- GET ​/get_period : obterPeriodo
  Método que retorna os programas, tempo previsto e tempo disponível para anuncios em um determinado período fornecido
  - Parâmetros:
    - begin : Formato date yyyy-mm-dd
    - end : Formato date yyyy-mm-dd

- GET ​/get_program : obterPeriodo
  Método que retorna uma estimativa de audiência e o tempo disponível para anuncios, para um determinado programa e data de exibição
  - Parâmetros: 
    - program_code  : Formato string
    - date : Formato date yyyy-mm-dd

### Possui dados sensíveis cobertos pela LGPD? 
  - [ ] sim
  - [X] não

- Caso afirmativo, quais?

# Execução do projeto:

Em um terminal miniconda executando na raiz do projeto execute:

## Instalação das dependencias com o gerenciador de pacotes NPM
```
$ npm install
```
## Configuração do ambiente python
Este comando instala um ambiente de execução no diretório ./env com a configuração dos pacotes flask, pandas, numpy. O pacote jupyter é instalado para verificação do notebook de experimentos.
```
$ npm run conda_env
```
## Ativação do ambiente python
Este comando ativa o ambiente instalado na etapa anterior
```
$ npm run conda_act
```
## Testes unitários do código python de processamento
Este comando executa o script python de testes unitários das funções de carregamento dos conjuntos de dados e da função de calculo da mediana
```
$ npm run pytest
```
## Execução da API e do projeto:
Este é o comando principal, que coloca a API em execução, executando o script python que carrega os conjuntos de dados, realiza o calculo da mediana e os proceprocessamentos, armazena em memória o conjunto de dados resultante, configura as rotas da API e a coloca em execução para atender as requisições e realizar consultas no conjunto de dados resultante.
```
$ npm run api
```
## Teste de integração da API com newman
Com a API em execução é possível realizar testes de integração com as rotas da API.
Em um novo terminal miniconda executando na raiz do projeto, execute:
```
$ npm run newman
```
# Artefatos Relacionados

ID do Artefato | Nome do Artefato | Ferramenta | Link do Artefato | Tipo | Versão |
:---:  | :--------------- | :---:   | :-------------| :----- | :---:  |
|1| Conjunto de dados de tempo disponível| .csv | Data/tvaberta_inventory_availability.csv(1).csv | Fornecido | 1.0
|2 | Conjunto de dados de media de audiências| .csv | Data/tvaberta_program_audience.csv | Fornecido | 1.0
|3 | Stub de testes do conjunto de estimativas| .csv | Data/tvaberta_program_audience(1)_test.csv | Gerado | 1.0
|4 | Funcoes de preprocessamento | Python | Functions/functions.py | Gerado | 1.0
|5 | Teste das funcoes de preprocessamento | Python | Functions/test_functions.py | Gerado | 1.0
|6 | Notebook de testes e desenvolvimento | Jupyter notebook | Notebooks/experimentos.ipynb | Gerado | 1.0
|7 | Arquivo de especificações da API em formato OPEN-API 3.0 | Swagger UI | specs_api/specs_api.yaml | Gerado  | 1.0
|8 | Conjunto de variáveis de teste de integração da API | newman,postman | tests_api/Datas.postman_scenario.csv | Gerado  | 1.0
|9 | Postman collection de teste de integração da API | newman,postman | tests_api/Globo_tests.postman_collection.json | Gerado | 1.0
|10 | Script principal da API para processamento dos dados e execução da API | Python | api.py | Gerado | 1.0
|11 | Configurações de dependencias e scripts do projeto | NPM | package.json | Gerado | 1.0
|12 | Postman collection para interagir com a API em execução | POSTMAN | Globo.postman_collection.json | Gerado | 1.0
# Critérios de Aceitação

- [x] Testes unitários de preprocessamento
- [x] Testes de integração da API
- [ ] Homologação dos dados estimados


# Prazos e Entregas

| Data de                 |      Prazo |
|:------------------------|-----------:|
| Solicitação | 11/03/2020 |
| Inicio do desenvolvimento | 22/03/2020 |
| Entrega pra Homologação | 25/03/2020 |
| Entrega em Produção     | dd/mm/YYYY |

| Revisão | Tempo |
|:--------|-------|
|         |       |

# Release Notes
## 24/03/2020
### 1.0 
Primeira versão da API pronta para execução, porém os artefatos 1 e 2 estão com intervalos temporais distintos não sendo possível mesclar a informação de audiência prevista e tempo disponível de anúncio em um mesmo registro.  
Portanto o conjunto de dados resultados gerenciado pelo artefato 10 para as resquisições, conterá falha de audiência estimada ou tempo alocado para anuncios de acordo com data solicitada de um registro.

# Referencias
- Dependência E1: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
- Dependência E2:  
  https://docs.npmjs.com/creating-a-package-json-file
- Artefato 10: API  
  https://medium.com/trainingcenter/flask-restplus-ea942ec30555  
  https://blog.4linux.com.br/api-em-python-flask-decorators-e-pytest-para-validacao-de-credito/

- Artefato 7:  
[OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md)  
[Visualizador Online](https://editor.swagger.io/)
- Artefatos 8, 9, 12:  
[Examples Postman](https://learning.postman.com/docs/sending-requests/examples/)  
[Collection Postman](https://learning.postman.com/docs/getting-started/creating-the-first-collection/)  
[Import and Export - Postman](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/)  
[Learning Postman](https://learning.postman.com/)