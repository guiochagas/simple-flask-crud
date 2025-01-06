from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A lista de tarefas será armazenada em memória (se desejar persistência, você pode usar banco de dados)
todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        todo_list.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['GET'])
def delete_task(task_id):
    if 0 <= task_id < len(todo_list):
        todo_list.pop(task_id)
    return redirect(url_for('index'))

# Rota para editar uma tarefa
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    # Verifica se o ID da tarefa existe
    if 0 <= task_id < len(todo_list):
        if request.method == 'POST':
            # Atualiza a tarefa
            new_task = request.form.get('task')
            if new_task:
                todo_list[task_id] = new_task
            return redirect(url_for('index'))
        # Exibe o formulário para editar a tarefa
        return render_template('edit_task.html', task=todo_list[task_id], task_id=task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
