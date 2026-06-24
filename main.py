from fastapi import FastAPI
from typing import Optional
 
app = FastAPI()
 
students = [
    {"id": 1, "name": "Rohan", "age": 21, "city": "Nanded"},
    {"id": 2, "name": "Amit", "age": 22, "city": "Pune"},
    {"id": 3, "name": "Priya", "age": 20, "city": "Mumbai"},
    {"id": 4, "name": "Rahul", "age": 21, "city": "Pune"},
    {"id": 5, "name": "Sneha", "age": 22, "city": "Mumbai"},
    {"id": 6, "name": "Anjali", "age": 21, "city": "Nanded"}
]
 
 
@app.get("/students")
def get_students(
    age: Optional[int] = None,
    city: Optional[str] = None,
    name: Optional[str] = None
):
    filtered_students = students
 
    # Filter by age
    if age is not None:
        filtered_students = [
            student for student in filtered_students
            if student["age"] == age
        ]
 
    # Filter by city
    if city is not None:
        filtered_students = [
            student for student in filtered_students
            if student["city"].lower() == city.lower()
        ]
 
    # Filter by name
    if name is not None:
        filtered_students = [
            student for student in filtered_students
            if name.lower() in student["name"].lower()
        ]
 
    return {
        "count": len(filtered_students),
        "students": filtered_students
    }
