# Python - Test-driven development

## Resources
<br> - <a href="https://docs.python.org/3.4/library/doctest.html"> 26.2. doctest — Test interactive Python examples</a>
<br> - <a href="https://pymotw.com/3/doctest/"> doctest — Testing Through Documentation</a>
<br> - <a href="https://www.youtube.com/watch?v=1Lfv5tUGsn8&ab_channel=Socratica"> Unit Tests in Python</a>


## Learning Objectives:
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
- Why Python programming is awesome
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

# Requirements
## Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case - The Checker is checking for tests! 

## Tasks

0. Integers addition
<br> Write a function that adds 2 integers.
- Prototype: def add_integer(a, b=98):
- a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
- a and b must be first casted to integers if they are float
- Returns an integer: the addition of a and b
- You are not allowed to import any module

<p>Write a function that adds 2 integers.</p>

<ul>
<li>Prototype: <code>def add_integer(a, b=98):</code></li>
<li><code>a</code> and <code>b</code> must be integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>a must be an integer</code> or <code>b must be an integer</code></li>
<li><code>a</code> and <code>b</code> must be first casted to integers if they are float</li>
<li>Returns an integer: the addition of <code>a</code> and <code>b</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__(&#39;0-add_integer&#39;).add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, &quot;School&quot;))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/$ python3 -c &#39;print(__import__(&quot;0-add_integer&quot;).__doc__)&#39; | wc -l
5
guillaume@ubuntu:~/$ python3 -c &#39;print(__import__(&quot;0-add_integer&quot;).add_integer.__doc__)&#39; | wc -l
3
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-test_driven_development</code></li>
            <li>File: <code>0-add_integer.py, tests/0-add_integer.txt</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">


1. Divide a matrix
<br> Write a function that divides all elements of a matrix.
- Prototype: def matrix_divided(matrix, div):
- matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
- Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
- div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
- div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
- All elements of the matrix should be divided by div, rounded to 2 decimal places
- Returns a new matrix
- You are not allowed to import any module

2. Say my name
<br>Write a function that prints My name is <first name> <last name>
- Prototype: def say_my_name(first_name, last_name=""):
- first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
- You are not allowed to import any module
- 
3. Print square
<br>Write a function that prints a square with the character #.
- Prototype: def print_square(size):
- size is the size length of the square
- size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
- if size is less than 0, raise a ValueError exception with the message size must be >= 0
- if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
- You are not allowed to import any module

4. Text indentation
<br>Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
- Prototype: def text_indentation(text):
- text must be a string, otherwise raise a TypeError exception with the message text must be a string
- There should be no space at the beginning or at the end of each printed line
- You are not allowed to import any module

5. Max integer - Unittest
<br> Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.
- In this task, you will write unittests for the function def max_integer(list=[]):.
- Your test file should be inside a folder tests
- You have to use the unittest module
- Your test file should be python files (extension: .py)
- Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
- All tests you make must be passable by the function below
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

