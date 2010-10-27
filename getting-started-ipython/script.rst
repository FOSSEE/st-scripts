.. Objectives
.. ----------

.. At the end of this tutorial, you will be able to 

.. 1. invoke the ``ipython`` interpreter. 
.. #. quit the ``ipython`` interpreter. 
.. #. navigate in the history of ``ipython``. 
.. #. use tab-completion. 
.. #. look-up documentation of functions. 
.. #. interrupt incomplete or incorrect commands.

.. Prerequisites
.. -------------

.. should have ``ipython`` and ``pylab`` installed. 
     
.. Author              : Puneeth 
   Internal Reviewer   : Anoop Jacob Thomas<anoop@fossee.in>
   External Reviewer   :
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]


Script
------

{{{ Show the slide containing title }}}

Hello Friends and Welcome to the tutorial on getting started with
``ipython``. 

{{{ Show slide with outline }}}

This tutorial will cover the basic usage of the ``ipython``
interpreter. The following topics would be covered.

IPython is an enhanced Python interpreter that provides features like
tabcompletion, easier access to help and lot of other functionality
which are not available in the vanilla Python interpreter.

First let us see how to invoke the ``ipython`` interpreter.

We type
::

  ipython

at the terminal prompt to invoke the ipython interpreter.

We get a prompt with ``In [1]:`` after getting some information about
the version of Python installed and some help commands.   

If you get an error saying something like ``ipython is not
installed``, refer to the tutorial on how to install the packages
required for this course.

Now, to quit the ipython interpreter, type Ctrl-D.  You are prompted
asking if you really want to exit, type y to say yes and quit ipython.

Start ipython again, as you did before.

The prompt that you have says ``In [1]``. ``In`` stands for input and the
ipython interpreter is ready to accept input from you.

Now let us see, how we can type some commands into the interpreter.

Start with the simplest thing, addition.

Let's type 
::
  1+2 

at the prompt. IPython promptly gives back the output as 3.  Notice
that the output is displayed with an ``Out[1]`` indication.

.. #[[Anoop: I think we can illustrate In [] and Out[] in slides]]

Let's try out few other mathematical operations.
::

  5 - 3
  7 - 4
  6 * 5

Now let's ``print 1+2``. Instead of typing the whole thing, we make
use of the fact that IPython remembers the history of the commands
that you have already used. We use the up arrow key to go back the
command ``1+2``. We then use the left-arrow key to navigate to the
beginning of the line and add the word ``print`` and a space. Then hit
enter and observe that the interpreter prints out the value as 3,
without the Out[] indication.

Now, let's change the previous command ``print 1+2`` to ``print
10*2``.  We use the up arrow again to navigate to the previous command
and use the left arrow key to move the cursor on to the + symbol and
then use the delete key to remove it and type 0 and * to change the
expression to the required one.  We hit enter to see the output of
``print``. 

.. #[[Anoop: We could create a slide with heading Tab Completion and
   give the question as an exercise, basically I feel more slides
   should be used]]

Now, let's say we want to use the function ``round``. We type ``ro``
at the prompt and hit the tab key. As you can see, the IPython
completes the command. This feature is called the tab-completion.

Now, we remove all the characters and just type ``r`` and then hit
tab. IPython does not complete the command since there are many
possibilities. It just lists out all the possible completions.

Following is an exercise that you must do. 

.. #[[Anoop: Include slides for exercises]]

%%1%% Type ``ab`` and hit tab to see what happens. Next, just type
``a`` and hit tab to see what happens.

Please, pause the video here. Do the exercise and then continue. 

``ab`` tab completes to ``abs`` and ``a<tab>`` gives us a list of all
the commands starting with a. 

Now, let's see what these functions are used for.  We will use the
help features of ipython to find this out.

.. #[[Anoop: Another slide which says about ? mark and round? etc, as
   few people cannot just follow by listening (like me) :)]]

To get the help of any function, we first type the function, ``abs``
in our case and then add a ? at the end and hit enter.

As the documentation says, ``abs`` accepts a number as an input and
returns it's absolute value.

We say, 
::

  abs(-19)

  abs(19)

We get 19, as expected, in both the cases.  

Does it work for decimals (or floats)?  Let's try typing abs(-10.5)
and we do get back 10.5.

Following is an exercise that you must do. 

.. #[[Anoop: add slide]]

%%2%% Look-up the documentation of ``round`` and see how to use it.

Please, pause the video here. Do the exercise and then continue. 

::

 round?

If you notice, there are extra square brackets around the ``ndigits``.
This means that ``ndigits`` is optional and 0 is the default value.
Optional parameters are shown in square brackets anywhere in Python
documentation.

The function ``round``, rounds a number to a given precision.

Following are exercises that you must do. 

.. #[[Anoop: add slide]]

%%3%% Check the output of::

  round(2.48)
  round(2.48, 1)
  round(2.48, 2)

  round(2.484)
  round(2.484, 1)
  round(2.484, 2)

Please, pause the video here. Do the exercises and then continue. 

We get 2.0, 2.5 and 2.48, which are what we expect. 

Let's now see how to correct typing errors that we make when typing at
the terminal. As already shown, if we haven't hit the enter key
already, we could navigate using the arrow keys and make deletions
using delete or backspace key and correct the errors. 

Let's now type round(2.484 and hit enter, without closing the
parenthesis. We get a prompt with dots.  This prompt is the
continuation prompt of ``ipython``.  It appears, the previous line is
incomplete in some way.  We now complete the command by typing, the
closing parenthesis and hitting enter.  We get the expected output of
2.5. 

In other instances, if we commit a typing error with a longer and more
complex expression and end up with the continuation prompt, we can
type Ctrl-C to interrupt the command and get back the ``ipython`` input
prompt.

Following is an exercise that you must do. 

.. #[[Anoop: add slide]]

%%4%% Try typing round(2.484, and hit enter. and then cancel the
command using Ctrl-C. Then, type the command, round(2.484, 2) and
resume the video.

Please, pause the video here. Do the exercises and then continue. 

::
  
  round(2.484 
  ^C

  round(2.484, 2)
  
This brings us to the end of the tutorial on getting started with
``ipython``.

.. #[[Anoop: add slides for interrupts, navigating history, I feel
    even a single point will also do]]

In this tutorial we have learnt, how to
{{{ show the outline/summary slide. }}}

  1. invoke the ``ipython`` interpreter. 
  #. quit the ``ipython`` interpreter. 
  #. navigate in the history of ``ipython``. 
  #. use tab-completion. 
  #. look-up documentation of functions. 
  #. interrupt incomplete or incorrect commands.

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!
