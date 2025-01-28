from flask import Flask, render_template
import requests
from collections import defaultdict

app = Flask(__name__)

API_BASE_URL = "http://localhost:8000"

@app.route('/')
def dashboard():
    try:
        # Fetch data from Django API
        students = requests.get(f"{API_BASE_URL}/api/students/").json()
        subjects = requests.get(f"{API_BASE_URL}/api/subjects/").json()
        grades = requests.get(f"{API_BASE_URL}/api/grades/").json()

        # Calculate overall averages for rankings
        student_grades = defaultdict(list)
        subject_grades = defaultdict(lambda: defaultdict(list))

        for grade in grades:
            student_id = grade['student']
            subject_id = grade['subject']
            student_grades[student_id].append(grade['grade'])
            subject_grades[student_id][subject_id].append(grade['grade'])

        # Prepare rankings
        rankings = []
        for student in students:
            grades_list = student_grades[student['id']]
            average = sum(grades_list) / len(grades_list) if grades_list else 0
            rankings.append({
                'name': student['name'],
                'average': average
            })
        
        # Sort rankings by average (descending)
        rankings.sort(key=lambda x: x['average'], reverse=True)

        # Prepare subject-wise grades
        student_subjects = []
        for student in students:
            subject_averages = []
            for subject in subjects:
                grades_list = subject_grades[student['id']][subject['id']]
                average = sum(grades_list) / len(grades_list) if grades_list else None
                subject_averages.append(average)
            
            student_subjects.append({
                'name': student['name'],
                'subject_grades': subject_averages
            })

        return render_template("dashboard.html",
                             rankings=rankings,
                             subjects=subjects,
                             student_subjects=student_subjects)

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)