# Flask To-Do List App

A simple **Flask-based To-Do List** application with full **CRUD (Create, Read, Update, Delete)** functionality.

## Features
- Add new tasks
- View all tasks
- Edit tasks
- Delete tasks

## Technologies Used
- **Backend:** Flask, SQLite
- **Frontend:** HTML, CSS
- **Templating Engine:** Jinja2

## Database Setup
The app uses SQLite for simplicity. The database is automatically created when running the app for the first time.

## Project Structure
```
flask-todolist/
│── static/        # CSS, JavaScript, images
│── templates/     # HTML templates
│── app.py         # Main application file
│── requirements.txt  # Dependencies
│── README.md      # Project documentation
```

## API Endpoints
| Method | Endpoint | Description |
|--------|------------|-------------|
| GET | `/` | Display all tasks |
| POST | `/add` | Add a new task |
| GET/POST | `/edit/<id>` | Edit an existing task |
| GET | `/delete/<id>` | Delete a task |

## CREDITS TO
[josh](https://github.com/Joshwen7947)


