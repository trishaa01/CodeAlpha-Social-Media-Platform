# Connectly — Social Media Web App

A full-stack social media application built with Django, featuring user authentication, follow system, posts with photos/videos, likes, comments, and private accounts.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-4.x-green?style=flat&logo=django)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?style=flat&logo=sqlite)

---

## Features

- **Authentication** — Register, login, logout
- **User Profiles** — Profile picture, bio, public/private toggle
- **Follow System** — Follow/unfollow users, send follow requests for private accounts, accept/reject requests
- **Posts** — Create posts with text, photos, or videos
- **Feed** — See posts from all users, ordered by latest
- **Likes & Comments** — Like/unlike posts, add and delete comments
- **Search** — Search users by username
- **Responsive UI** — Works on desktop and mobile

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Database | SQLite |
| Frontend | HTML, CSS, JavaScript |
| Media Storage | Local filesystem |
| Auth | Django built-in auth |

---

## Project Structure

```text

Social_media project/
├── posts/                  # Posts, likes, comments app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── users/                  # User profiles, follow system app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── templates/              # HTML templates
│   ├── base.html
│   ├── feed.html
│   ├── profile.html
│   ├── create_post.html
│   ├── login.html
│   ├── register.html
│   ├── search.html
│   ├── requests.html
│   └── edit_profile.html
├── static/
│   ├── css/style.css
│   └── js/app.js
├── media/                  # Uploaded files (gitignored)
├── socialmedia/            # Project settings
│   ├── settings.py
│   └── urls.py
└── manage.py

```

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
```bash
   git clone [https://github.com/trishaa01/CodeAlpha-Social-Media-Platform.git]
   cd CodeAlpha Social Media Platform
```

2. **Install dependencies**
```bash
   pip install django pillow
```

3. **Run migrations**
```bash
   python manage.py migrate
```

4. **Start the server**
```bash
   python manage.py runserver
```

5. **Open in browser**

http://127.0.0.1:8000

###Admin Setup

```bash
python manage.py createsuperuser
```

Then visit `http://127.0.0.1:8000/admin`

---

## Author

**Trisha**
- GitHub: [@trishaa01](https://github.com/trishaa01)

---

## License

This project is developed for educational purposes as part of the **CodeAlpha Internship Program**.
