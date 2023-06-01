# Python - Almost a circle


  <h2>Background Context</h2>

<p>In this project, you will review everything about Python:</p>

<ul>
<li>Import</li>
<li>Exceptions</li>
<li>Class</li>
<li>Private attribute</li>
<li>Getter/Setter</li>
<li>Class method</li>
<li>Static method</li>
<li>Inheritance</li>
<li>Unittest</li>
<li>Read/Write file</li>
</ul>

<p>You will also learn about:</p>

<ul>
<li><code>args</code> and <code>kwargs</code></li>
<li>Serialization/Deserialization</li>
<li>JSON</li>
</ul>


<h2>Step by step</h2>

<ul>
<li>Write the first class Base</li>
<li>Write the class Rectangle that inherits from Base</li>
<li>Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)</li>
<li>Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance</li>
<li>Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here</li>
<li>Update the class Rectangle by overriding the str method so that it returns [Rectangle] instance</li>
<li>Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y</li>
<li>Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute</li>
<li>Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, kwargs) that assigns a key/value argument to attributes</li>
<li>Write the class Square that inherits from Rectangle</li>
<li>Update the class Square by adding the public getter and setter size</li>
<li>Update the class Square by adding the public method def update(self, *args, kwargs) that assigns attributes</li>
<li>Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle</li>
<li>Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square</li>
<li>Update the class Base by adding the class method def save<em>to</em>file(cls, list<em>objs): that writes the JSON string representation of list</em>objs to a file</li>
<li>Update the class Base by adding the static method def from<em>json</em>string(json<em>string): that returns the list of the JSON string representation json</em>string</li>
<li>Update the class Base by adding the class method def create(cls, dictionary): that returns an instance with all attributes already set</li>
<li>Update the class Base by adding the class method def load<em>from</em>file(cls): that returns a list of instances</li>
</ul>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/1VFpovKWOxo91RtP2lebZg" title="args/kwargs" target="_blank">args/kwargs</a> </li>
<li><a href="/rltoken/DfJsuOTXTv2t7ycPfEXZuw" title="JSON encoder and decoder" target="_blank">JSON encoder and decoder</a> </li>
<li><a href="/rltoken/_jqAzT_nImg88Bk36NHjMw" title="unittest module" target="_blank">unittest module</a> </li>
<li><a href="/rltoken/n7aJtd_G82AIQ9hxMg7nng" title="Python test cheatsheet" target="_blank">Python test cheatsheet</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/H-uthlOO7nk1vorFnZtI7A" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is Unit testing and how to implement it in a large project</li>
<li>How to serialize and deserialize a Class</li>
<li>How to write and read a JSON file</li>
<li>What is <code>*args</code> and how to use it</li>
<li>What is <code>**kwargs</code> and how to use it</li>
<li>How to handle named arguments in a function</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should be documented: <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code></li>
<li>All your classes should be documented: <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code></li>
<li>All your functions (inside and outside a class) should be documented: <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code></li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h3>Python Unit Tests</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="/rltoken/_jqAzT_nImg88Bk36NHjMw" title="unittest module" target="_blank">unittest module</a> </li>
<li>All your test files should be python files (extension: <code>.py</code>)</li>
<li>All your test files and folders should start with <code>test_</code></li>
<li>Your file organization in the tests folder should be the same as your project: ex: for <code>models/base.py</code>, unit tests must be in: <code>tests/test_models/test_base.py</code></li>
<li>All your tests should be executed by using this command: <code>python3 -m unittest discover tests</code></li>
<li>You can also test file by file by using this command: <code>python3 -m unittest tests/test_models/test_base.py</code></li>
<li>We strongly encourage you to work together on test cases so that you don&rsquo;t miss any edge case</li>
</ul>

 <h2 class="gap">Tasks</h2>

   <h3 class="panel-title">
     0. If it&#39;s not tested it doesn&#39;t work
  </h3>

 
  <div class="panel-body">
  <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>All your files, classes and methods must be unit tested and be PEP 8 validated. </p>

<pre><code>guillaume@ubuntu:~/$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/$
</code></pre>


 <div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      1. Base class
    </h3>
  </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write the first class <code>Base</code>:</p>

<p>Create a folder named <code>models</code> with an empty file <code>__init__.py</code> inside - with this file, the folder will become a Python package</p>

<p>Create a file named <code>models/base.py</code>:</p>

<ul>
<li>Class <code>Base</code>:

<ul>
<li>private class attribute <code>__nb_objects = 0</code></li>
<li>class constructor: <code>def __init__(self, id=None):</code>:

<ul>
<li>if <code>id</code> is not <code>None</code>, assign the public instance attribute <code>id</code> with this argument value - you can assume <code>id</code> is an integer and you don&rsquo;t need to test the type of it</li>
<li>otherwise, increment <code>__nb_objects</code> and assign the new value to the public instance attribute <code>id</code></li>
</ul></li>
</ul></li>
</ul>

<p>This class will be the &ldquo;base&rdquo; of all other classes in this project. The goal of it is to manage <code>id</code> attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)</p>

<pre><code>guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 0-main &quot;&quot;&quot;
from models.base import Base

if __name__ == &quot;__main__&quot;:

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

guillaume@ubuntu:~/$ ./0-main.py
1
2
3
12
4
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      2. First Rectangle
    </h3>

   </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write the class <code>Rectangle</code> that inherits from <code>Base</code>:</p>

<ul>
<li>In the file <code>models/rectangle.py</code></li>
<li>Class <code>Rectangle</code> inherits from <code>Base</code></li>
<li>Private instance attributes, each with its own public getter and setter:

<ul>
<li><code>__width</code> -&gt; <code>width</code></li>
<li><code>__height</code> -&gt; <code>height</code></li>
<li><code>__x</code> -&gt; <code>x</code></li>
<li><code>__y</code> -&gt; <code>y</code></li>
</ul></li>
<li>Class constructor: <code>def __init__(self, width, height, x=0, y=0, id=None)</code>:

<ul>
<li>Call the super class with <code>id</code> - this super call with use the logic of the <code>__init__</code> of the <code>Base</code> class</li>
<li>Assign each argument <code>width</code>, <code>height</code>, <code>x</code> and <code>y</code> to the right attribute</li>
</ul></li>
</ul>

<p>Why private attributes with getter/setter? Why not directly public attribute?</p>

<p>Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can &ldquo;trust&rdquo; these attributes.</p>

<pre><code>guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 1-main &quot;&quot;&quot;
from models.rectangle import Rectangle

if __name__ == &quot;__main__&quot;:

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

guillaume@ubuntu:~/$ ./1-main.py
1
2
12
guillaume@ubuntu:~/$ 
</code></pre>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      3. Validate attributes
    </h3>

  </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>
   <!-- Progress vs Score -->
   <!-- Task Body -->
   <p>Update the class <code>Rectangle</code> by adding validation of all setter methods and instantiation (<code>id</code> excluded):</p>

<ul>
<li>If the input is not an integer, raise the <code>TypeError</code> exception with the message: <code>&lt;name of the attribute&gt; must be an integer</code>. Example: <code>width must be an integer</code></li>
<li>If <code>width</code> or <code>height</code> is under or equals 0, raise the <code>ValueError</code> exception with the message: <code>&lt;name of the attribute&gt; must be &gt; 0</code>. Example: <code>width must be &gt; 0</code></li>
<li>If <code>x</code> or <code>y</code> is under 0, raise the <code>ValueError</code> exception with the message: <code>&lt;name of the attribute&gt; must be &gt;= 0</code>. Example: <code>x must be &gt;= 0</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 2-main &quot;&quot;&quot;
from models.rectangle import Rectangle

if __name__ == &quot;__main__&quot;:

    try:
        Rectangle(10, &quot;2&quot;)
    except Exception as e:
        print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./2-main.py
[TypeError] height must be an integer
[ValueError] width must be &gt; 0
[TypeError] x must be an integer
[ValueError] y must be &gt;= 0
guillaume@ubuntu:~/$ 
</code></pre>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      4. Area first
    </h3>

  </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Update the class <code>Rectangle</code> by adding the public method <code>def area(self):</code> that returns the area value of the <code>Rectangle</code> instance.</p>

<pre><code>guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 3-main &quot;&quot;&quot;
from models.rectangle import Rectangle

if __name__ == &quot;__main__&quot;:

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

guillaume@ubuntu:~/$ ./3-main.py
6
20
56
guillaume@ubuntu:~/$ 
</code></pre>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      5. Display #0
    </h3>

   </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Update the class <code>Rectangle</code> by adding the public method <code>def display(self):</code> that prints in stdout the <code>Rectangle</code> instance with the character <code>#</code> - you don&rsquo;t need to handle <code>x</code> and <code>y</code> here.</p>

<pre><code>guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 4-main &quot;&quot;&quot;
from models.rectangle import Rectangle

if __name__ == &quot;__main__&quot;:

    r1 = Rectangle(4, 6)
    r1.display()

    print(&quot;---&quot;)

    r1 = Rectangle(2, 2)
    r1.display()

guillaume@ubuntu:~/$ ./4-main.py
####
####
####
####
####
####
---
##
##
guillaume@ubuntu:~/$ 
</code></pre>
