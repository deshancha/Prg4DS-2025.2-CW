# Prg4DS-2025.2-CW
Programming for DS : 2025.2 CW

## 📌 Question 1 – Enhanced OOP

This project demonstrates an **Enhanced Object-Oriented Design** that follows **Clean Architecture** principles.

### ✅ Features
- Separation of **Domain** and **Data** layers  
- **Presentation Layer** covered with unit tests  
- Extensible design using interfaces and implementations  

---

## 📂 Project Structure

```yaml
Q1-EnhancedOOP:
  src:
    domain:
      model:
        people:
          - person.py
          - student.py
          - faculty.py
        other:
            - academic_status.py
            - course.py
            - grade.py
      manager:
       - istudent_manager.py
    data:
      manager:
        - student_manager_imp.py
    - main.py
  tests:
    - test_faculty.py
    - test_person.py
    - test_student_logics.py
    - test_student.py

## ▶️ Running Unit Tests

From the project root:

```bash
cd Q1-EnhancedOOP
PYTHONPATH=src python -m unittest discover -s tests