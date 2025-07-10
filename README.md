# TaskLite 📝

TaskLite is a simple task manager built with **Flask (Python)**. It lets you create, view, and manage tasks using a basic **JSON file** instead of a traditional database.

## Features

-   Add new tasks
-   List all tasks
-   Mark tasks as complete

## Tech Stack

-   Python 🐍
-   Flask 🌶️
-   JSON for storage (no database needed)

## How to Run Locally

1.  **Clone the repository and navigate to the directory:**
    ```bash
    git clone [https://github.com/Zarahhhh/tasklite.git](https://github.com/Zarahhhh/tasklite.git)
    cd tasklite
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python3 app.py
    ```

4.  **Test in your browser:**
    Go to `http://127.0.0.1:5000`

## API Endpoints

-   **GET /tasks**: View all tasks.
-   **POST /tasks**: Add a new task.

### Example

Here's how you can add a task using `curl`:

```bash
curl -X POST [http://127.0.0.1:5000/tasks](http://127.0.0.1:5000/tasks) \
-H "Content-Type: application/json" \
-d '{"title": "Buy milk"}'

### Deployment

You can easily deploy this app to platforms like Render, Railway, or Heroku using the provided Procfile.
