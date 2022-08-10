# PlannYear

## Equipe

O sistema foi desenvolvido por Jordan Gonçalves Pereira.

## O Sistema

PlannYear é um sistema básico que possibilita a criação de tarefas a serem realizadas com a possibilidade de alocalas em dias específicos (Coisas a Fazer), tendo também há possibilidade de criar tarefas que não estão alocadas a um dia (Coisas Importantes). Além disso, podemos colocar os gastos diários, fazendo assim um controle de gastos diários e tendo, em retorno, o gasto total do mês.

## Execução

Utilizando o ambiente virtual de Python, foi criado um arquivo texto (*requirements.txt*) com requisitos de instalação, então não é necessário informar quais são, já que, utilizando o comando Docker Compose, ele fará todas as instalações necessárias.

Sendo assim, para executar, basta estar dentro da pasta *"PlannYear"* e utilizar o comando:
``` docker-compose -f code/docker-compose.yml up --build ```

Com isso, ele irá fazer o download (caso não tenha) das imagens do Python e do MySQL, assim como a instalação das dependências para o Python e a criação do Banco de Dados.

Depois de terminado, basta acessar o [localhost](localhost:3000), já que está fazendo a conexão da porta 5000 do Docker com a 3000 do computador.