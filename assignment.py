from fastapi import FastAPI, HTTPException, Query, status

app = FastAPI(title="Student Management API")

# Sample student data
students = [
    {
        "student_id": 1,
        "name": "Rahul",
        "age": 20,
        "city": "Pune",
        "course": "Computer Science"
    },
    {
        "student_id": 2,
        "name": "Priya",
        "age": 22,
        "city": "Mumbai",
        "course": "AI & ML"
    },
    {
        "student_id": 3,
        "name": "Amit",
        "age": 19,
        "city": "Pune",
        "course": "Computer Science"
    }
]


# Home Endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


# Get all students
@app.get("/students", status_code=status.HTTP_200_OK)
def get_students(
    city: str = Query(None),
    course: str = Query(None),
    min_age: int = Query(None, ge=0)
):
    result = students

    # Filter by city
    if city:
        result = [student for student in result
                  if student["city"].lower() == city.lower()]

    # Filter by course
    if course:
        result = [student for student in result
                  if course.lower() in student["course"].lower()]

    # Filter by minimum age
    if min_age is not None:
        result = [student for student in result
                  if student["age"] >= min_age]

    if not result:
        raise HTTPException(
            status_code=404,
            detail="No matching students found"
        )

    return result


# Get student by ID (Path Parameter)
@app.get("/students/{student_id}", status_code=status.HTTP_200_OK)
def get_student(student_id: int):

    for student in students:
        if student["student_id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail=f"Student with ID {student_id} not found"
    )


# Add a new student
@app.post("/students", status_code=status.HTTP_201_CREATED)
def add_student(student: dict):

    for s in students:
        if s["student_id"] == student["student_id"]:
            raise HTTPException(
                status_code=400,
                detail="Student ID already exists"
            )

    students.append(student)

    return {
        "message": "Student added successfully",
        "student": student
    }