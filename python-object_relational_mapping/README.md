<h1>Python - Object-relational mapping</h1>


<h2>Before you start&hellip;</h2>

<p><strong>Please make sure your MySQL server is in 8.0</strong> -&gt; <a href="/rltoken/XGGI_GSNhqZU7q_GlvDkCQ" title="How to install MySQL 8.0 in Ubuntu 20.04" target="_blank">How to install MySQL 8.0 in Ubuntu 20.04</a></p>

<h2>Background Context</h2>

<p>In this project, you will link two amazing worlds: Databases and Python!</p>

<p>In the first part, you will use the module <code>MySQLdb</code> to connect to a MySQL database and execute your SQL queries.</p>

<p>In the second part, you will use the module <code>SQLAlchemy</code> (don&rsquo;t ask me how to pronounce it&hellip;) an Object Relational Mapper (ORM). </p>

<p>The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be &ldquo;What can I do with my objects&rdquo; and not &ldquo;How this object is stored? where? when?&rdquo;. You won&rsquo;t write any SQL queries only Python code. Last thing, your code won&rsquo;t be &ldquo;storage type&rdquo; dependent. You will be able to change your storage easily without re-writing your entire project.</p>

<p>Without ORM:</p>

<pre><code>conn = MySQLdb.connect(host=&quot;localhost&quot;, port=3306, user=&quot;root&quot;, passwd=&quot;root&quot;, db=&quot;my_db&quot;, charset=&quot;utf8&quot;)
cur = conn.cursor()
cur.execute(&quot;SELECT * FROM states ORDER BY id ASC&quot;) # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
</code></pre>

<p>With an ORM:</p>

<pre><code>engine = create_engine(&#39;mysql+mysqldb://{}:{}@localhost/{}&#39;.format(&quot;root&quot;, &quot;root&quot;, &quot;my_db&quot;), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print(&quot;{}: {}&quot;.format(state.id, state.name))
session.close()
</code></pre>

<p>Do you see the difference? Cool, right? </p>

<p>The biggest difficulty with ORM is: The syntax!</p>

<p>Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don&rsquo;t read the entire documentation before starting, just jump on it if you don&rsquo;t get something. </p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/tCytNeWUzuWhAn9APwtp9A" title="Object-relational mappers" target="_blank">Object-relational mappers</a> </li>
<li><a href="/rltoken/V8KJv3QCReECPZ0V-kXRwg" title="mysqlclient/MySQLdb documentation" target="_blank">mysqlclient/MySQLdb documentation</a> (<em>please don&rsquo;t pay attention to <code>_mysql</code></em>)</li>
<li><a href="/rltoken/j_7jU3C9Jsa0o53pgfwxOQ" title="MySQLdb tutorial" target="_blank">MySQLdb tutorial</a> </li>
<li><a href="/rltoken/7y1s8FDE_0S-uhBtCgt5-A" title="SQLAlchemy tutorial" target="_blank">SQLAlchemy tutorial</a> </li>
<li><a href="/rltoken/j6kxlUETdjiFwiu0k_JI6Q" title="SQLAlchemy" target="_blank">SQLAlchemy</a> </li>
<li><a href="/rltoken/vzsiR8tCdY3_OWsMH33jUA" title="mysqlclient/MySQLdb" target="_blank">mysqlclient/MySQLdb</a> </li>
<li><a href="/rltoken/7m6F57mBASM7A2r_GcIeMA" title="Introduction to SQLAlchemy" target="_blank">Introduction to SQLAlchemy</a> </li>
<li><a href="/rltoken/riV6WcWo1MGRpF3WSmv4Zw" title="Flask SQLAlchemy" target="_blank">Flask SQLAlchemy</a> </li>
<li><a href="/rltoken/uRrjdEkHmjrVenCqjwJRWQ" title="10 common stumbling blocks for SQLAlchemy newbies" target="_blank">10 common stumbling blocks for SQLAlchemy newbies</a> </li>
<li><a href="/rltoken/RfLwdV21O_TVoQU4iwaIFw" title="Python SQLAlchemy Cheatsheet" target="_blank">Python SQLAlchemy Cheatsheet</a> </li>
<li><a href="/rltoken/2BoGpuT2vAaoeuC3SN_wPA" title="SQLAlchemy ORM Tutorial for Python Developers" target="_blank">SQLAlchemy ORM Tutorial for Python Developers</a> (<em><strong>Warning:</strong> This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL</em>)</li>
<li><a href="/rltoken/DrwY56jSHCOADKEbSOBa0A" title="SQLAlchemy Tutorial" target="_blank">SQLAlchemy Tutorial</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/zAH3PxVw_N-4dQ45aCW8yw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to connect to a MySQL database from a Python script</li>
<li>How to <code>SELECT</code> rows in a MySQL table from a Python script</li>
<li>How to <code>INSERT</code> rows in a MySQL table from a Python script </li>
<li>What ORM means</li>
<li>How to map a Python Class to a MySQL table</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.8.5)</li>
<li>Your files will be executed with <code>MySQLdb</code> version <code>2.0.x</code></li>
<li>Your files will be executed with <code>SQLAlchemy</code> version <code>1.4.x</code></li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.#)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>You are not allowed to use <code>execute</code> with sqlalchemy</li>
</ul>

<h2>More Info</h2>

<h3>Install MySQL 8.0 on Ubuntu 20.04 LTS</h3>

<pre><code>$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
</code></pre>

<p>Connect to your MySQL server:</p>

<pre><code>$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type &#39;help;&#39; or &#39;\h&#39; for help. Type &#39;\c&#39; to clear the current input statement.

mysql&gt;
mysql&gt; quit
Bye
$
</code></pre>

<h3>Install <code>MySQLdb</code> module version <code>2.0.x</code></h3>

<p>For installing <code>MySQLdb</code>, you need to have <code>MySQL</code> installed.</p>

<pre><code>$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
&gt;&gt;&gt; import MySQLdb
&gt;&gt;&gt; MySQLdb.version_info 
(2, 0, 3, &#39;final&#39;, 0)
</code></pre>

<h3>Install <code>SQLAlchemy</code> module version <code>1.4.x</code></h3>

<pre><code>$ sudo pip3 install SQLAlchemy
...
$ python3
&gt;&gt;&gt; import sqlalchemy
&gt;&gt;&gt; sqlalchemy.__version__ 
&#39;1.4.22&#39;
</code></pre>

<p>Also, you can have this warning message:</p>

<pre><code>/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, &quot;&#39;@@SESSION.GTID_EXECUTED&#39; is deprecated and will be re
moved in a future release.&quot;)                                                                                                                    
  cursor.execute(statement, parameters)  
</code></pre>

<p>You can ignore it.</p>

  </div>
</div>

 
   <h2 class="gap">Tasks</h2>

   <div data-role="task20353" data-position="1" id="task-num-0">
   <div class="panel panel-default task-card " id="task-20353">
  <span id="user_id" data-id="6138"></span>

  <div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      0. Get all states
    </h3>

  </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a script that lists all <code>states</code> from the database <code>hbtn_0e_0_usa</code>: </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
(1, &#39;California&#39;)
(2, &#39;Arizona&#39;)
(3, &#39;Texas&#39;)
(4, &#39;New York&#39;)
(5, &#39;Nevada&#39;)
guillaume@ubuntu:~/$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      1. Filter states
    </h3>
  </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a script that lists all <code>states</code> with a <code>name</code> starting with <code>N</code> (upper N) from the database <code>hbtn_0e_0_usa</code>: </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, &#39;New York&#39;)
(5, &#39;Nevada&#39;)
guillaume@ubuntu:~/$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      2. Filter states by user input
    </h3>
  </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a script that takes in an argument and displays all values in the <code>states</code> table of <code>hbtn_0e_0_usa</code> where <code>name</code> matches the argument.</p>

<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name searched</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You must use <code>format</code> to create the SQL query with the user input</li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa &#39;Arizona&#39;
(2, &#39;Arizona&#39;)
guillaume@ubuntu:~/$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

...
