.. Objectives
.. ----------

.. Clearly state the objectives of the LO (along with RBT level)

.. By the end of this tutorial, you should -- 

..   #. Know what Sage and Sage notebook are.
..   #. Be able to start a Sage shell or notebook
..   #. Be able to start using the notebook
..   #. Be able to create new worksheets 
..   #. Know about the menu options available 
..   #. Know about the cells in the worksheet
..   #. Be able to evaluate cells, create and delete cells, navigate them.
..   #. Be able to make annotations in the worksheet
..   #. Be able to use tab completion. 
..   #. Be able to use code from other languages in the cells.            

.. Prerequisites
.. -------------

.. None. 
     
.. Author              : Madhu
   Internal Reviewer   : Punch
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <15-11-2010, Anand,  OK> [2010-10-05]


Script
------

{{{ Show the slide containing the title }}}

Hello friends. Welcome to this spoken tutorial on Getting started with
Sage and Sage notebook.

{{{ Show the slide containing the outline }}}

In this tutorial, we will learn what Sage is, what is Sage notebook,
how to start and use the sage notebook. In the notebook we will be
specifically learning how to execute our code, how to write
annotations and other content, typesetting the content and how to use
the offline help available.

{{{ Show the slide on what is Sage }}}

To start with, What is Sage? Sage is a free, open-source mathematical
software. Sage can do a lot of math stuff for you including, but not
limited to, algebra, calculus, geometry, cryptography, graph theory
among other things. It can also be used as aid in teaching and
research in any of the areas that Sage supports. So let us start Sage
now

{{{ Shift to terminal }}}

We are assuming that you have Sage installed on your computer now. If
not please visit the page
http://sagemath.org/doc/tutorial/introduction.html#installation for
the tutorial on how to install Sage. 


Let us now learn how to start Sage. On the terminal type::

  sage

This should start a new Sage shell with the prompt sage: which looks
like this

{{{ Show what is displayed on the terminal }}}

So now we can type all the commands that Sage supports here. But Sage
comes bundled with a much more elegant tool called Sage
Notebook? What is Sage Notebook? Sage Notebook provides a web based
user interface to use Sage. So once we have a Sage notebook server up
and running, all we want is a browser to access the Sage
functionality. For example there is an official instance of Sage
Notebook server running at http://sagenb.org You can visit that page,
create an account there and start using Sage! So all you need is just
a browser, a modern browser 

{{{ Intentional *cough* *cough* }}}

#[[Bhanu: what? Are you serious?]]

to use Sage and nothing else! The Sage notebook also provides a
convenient way of sharing and publishing our work, which is very handy
for research and teaching.

However we can also run our own instances of Sage notebook servers on
all the computers we have a local installation of Sage. To start the
notebook server just type::

  notebook()

on the Sage prompt. This will start the Sage Notebook server. If we
are starting the notebook server for the first time, we are prompted
to enter the password for the admin. Type the password and make a note
of it. After this Sage automatically starts a browser page for you
with the notebook opened.

If it doesn't automatically start a browser page check if the Notebook
server started and there were no problems. If so open your browser and
in the address bar type the URL shown in the instructions upon running
the notebook command on the sage prompt.

{{{ The notebook() command gives an instruction telling 
Open your web browser to http://localhost:8000. Point towards it }}}

In our case it is http://localhost:{{{ Tell whatever is shown }}}

{{{ Show the browser with Sage notebook }}}

If you are not logged in yet, it shows the Notebook home page and
textboxes to type the username and the password. You can use the
username 'admin' and the password you gave while starting the notebook
server for the first time. There are also links to recover forgotten
password and to create new accounts.

{{{ If you are logged in tell that you are logged in, log out and show
what is said above for the login page }}}

Once we are logged in with the admin account we can see the notebook
admin page. A notebook can contain a collection of Sage Notebook
worksheets. Worksheet is basically a working area. This is where
we enter all the Sage commands on the notebook.

The admin page lists all the worksheets created. On the topmost part
of this page we have the links to various pages. 

{{{ Whenever you talk on an individual link point your mouse towards
the link. For each of the link go to the page and explain as below }}}

The home link takes us to the admin home page. The published link
takes us to the page which lists all the published worksheets. The log
link has the complete log of all the actions we did on the
notebook. We have the settings link where we can configure our notebook,
the notebook server, create and  mangage accounts. We have a
link to help upon clicking opens a new window with the complete help
of Sage. The entire documentation of Sage is supplied with Sage for
offline reference and this help link is the way to get into it. Then
we can report bugs about Sage by clicking on Report a Problem link and
there is a link to sign out of the notebook.

We can create a new worksheet by clicking New Worksheet link

{{{ Click on the link }}}

Sage prompts you for a name for the worksheet. Let us name the
worksheet as nbtutorial. Now we have our first worksheet which is
empty.

A worksheet will contain a collection of cells. Every Sage command
must be entered in this cell. Cell is equivalent to the prompt on
console. When we create a new worksheet, to start with we will have
one empty cell. Let us try out some math here::

  2 + 2
  57.1 ^ 100

The cap operator is used for exponentiation. If you observed carefully
we typed two commands but the output of only last command was
displayed. By default each cell displays the result of only the last
operation. We have to use print statement to display all the results
we want to be displayed.

{{{ Demonstrate creating a new cell }}}

Now to perform more operations we want more cells. So how do we create
a new cell? It is very simple. As we hover our mouse above or below
the existing cells we see a blue line, by clicking on this new line we
can create a new cell. 

We have a cell, we have typed some commands in it, but how do we
evaluate that cell? Pressing Shift along with Enter evaluates the
cell. Alternatively we can also click on the evaluate link to evaluate
the cell

{{{ Evaluate the cell and demonstrate for both methods separately
}}}::

  matrix([[1,2], [3,4]])^(-1)

After we create many cells, we may want to move between the cells. To
move between the cells use Up and Down arrow keys. Also clicking on
the cell will let you edit that particular cell.

{{{ Move between two cells created }}}

To delete a cell, clear the contents of the cell and hit backspace

{{{ Clear and demonstrate deleting the cell }}}::

  Makes no sense

If you want to add annotations in the worksheet itself on the blue
line that appears on hovering the mouse around the cell, Hold Shift
and click on the line. This creates a What You See Is What You Get
cell.

{{{ Create a HTML editable cell }}}

We can make our text here rich text. We can make it bold, Italics, we
can create bulleted and enumerated lists in this area::

  This text contains both the **bold** text and also *italicised*
  text.
  It also contains bulleted list:
  * Item 1
  * Item 2
  It also contains enumerate list:
  1. Item 1
  2. Item 2

In the same cell we can display typeset math using the LaTeX like
syntax::

  $\int_0^\infty e^{-x} \, dx$

We enclose the math to be typeset within $ and $ or $$ and $$ as in
LaTeX.

We can also obtain help for a particular Sage command or function
within the worksheet itself by using a question mark following the
command::

  sin?

Evaluating this cell gives me the entire help for the sin function
inline on the worksheet itself. Similarly we can also look at the
source code of each command or function using double question mark::

  matrix??

Sage notebook also provides the feature for autocompletion. To
autocomplete a command type first few unique characters and hit tab
key::

  sudo<tab>

To see all the commands starting with a specific name type those
characters and hit tab::

  plo<tab>

To list all the methods that are available for a certain variable or
a datatype we can use the variable name followed by the dot to access
the methods available on it and then hit tab::

  s = 'Hello'
  s.rep<tab>

The output produced by each cell can be one of the three states. It
can be either the full output, or truncated output or hidden output.
The output area will display the error if the Sage code we wrote in
the cell did not successfully execute::

  a, b = 10

{{{ Show the three states }}}

The default output we obtained now is a truncated output. Clicking at
the left of the output area when the mouse pointer turns to hand gives
us the full output, clicking again makes the output hidden and it
cycles.

Lastly, Sage supports a variety of languages and each cell on the
worksheet can contain code written in a specific language. It is
possible to instruct Sage to interpret the code in the language we
have written. This can be done by putting percentage sign(%) followed
by the name of the language. For example, to interpret the cell as
Python code we put::

  %python

as the first line in the cell. Similarly we have: %sh for shell
scripting, %fortran for Fortran, %gap for GAP and so on. Let us see
how this works. Say I have an integer. The type of the integer in
default Sage mode is
{{{ Read the output }}}::

  a = 1
  type(a)

  Output: <type 'sage.rings.integer.Integer'>

We see that Integers are Sage Integers. Now let us put %python as the
first line of the cell and execute the same code snippet::

  %python
  a = 1
  type(a)

  Output: <type 'int'>

Now we see that the integer is a Python integer. Why? Because now we
instructed Sage to interpret that cell as Python code.

This brings us to the end of the tutorial on using Sage. We learnt
quite a lot about using the Notebook User Interface of Sage. We are
now confident that we can comfortably use the notebook to learn more
about Sage in the following tutorials. Let us summarize what we
learnt. In this session we learnt

  * What is Sage
  * How to start Sage shell
  * What is Sage notebook
  * How to start the Sage notebook
  * How to create accounts and start using the notebook
  * How to create new worksheets
  * The menus available on the notebook
  * About cells in the worksheet
  * Methods to evaluate the cell, create new cells, delete the cells
    and navigate around the cells
  * To make annotations in the worksheet
  * Tab completions
  * And embedding code of other scripting languages in the cells

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!
