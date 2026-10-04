# Hello Flask 👋

The simplest possible Flask app — a starting point for learning how Flask routes work.

## 📖 What This Project Covers

- Setting up a basic Flask application
- Creating routes with `@app.route()`
- Returning simple text responses
- Running the Flask development server

## 🛠️ Tech Stack

- Python 3
- Flask

## 🚀 How to Run

1. Clone the repo and navigate to this folder:
   ```bash
   cd 01-beginner-flask-basics/01-hello-flask
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

5. Open your browser and visit:
   - `http://127.0.0.1:5000/` → "Hello, Flask!"
   - `http://127.0.0.1:5000/about` → "This is my first Flask app!"

## 📁 Files

```
01-hello-flask/
├── app.py          # Main Flask application
└── README.md        # This file
```

## 💡 What I Learned

- How Flask maps URL paths to Python functions using decorators
- The difference between running via `python app.py` and `flask run`
- What `debug=True` does during local development
