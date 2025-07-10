from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'tasks.json'

@app.route('/')
def home():
    return '<h1>Welcome to TaskLite!</h1><p>Use /tasks to view tasks.</p>'

# If no task file exists, create one
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

# Load all tasks
def load_tasks():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save tasks
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Show all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(load_tasks())

# Add a task
@app.route('/tasks', methods=['POST'])
def add_task():
    tasks = load_tasks()
    data = request.json
    new_task = {
        'id': len(tasks) + 1,
        'title': data.get('title', 'Untitled Task'),
        'completed': False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task), 201

# Mark task complete
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def mark_complete(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks)
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [t for t in tasks if t['id'] != task_id]
    if len(updated_tasks) == len(tasks):
        return jsonify({'error': 'Task not found'}), 404
    save_tasks(updated_tasks)
    return jsonify({'message': 'Task deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)

