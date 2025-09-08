# Prg4DS-2025.2-CW
Programming for DS : 2025.2 CW

## 📌 Question 1 – Enhanced OOP

This project demonstrates an **Enhanced Object-Oriented Design** that follows **Clean Architecture** principles.

### ✅ Features
- Extensible design using interfaces and implementations (eg: StudentManagerImp, CourseManagerImp)
- models, log manager

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
    - SecureStudentRecord.py
  tests:
    - test_faculty.py
    - test_person.py
    - test_student_logics.py
    - test_student.py
```

## Running Unit Tests

This will execute all university system unit tests.

▶️  From the project root:

```bash
cd project/question1_university_system
PYTHONPATH=src python -m unittest discover -s tests
```

Enabling Logs

By default, logs are disabled.
If you want to see logs during test execution, set the LOG_ENABLED environment variable:

```bash
PYTHONPATH=src LOG_ENABLED=1 python -m unittest discover -s tests
```

### 1. Student Logic Tests

The `tests/test_student_logics.py` has following test classes:

- `TestStudentEnrollment`
- `TestStudentDropCourse`
- `TestCalculateGPA`
- `TestStudentAcademicStatus`

#### ▶️ Student Tests
```bash
PYTHONPATH=src LOG_ENABLED=1 python -m unittest tests.test_student_logics
```

### 2. Course Logic Tests

The `tests/test_course_logics.py` has following test classes:

- `TestCourseAddRemoveStudent`

#### ▶️ Course Tests
```bash
PYTHONPATH=src LOG_ENABLED=1 python -m unittest tests.test_course_logics
```

### 3. Faculty Logic Tests

The `tests/test_faculty_logics.py` has following test classes:

- `TestFacultyCouseAssignement`

#### ▶️ Faculty Tests
```bash
PYTHONPATH=src LOG_ENABLED=1 python -m unittest tests.test_faculty_logics
```

### 4. Secure Strudent Record Tests

The `tests/test_secure_student_record.py` has following test classes:

- `TestSecureStudentRecord`

#### ▶️ Secure Strudent Record Tests
```bash
PYTHONPATH=src LOG_ENABLED=1 python -m unittest tests.test_secure_student_record
```

### 5. Person Tests

The `tests/test_person.py` has following test classes:

- `TestStudent`
- `TestFaculty`

#### ▶️ Person Tests
```bash
PYTHONPATH=src LOG_ENABLED=1 python -m unittest tests.test_person
```