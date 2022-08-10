from flask import Flask, flash, redirect, url_for, render_template, jsonify, request
from flask_mysqldb import MySQL
import database as db
import datetime 

# Iniciando aplicação Flask e o Banco de Dados
app = Flask(__name__)
app.secret_key = 'the random string'

app.config['JSON_SORT_KEYS'] = False

app.config['MYSQL_HOST'] = 'host.docker.internal' # Tive problemas com o IP do Docker do MySQL e, aparentemente, isso resolve. Senão resolver, teria que colocar manualmente o IP do MySQL.
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysqlpswd'
app.config['MYSQL_DB'] = 'plannyear'

mysql = MySQL(app)

@app.route("/", methods=["GET"])
def home():
    """Base de redirecionamento para as funcionalidades"""

    return render_template("home.html")

# Rotas relacionadas a Coisas Importantes (As funções de Coisas Importantes são similares para Coisas a Fazer e Gastos)

@app.route("/importantThings/", methods=["GET"])
def importantThings():
    """Gera a Página de Coisas Importantes"""

    items = db.getImportantThings(mysql) # Pega os dados de Coisas Importantes
    return render_template("importantThings.html", items=items)

@app.route("/importantThings/create", methods=['POST'])
def createImportantThings():
    """Realiza a criação de tarefas em Coisas Importantes"""

    data = request.get_json() # Pega a descrição inserida
    db.createImportantThings(mysql, data['description'])
    result = {'Sucesso': True, 'Resposta': 'Criado.'}
    return jsonify(result)

@app.route("/importantThings/update/<int:task_id>", methods=['POST'])
def updateImportantThings(task_id):
    """Realiza a alteração em uma tarefa de Coisas Importantes baseada no ID"""

    data = request.get_json() # Pega o dado para verificar se é uma mudança de Status ou de Descrição

    try:
        if "status" in data: # Alteração de Status
            db.updateStatusImportantThings(mysql, task_id, data["status"])
            result = {'Sucesso': True, 'Resposta': 'Status Atualizado.'}
        elif "description" in data: # Alteração de Descrição
            db.updateTaskImportantThings(mysql, task_id, data["description"])
            result = {'Sucesso': True, 'Resposta': 'Tarefa Atualizada.'}
        else:
            result = {'Sucesso': True, 'Resposta': 'Nada Alterado.'}
    except:
        result = {'Sucesso': False, 'Resposta': 'Algo deu de Errado.'}

    return jsonify(result)

@app.route("/importantThings/delete/<int:task_id>", methods=['POST'])
def deleteImportantThings(task_id):
    """Deleta uma tarefa de Coisas Importantes baseado no ID"""

    try:
        db.deleteImportantThings(mysql, task_id)
        result = {'Sucesso': True, 'Resposta': 'Tarefa Removida.'}
    except:
        result = {'Sucesso': False, 'Resposta': 'Algo deu de Errado.'}

    return jsonify(result)

# Rotas relacionadas a Coisas a Fazer

@app.route("/todoThings/", methods=["GET"])
def todoThings():
    """Gera a Página de Coisas a Fazer"""
    d, m, y = getDate()

    items = db.getTodoThings(mysql, d, m, y)
    spendingsItems, spendingDay = db.getSpendingsDay(mysql, d, m, y)
    spendingMonth = db.getTotalSpendingsMonth(mysql, m, y)
    return render_template("todoThings.html", items=items, spendingItems=spendingsItems, spendingDay=spendingDay, spendingMonth=spendingMonth)

@app.route("/todoThings/create", methods=['POST'])
def createTodoThings():
    """Realiza a criação de tarefas em Coisas a Fazer"""
    d, m, y = getDate()
    data = request.get_json()

    db.createTodoThings(mysql, d, m, y, data['description'])
    result = {'Sucesso': True, 'Resposta': 'Criado.'}
    return jsonify(result)

@app.route("/todoThings/update/<int:task_id>", methods=['POST'])
def updateTodoThings(task_id):
    """Realiza a alteração em uma tarefa de Coisas a Fazer baseada no ID"""
    d, m, y = getDate()
    data = request.get_json()

    try:
        if "status" in data:
            db.updateStatusTodoThings(mysql, d, m, y, task_id, data["status"])
            result = {'Sucesso': True, 'Resposta': 'Status Atualizado.'}
        elif "description" in data:
            db.updateTaskTodoThings(mysql, d, m, y, task_id, data["description"])
            result = {'Sucesso': True, 'Resposta': 'Tarefa Atualizada.'}
        else:
            result = {'Sucesso': True, 'Resposta': 'Nada Alterado.'}
    except:
        result = {'Sucesso': False, 'Resposta': 'Algo deu de Errado.'}

    return jsonify(result)

def getDate():
    current_time = datetime.datetime.now()
    return current_time.day, current_time.month, current_time.year

@app.route("/todoThings/delete/<int:task_id>", methods=['POST'])
def deleteTodoThings(task_id):
    """Deleta uma tarefa de Coisas a Fazer baseado no ID"""
    d, m, y = getDate()
    try:
        db.deleteTodoThings(mysql, d, m, y, task_id)
        result = {'Sucesso': True, 'Resposta': 'Tarefa Removida.'}
    except:
        result = {'Sucesso': False, 'Resposta': 'Algo deu de Errado.'}

    return jsonify(result)

# Rotas relacionadas a Gastos
@app.route("/todoThings/create_spending", methods=['POST'])
def createSpending():
    """Realiza a criação de um Gasto"""
    d, m, y = getDate()
    data = request.get_json()

    db.createSpending(mysql, d, m, y, data['description'])
    result = {'Sucesso': True, 'Resposta': 'Criado.'}
    return jsonify(result)

@app.route("/todoThings/update_spending/<int:id>", methods=['POST'])
def updateSpending(id):
    """Realiza a alteração de um Gasto baseado no ID"""
    d, m, y = getDate()
    data = request.get_json()

    try:
        if "description" in data:
            db.updateSpending(mysql, d, m, y, id, data["description"])
            result = {'Sucesso': True, 'Resposta': 'Valor Atualizado.'}
        else:
            result = {'Sucesso': True, 'Resposta': 'Nada Alterado.'}
    except:
        result = {'Sucesso': False, 'Resposta': 'Algo deu de Errado.'}

    return jsonify(result)

@app.route("/todoThings/delete_spending/<int:id>", methods=['POST'])
def deleteSpending(id):
    """Deleta um Gasto baseado no ID"""
    d, m, y = getDate()
    try:
        db.deleteSpending(mysql, d, m, y, id)
        result = {'Sucesso': True, 'Resposta': 'Valor Removido.'}
    except:
        result = {'Sucesso': False, 'Resposta': 'Algo deu de Errado.'}

    return jsonify(result)

if __name__ == "__main__":
    """Main para inicialização"""
    app.run(debug=True)