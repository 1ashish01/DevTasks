# DevTrack - Engineering Issue Tracker

DevTrack is a simple backend API for tracking engineering bugs and tasks.

It allows engineers to create issues, assign priorities and statuses, and associate each issue with the reporter who filed it.

## Features

- Create and manage reporters
- Create and manage engineering issues
- Track issue status
- Track issue priority
- One-to-many relationship between Reporter and Issue
- REST API using Django REST Framework
- Django Admin interface
- Basic frontend
- API testing with Postman

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- HTML
- CSS
- JavaScript
- Postman

---

## Project Structure

```text
DevTrack/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── devtrack/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── issues/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    │
    ├── templates/
    │   └── issues/
    │       └── index.html
    │
    └── static/
        └── issues/
            ├── style.css
            └── app.js