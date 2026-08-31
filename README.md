# DjangoFullStack — Blog Web App

A full-stack blog application built with **Django**. Users can register, log in, manage their profile (with picture upload), and create/read/update/delete blog posts. Password reset is handled via email. Deployed on **Railway** with a **MySQL** database.

## Features

- User registration and authentication (login/logout)
- User profile with profile picture upload (`media/profile_pics`)
- Blog posts — full CRUD (create, view, update, delete) using Django class-based views
- Password reset flow via email (Gmail SMTP)
- Django admin panel
- Static files served with WhiteNoise
- MySQL database in production, configurable via environment variables

## Tech Stack

- **Backend:** Python, Django 6.0
- **Database:** MySQL (`mysqlclient`)
- **Frontend:** Django Templates, Bootstrap 4 (via `django-crispy-forms` / `crispy-bootstrap4`)
- **Static files:** WhiteNoise
- **Server:** Gunicorn
- **Deployment:** Railway
- **Env management:** python-dotenv

## Project Structure

```
DjangoFullStack/
├── blog/                  # Blog app
│   ├── models.py          # Post model (title, content, date_posted, author)
│   ├── views.py           # PostListView, PostDetailView, PostCreateView,
│   │                       # PostUpdateView, PostDeleteView, about
│   ├── urls.py
│   ├── templates/
│   └── static/
├── users/                 # Auth & profile app
│   ├── models.py          # Profile model (linked to User)
│   ├── forms.py
│   ├── views.py           # register, profile
│   ├── signals.py         # auto-creates Profile on User creation
│   └── templates/
├── django_project/        # Project settings & root URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── media/                 # Uploaded profile pictures (default.png, profile_pics/)
├── manage.py
├── requirements.txt
└── Procfile                # web: gunicorn django_project.wsgi:application --bind 0.0.0.0:$PORT
```

## Routes

| URL | View | Name |
|---|---|---|
| `/` | Post list | `blog-home` |
| `/post/<pk>/` | Post detail | `post-detail` |
| `/post/new/` | Create post | `post-create` |
| `/post/<pk>/update` | Update post | `post-update` |
| `/post/<pk>/delete` | Delete post | `post-delete` |
| `/about/` | About page | `blog-about` |
| `/register/` | User registration | `register` |
| `/login/` | Login | `login` |
| `/logout/` | Logout | `logout` |
| `/profile/` | User profile | `profile` |
| `/password-reset/` | Password reset flow | `password_reset` |
| `/admin/` | Django admin | — |

## Getting Started (Local Setup)

### 1. Clone the repository

```bash
git clone https://github.com/DevAyushKumar/DjangoFullStack.git
cd DjangoFullStack
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-django-secret-key

MYSQLDATABASE=your_db_name
MYSQLUSER=your_db_user
MYSQLPASSWORD=your_db_password
MYSQLHOST=your_db_host
MYSQLPORT=3306

EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
```

> Note: `settings.py` currently has `DEBUG = True` hardcoded — set it to read from an environment variable before deploying anywhere public, and lock down `ALLOWED_HOSTS` (it's currently `"*"`).

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Deployment (Railway)

1. Push the repo to GitHub and create a new Railway project from it.
2. Add a **MySQL** database plugin in Railway — it provides `MYSQLDATABASE`, `MYSQLUSER`, `MYSQLPASSWORD`, `MYSQLHOST`, `MYSQLPORT` automatically.
3. In the Railway project's **Variables** tab, set:
   - `SECRET_KEY`
   - `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`
   - (the `MYSQL*` variables are auto-injected if you link the MySQL plugin)
4. Railway uses the existing `Procfile`:
   ```
   web: gunicorn django_project.wsgi:application --bind 0.0.0.0:$PORT
   ```
5. `CSRF_TRUSTED_ORIGINS` in `settings.py` is already set for `https://*.up.railway.app`, so CSRF works out of the box on a Railway domain.
6. Run `python manage.py collectstatic` (or add it as a Railway build step) so WhiteNoise can serve static files from `staticfiles/`.
7. Push to the connected branch — Railway builds and deploys automatically.

## Environment Variables Reference

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `MYSQLDATABASE` | MySQL database name |
| `MYSQLUSER` | MySQL username |
| `MYSQLPASSWORD` | MySQL password |
| `MYSQLHOST` | MySQL host |
| `MYSQLPORT` | MySQL port (default 3306) |
| `EMAIL_HOST_USER` | Gmail address used to send password-reset emails |
| `EMAIL_HOST_PASSWORD` | Gmail app password |

## License

This project is for educational purposes.
