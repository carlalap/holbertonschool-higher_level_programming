# Project: Python - Input/Output

## Resources

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/n4cEqOMm5PdqDE26lyWcDw" title="7.2. Reading and Writing Files" target="_blank">7.2. Reading and Writing Files</a> </li>
<li><a href="/rltoken/PhUB_UH5Ry2tGGK2VGJNGA" title="8.7. Predefined Clean-up Actions" target="_blank">8.7. Predefined Clean-up Actions</a> </li>
<li><a href="/rltoken/ciGk1flXa0Pbn8gv-x1FxQ" title="Dive Into Python 3: Chapter 11. Files" target="_blank">Dive Into Python 3: Chapter 11. Files</a> (<em>until &ldquo;11.4 Binary Files&rdquo; (included)</em>)</li>
<li><a href="/rltoken/0p1V5yvlnt3iCTE0DWV2Cg" title="JSON encoder and decoder" target="_blank">JSON encoder and decoder</a> </li>
<li><a href="/rltoken/zjejIRFH-ZgDaLLp6BWYnA" title="Learn to Program 8 : Reading / Writing Files" target="_blank">Learn to Program 8 : Reading / Writing Files</a> </li>
<li><a href="/rltoken/AOiShF_tqAawS_pKaiX51w" title="Automate the Boring Stuff with Python" target="_blank">Automate the Boring Stuff with Python</a> (<em>ch. 8 p 180-183 and ch. 14 p 326-333</em>)</li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/Hz3CSCRXnnDyjdTSHQcUKQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>How to open a file</li>
<li>How to write text in a file</li>
<li>How to read the full content of a file </li>
<li>How to read a file line by line</li>
<li>How to move the cursor in a file</li>
<li>How to make sure a file is closed after using it</li>
<li>What is and how to use the <code>with</code> statement</li>
<li>What is <code>JSON</code></li>
<li>What is serialization</li>
<li>What is deserialization</li>
<li>How to convert a Python data structure to a JSON string </li>
<li>How to convert a JSON string to a Python data structure</li>
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
</ul>

<h3>Python Test Cases</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder <code>tests</code></li>
<li>All your test files should be text files (extension: <code>.txt</code>)</li>
<li>All your tests should be executed by using this command: <code>python3 -m doctest ./tests/*</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
</ul>

<h2 class="gap">Tasks</h2>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      0. Read file
   </h3>
    
  </div>

<div class="panel-body">
   <span id="user_id" data-id="6138"></span>

<p>Write a function that reads a text file (<code>UTF8</code>) and prints it to stdout:</p>

<ul>
<li>Prototype: <code>def read_file(filename=&quot;&quot;):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&rsquo;t need to manage <code>file permission</code> or <code>file doesn&#39;t exist</code> exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__(&#39;0-read_file&#39;).read_file

read_file(&quot;my_file_0.txt&quot;)

guillaume@ubuntu:~/$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      1. Write to a file
    </h3>
  </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

    
  <p>Write a function that writes a string to a text file (<code>UTF8</code>) and returns the number of characters written:</p>

<ul>
<li>Prototype: <code>def write_file(filename=&quot;&quot;, text=&quot;&quot;):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&rsquo;t need to manage file permission exceptions.</li>
<li>Your function should create the file if doesn&rsquo;t exist.</li>
<li>Your function should overwrite the content of the file if it already exists.</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
write_file = __import__(&#39;1-write_file&#39;).write_file

nb_characters = write_file(&quot;my_first_file.txt&quot;, &quot;This School is so cool!\n&quot;)
print(nb_characters)

guillaume@ubuntu:~/$ ./1-main.py
24
guillaume@ubuntu:~/$ cat my_first_file.txt
This School is so cool!
guillaume@ubuntu:~/$ 
</code></pre>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      2. Append to a file
    </h3>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a function that appends a string at the end of a text file (<code>UTF8</code>) and returns the number of characters added:</p>

<ul>
<li>Prototype: <code>def append_write(filename=&quot;&quot;, text=&quot;&quot;):</code></li>
<li>If the file doesn&rsquo;t exist, it should be created</li>
<li>You must use the <code>with</code> statement</li>
<li>You don&rsquo;t need to manage <code>file permission</code> or <code>file doesn&#39;t exist</code> exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
append_write = __import__(&#39;2-append_write&#39;).append_write

nb_characters_added = append_write(&quot;file_append.txt&quot;, &quot;This School is so cool!\n&quot;)
print(nb_characters_added)

guillaume@ubuntu:~/$ cat file_append.txt
cat: file_append.txt: No such file or directory
guillaume@ubuntu:~/$ ./2-main.py
24
guillaume@ubuntu:~/$ cat file_append.txt
This School is so cool!
guillaume@ubuntu:~/$ ./2-main.py
24
guillaume@ubuntu:~/$ cat file_append.txt
This School is so cool!
This School is so cool!
guillaume@ubuntu:~/$ 
</code></pre>

 <div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      3. To JSON string
    </h3>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
  <p>Write a function that returns the JSON representation of an object (string):</p>

<ul>
<li>Prototype: <code>def to_json_string(my_obj):</code></li>
<li>You don&rsquo;t need to manage exceptions if the object can&rsquo;t be serialized.</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
to_json_string = __import__(&#39;3-to_json_string&#39;).to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { 
    &#39;id&#39;: 12,
    &#39;name&#39;: &quot;John&quot;,
    &#39;places&#39;: [ &quot;San Francisco&quot;, &quot;Tokyo&quot; ],
    &#39;is_active&#39;: True,
    &#39;info&#39;: {
        &#39;age&#39;: 36,
        &#39;average&#39;: 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./3-main.py
[1, 2, 3]
&lt;class &#39;str&#39;&gt;
{&quot;id&quot;: 12, &quot;is_active&quot;: true, &quot;name&quot;: &quot;John&quot;, &quot;info&quot;: {&quot;average&quot;: 3.14, &quot;age&quot;: 36}, &quot;places&quot;: [&quot;San Francisco&quot;, &quot;Tokyo&quot;]}
&lt;class &#39;str&#39;&gt;
[TypeError] {3, 132} is not JSON serializable
guillaume@ubuntu:~/$ 
</code></pre>


<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      4. From JSON string to Object
    </h3>
  
  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

   <!-- Task Body -->
  <p>Write a function that returns an object (Python data structure) represented by a JSON string:</p>

<ul>
<li>Prototype: <code>def from_json_string(my_str):</code></li>
<li>You don&rsquo;t need to manage exceptions if the JSON string doesn&rsquo;t represent an object.</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
from_json_string = __import__(&#39;4-from_json_string&#39;).from_json_string

s_my_list = &quot;[1, 2, 3]&quot;
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = &quot;&quot;&quot;
{&quot;is_active&quot;: true, &quot;info&quot;: {&quot;age&quot;: 36, &quot;average&quot;: 3.14}, 
&quot;id&quot;: 12, &quot;name&quot;: &quot;John&quot;, &quot;places&quot;: [&quot;San Francisco&quot;, &quot;Tokyo&quot;]}
&quot;&quot;&quot;
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_dict = &quot;&quot;&quot;
    {&quot;is_active&quot;: true, 12 }
    &quot;&quot;&quot;
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./4-main.py
[1, 2, 3]
&lt;class &#39;list&#39;&gt;
{&#39;id&#39;: 12, &#39;is_active&#39;: True, &#39;name&#39;: &#39;John&#39;, &#39;info&#39;: {&#39;age&#39;: 36, &#39;average&#39;: 3.14}, &#39;places&#39;: [&#39;San Francisco&#39;, &#39;Tokyo&#39;]}
&lt;class &#39;dict&#39;&gt;
[JSONDecodeError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
guillaume@ubuntu:~/$ 
</code></pre>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      5. Save Object to a file
    </h3>

   <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a function that writes an Object to a text file, using a JSON representation:</p>

<ul>
<li>Prototype: <code>def save_to_json_file(my_obj, filename):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&rsquo;t need to manage exceptions if the object can&rsquo;t be serialized.</li>
<li>You don&rsquo;t need to manage file permission exceptions.</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
save_to_json_file = __import__(&#39;5-save_to_json_file&#39;).save_to_json_file

filename = &quot;my_list.json&quot;
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = &quot;my_dict.json&quot;
my_dict = { 
    &#39;id&#39;: 12,
    &#39;name&#39;: &quot;John&quot;,
    &#39;places&#39;: [ &quot;San Francisco&quot;, &quot;Tokyo&quot; ],
    &#39;is_active&#39;: True,
    &#39;info&#39;: {
        &#39;age&#39;: 36,
        &#39;average&#39;: 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = &quot;my_set.json&quot;
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./5-main.py
[TypeError] Object of type set is not JSON serializable
guillaume@ubuntu:~/$ cat my_list.json ; echo &quot;&quot;
[1, 2, 3]
guillaume@ubuntu:~/$ cat my_dict.json ; echo &quot;&quot;
{&quot;name&quot;: &quot;John&quot;, &quot;places&quot;: [&quot;San Francisco&quot;, &quot;Tokyo&quot;], &quot;id&quot;: 12, &quot;info&quot;: {&quot;average&quot;: 3.14, &quot;age&quot;: 36}, &quot;is_active&quot;: true}
guillaume@ubuntu:~/$ cat my_set.json ; echo &quot;&quot;

guillaume@ubuntu:~/$ 
</code></pre>

div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      6. Create object from a JSON file
   </h3>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a function that creates an Object from a &ldquo;JSON file&rdquo;:</p>

<ul>
<li>Prototype: <code>def load_from_json_file(filename):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&rsquo;t need to manage exceptions if the JSON string doesn&rsquo;t represent an object.</li>
<li>You don&rsquo;t need to manage file permissions / exceptions.</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat my_fake.json
{&quot;is_active&quot;: true, 12 }
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
load_from_json_file = __import__(&#39;6-load_from_json_file&#39;).load_from_json_file

filename = &quot;my_list.json&quot;
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = &quot;my_dict.json&quot;
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = &quot;my_set_doesnt_exist.json&quot;
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

try:
    filename = &quot;my_fake.json&quot;
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ cat my_list.json ; echo &quot;&quot;
[1, 2, 3]
guillaume@ubuntu:~/$ cat my_dict.json ; echo &quot;&quot;
{&quot;name&quot;: &quot;John&quot;, &quot;places&quot;: [&quot;San Francisco&quot;, &quot;Tokyo&quot;], &quot;id&quot;: 12, &quot;info&quot;: {&quot;average&quot;: 3.14, &quot;age&quot;: 36}, &quot;is_active&quot;: true}
guillaume@ubuntu:~/$ cat my_fake.json ; echo &quot;&quot;
{&quot;is_active&quot;: true, 12 }
guillaume@ubuntu:~/$ ./6-main.py
[1, 2, 3]
&lt;class &#39;list&#39;&gt;
{&#39;name&#39;: &#39;John&#39;, &#39;info&#39;: {&#39;age&#39;: 36, &#39;average&#39;: 3.14}, &#39;id&#39;: 12, &#39;places&#39;: [&#39;San Francisco&#39;, &#39;Tokyo&#39;], &#39;is_active&#39;: True}
&lt;class &#39;dict&#39;&gt;
[FileNotFoundError] [Errno 2] No such file or directory: &#39;my_set_doesnt_exist.json&#39;
[ValueError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
guillaume@ubuntu:~/$ 
</code></pre>


<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      7. Load, add, save
    </h3>
</div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a script that adds all arguments to a Python list, and then save them to a file:</p>

<ul>
<li>You must use your function <code>save_to_json_file</code> from <code>5-save_to_json_file.py</code></li>
<li>You must use your function <code>load_from_json_file</code> from <code>6-load_from_json_file.py</code></li>
<li>The list must be saved as a JSON representation in a file named <code>add_item.json</code></li>
<li>If the file doesn&rsquo;t exist, it should be created</li>
<li>You don&rsquo;t need to manage file permissions / exceptions.</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat add_item.json
cat: add_item.json: No such file or directory
guillaume@ubuntu:~/$ ./7-add_item.py
guillaume@ubuntu:~/$ cat add_item.json ; echo &quot;&quot;
[]
guillaume@ubuntu:~/$ ./7-add_item.py Best School
guillaume@ubuntu:~/$ cat add_item.json ; echo &quot;&quot;
[&quot;Best&quot;, &quot;School&quot;]
guillaume@ubuntu:~/$ ./7-add_item.py 89 Python C
guillaume@ubuntu:~/$ cat add_item.json ; echo &quot;&quot;
[&quot;Best&quot;, &quot;School&quot;, &quot;89&quot;, &quot;Python&quot;, &quot;C&quot;]
guillaume@ubuntu:~/$ 
</code></pre>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      8. Class to JSON
    </h3>
  </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:</p>

<ul>
<li>Prototype: <code>def class_to_json(obj):</code></li>
<li><code>obj</code> is an instance of a Class</li>
<li>All attributes of the <code>obj</code> Class are serializable: list, dictionary, string, integer and boolean</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 8-my_class.py 
#!/usr/bin/python3
&quot;&quot;&quot; My class module
&quot;&quot;&quot;

class MyClass:
    &quot;&quot;&quot; My class
    &quot;&quot;&quot;

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return &quot;[MyClass] {} - {:d}&quot;.format(self.name, self.number)

guillaume@ubuntu:~/$ cat 8-main.py 
#!/usr/bin/python3
MyClass = __import__(&#39;8-my_class&#39;).MyClass
class_to_json = __import__(&#39;8-class_to_json&#39;).class_to_json

m = MyClass(&quot;John&quot;)
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

guillaume@ubuntu:~/$ ./8-main.py 
&lt;class &#39;8-my_class.MyClass&#39;&gt;
[MyClass] John - 89
&lt;class &#39;dict&#39;&gt;
{&#39;name&#39;: &#39;John&#39;, &#39;number&#39;: 89}
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ cat 8-my_class_2.py 
#!/usr/bin/python3
&quot;&quot;&quot; My class module
&quot;&quot;&quot;

class MyClass:
    &quot;&quot;&quot; My class
    &quot;&quot;&quot;

    score = 0

    def __init__(self, name, number = 4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return &quot;[MyClass] {} - {:d} =&gt; {:d}&quot;.format(self.__name, self.number, self.score)

guillaume@ubuntu:~/$ cat 8-main_2.py 
#!/usr/bin/python3
MyClass = __import__(&#39;8-my_class_2&#39;).MyClass
class_to_json = __import__(&#39;8-class_to_json&#39;).class_to_json

m = MyClass(&quot;John&quot;)
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

guillaume@ubuntu:~/$ ./8-main_2.py 
&lt;class &#39;8-my_class_2.MyClass&#39;&gt;
[MyClass] John - 4 =&gt; 1
&lt;class &#39;dict&#39;&gt;
{&#39;number&#39;: 4, &#39;_MyClass__name&#39;: &#39;John&#39;, &#39;is_team_red&#39;: True, &#39;score&#39;: 1}
guillaume@ubuntu:~/$
</code></pre>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      8. Class to JSON
   </h3>

   </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:</p>

<ul>
<li>Prototype: <code>def class_to_json(obj):</code></li>
<li><code>obj</code> is an instance of a Class</li>
<li>All attributes of the <code>obj</code> Class are serializable: list, dictionary, string, integer and boolean</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 8-my_class.py 
#!/usr/bin/python3
&quot;&quot;&quot; My class module
&quot;&quot;&quot;

class MyClass:
    &quot;&quot;&quot; My class
    &quot;&quot;&quot;

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return &quot;[MyClass] {} - {:d}&quot;.format(self.name, self.number)

guillaume@ubuntu:~/$ cat 8-main.py 
#!/usr/bin/python3
MyClass = __import__(&#39;8-my_class&#39;).MyClass
class_to_json = __import__(&#39;8-class_to_json&#39;).class_to_json

m = MyClass(&quot;John&quot;)
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

guillaume@ubuntu:~/$ ./8-main.py 
&lt;class &#39;8-my_class.MyClass&#39;&gt;
[MyClass] John - 89
&lt;class &#39;dict&#39;&gt;
{&#39;name&#39;: &#39;John&#39;, &#39;number&#39;: 89}
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ cat 8-my_class_2.py 
#!/usr/bin/python3
&quot;&quot;&quot; My class module
&quot;&quot;&quot;

class MyClass:
    &quot;&quot;&quot; My class
    &quot;&quot;&quot;

    score = 0

    def __init__(self, name, number = 4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return &quot;[MyClass] {} - {:d} =&gt; {:d}&quot;.format(self.__name, self.number, self.score)

guillaume@ubuntu:~/$ cat 8-main_2.py 
#!/usr/bin/python3
MyClass = __import__(&#39;8-my_class_2&#39;).MyClass
class_to_json = __import__(&#39;8-class_to_json&#39;).class_to_json

m = MyClass(&quot;John&quot;)
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

guillaume@ubuntu:~/$ ./8-main_2.py 
&lt;class &#39;8-my_class_2.MyClass&#39;&gt;
[MyClass] John - 4 =&gt; 1
&lt;class &#39;dict&#39;&gt;
{&#39;number&#39;: 4, &#39;_MyClass__name&#39;: &#39;John&#39;, &#39;is_team_red&#39;: True, &#39;score&#39;: 1}
guillaume@ubuntu:~/$
</code></pre>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      10. Student to JSON with filter
    </h3>

   </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a class <code>Student</code> that defines a student by: (based on <code>9-student.py</code>)</p>

<ul>
<li>Public instance attributes: 

<ul>
<li><code>first_name</code></li>
<li><code>last_name</code></li>
<li><code>age</code></li>
</ul></li>
<li>Instantiation with <code>first_name</code>, <code>last_name</code> and <code>age</code>: <code>def __init__(self, first_name, last_name, age):</code></li>
<li>Public method <code>def to_json(self, attrs=None):</code> that retrieves a dictionary representation of a <code>Student</code> instance (same as <code>8-class_to_json.py</code>):

<ul>
<li>If <code>attrs</code> is a list of strings, only attribute names contained in this list must be retrieved. </li>
<li>Otherwise, all attributes must be retrieved</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 10-main.py 
#!/usr/bin/python3
Student = __import__(&#39;10-student&#39;).Student

student_1 = Student(&quot;John&quot;, &quot;Doe&quot;, 23)
student_2 = Student(&quot;Bob&quot;, &quot;Dylan&quot;, 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json([&#39;first_name&#39;, &#39;age&#39;])
j_student_3 = student_2.to_json([&#39;middle_name&#39;, &#39;age&#39;])

print(j_student_1)
print(j_student_2)
print(j_student_3)

guillaume@ubuntu:~/$ ./10-main.py 
{&#39;age&#39;: 23, &#39;last_name&#39;: &#39;Doe&#39;, &#39;first_name&#39;: &#39;John&#39;}
{&#39;age&#39;: 27, &#39;first_name&#39;: &#39;Bob&#39;}
{&#39;age&#39;: 27}
guillaume@ubuntu:~/$
</code></pre>


<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      11. Student to disk and reload
    </h3>

   </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a class <code>Student</code> that defines a student by: (based on <code>10-student.py</code>)</p>

<ul>
<li>Public instance attributes: 

<ul>
<li><code>first_name</code></li>
<li><code>last_name</code></li>
<li><code>age</code></li>
</ul></li>
<li>Instantiation with <code>first_name</code>, <code>last_name</code> and <code>age</code>: <code>def __init__(self, first_name, last_name, age):</code></li>
<li>Public method <code>def to_json(self, attrs=None):</code> that retrieves a dictionary representation of a <code>Student</code> instance (same as <code>8-class_to_json.py</code>):

<ul>
<li>If <code>attrs</code> is a list of strings, only attributes name contain in this list must be retrieved. </li>
<li>Otherwise, all attributes must be retrieved</li>
</ul></li>
<li>Public method <code>def reload_from_json(self, json):</code> that replaces all attributes of the <code>Student</code> instance:

<ul>
<li>You can assume <code>json</code> will always be a dictionary</li>
<li>A dictionary key will be the public attribute name</li>
<li>A dictionary value will be the value of the public attribute</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<p>Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)</p>

<pre><code>guillaume@ubuntu:~/$ cat 11-main.py 
#!/usr/bin/python3
import os
import sys

Student = __import__(&#39;11-student&#39;).Student
read_file = __import__(&#39;0-read_file&#39;).read_file
save_to_json_file = __import__(&#39;5-save_to_json_file&#39;).save_to_json_file
load_from_json_file = __import__(&#39;6-load_from_json_file&#39;).load_from_json_file

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)

student_1 = Student(&quot;John&quot;, &quot;Doe&quot;, 23)
j_student_1 = student_1.to_json()
print(&quot;Initial student:&quot;)
print(student_1)
print(type(student_1))
print(type(j_student_1))
print(&quot;{} {} {}&quot;.format(student_1.first_name, student_1.last_name, student_1.age))


save_to_json_file(j_student_1, path)
read_file(path)
print(&quot;\nSaved to disk&quot;)


print(&quot;Fake student:&quot;)
new_student_1 = Student(&quot;Fake&quot;, &quot;Fake&quot;, 89)
print(new_student_1)
print(type(new_student_1))
print(&quot;{} {} {}&quot;.format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))


print(&quot;Load dictionary from file:&quot;)
new_j_student_1 = load_from_json_file(path)

new_student_1.reload_from_json(j_student_1)
print(new_student_1)
print(type(new_student_1))
print(&quot;{} {} {}&quot;.format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

guillaume@ubuntu:~/$ ./11-main.py student.json
Initial student:
&lt;11-student.Student object at 0x7f832826eda0&gt;
&lt;class &#39;11-student.Student&#39;&gt;
&lt;class &#39;dict&#39;&gt;
John Doe 23
{&quot;last_name&quot;: &quot;Doe&quot;, &quot;first_name&quot;: &quot;John&quot;, &quot;age&quot;: 23}
Saved to disk
Fake student:
&lt;11-student.Student object at 0x7f832826edd8&gt;
&lt;class &#39;11-student.Student&#39;&gt;
Fake Fake 89
Load dictionary from file:
&lt;11-student.Student object at 0x7f832826edd8&gt;
&lt;class &#39;11-student.Student&#39;&gt;
John Doe 23
guillaume@ubuntu:~/$ cat student.json ; echo &quot;&quot;
{&quot;last_name&quot;: &quot;Doe&quot;, &quot;first_name&quot;: &quot;John&quot;, &quot;age&quot;: 23}
guillaume@ubuntu:~/$ 
</code></pre>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      12. Pascal&#39;s Triangle
    </h3>

 </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p><strong>Technical interview preparation</strong>: </p>

<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>

<p>Create a function <code>def pascal_triangle(n):</code> that returns a list of lists of integers representing the Pascal&rsquo;s triangle of <code>n</code>:</p>

<ul>
<li>Returns an empty list if <code>n &lt;= 0</code></li>
<li>You can assume <code>n</code> will be always an integer</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 12-main.py
#!/usr/bin/python3
&quot;&quot;&quot;
12-main
&quot;&quot;&quot;
pascal_triangle = __import__(&#39;12-pascal_triangle&#39;).pascal_triangle

def print_triangle(triangle):
    &quot;&quot;&quot;
    Print the triangle
    &quot;&quot;&quot;
    for row in triangle:
        print(&quot;[{}]&quot;.format(&quot;,&quot;.join([str(x) for x in row])))


if __name__ == &quot;__main__&quot;:
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ ./12-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/$ 
</code></pre>

