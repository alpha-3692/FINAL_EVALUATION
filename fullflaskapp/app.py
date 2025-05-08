from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# In-memory storage for tasks
tasks = {
    "pending": [],
    "completed": []
}

@app.route('/team', methods=['GET'])
def team():
    team_info = {
        "company": "Taskly",
        "description": "Taskly is a productivity software platform designed to simplify task management for individuals and teams.",
        "team_members": [
            {
                "name": "Mohit",
                "role": "Technical Lead",
                "bio": "Mohit is a visionary software developer with vast experience in productivity software. He co-founded Taskly with the goal of making task management simple and efficient for everyone."
            },
            {
                "name": "Aditya",
                "role": "Team Lead",
                "bio": "Aditya is a talented developer with a passion for creating intuitive user interfaces. He leads our development team in building robust and user-friendly features for Taskly."
            },
            {
                "name": "Hardik Chawla",
                "role": "Java Lead",
                "bio": "Hardik Chawla is a visionary software developer with vast experience in productivity software. He co-founded Taskly with the goal of making task management simple and efficient for everyone."
            },
            {
                "name": "Ishan",
                "role": "UI/UX Lead",
                "bio": "Ishan brings creativity and user-centered design principles to Taskly. With his innovative approach, he consistently delivers intuitive designs that enhance user experience."
            }
        ]
    }
    return jsonify(team_info)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    task = {
        "id": len(tasks["pending"]) + len(tasks["completed"]) + 1,
        "text": data.get("text"),
        "priority": data.get("priority"),
        "completed": False,
        "createdAt": "2023-10-01T00:00:00"  # You can use a proper timestamp
    }
    tasks["pending"].append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    completed = data.get("completed", False)

    # Search in pending tasks
    for task in tasks["pending"]:
        if task["id"] == task_id:
            task["text"] = data.get("text", task["text"])
            task["priority"] = data.get("priority", task["priority"])
            if completed:
                task["completed"] = True
                tasks["pending"].remove(task)
                tasks["completed"].append(task)
            return jsonify(task)

    # Search in completed tasks
    for task in tasks["completed"]:
        if task["id"] == task_id:
            task["text"] = data.get("text", task["text"])
            task["priority"] = data.get("priority", task["priority"])
            if not completed:
                task["completed"] = False
                tasks["completed"].remove(task)
                tasks["pending"].append(task)
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks["pending"] = [task for task in tasks["pending"] if task["id"] != task_id]
    tasks["completed"] = [task for task in tasks["completed"] if task["id"] != task_id]
    return jsonify({"result": "Task deleted"})

if __name__ == '__main__':
    app.run(debug=True)
