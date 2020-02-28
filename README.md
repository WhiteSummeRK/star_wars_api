# star_wars_api
Projeto utilizando a swapi


# Funcionamento do projeto

Utilizando a API swapi.co/ este projeto faz a listagem de todos personagens e suas caracteristicas
na url /character, e todas as suas naves e os respectivos scores na url /ships.

# Rodando os testes

WORKDIR: star_wars_api/star_wars_api/

COMMAND: coverage run --source . -m unittest discover -s tests -v