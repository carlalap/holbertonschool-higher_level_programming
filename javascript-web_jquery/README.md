# Project: JavaScript - Web jQuery

<div class="panel panel-default" id="project-description">
  <div class="panel-body">

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript" title="What is JavaScript?" target="_blank">What is JavaScript?</a> </li>
<li><a href="https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/" title="Selector" target="_blank">Selector</a> </li>
<li><a href="https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/" title="Get and set content" target="_blank">Get and set content</a> </li>
<li><a href="https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/" title="Manipulate CSS classes" target="_blank">Manipulate CSS classes</a> </li>
<li><a href="https://jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/" title="Manipulate DOM elements" target="_blank">Manipulate DOM elements</a> </li>
<li><a href="https://oscarotero.com/jquery/" title="API" target="_blank">API</a> </li>
<li><a href="https://jquery-tutorial.net/ajax/introduction/" title="Introduction" target="_blank">Introduction</a> </li>
<li><a href="https://jquery-tutorial.net/ajax/the-get-and-post-methods/" title="GET &amp; POST request" target="_blank">GET &amp; POST request</a> </li>
<li><a href="https://www.youtube.com/watch?v=fEYx8dQr_cQ&ab_channel=LearnCode.academy" title="JQuery Ajax Tutorial #1 - Using AJAX &amp; API&#39;s" target="_blank">JQuery Ajax Tutorial #1 - Using AJAX &amp; API&rsquo;s</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong" title="What went wrong? Troubleshooting JavaScript" target="_blank">What went wrong? Troubleshooting JavaScript</a> </li>
<li><a href="https://jquery.com/" title="JQuery" target="_blank">JQuery</a> </li>
<li><a href="https://api.jquery.com/" title="JQuery API" target="_blank">JQuery API</a> </li>
<li><a href="https://learn.jquery.com/ajax/" title="JQuery Ajax" target="_blank">JQuery Ajax</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/rL7HMo8ZPWu1icccmE6zvw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))</li>
<li>How to select HTML elements in JavaScript</li>
<li>How to select HTML elements with JQuery</li>
<li>What are differences between <code>ID</code>, <code>class</code> and <code>tag name</code> selectors</li>
<li>How to modify an HTML element style</li>
<li>How to get and update an HTML element content</li>
<li>How to modify the DOM</li>
<li>How to make a <code>GET</code> request with JQuery Ajax</li>
<li>How to make a <code>POST</code> request with JQuery Ajax</li>
<li>How to listen/bind to DOM events</li>
<li>How to listen/bind to user events</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Chrome (version 57.0)</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be <code>semistandard</code> compliant with the flag <code>--global $</code>: <code>semistandard *.js --global $</code></li>
<li>You must use JQuery version 3.x</li>
<li>You are not allowed to use <code>var</code></li>
<li>HTML should not reload for each action: DOM manipulation, update values, fetch data&hellip;</li>
</ul>

<h2>More Info</h2>

<h3>Import JQuery</h3>

<pre><code>&lt;head&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
&lt;/head&gt;
</code></pre>
  </div>
</div>

<h2 class="gap">Tasks</h2>

<div data-role="task19619" data-position="1" id="task-num-0">
    <div class="panel panel-default task-card " id="task-19619">
  <span id="user_id" data-id="6138"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. No JQuery
    </h3>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a JavaScript script that updates the text color of the <code>&lt;header&gt;</code> element to red (<code>#FF0000</code>):</p>

<ul>
<li>You must use <code>document.querySelector</code> to select the HTML tag</li>
<li>You can&rsquo;t use the JQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/$ cat 0-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;0-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. With JQuery
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a JavaScript script that updates the text color of the <code>&lt;header&gt;</code>  element to red (<code>#FF0000</code>):</p>

<ul>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the JQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/$ cat 1-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;1-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Click and turn red
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

<!-- Task Body -->
   <p>Write a JavaScript script that updates the text color of the  <code>&lt;header&gt;</code> element to red (<code>#FF0000</code>) when the user clicks on the tag <code>DIV#red_header</code>:</p>

<ul>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the JQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/$ cat 2-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id=&quot;red_header&quot;&gt;Red header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;2-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Add `.red` class
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a JavaScript script that adds the class <code>red</code> to the <code>&lt;header&gt;</code> element  when the user clicks on the tag <code>DIV#red_header</code></p>

<ul>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the JQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/$ cat 3-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;style&gt;
      .red {
        color: #FF0000;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id=&quot;red_header&quot;&gt;Red header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;3-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Toggle classes
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a JavaScript script that toggles the class of the <code>&lt;header&gt;</code> element  when the user clicks on the tag <code>DIV#toggle_header</code>:</p>

<ul>
<li>The <code>&lt;header&gt;</code> element must always have one class: <code>red</code> or <code>green</code>, never both in the same time and never empty.</li>
<li>If the current class is <code>red</code>, when the user click on <code>DIV#toggle_header</code>, the class must be updated to <code>green</code> ; and the reverse.</li>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the JQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/$ cat 4-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;style&gt;
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header class=&quot;green&quot;&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id=&quot;toggle_header&quot;&gt;Toggle header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;4-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. List of elements
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a JavaScript script that adds a <code>&lt;li&gt;</code> element to a list when the user clicks on the tag <code>DIV#add_item</code>:</p>

<ul>
<li>The new element must be: <code>&lt;li&gt;Item&lt;/li&gt;</code></li>
<li>The new element must be added to <code>UL.my_list</code></li>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the JQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/$ cat 5-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;add_item&quot;&gt;Add item&lt;/div&gt;
    &lt;br /&gt;
    &lt;ul class=&quot;my_list&quot;&gt;
      &lt;li&gt;Item&lt;/li&gt;
    &lt;/ul&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;5-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Change the text
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a JavaScript script that updates the text of the <code>&lt;header&gt;</code> element  to <code>New Header!!!</code> when the user clicks on <code>DIV#update_header</code></p>

<ul>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the JQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/$ cat 6-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;update_header&quot;&gt;Update the header&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;6-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. Star wars character
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a JavaScript script that fetches the character <code>name</code> from this URL: <code>https://swapi-api.hbtn.io/api/people/5/?format=json</code></p>

<ul>
<li>The name must be displayed in the HTML tag <code>DIV#character</code></li>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the JQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/$ cat 7-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Star Wars character
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;character&quot;&gt;&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;7-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. Star Wars movies
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a JavaScript script that fetches and lists the <code>title</code> for all movies by using this URL: <code>https://swapi-api.hbtn.io/api/films/?format=json</code></p>

<ul>
<li>All movie titles must be list in the HTML tag <code>UL#list_movies</code></li>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the JQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/$ cat 8-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Star Wars movies
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;ul id=&quot;list_movies&quot;&gt;
    &lt;/ul&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;8-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      9. Say Hello!
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a JavaScript script that fetches from <code>https://stefanbohacek.com/hellosalut/?lang=fr</code> and displays the value of <code>hello</code> from that fetch in the HTML tag <code>DIV#hello</code>.</p>

<ul>
<li>The translation of &ldquo;hello&rdquo; must be displayed in the HTML tag <code>DIV#hello</code></li>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the JQuery API</li>
<li>Your script must work when it is imported from the <code>&lt;head&gt;</code> tag</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/$ cat 9-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;9-script.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Say Hello!
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;hello&quot;&gt;&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/$ 
</code></pre>

  </div>
