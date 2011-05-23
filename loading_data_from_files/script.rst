.. Objectives
.. ----------

.. At the end of this tutorial, you will be able to

.. + Read data from files, containing a single column of data using the
..   ``loadtxt`` command.
.. + Read multiple columns of data, separated by spaces or other
..   delimiters.


.. Prerequisites
.. -------------

.. 1. getting started with ``ipython``
     
.. Author              : Puneeth Changanti
   Internal Reviewer   : Nishanth Amuluru
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <06-11-2010 Anand, OK> [2010-10-05]

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello Friends and Welcome to this tutorial on "loading data from files".

.. L2

{{{ Show slide with objectives }}}

.. R2

At the end of this tutorial, you will be able to,

 1. Read data from files, containing a single column of data 
 #. Read multiple columns of data, separated by spaces or other 
    delimiters.

.. L3

{{{ switch to the terminal }}}
::

    ipython -pylab 

.. R3

Let us switch to the terminal and start IPython, using ipython -pylab

.. R4

Now, Let us begin with reading the file primes.txt, which contains
a list of prime numbers listed in a column, using the loadtxt command.
Please make sure that you provide the correct path of the file, 
'primes.txt'.
The file, in our case, is present in ``/home/fossee/primes.txt``. 

.. L4

{{{ Navigate to the path in the OS, open the file and show it }}}

.. L5
::

     cat /home/fossee/primes.txt

.. R5

Otherwise we can use the ``cat`` command to locate the file and read the 
contents of it.

.. R6

Now let us read this list into the variable ``primes``.

.. L6
::

    primes = loadtxt('/home/fossee/primes.txt')

.. R7

``primes`` is now a sequence of prime numbers, that was listed in the
file,``primes.txt``.

We now type, ``print primes`` to see the sequence printed.

.. L7
::

    print primes

.. R8

We observe that all the numbers end with a period. This is so,
because these numbers are actually read as ``floats``. 

.. L8

{{{Highlight the output on the terminal}}}

.. R9

Now, let us use the ``loadtxt`` command to read a file ``pendulum.txt`` 
that contains two columns of data. This file contains the length
of the pendulum in the first column and the corresponding time period
in the second. Note that here ``loadtxt`` needs both the columns to 
have equal number of rows. 

We use the ``cat`` command to view the contents of this file.

.. L9
::

    cat /home/fossee/pendulum.txt

.. R10

Let us, now, read the data into the variable ``pend``. Again, it is
assumed that the file is in ``/home/fossee/``

.. L10
::

    pend = loadtxt('/home/fossee/pendulum.txt')

.. R11

Let us now print the variable ``pend`` and see what it contains. 

.. L11
::

    print pend

.. R12

Notice that ``pend`` is not a simple sequence like ``primes``. It has
two sequences, containing both the columns of the data file. Let us
use an additional argument of the ``loadtxt`` command, to read it into
two separate, simple sequences.

.. L12
::

    L, T = loadtxt('/home/fossee/pendulum.txt', unpack=True)

.. R13

Let us now, print the variables L and T, to see what they contain.

.. L13

::

    print L
    print T

.. R14

Notice, that L and T now contain the first and second columns of data
from the data file, ``pendulum.txt``, and they are both simple
sequences. ``unpack=True`` has given us the two columns into two
separate sequences instead of one complex sequence. 

.. L14

.. L15

{{{ Show slide with exercise 1 }}}

.. R15

Till now, we have learnt the basic use of the ``loadtxt``
command.Let us try an example.

Pause the video here, try out the following exercise and resume the video.

Read the file ``pendulum_semicolon.txt`` which contains the same
data as ``pendulum.txt``, but the columns are separated by semi-colons
instead of spaces. Use the IPython help to see how to do this. 

.. L16

{{{ switch back to the terminal }}}
::

    L, T = loadtxt('/home/fossee/pendulum_semicolon.txt', unpack=True, 
                   delimiter=';')

    print L

    print T

.. R16

.. L17

{{{ show the summary slide }}}

.. R17

This brings us to the end of this tutorial.In this tutorial,
we have learnt to,

 1. To Read data from files, containing a single column of data 
    using the ``loadtxt`` command.
 #. To Read multiple columns of data, separated by spaces or other 
    delimiters.

.. L18

{{Show self assessment questions slide}}

.. R18

1. ``loadtxt`` can read data from a file with one column
   only. True or False?

2. Given a file ``data.txt`` with three columns of data separated by
   spaces, read it into 3 separate simple sequences. 

3. Given a file ``data.txt`` with three columns of data separated by
   ":", read it into 3 separate simple sequences. 
  

.. L19

{{{solution of self assessment questions on slide}}}

.. R19

And the answers,

1. False. ``loadtxt`` command can read data from files having both single 
   columns as well as multiple columns.

2. A file with three columns of data seperated by spaces to be read into 
   3 seperate sequences,
   we use the loadtxt command as,
::

     x = loadtxt("data.txt", unpack=True)

3. If a file with three columns of data seperated by delimiters,we read 
   it into three seperate sequences by using an additional argument of 
   delimiter in the loadtxt command
::

    x = loadtxt("data.txt", unpack=True, delimiter=":")

.. L20

{{{ Show the Thankyou slide }}}

.. R20

Hope you have enjoyed this tutorial and found it useful.
Thank you!

