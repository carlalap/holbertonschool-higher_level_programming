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

</div>
    <div data-role="task19432" data-position="3" id="task-num-1">
      <div class="panel panel-default task-card " id="task-19432">
  <span id="user_id" data-id="6138"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Divide a matrix
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that divides all elements of a matrix.</p>

<ul>
<li>Prototype: <code>def matrix_divided(matrix, div):</code></li>
<li><code>matrix</code> must be a list of lists of integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>matrix must be a matrix (list of lists) of integers/floats</code></li>
<li>Each row of the <code>matrix</code> must be of the same size, otherwise raise a <code>TypeError</code> exception with the message <code>Each row of the matrix must have the same size</code></li>
<li><code>div</code> must be a number (integer or float), otherwise raise a <code>TypeError</code> exception with the message <code>div must be a number</code></li>
<li><code>div</code> can&rsquo;t be equal to <code>0</code>, otherwise raise a <code>ZeroDivisionError</code> exception with the message <code>division by zero</code></li>
<li>All elements of the matrix should be divided by <code>div</code>, rounded to 2 decimal places </li>
<li>Returns a new matrix</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__(&#39;2-matrix_divided&#39;).matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

guillaume@ubuntu:~/$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/$ 
</code></pre>


<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Say my name
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that prints <code>My name is &lt;first name&gt; &lt;last name&gt;</code></p>

<ul>
<li>Prototype: <code>def say_my_name(first_name, last_name=&quot;&quot;):</code></li>
<li><code>first_name</code> and <code>last_name</code> must be strings otherwise, raise a <code>TypeError</code> exception with the message <code>first_name must be a string</code> or <code>last_name must be a string</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__(&#39;3-say_my_name&#39;).say_my_name

say_my_name(&quot;John&quot;, &quot;Smith&quot;)
say_my_name(&quot;Walter&quot;, &quot;White&quot;)
say_my_name(&quot;Bob&quot;)
try:
    say_my_name(12, &quot;White&quot;)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/$ 
</code></pre>


<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Print square
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that prints a square with the character <code>#</code>.</p>

<ul>
<li>Prototype: <code>def print_square(size):</code></li>
<li><code>size</code> is the size length of the square</li>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
<li>if <code>size</code> is a float and is less than 0, raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
print_square = __import__(&#39;4-print_square&#39;).print_square

print_square(4)
print(&quot;&quot;)
print_square(10)
print(&quot;&quot;)
print_square(0)
print(&quot;&quot;)
print_square(1)
print(&quot;&quot;)
try:
    print_square(-1)
except Exception as e:
    print(e)
print(&quot;&quot;)

guillaume@ubuntu:~/$ ./4-main.py
####
####
####
####

##########
##########
##########
##########
##########
##########
##########
##########
##########
##########


#

size must be &gt;= 0

guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/4-print_square.txt
guillaume@ubuntu:~/$ 
</code></pre>

</div>
    <div data-role="task19435" data-position="6" id="task-num-4">
      <div class="panel panel-default task-card " id="task-19435">
  <span id="user_id" data-id="6138"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Text indentation
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that prints a text with 2 new lines after each of these characters: <code>.</code>, <code>?</code> and <code>:</code></p>

<ul>
<li>Prototype: <code>def text_indentation(text):</code></li>
<li><code>text</code> must be a string, otherwise raise a <code>TypeError</code> exception with the message <code>text must be a string</code></li>
<li>There should be no space at the beginning or at the end of each printed line</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
text_indentation = __import__(&#39;5-text_indentation&#39;).text_indentation

text_indentation(&quot;&quot;&quot;Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres&quot;&quot;&quot;)

guillaume@ubuntu:~/$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresguillaume@ubuntu:~/$
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/5-text_indentation.txt
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div data-role="task19438" data-position="7" id="task-num-5">
      <div class="panel panel-default task-card " id="task-19438">
  <span id="user_id" data-id="6138"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Max integer - Unittest
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Since the beginning you have been creating &ldquo;Interactive tests&rdquo;. For this exercise, you will add Unittests.</p>

<p>In this task, you will write unittests for the function <code>def max_integer(list=[]):</code>.</p>

<ul>
<li>Your test file should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="/rltoken/0a3DSCMIMni_V7pgq1myLQ" title="unittest module" target="_blank">unittest module</a> </li>
<li>Your test file should be python files (extension: <code>.py</code>)</li>
<li>Your test file should be executed by using this command: <code>python3 -m unittest tests.6-max_integer_test</code> </li>
<li>All tests you make must be passable by the function below</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 6-max_integer.py
#!/usr/bin/python3
&quot;&quot;&quot;Module to find the max integer in a list
&quot;&quot;&quot;


def max_integer(list=[]):
    &quot;&quot;&quot;Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    &quot;&quot;&quot;
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i &lt; len(list):
        if list[i] &gt; result:
            result = list[i]
        i += 1
    return result

guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__(&#39;6-max_integer&#39;).max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./6-main.py
4
4
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ python3 -m unittest tests.6-max_integer_test 2&gt;&amp;1 | tail -1
OK
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
&quot;&quot;&quot;Unittest for max_integer([..])
&quot;&quot;&quot;
import unittest
max_integer = __import__(&#39;6-max_integer&#39;).max_integer

class TestMaxInteger(unittest.TestCase):
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

