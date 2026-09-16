# python-pytest-workflow

I conducted a surface level research on pytest and its syntax to enable me write a simple pytest script and implement an GitHub Actions workflow.

## Introduction

Pytest is a popular software testing framework for Python that makes it easy to write and run tests. Python’s simple syntax and readability make writing test cases easy. With pytest, teams can write concise and readable test cases using Python’s familiar syntax. Additionally, pytest’s large collection of plugins extends its capabilities and allows for customized testing workflows.

pytest also supports popular Python frameworks like Flask, Django, and more.

## Key features of Pytest

1. Flexibility: it provides flexibility in test structure by supporting tests for functions, classes, and modules.

2. Detailed test output: it provides a detailed and readable test output, making it easy to understand test failures and errors.
3. Automatic test discovery: it automatically discovers tests by looking for files that start with `test_` or end with `_test.py`. This eliminates the need for manually specifying test files.

4. Parameterization: it supports parameterized tests, which allows one to run a single test function with multiple sets of inputs.
5. Fixtures: This provides `setup` and `tearDown` methods that help prevent code repetition. This enables you to set up reliable environments or data before tests run, and clean up after each test.

6. Plugins and extensions: It has a rich ecosystem of plugins and extensions that add extra functionalities, such as detailed tests reporting, and integration with other tools and Python frameworks like Django and Flask.
7. Compatibility: It is compatible with other testing frameworks like `unittest`, allowing one to migrate tests from different testing frameworks and run them seamlessly on it.

## Methods of Writing Tests

pytest has 2 basic methods of writing tests, which include:

1. The function-based method:  
This method is straightforward for writing tests because I can write the tests in individual functions.

Note: Each function name must be prefixed with the word `test_` for pytest to discover and run these tests automatically.

Below is an example of a function-based test:
```
def test_multiplication():
      assert 2 * 1 == 2
```

Note: In the code above, the assert statement used here in pytest is Python’s built-in “assert”. It’s more convenient and doesn’t require the specific methods like assertEqual and assertTrue which are common with unittest. Another advantage of using the assert statement is that it provides more detailed error messages when an assertion fails.

2. Class-based method:  
This method is similar to the way of writing tests in unittest, except that your test class does not inherit any methods. An example is shown below:
```
  class TestMathOperations:
      def test_multiplication(self):
          assert 2 * 1 == 2
```

This method of writing tests in pytest is useful when you want to group related tests together.

## How to Run Pytest Tests

Running pytest differs slightly from the normal convention of running regular Python scripts.

The general method of running pytest tests is by running the pytest command in the terminal. pytest will automatically look for and run all files of the form `test_py` or `_test.py` in the current directory and subdirectories. But while this may be a great way to run tests, pytest offers more flexibility beyond this general method of running tests.

Depending on preferences, you may want to run your test files based on the following:

1. To run a specific test file: To run tests in a specific file, use the `pytest` command followed by the file name. For example: `pytest test_example.py`.

2. To run tests in a directory: Let’s say I have a directory named `tests` that contains some test files. To run all the tests in that directory, use the pytest command followed by the directory and a forward slash. For example: `pytest tests/`.

3. To run tests using specific keywords: To run tests based on a certain keyword, use the command `pytest -k "keyword"`. Pytest will automatically look for and run function names, class names, or file names matching that keyword in the current directory and subdirectories. But to run tests matching a certain keyword in a specific file, I'd have to specify the file name after the pytest command. For example: `pytest test_example.py -k "keyword"`.

4. Run a specific test within a test file: To run only a specific test inside a test file, use the command `pytest test_example.py::test_addition`. This will run only the `test_addition` test function within the `test_example.py module`.

5. To run all test methods in a specific class: To run all the tests within a specific class, use `pytest test_example.py::TestClass`. This command would run all the test methods inside the `TestClass` class in the `test_example.py` module.

6. To run a specific test method inside a specific class: To run a specific test inside a specific class, use `pytest test_example.py::TestClass::test_addition`. This command would run the specific `test_addition` method within the `TestClass` class in the `test_example.py` module.

## How to Interpret pytest Results

One major advantage pytest has over other Python testing frameworks is the rich output it provides, which gives very detailed information about the status of your tests.

Using a basic test to understand how to interpret pytest’s output:
```
import pytest

def test_addition():
    assert 1 + 1 == 3
```

Run this test, and we get an output similar to the one below:
```
============================== test session starts ====================================
platform win32 -- Python 3.10.5, pytest-8.4.1, pluggy-1.6.0
rootdir: C:\\Users\\hp\\Desktop\\Pytest
collected 1 items

                                                                                  [ 50%]
test_example.py F                                                                 [100%]

===================================== FAILURES =========================================
____________________________________test_addition ______________________________________

    def test_addition():
>       assert 1 + 1 == 3
E       assert (1 + 1) == 3

test_example.py:4: AssertionError
============================== short test summary info =================================
FAILED test_example.py::test_addition - assert (1 + 1) == 3
========================= 1 failed, 1 passed in 0.13s ==================================
```

The above output is divided into several sections. Here’s a breakdown of what each section means:

1. Test session information:
```

 =============================== test session starts ===============================
 platform win32 -- Python 3.10.5, pytest-8.4.1, pluggy-1.6.0
 rootdir: C:\\Users\\hp\\Desktop\\TDD pytest
 collected 1 item
```

This section displays a summary of the test environment. It begins with a line marker that indicates the beginning of the test session.

Below the marker, pytest displays information about the operating system, along with the installed versions of Python, pytest and pluggy. (Pluggy is a pytest dependency used to manage plugins.)

The next line indicates the root directory where the test is being run.

The last line in this section displays the number of tests found in this directory.

2. Test status:
```
 test_example.py F                                                              [100%]

 ================================== FAILURES =========================================
 ________________________________ test_addition ______________________________________

     def test_addition():
 >       assert 1 + 1 == 3
 E       assert (1 + 1) == 3

 test_example.py:4: AssertionError
```
This section displays information about the status of our tests

The first line in this section specifies the test file which is being run, followed by the status (F in this case, which indicates a test failure).

The next set of lines gives specific information about the failed tests. This includes the function where the failure occurred (`test_addition`), and the exact line of code responsible for the error.

The last line gives a concise summary of this section. It indicates that the error occurred in `test_example.py` on line 4 and it was an `AssertionError`.

3. Test summary:
```
 ============================= short test summary info =============================
 FAILED test_example.py::test_addition - assert (1 + 1) == 3
 ================================ 1 failed in 0.13s ================================
 ```

This section provides an overall summary of the test.

It indicates that the failed test occurred in `test_example.py` file in the `test_addition` function because of an incorrect `assertion (1 + 1) == 3` which isn’t true.

Edit the code with the correct assertion `assert(1 + 1) == 2` and rerun the code. This time, the code passes with a different output.
```
=============================== test session starts ==================================
platform win32 -- Python 3.10.5, pytest-8.3.2, pluggy-1.5.0
rootdir: C:\\Users\\hp\\Desktop\\TDD pytest
collected 1 items

test_example.py .                                                               [100%]

=============================== 1 passed in 0.01s =================================
```

## Deployment Guide

### Step 1: Create Project Structure

A typical pytest project structure is as shown below:

```
pytest-project/
├── .pytest_cache/        # Automatically generated by pytest
├── src/                  # All application source code goes here
|   ├── __pycache__       # Automatically generated by pytest
│   ├── __init__.py       # Automatically generated by pytest
│   ├── app.py
│      
├── tests/                # All test files sit parallel to src/
|   ├── __pycache__       # Automatically generated by pytest
│   ├── test_app.py       
│   
├── pyproject.toml        # Modern tool configurations (or pytest.ini)
├── README.md
└── requirements.txt
```

### Step 2: Manually Test the Application

In my project structure, I included a `main.py` file in the parent directory `pytest-project/` to manually test my `calculator.py` application.

To test the application, run:

```
python3 calculator.py
```

The application runs as expected.

### Step 3: Set Up Virtual Environment for Testing

First, let’s create an isolated environment for our project to avoid dependency conflicts.

```
# Install virtualenv
pip install virtualenv

# Create virtual environment
virtualenv venv 

# Or specify Python version
virtualenv -p python3.13 venv

# Activate Virtual Environment
source venv/bin/activate # Mac OS
venv\Scripts\activate # Windows

# Install dependencies
pip install -r requirements.txt
```

### Step 4: Configure Pytest

Create `pytest.ini` configuration file to configure the testing environment:
```
[pytest]
pythonpath = .
testpaths = tests
```

What does this configuration do?

pythonpath = . : Tells pytest to include the current directory in Python path.   
testpaths = tests: Specifies where pytest should look for test files.    
This configuration ensures pytest can find our source code and knows where our tests are located.

### Step 5. Run the Pytest

Execute the below command in the virtual environment to run the pytest.
```
pytest -v   # -v for verbose output
```

Expected output:
```
================================================== 1 error in 0.23s ===================================================
(venv)
User@Udo MINGW64 ~/OneDrive/Documents/cicd/python-pytest-workflow (main)
$ pytest -v
================================================= test session starts =================================================
platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\User\OneDrive\Documents\cicd\python-pytest-workflow\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\User\OneDrive\Documents\cicd\python-pytest-workflow
configfile: pytest.ini
testpaths: test
plugins: cov-7.1.0
collected 2 items

test/test_calculator.py::test_add PASSED                                                                         [ 50%]
test/test_calculator.py::test_multiply PASSED                                                                    [100%]

================================================== 2 passed in 0.03s ==================================================
```

### Step 6: Deactivate the Virtual Environment

Execute the command:
```
deactivate
```

### Step 7: Set up CI/CD Pipeline

What this pipeline does:

1. Triggers - Runs on pushes to main branch and pull requests.
2. Environment - Uses Ubuntu with Python 3.14
3. Dependencies - Installs required packages automatically.
4. Testing - Executes pytest with verbose output.
5. Feedback - Provides clear success/failure messages.

Thank you!
