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
