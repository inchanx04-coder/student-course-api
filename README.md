# Student Course API

A beginner-friendly, read-only Flask API for a System Integration and Architecture classroom demonstration.

## Important
- Uses fictional sample course data only.
- Does not connect to a database.
- Does not store real student records.
- Provides read-only GET endpoints.

## Endpoints

| Method | Endpoint | Expected result |
|---|---|---|
| GET | `/api/health` | HTTP 200 and API status JSON |
| GET | `/api/courses` | HTTP 200 and five fictional courses |
| GET | `/api/courses/1` | HTTP 200 and course with ID 1 |
| GET | `/api/courses/9999` | HTTP 404 and an error message |

## Run locally

1. Install Python 3.
2. Install dependencies: `pip install -r requirements.txt`
3. Start the server: `python app.py`
4. Open `http://127.0.0.1:5000/api/health`

## Deploy to Render

Create a **Web Service** from this GitHub repository.

- Runtime: Python 3
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`

The start command assumes the file is named `app.py` and the Flask application object is named `app`.
Render supplies the `PORT` environment variable. The application listens on `0.0.0.0`.

After deployment, test these paths using the public Render URL:
- `/api/health`
- `/api/courses`
- `/api/courses/1`
- `/api/courses/9999`

## Limitations

This is a prototype using in-memory sample data. It is not a production student information system and has no authentication or persistent database.
