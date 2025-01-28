# PythonForWebApp

A Django REST Framework (DRF) project for managing school data, including students, subjects, and grades. This project provides a robust API for CRUD operations and facilitates integration with other applications.

## Project Structure

- **api**: Contains the core API logic, including models, views, serializers, and URLs.
- **school_management**: Main Django application directory with settings and configurations.
- **db.sqlite3**: SQLite database file.

## Endpoints

The project includes the following API endpoints:

### Students
- **`GET /students/`**  
  Retrieves a list of all students.
- **`POST /students/`**  
  Creates a new student.
- **`GET /students/{id}/`**  
  Retrieves details of a specific student.
- **`PUT /students/{id}/`**  
  Updates the details of a specific student.
- **`DELETE /students/{id}/`**  
  Deletes a specific student.

### Subjects
- **`GET /subjects/`**  
  Retrieves a list of all subjects.
- **`POST /subjects/`**  
  Creates a new subject.
- **`GET /subjects/{id}/`**  
  Retrieves details of a specific subject.
- **`PUT /subjects/{id}/`**  
  Updates the details of a specific subject.
- **`DELETE /subjects/{id}/`**  
  Deletes a specific subject.

### Grades
- **`GET /grades/`**  
  Retrieves a list of all grades.
- **`POST /grades/`**  
  Creates a new grade.
- **`GET /grades/{id}/`**  
  Retrieves details of a specific grade.
- **`PUT /grades/{id}/`**  
  Updates the details of a specific grade.
- **`DELETE /grades/{id}/`**  
  Deletes a specific grade.

## Installation

### Prerequisites
- Python 3.8 or higher
- Django 4.x
- Django REST Framework

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd PythonForWebApp
