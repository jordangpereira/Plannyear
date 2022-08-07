from flask_mysqldb import MySQL

# MySQL no Python trabalha com Cursor, então é necessário fazer conexão com o cursor para executar comandos.

###### COISAS IMPORTANTES ######

# GET
def getImportantThings(mysql):
    cursor = mysql.connection.cursor()
    
    # Seleciona todas as Tasks
    cursor.execute("SELECT id, task, status FROM importantThings")
    
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
def createImportantThings(mysql, task):
    cursor = mysql.connection.cursor()

    cursor.execute("SELECT * FROM importantThings ORDER BY id DESC LIMIT 1")
    
    if cursor.rowcount == 0:
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
    cursor = mysql.connection.cursor()

    # Atualiza a Task/Status no Banco de Dados com base no ID
    cursor.execute("UPDATE importantThings SET task = %s WHERE id = %s", (task, str(id)))

    # Realiza o Commit no banco de dados da alteração realizada.
    mysql.connection.commit()

# UPDATE
def updateStatusImportantThings(mysql, id, status):
    cursor = mysql.connection.cursor()

    # Atualiza a Task/Status no Banco de Dados com base no ID
    cursor.execute("UPDATE importantThings SET status = %s WHERE id = %s", (status, str(id)))

    # Realiza o Commit no banco de dados da alteração realizada.
    mysql.connection.commit()

# DELETE
def deleteImportantThings(mysql, id):
    cursor = mysql.connection.cursor()

    # Deleta a Task no Banco de Dados com base no ID
    cursor.execute("DELETE FROM importantThings WHERE id = %s", (str(id), ))

    # Realiza o Commit no banco de dados da alteração realizada.
    mysql.connection.commit()


###### TO DO LIST ######

# GET
def getTodoThings(mysql, day, month, year):
    cursor = mysql.connection.cursor()

    # Seleciona todas as Tasks da Data
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
    cursor = mysql.connection.cursor()

    cursor.execute("SELECT * FROM todoList ORDER BY id DESC LIMIT 1")

    if cursor.rowcount == 0:
        task_id = 1
    else:
        result = cursor.fetchall()
        task_id = result[0][0] + 1

    status = "A Fazer"

    # Insere a Task no Banco de Dados com o Status Inicial de "A Fazer"
    cursor.execute("INSERT INTO todoList (id, day, month, year, task, status) VALUES (%s, %s, %s, %s, %s, %s)", (str(task_id), str(day), str(month), str(year), task, status))

    # Realiza o Commit no banco de dados da alteração realizada.
    mysql.connection.commit()

# UPDATE
def updateTaskTodoThings(mysql, day, month, year, id, task,):
    cursor = mysql.connection.cursor()

    # Atualiza a Task/Status no Banco de Dados com base na data e no ID
    cursor.execute("UPDATE todoList SET task = %s WHERE day = %s AND month = %s AND year = %s AND id = %s", (task, str(day), str(month), str(year), str(id)))

    # Realiza o Commit no banco de dados da alteração realizada.
    mysql.connection.commit()

# UPDATE
def updateStatusTodoThings(mysql, day, month, year, id, status):
    cursor = mysql.connection.cursor()

    # Atualiza a Task/Status no Banco de Dados com base no ID
    cursor.execute("UPDATE todoList SET status = %s WHERE day = %s AND month = %s AND year = %s AND id = %s", (status, str(day), str(month), str(year), str(id)))

    # Realiza o Commit no banco de dados da alteração realizada.
    mysql.connection.commit()

# DELETE
def deleteTodoThings(mysql, day, month, year, id):
    cursor = mysql.connection.cursor()

    # Deleta a Task no Banco de Dados com base no ID e na Data
    cursor.execute("DELETE FROM todoList WHERE day = %s AND month = %s AND year = %s AND id = %s", (str(day), str(month), str(year), str(id)))

    # Realiza o Commit no banco de dados da alteração realizada.
    mysql.connection.commit()


###### SPENDING LIST ######

# GET
def getSpendingsDay(mysql, day, month, year):
    cursor = mysql.connection.cursor()

    # Seleciona todas as Tasks da Data
    cursor.execute("SELECT id, amount FROM spendingList WHERE day = %s AND month = %s AND year = %s", (str(day), str(month), str(year)))
    
    if cursor.rowcount == 0: # Caso a quantidade de linhas seja 0 (não foi encontrada nenhuma informação)
        return
    else:
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
    cursor = mysql.connection.cursor()

    # Seleciona todas as Tasks da Data
    cursor.execute("SELECT amount FROM spendingList WHERE month = %s AND year = %s", (str(month), str(year)))
    
    if cursor.rowcount == 0: # Caso a quantidade de linhas seja 0 (não foi encontrada nenhuma informação)
        return
    else:
        result = cursor.fetchall()
        totalValue = 0

        for row in result:
            totalValue += row[0]

        return totalValue

# PUT
def createSpending(mysql, day, month, year, amount):
    cursor = mysql.connection.cursor()

    # Insere a Task no Banco de Dados com o Status Inicial de "A Fazer"
    cursor.execute("INSERT INTO spendingList (day, month, year, amount) VALUES (%s, %s, %s, %s)", (str(day), str(month), str(year), str(amount)))

    # Realiza o Commit no banco de dados da alteração realizada.
    mysql.connection.commit()

# UPDATE
def updateSpending(mysql, day, month, year, id, amount):
    cursor = mysql.connection.cursor()

    # Atualiza a Task/Status no Banco de Dados com base na data e no ID
    cursor.execute("UPDATE spendingList SET amount = %s WHERE day = %s AND month = %s AND year = %s AND id = %s", (str(amount), str(day), str(month), str(year), str(id)))

    # Realiza o Commit no banco de dados da alteração realizada.
    mysql.connection.commit()

# DELETE
def deleteSpending(mysql, day, month, year, id):
    cursor = mysql.connection.cursor()

    # Deleta a Task no Banco de Dados com base no ID e na Data
    cursor.execute("DELETE FROM spendingList WHERE day = %s AND month = %s AND year = %s AND id = %s", (str(day), str(month), str(year), str(id)))

    # Realiza o Commit no banco de dados da alteração realizada.
    mysql.connection.commit()