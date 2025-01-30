# 📚 Python for Web App – Student Management System

## 📝 Project Overview
This project is a **Student Management System** built using **Django and Flask**, aimed at **digitalizing grade management** for a school that still relies on paper files.

### **🔹 Features**
✔ **Django Application (Backend)**
   - Manages students, subjects, and grades.
   - Provides data through a **REST API** using **Django REST Framework**.
   - Enables CRUD operations for students, subjects, and grades.

✔ **Flask Application (Frontend)**
   - **Consumes** data from the Django REST API.
   - **Calculates & displays** student averages and rankings.
   - Provides a **graphical interface** for users.

---

## 🔑 Access & Usage Details

### **🌐 Flask Dashboard (Frontend)**
📍 Accessible at: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**  
- This is the main **dashboard** where you can view student **rankings and grades**.
- It fetches data from the **Django API**.

### **🛠 Django Backend (Admin Panel)**
📍 Accessible at: **[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)**  
- You can **add, edit, delete, and group** students, subjects, and grades here.  
- Any changes made in Django **automatically reflect** in the Flask frontend.
- You can create a super user by running "python manage.py createsuperuser" or you can use mine if you want , I have already added few students, subject and grades for better explanation (if you use my credentials)

#### **🔐 Login Credentials for Django Admin**
- **Username:** `jay15`  
- **Password:** `Jay@1101`  
- After logging in, you can:
  - **Add, remove, edit, delete, and group students, subjects, and grades**.
  - **View all changes in real-time on the Flask dashboard (http://127.0.0.1:5000)**.

---

## 🔗 API Endpoints (Django Backend)
The Django REST API provides the following endpoints:

| Method | Endpoint                   | Description |
|--------|----------------------------|-------------|
| GET    | `/api/students/`           | Get all students |
| POST   | `/api/students/`           | Add a new student |
| GET    | `/api/students/{id}/`      | Get a specific student |
| PUT    | `/api/students/{id}/`      | Update student details |
| DELETE | `/api/students/{id}/`      | Delete a student |
| GET    | `/api/subjects/`           | Get all subjects |
| POST   | `/api/subjects/`           | Add a new subject |
| GET    | `/api/grades/`             | Get all grades |
| POST   | `/api/grades/`             | Add a new grade |

---

## 📊 Flask Application Functionalities
✔ Fetches data from the **Django API**  
✔ Displays **student rankings**  
✔ Shows **subject-wise and overall averages**  
✔ Simple, **interactive UI**  

---

## 🏆 Project Summary
- The **Django backend** was developed **from scratch** to provide a clean and functional REST API.  
- The **Flask frontend** was **fixed and improved** to properly fetch and display student data.  
- The **project ensures an easy-to-use interface** for managing students, subjects, and grades efficiently.  
- **All modifications made in Django reflect in Flask in real-time.** 

---

## 👨‍💻 Author
**🔗 GitHub:** [jayy1511](https://github.com/jayy1511)  

---
