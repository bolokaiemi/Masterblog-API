1. Description of the Blog Application:
   Allows users to create, view, update, and delete posts
   Is a full-stack app with backend + frontend
   
3. Tech Stack
    Backend: Python, Flask Api
    Frontend: HTML/CSS/JS also using SQLAlchemy with SQLite for persistent storage,
    createed database tables.
4. Setup
   backend(in codio)
   pip install flask flask-cors
   python3 backend_app.py
   Run in codio 

5.Frontend (Local)
  Run it on local computer and copy the Api to postman

  Finally connecting Frontend & Backend
  Paste the backend API URL into your frontend config:
  const API_URL = "http://127.0.0.1:5001";
  The frontend will use this to send requests (e.g., when clicking the “Post” button)
  
