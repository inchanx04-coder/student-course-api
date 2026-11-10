import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Classroom demonstration only. Restrict origins further for a real application.
CORS(app)

courses = [
    {
        "id": 1,
        "code": "ITAS 3228",
        "name": "Web and Mobile Development",
        "description": "Introduction to web and mobile application development."
    },
    {
        "id": 2,
        "code": "SIA 3102",
        "name": "System Integration and Architecture",
        "description": "Fundamentals of integrating software systems and services."
    },
    {
        "id": 3,
        "code": "DBMS 2201",
        "name": "Database Management Systems",
        "description": "Introduction to organizing, storing, and retrieving data."
    },
    {
        "id": 4,
        "code": "PROG 2101",
        "name": "Programming Fundamentals",
        "description": "Core programming concepts, logic, and problem solving."
    },
    {
        "id": 5,
        "code": "NET 2301",
        "name": "Networking Fundamentals",
        "description": "Basic computer networking concepts and protocols."
    }
]

@app.get("/")
def home():
    return jsonify({
        "message": "Student Course API is running.",
        "available_endpoints": [
            "/api/health",
            "/api/courses",
            "/api/courses/1"
        ]
    })

@app.get("/api/health")
def health():
    return jsonify({"status": "success", "message": "Student Course API is running."}), 200

@app.get("/api/courses")
def get_courses():
    return jsonify(courses), 200

@app.get("/api/courses/<int:course_id>")
def get_course(course_id):
    course = next((item for item in courses if item["id"] == course_id), None)
    if course is None:
        return jsonify({"error": "Course not found", "course_id": course_id}), 404
    return jsonify(course), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
