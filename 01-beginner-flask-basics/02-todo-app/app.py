from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks (resets every time the server restarts)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the task text from the submitted form
        task = request.form.get('task')
        if task:  # avoid adding empty tasks
            tasks.append(task)
        # Redirect back to '/' to avoid resubmitting the form on refresh
        return redirect(url_for('index'))

    # GET request: just show the page with current tasks
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    # Remove a task by its position in the list
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/clear_all')
def clear_all():
    tasks.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)