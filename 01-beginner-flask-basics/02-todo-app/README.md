# To-Do List App ✅

A simple to-do list web app built with Flask. Tasks are stored in memory (no database yet) — this project focuses on handling forms, POST requests, and basic CRUD-style actions (add, delete, clear).

## 📖 What This Project Covers

- Handling both GET and POST requests on the same route
- Reading form data with `request.form`
- The Post/Redirect/Get pattern to prevent duplicate form submissions
- Looping through data in HTML using Jinja2 (`{% for %}`)
- Dynamic URLs with `url_for()`
- Serving static files (CSS) with Flask's `static/` folder convention

## 🛠️ Tech Stack

- Python 3
- Flask
- Jinja2 (templating)
- HTML/CSS

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd 01-beginner-flask-basics/02-todo-app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Install Flask:
   ```bash
   pip install flask
   ```

4. Run the app:
   ```bash
   python app.py
   ```

5. Open your browser and visit `http://127.0.0.1:5000/`

## ✨ Features

- Add a new task via a simple form
- Delete an individual task
- Clear all tasks at once
- Basic CSS styling for a clean layout

## 📁 Files

```
02-todo-app/
├── app.py              # Main Flask application
├── static/
│   └── style.css       # Styling for the app
└── templates/
    └── index.html      # HTML template with Jinja2 logic
```

## ⚠️ Known Limitation

Tasks are stored in memory, so they're lost every time the server restarts. This will be fixed in a later project when a database (SQLite + SQLAlchemy) is introduced.

## 💡 What I Learned

- How Flask handles form submissions with `request.form`
- Why GET requests shouldn't be used for actions that change data (like delete/clear) — and that this project uses GET for simplicity, with POST-based actions planned for a later, more advanced project
- How `url_for()` keeps routes and static file paths flexible and maintainable
- Flask's `static/` folder convention for CSS, JS, and images