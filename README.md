# 📝 Blog Post Project

Welcome to the **Blog Post Project**, a full-stack web application for creating, reading, updating, and deleting blog posts. This project aims to provide users with a simple yet intuitive blogging platform.

---

## 🚀 Features

- **User Authentication**
  - Register new users.
  - Login and logout functionality.
- **Post Management**
  - Create, edit, and delete blog posts.
  - View a list of all posts.
  - View full post details.
- **Responsive UI**
  - Clean, user-friendly design.
  - Mobile-friendly layout.

---

## 🖼️ Screenshots

> _Replace these image links with your actual screenshots stored in the `images` folder or hosted publicly._

- **🏠 Home Page**
  ![Home Page](images/home_page.png)

- **🔐 Login Page**
  ![Login Page](images/login_page.png)

- **🔓 Logout**
  ![Logout Page](images/logout_page.png)

- **📄 Full Post View**
  ![Full Post](images/full_post.png)

---

## ⚙️ Technologies Used

- **Backend:** Django (Python)
- **Frontend:** Django Templates, Bootstrap
- **Database:** SQLite (default, easy to configure for PostgreSQL/MySQL)
- **Authentication:** Django’s built-in authentication system
- **Deployment:** Locally or easily configurable for platforms like Heroku, Vercel, or Render.

---

## 📂 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/rahat-abir/Blog_post_project.git
   cd Blog_post_project
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Run migrations**
   ```bash
   python manage.py migrate
5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
6. **Start the development server**
   ```bash
   python manage.py runserver
7. **Visit the app in your browser**
   ```bash
   http://127.0.0.1:8000/

