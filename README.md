
# Advanced Personal Website

This project is a **Django-based personal portfolio website**, designed to showcase skills, projects, and professional background with modern animations, admin control, and API functionality.

---

## 🌟 Features

- Responsive and clean design
- Dynamic project showcase
- Animated skill bars
- About me and services sections
- Contact form
- Admin panel for content management
- Django Rest Framework (DRF) powered API:
  - Projects, Skills, Services listing & management
- Secure API access with Basic Authentication
- Dynamic CORS control via admin panel
- Animations and interactive UI elements

---

## 🛠️ Technologies Used

- **Python 3**
- **Django**
- **Django Rest Framework**
- **HTML5, CSS3, JavaScript**
- **Bootstrap**
- **FontAwesome**
- **SQLite** (default, can be replaced)
- **Responsive Design Principles**

---

## 🚀 Getting Started

1. **Clone the repository**

```bash
git clone https://github.com/kaanakboga/Advanced-Personal-Website.git
cd Advanced-Personal-Website
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser**

```bash
python manage.py createsuperuser
```

6. **Run the project**

```bash
python manage.py runserver
```

Website will be accessible at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📱 API Usage

- List & create projects:
  ```
  GET/POST http://127.0.0.1:8000/api/projects/
  ```
- Retrieve, update or delete project:
  ```
  GET/PUT/DELETE http://127.0.0.1:8000/api/projects/<id>/
  ```
- Same structure applies for:
  ```
  /api/skills/
  /api/services/
  ```

**Notes:**

- API requires Basic Authentication
- External requests require CORS permission managed via admin panel

---

## ⚠️ Important

- `.env`, database files, and virtual environment folders are excluded via `.gitignore`
- Replace default `SECRET_KEY` and sensitive settings before production deployment

---

## 👨‍💻 About the Developer

Created by **Kaan Akboğa**, a passionate developer focusing on modern, responsive, and interactive web applications with backend control and secure API architecture.
