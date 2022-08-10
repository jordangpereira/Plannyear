from flask_mysqldb import MySQL

# MySQL no Python trabalha com Cursor, então é necessário fazer conexão com o cursor para executar comandos.

###### COISAS IMPORTANTES ###### 
# As Funções de Coisas Importantes são similares para Coisas a Fazer e Gastos

# GET
def getImportantThings(mysql):
    """Retorna uma Lista com as Coisas Importantes salvas na Tabela importantThings"""

    cursor = mysql.connection.cursor()
    
    # Seleciona todas as Tasks
    cursor.execute("SELECT id, task, status FROM importantThings")
    
    result = cursor.fetchall()
    listTasks = []

    for row in result: # Cria um dicionário de Dados
        task = {
            "id" : row[0],
            "task" : row[1],
            "status" : row[2]
        }
        listTasks.append(task)

    return listTasks

# PUT
def createImportantThings(mysql, task):
    """Cria uma Tarefa em Coisas Importantes"""

    cursor = mysql.connection.cursor()

    # Pega o dado com o maior ID no Banco
    cursor.execute("SELECT * FROM importantThings ORDER BY id DESC LIMIT 1")
    
    if cursor.rowcount == 0: # Verifica se há alguma linha (se há dado)
        task_id = 1
    else:
        result = cursor.fetchall()
        task_id = result[0][0] + 1

    status = "A Fazer"

    # Insere a Task no Banco de Dados com o Status Inicial de "A Fazer"
    cursor.execute("INSERT INTO importantThings (id, task, status) VALUES (%s, %s, %s)", (str(task_id), task, status))

    # Realiza o Commit no banco de dados da alteração realizada.
    mysql.connection.commit()

# UPDATE
def updateTaskImportantThings(mysql, id, task):
    """Realiza a alteração da descrição de uma Tarefa de Coisas Importantes"""

    cursor = mysql.connection.cursor()

    # Atualiza a Task no Banco de Dados com base no ID
    cursor.execute("UPDATE importantThings SET task = %s WHERE id = %s", (task, str(id)))

    # Realiza o Commit no banco de dados da alteração realizada.
    mysql.connection.commit()

# UPDATE
def updateStatusImportantThings(mysql, id, status):
    """Realiza a alteração do Status de uma Tarefa de Coisas Importantes"""

    cursor = mysql.connection.cursor()

    # Atualiza o Status no Banco de Dados com base no ID
    cursor.execute("UPDATE importantThings SET status = %s WHERE id = %s", (status, str(id)))

    # Realiza o Commit no banco de dados da alteração realizada.
    mysql.connection.commit()

# DELETE
def deleteImportantThings(mysql, id):
    """Deleta uma tarefa de Coisas Importantes"""

    cursor = mysql.connection.cursor()

    # Deleta a Task no Banco de Dados com base no ID
    cursor.execute("DELETE FROM importantThings WHERE id = %s", (str(id), ))

    # Realiza o Commit no banco de dados da alteração realizada.
    mysql.connection.commit()


###### TO DO LIST ######

# GET
def getTodoThings(mysql, day, month, year):
    """Retorna uma Lista com as Coisas a Fazer salvas na Tabela todoList"""

    cursor = mysql.connection.cursor()

    cursor.execute("SELECT id, task, status FROM todoList WHERE day = %s AND month = %s AND year = %s", (str(day), str(month), str(year)))
    
    result = cursor.fetchall()
    listTasks = []

    for row in result:
        task = {
            "id" : row[0],
            "task" : row[1],
            "status" : row[2]
        }
        listTasks.append(task)

    return listTasks

# PUT
def createTodoThings(mysql, day, month, year, task):
    """Cria uma tarefa em Coisas a Fazer em um determinado dia"""

    cursor = mysql.connection.cursor()

    cursor.execute("SELECT * FROM todoList ORDER BY id DESC LIMIT 1")

    if cursor.rowcount == 0:
        task_id = 1
    else:
        result = cursor.fetchall()
        task_id = result[0][0] + 1

    status = "A Fazer"

    cursor.execute("INSERT INTO todoList (id, day, month, year, task, status) VALUES (%s, %s, %s, %s, %s, %s)", (str(task_id), str(day), str(month), str(year), task, status))

    mysql.connection.commit()

# UPDATE
def updateTaskTodoThings(mysql, day, month, year, id, task,):
    """Realiza a alteração da descrição de uma Tarefa de Coisas a Fazer"""

    cursor = mysql.connection.cursor()

    cursor.execute("UPDATE todoList SET task = %s WHERE day = %s AND month = %s AND year = %s AND id = %s", (task, str(day), str(month), str(year), str(id)))

    mysql.connection.commit()

# UPDATE
def updateStatusTodoThings(mysql, day, month, year, id, status):
    """Realiza a alteração do Status de uma Tarefa de Coisas a Fazer"""

    cursor = mysql.connection.cursor()

    cursor.execute("UPDATE todoList SET status = %s WHERE day = %s AND month = %s AND year = %s AND id = %s", (status, str(day), str(month), str(year), str(id)))

    mysql.connection.commit()

# DELETE
def deleteTodoThings(mysql, day, month, year, id):
    """Deleta uma tarefa de Coisas a Fazer"""

    cursor = mysql.connection.cursor()

    cursor.execute("DELETE FROM todoList WHERE day = %s AND month = %s AND year = %s AND id = %s", (str(day), str(month), str(year), str(id)))

    mysql.connection.commit()


###### SPENDING LIST ######

# GET
def getSpendingsDay(mysql, day, month, year):
    """Retorna uma Lista com os Gastos do dia salvos na Tabela spendingList, assim como a Soma dos gastos do dia"""

    cursor = mysql.connection.cursor()

    cursor.execute("SELECT id, amount FROM spendingList WHERE day = %s AND month = %s AND year = %s", (str(day), str(month), str(year)))
    
    result = cursor.fetchall()
    listSpendings = []
    totalValue = 0

    for row in result:
        task = {
            "id" : row[0],
            "amount" : row[1]
        }
        listSpendings.append(task)
        totalValue += row[1]

    return listSpendings, totalValue

# GET
def getTotalSpendingsMonth(mysql, month, year):
    """Retorna o valor total gasto no mês"""

    cursor = mysql.connection.cursor()

    cursor.execute("SELECT amount FROM spendingList WHERE month = %s AND year = %s", (str(month), str(year)))
    
    result = cursor.fetchall()
    totalValue = 0

    for row in result:
        totalValue += row[0]

    return totalValue

# PUT
def createSpending(mysql, day, month, year, amount):
    """Cria um Gasto em um determinado dia"""
    
    cursor = mysql.connection.cursor()

    cursor.execute("SELECT * FROM spendingList ORDER BY id DESC LIMIT 1")

    if cursor.rowcount == 0:
        id = 1
    else:
        result = cursor.fetchall()
        id = result[0][0] + 1

    cursor.execute("INSERT INTO spendingList (id, day, month, year, amount) VALUES (%s, %s, %s, %s, %s)", (str(id), str(day), str(month), str(year), str(amount)))

    mysql.connection.commit()

# UPDATE
def updateSpending(mysql, day, month, year, id, amount):
    """Realiza a alteração do Valor de um Gasto"""

    cursor = mysql.connection.cursor()

    cursor.execute("UPDATE spendingList SET amount = %s WHERE day = %s AND month = %s AND year = %s AND id = %s", (str(amount), str(day), str(month), str(year), str(id)))

    mysql.connection.commit()

# DELETE
def deleteSpending(mysql, day, month, year, id):
    """Deleta um Gasto"""

    cursor = mysql.connection.cursor()

    cursor.execute("DELETE FROM spendingList WHERE day = %s AND month = %s AND year = %s AND id = %s", (str(day), str(month), str(year), str(id)))

    mysql.connection.commit()