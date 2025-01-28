# Student Management System

A web-based student management system built with Django REST API backend and Flask frontend for managing student grades and academic performance.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Student Management (CRUD operations)
- Subject Management
- Grade Recording System
- Student Rankings
- Subject-wise Grade Analysis
- REST API Integration

## Tech Stack
### Backend
- Django 5.1.5
- Django REST Framework
- SQLite3

### Frontend
- Flask
- HTML/CSS
- Python Requests Library

## Project Structure

student-management-system/ ├── school_management/ # Django Backend │ ├── api/ │ │ ├── __init__.py │ │ ├── admin.py │ │ ├── apps.py │ │ ├── migrations/ │ │ │ └── 0001_initial.py │ │ ├── models.py │ │ ├── serializers.py │ │ ├── tests.py │ │ ├── urls.py │ │ └── views.py │ ├── db.sqlite3 │ ├── manage.py │ ├── school_management/ │ │ ├── __init__.py │ │ ├── asgi.py │ │ ├── settings.py │ │ ├── urls.py │ │ └── wsgi.py └── flask/ # Flask Frontend ├── app.py ├── static/ │ └── styles.css └── templates/ └── dashboard.html
