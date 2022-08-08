from flask import Flask, flash, redirect, url_for, render_template, jsonify, request
from flask_mysqldb import MySQL
import database as db
import datetime 

# Iniciando aplicação Flask
app = Flask(__name__)
app.secret_key = 'the random string'

app.config['JSON_SORT_KEYS'] = False # Utilizado para que o Json não ordene as saídas pelas chaves.

app.config['MYSQL_HOST'] = 'host.docker.internal' # Tive problemas com o IP do Docker do MySQL e, aparentemente, isso resolve. Senão resolver, teria que colocar manualmente o IP do MySQL.
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysqlpswd'
app.config['MYSQL_DB'] = 'plannyear'

mysql = MySQL(app)

# Base de redirecionamento para as funcionalidades
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

# Coisas Importantes
@app.route("/importantThings/", methods=["GET"])
def importantThings():
    items = db.getImportantThings(mysql)
    return render_template("importantThings.html", items=items)

@app.route("/importantThings/delete/<int:task_id>", methods=['POST'])
def deleteImportantThings(task_id):
    try:
        db.deleteImportantThings(mysql, task_id)
        result = {'Sucesso': True, 'Resposta': 'Tarefa Removida.'}
    except:
        result = {'Sucesso': False, 'Resposta': 'Algo deu de Errado.'}

    return jsonify(result)

@app.route("/importantThings/update/<int:task_id>", methods=['POST'])
def updateImportantThings(task_id):
    data = request.get_json()

    try:
        if "status" in data:
            db.updateStatusImportantThings(mysql, task_id, data["status"])
            result = {'Sucesso': True, 'Resposta': 'Status Atualizado.'}
        elif "description" in data:
            db.updateTaskImportantThings(mysql, task_id, data["description"])
            result = {'Sucesso': True, 'Resposta': 'Tarefa Atualizada.'}
        else:
            result = {'Sucesso': True, 'Resposta': 'Nada Alterado.'}
    except:
        result = {'Sucesso': False, 'Resposta': 'Algo deu de Errado.'}

    return jsonify(result)

@app.route("/importantThings/create", methods=['POST'])
def createImportantThings():
    data = request.get_json()
    db.createImportantThings(mysql, data['description'])
    result = {'Sucesso': True, 'Resposta': 'Criado.'}
    return jsonify(result)

# Todo
@app.route("/todoThings/", methods=["GET"])
def todoThings():
    d, m, y = getDate()

    items = db.getTodoThings(mysql, d, m, y)
    spendingsItems, spendingDay = db.getSpendingsDay(mysql, d, m, y)
    spendingMonth = db.getTotalSpendingsMonth(mysql, m, y)
    return render_template("todoThings.html", items=items, spendingItems=spendingsItems, spendingDay=spendingDay, spendingMonth=spendingMonth)

@app.route("/todoThings/delete/<int:task_id>", methods=['POST'])
def deleteTodoThings(task_id):
    d, m, y = getDate()
    try:
        db.deleteTodoThings(mysql, d, m, y, task_id)
        result = {'Sucesso': True, 'Resposta': 'Tarefa Removida.'}
    except:
        result = {'Sucesso': False, 'Resposta': 'Algo deu de Errado.'}

    return jsonify(result)

@app.route("/todoThings/update/<int:task_id>", methods=['POST'])
def updateTodoThings(task_id):
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

@app.route("/todoThings/create", methods=['POST'])
def createTodoThings():
    d, m, y = getDate()
    data = request.get_json()

    db.createTodoThings(mysql, d, m, y, data['description'])
    result = {'Sucesso': True, 'Resposta': 'Criado.'}
    return jsonify(result)

def getDate():
    current_time = datetime.datetime.now()
    return current_time.day, current_time.month, current_time.year

# Spending
@app.route("/todoThings/delete_spending/<int:id>", methods=['POST'])
def deleteSpending(id):
    d, m, y = getDate()
    try:
        db.deleteSpending(mysql, d, m, y, id)
        result = {'Sucesso': True, 'Resposta': 'Valor Removido.'}
    except:
        result = {'Sucesso': False, 'Resposta': 'Algo deu de Errado.'}

    return jsonify(result)

@app.route("/todoThings/update_spending/<int:id>", methods=['POST'])
def updateSpending(id):
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

@app.route("/todoThings/create_spending", methods=['POST'])
def createSpending():
    d, m, y = getDate()
    data = request.get_json()

    db.createSpending(mysql, d, m, y, data['description'])
    result = {'Sucesso': True, 'Resposta': 'Criado.'}
    return jsonify(result)

# Main para inicialização.
if __name__ == "__main__":
    app.run(debug=True)