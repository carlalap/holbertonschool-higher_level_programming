# Project: Python - Inheritance

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/pRigaMtzlZIXHVXZJ7yRMQ" title="Inheritance" target="_blank">Inheritance</a> </li>
<li><a href="/rltoken/q7hgZ43Gu_snerCNUwqzuw" title="Multiple inheritance" target="_blank">Multiple inheritance</a> </li>
<li><a href="/rltoken/5WGBg0vfHlumaNORrvU4Ng" title="Inheritance in Python" target="_blank">Inheritance in Python</a> </li>
<li><a href="/rltoken/fojEQ8bllfZecx-ZKKurTw" title="Learn to Program 10 : Inheritance Magic Methods" target="_blank">Learn to Program 10 : Inheritance Magic Methods</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/qtTNU4FKGaIHTtnDLLrVYQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a superclass, baseclass or parentclass</li>
<li>What is a subclass</li>
<li>How to list all attributes and methods of a class or instance</li>
<li>When can an instance have new attributes</li>
<li>How to inherit class from another</li>
<li>How to define a class with multiple base classes </li>
<li>What is the default class every class inherit from</li>
<li>How to override a method or attribute inherited from the base class</li>
<li>Which attributes or methods are available by heritage to subclasses</li>
<li>What is the purpose of inheritance</li>
<li>What are, when and how to use <code>isinstance</code>, <code>issubclass</code>, <code>type</code> and <code>super</code> built-in functions</li>
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

<h3>Documentation</h3>

<ul>
<li>Do not use the words <code>import</code> or <code>from</code> inside your comments, the checker will think you are trying to import some modules</li>
</ul>

  </div>
</div>

<h2 class="gap">Tasks</h2>

    <div data-role="task19498" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-19498">
  <span id="user_id" data-id="6138"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Lookup
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
    <p>Write a function that returns the list of available attributes and methods of an object:</p>

<ul>
<li>Prototype: <code>def lookup(obj):</code></li>
<li>Returns a <code>list</code> object</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
lookup = __import__(&#39;0-lookup&#39;).lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

guillaume@ubuntu:~/$ ./0-main.py
[&#39;__class__&#39;, &#39;__delattr__&#39;, &#39;__dict__&#39;, &#39;__dir__&#39;, &#39;__doc__&#39;, &#39;__eq__&#39;, &#39;__format__&#39;, &#39;__ge__&#39;, &#39;__getattribute__&#39;, &#39;__gt__&#39;, &#39;__hash__&#39;, &#39;__init__&#39;, &#39;__le__&#39;, &#39;__lt__&#39;, &#39;__module__&#39;, &#39;__ne__&#39;, &#39;__new__&#39;, &#39;__reduce__&#39;, &#39;__reduce_ex__&#39;, &#39;__repr__&#39;, &#39;__setattr__&#39;, &#39;__sizeof__&#39;, &#39;__str__&#39;, &#39;__subclasshook__&#39;, &#39;__weakref__&#39;]
[&#39;__class__&#39;, &#39;__delattr__&#39;, &#39;__dict__&#39;, &#39;__dir__&#39;, &#39;__doc__&#39;, &#39;__eq__&#39;, &#39;__format__&#39;, &#39;__ge__&#39;, &#39;__getattribute__&#39;, &#39;__gt__&#39;, &#39;__hash__&#39;, &#39;__init__&#39;, &#39;__le__&#39;, &#39;__lt__&#39;, &#39;__module__&#39;, &#39;__ne__&#39;, &#39;__new__&#39;, &#39;__reduce__&#39;, &#39;__reduce_ex__&#39;, &#39;__repr__&#39;, &#39;__setattr__&#39;, &#39;__sizeof__&#39;, &#39;__str__&#39;, &#39;__subclasshook__&#39;, &#39;__weakref__&#39;, &#39;my_attr1&#39;, &#39;my_meth&#39;]
[&#39;__abs__&#39;, &#39;__add__&#39;, &#39;__and__&#39;, &#39;__bool__&#39;, &#39;__ceil__&#39;, &#39;__class__&#39;, &#39;__delattr__&#39;, &#39;__dir__&#39;, &#39;__divmod__&#39;, &#39;__doc__&#39;, &#39;__eq__&#39;, &#39;__float__&#39;, &#39;__floor__&#39;, &#39;__floordiv__&#39;, &#39;__format__&#39;, &#39;__ge__&#39;, &#39;__getattribute__&#39;, &#39;__getnewargs__&#39;, &#39;__gt__&#39;, &#39;__hash__&#39;, &#39;__index__&#39;, &#39;__init__&#39;, &#39;__int__&#39;, &#39;__invert__&#39;, &#39;__le__&#39;, &#39;__lshift__&#39;, &#39;__lt__&#39;, &#39;__mod__&#39;, &#39;__mul__&#39;, &#39;__ne__&#39;, &#39;__neg__&#39;, &#39;__new__&#39;, &#39;__or__&#39;, &#39;__pos__&#39;, &#39;__pow__&#39;, &#39;__radd__&#39;, &#39;__rand__&#39;, &#39;__rdivmod__&#39;, &#39;__reduce__&#39;, &#39;__reduce_ex__&#39;, &#39;__repr__&#39;, &#39;__rfloordiv__&#39;, &#39;__rlshift__&#39;, &#39;__rmod__&#39;, &#39;__rmul__&#39;, &#39;__ror__&#39;, &#39;__round__&#39;, &#39;__rpow__&#39;, &#39;__rrshift__&#39;, &#39;__rshift__&#39;, &#39;__rsub__&#39;, &#39;__rtruediv__&#39;, &#39;__rxor__&#39;, &#39;__setattr__&#39;, &#39;__sizeof__&#39;, &#39;__str__&#39;, &#39;__sub__&#39;, &#39;__subclasshook__&#39;, &#39;__truediv__&#39;, &#39;__trunc__&#39;, &#39;__xor__&#39;, &#39;bit_length&#39;, &#39;conjugate&#39;, &#39;denominator&#39;, &#39;from_bytes&#39;, &#39;imag&#39;, &#39;numerator&#39;, &#39;real&#39;, &#39;to_bytes&#39;]
guillaume@ubuntu:~/$ 
</code></pre>

