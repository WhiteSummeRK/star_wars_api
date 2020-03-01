# star_wars_api
Projeto utilizando a swapi


# Funcionamento do projeto

Utilizando a API swapi.co/ este projeto faz a listagem de todos personagens e suas caracteristicas
na url /character, e todas as suas naves e os respectivos scores na url /ships.

# Rodando os testes

WORKDIR: star_wars_api/star_wars_api/

COMMAND: coverage run --source . -m unittest discover -s tests -v

# Subindo o ambiente docker

- docker build -t <image_name> .
- docker run -d -p 5000:5000 <image_name>

Amazon URL:

characters: http://star-wars-api-dev.eu-west-2.elasticbeanstalk.com/character/
ships: http://star-wars-api-dev.eu-west-2.elasticbeanstalk.com/ships/

Também foi criado um simples index.html na url: http://star-wars-api-dev.eu-west-2.elasticbeanstalk.com/
