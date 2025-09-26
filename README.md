# Prg4DS-2025.2-CW
Programming for DS : 2025.2 CW

## Dependecies
```bash
cd project
pip install -r requirements.txt
```

## 📌 Question 1 – Enhanced OOP

This project demonstrates an **Enhanced Object-Oriented Design** that follows **Seperation** principles.

### ✅ Features
- Extensible design using interfaces and implementations (eg: StudentManagerImp, CourseManagerImp)
- models, log manager

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

## 📌 Question 2 – Social Media Analysis

## Data Collection

This project demonstrates an **Enhanced Object-Oriented Design** that follows **Clean Architecture** principles.

### ✅ Features
- Extensible design using clean architecture
- Asynchronous Book Scraping with python coroutines
- Dependancy Injection
- Colored Logs [Info, Warn, Error, Verbose]
- Tests and Mocks

## Execute Book Scraping Async, this is faster (~16 Sec)

This will scrape all 1000 books and save in the raw_files/books.json

▶️  From the project root:

```bash
cd project/question2_social_media_analysis/data_collection
LOG_ENABLED=1 ASYNC=1 python main.py
```

## Execute Book Scraping thread blocking, this is slow (~500+ Sec)

This will scrape all 1000 books and save in the raw_files/books.json

▶️  From the project root:

```bash
cd project/question2_social_media_analysis/data_collection
LOG_ENABLED=1 ASYNC=0 python main.py
```

### 3. HTTP Client Tests

The `tests/test_http_async.py` has following test classes:

- `TestHttpClientImp`

#### ▶️ TestHttpClientImp Tests
```bash
PYTHONPATH=. python -m unittest tests.test_http_async
```