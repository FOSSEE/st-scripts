.. Objectives
.. ----------

.. At the end of this spoken tutorial, you will be able to: 
.. 1. Open a file. 
.. #. Read the content of the file line by line. 
.. #. Read entire contents of the file at once. 
.. #. Close the file. 

.. Prerequisites
.. -------------

.. 1. getting started with ipython
.. #. getting started with lists
.. #. getting started with for
     
.. Author              : Puneeth
   Internal Reviewer   : Anoop Jacob Thomas<anoop@fossee.in>
   External Reviewer   :
   Language Reviewer    : Bhanukiran
   Checklist OK?       : <06-11-2010, Anand, OK> [2010-10-05]

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello Friends and Welcome to the tutorial on "Getting started with files". 

.. L2

{{{ Show slide with objectives }}}

.. R2

At the end of this tutorial, you will be able to, 
 
 1. Open a file. 
 #. Read the contents of the file line by line. 
 #. Read the entire content of file at once. 
 #. Append the lines of a file to a list.
 #. Close the file. 

.. L3

{{{ Show slide with pre-requisite }}}

{{{ switch to the terminal }}}
::

    ipython -pylab 

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with Lists" and "Getting started with For".

Open the terminal and start ipython

.. R4

Let us first open the file, ``pendulum.txt`` present in
``/home/fossee/``. 

.. L4
::

    f = open('/home/fossee/pendulum.txt')

.. R5

Here ``f`` is called a file object. Let us type ``f`` on the terminal to
see what it is. 

.. L5
::

    f

.. R6

The file object shows the filepath and mode of the file which is open. 
'r' stand for read only mode and 'w' stands for write mode. 
As you can see, this file is open in read only mode.

.. L6

.. R7

We shall first learn to read the whole file into a single
variable. We use the ``read`` method to read all the contents of the file
into the variable, ``pend``. 

.. L7
::

    pend = f.read()

.. R8

Now, let us see what ``pend`` contains, by typing ``print pend``

.. L8
::

    print pend

.. R9

We can see that ``pend`` has all the data of the file. Type just ``pend``
to see more explicitly, what it contains. 

.. L9
::

    pend

.. L10

{{{ show slide with exercise 1 }}}

.. R10

Pause the video here, try out the following exercise and resume the video.

Split the variable into a list, ``pend_list``, of the lines in
the file.

.. L11
::

    pend_list = pend.splitlines()
    pend_list

.. R11

We use the function ``splitlines`` to solve this problem.

.. R12

Now, let us learn to read the file line-by-line. But, before that we
will have to close the file, since the file has already been read till
the end.

Let us close the file opened into f.

.. L12
::

    f.close()

.. R13

Again type ``f`` on the prompt to see what it contains. 

.. L13
::

    f

.. R14

Notice, that it now says the file has been closed. It is a good
programming practice to close any file objects that we have
opened, after their job is done.

.. L14

.. L15

{{{ Show slide with exercise 2 }}}

.. R15

Let us, now move on to reading files line-by-line. 
Pause the video here, try out the following exercise and resume the video.

Re-open the file ``pendulum.txt`` with ``f`` as the file object.

.. R16

We just use the up arrow until we reach the open command and issue
it again. 

.. L16
::

    f = open('/home/fossee/pendulum.txt')

.. R17

Now, to read the file line-by-line, we iterate over the file
object line-by-line, using the ``for`` command. Let us iterate over
the file line-wise and print each of the lines. 

.. L17
::

    for line in f:
        print line

.. R18

``line`` is a variable, sometimes called the loop
variable, and it is not a keyword. We could have used any other
variable name, but ``line`` seems meaningful enough.

.. L18

.. R19

Instead of just printing the lines, let us append them to a list,
``line_list``. We first initialize an empty list, ``line_list``. 

.. L19
::

    line_list = [ ]

.. R20

Let us then read the file line-by-line and then append each of the
lines to the list. We could, as usual close the file using
``f.close`` and re-open it. But, this time, let's leave alone the
file object ``f`` and directly open the file within the for
statement. This will save us the trouble of closing the file, each
time we open it. 

.. L20
::

    for line in open('/home/fossee/pendulum.txt'):
        line_list.append(line)

.. R21

Let us see what ``line_list`` contains. 

.. L21
::

    line_list

.. R22

Notice that ``line_list`` is a list of the lines in the file, along
with the newline characters. If you noticed, ``pend_list`` did not
contain the newline characters, because the string ``pend``, was
split on the newline characters. 

We can strip out the newline characters from the lines by using some 
string methods which we shall look in the further tutorial on strings.

.. L22

.. L23

{{{ Show the summary slide }}}

.. R23

This brings us to the end of this tutorial. In this tutorial, we 
learnt to,
  
 1. Open and close files using the ``open`` and ``close`` functions 
    respectively.
 #. Read the data in the files as a whole,by using the ``read`` function.
 #. Read the data in the files line by line by iterating over the file 
    object using the
    ``for`` loop. 
 #. Append the lines of a file to a list using the ``append`` function 
    within the ``for`` loop.

.. L24

{{{Show self assessment questions slide}}}

.. R24

Here are some self assessment questions for you to solve

1. The ``open`` function returns a 

   - string
   - list
   - file object
   - function

2. What does the function ``splitlines()`` do.

   - Displays the data as strings,all in a line
   - Displays the data line by line as strings
   - Displays the data line by line but not as strings

.. L25

{{{solution of self assessment questions on slide}}}

.. R25

And the answers,

1. The function ``open``, returns a file object.
2. The function ``splitlines`` displays the data line by line as strings.

.. L26

{{{ Show the Thankyou slide }}}

.. R26

Hope you have enjoyed this tutorial and found it useful.
Thank you!

