from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='.')

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/edit_task', methods=['POST'])
def edit_task():
    task_index = int(request.form.get('task_index'))
    updated_task = request.form.get('updated_task')
    if 0 <= task_index < len(tasks) and updated_task:
        tasks[task_index] = updated_task
    return redirect(url_for('index'))

@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_index = int(request.form.get('task_index'))
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
