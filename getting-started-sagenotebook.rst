Hello friends. Welcome to this spoken tutorial on Getting started with
sage and sage notebook.

{{{ Show the slide containing the title }}}

{{{ Show the slide containing the outline }}}

In this tutorial, we will learn what Sage is, what is Sage notebook,
how to start and use the sage notebook. In the notebook we will be
specifically learning how to execute our code, how to write
annotations and other content, typesetting the content and how to use
the offline help available.

{{{ Show the slide on what is Sage }}}

To start with, What is Sage? Sage is a free, open-source mathematical
software. Sage can do a lot of math stuff for you including but not
limited to algebra, calculus, geometry, cryptography, graph theory
among other things. It can also be used as aid in teaching and
research in any of the areas that Sage supports. So let us start Sage
now

{{{ Shift to terminal }}}

We are assuming that you have Sage installed on your computer now. If
not please visit the page
http://sagemath.org/doc/tutorial/introduction.html#installation for
the tutorial on how to install Sage. Let us move on now.

On the terminal type::

  sage

This should start a new Sage shell with the prompt sage: which looks
like this

{{{ Show what is displayed on the terminal }}}

So now we can type all the commands that Sage supports here. But Sage
comes bundled with a much much much more elegant tool called Sage
Notebook? What is Sage Notebook? Sage Notebook provides a web based
user interface to use Sage. So once we have a Sage notebook server up
and running all we want is a browser to access the Sage
functionality. For example there is an official instance of Sage
Notebook server running at http://sagenb.org You can visit that page,
create an account there and start using Sage! So all you need is just
a browser, a modern browser 

{{{ Intentional *cough* *cough* }}}

to use Sage and nothing else!

However we can also run our own instances of Sage notebook servers on
all the computers we have a local installation of Sage. To start the
notebook server just type::

  notebook()

on the Sage prompt. This will start the Sage Notebook server.
If we are starting the notebook server for the first time, we are
prompted to enter the password for the admin. Type the password and
make a note of it. After this Sage automatically starts a browser page
for you with the notebook opened.

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
worksheets. Worksheets are basically the working area. This is where
we enter all the Sage commands on the notebook.

The admin page lists all the worksheets created. On the topmost part
of this page we have the links to various pages. The home link takes
to the admin home page. The published link takes us the page which
lists all the published worksheets.




This brings us to the end of the session on using Sage notebook. In
this tutorial session we learnt

  *

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thankyou
 
.. Author              : Madhu
   Internal Reviewer 1 :         [potential reviewer: Anoop]
   Internal Reviewer 2 :         [potential reviewer: Puneeth]
   External Reviewer   :

