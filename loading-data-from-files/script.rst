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
     
.. #[Anand: author and internal reviewer  not mentioned]
.. Author              : Puneeth Changanti
   Internal Reviewer   : Nishanth Amuluru
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <06-11-2010 Anand, OK> [2010-10-05]

Script
------

{{{ Show the slide containing title }}}

Hello Friends. Welcome to this tutorial on loading data from files.

{{{ Screen shows welcome slide }}}

We often require to plot points obtained from experimental
observations. In this tutorial we shall learn to read data from files
and save it into sequences that can later be used to plot.

{{{ Show the outline for this tutorial }}} 

We shall use the ``loadtxt`` command to load data from files. We will
be looking at how to read a file with multiple columns of data and
load each column of data into a sequence. 

{{{ switch back to the terminal }}}

As usual, let us start IPython, using 
::

  ipython -pylab 

Now, Let us begin with reading the file primes.txt, which contains
just a list of primes listed in a column, using the loadtxt command.
The file, in our case, is present in ``/home/fossee/primes.txt``. 

{{{ Navigate to the path in the OS, open the file and show it }}}

.. #[punch: do we need a slide for showing the path?]

.. We use the ``cat`` command to see the contents of this file. 

.. #[punch: should we show the cat command here? seems like a good place
   to do it] ::

     cat /home/fossee/primes.txt

.. #[Nishanth]: A problem for windows users.
                Should we simply open the file and show them the data
                so that we can be fine with GNU/Linux ;) and windows?

Now let us read this list into the variable ``primes``.
::

  primes = loadtxt('/home/fossee/primes.txt')

``primes`` is now a sequence of primes, that was listed in the file,
``primes.txt``.

We now type, ``print primes`` to see the sequence printed.

We observe that all of the numbers end with a period. This is so,
because these numbers are actually read as ``floats``. We shall learn
about them, later.

Now, let us use the ``loadtxt`` command to read a file that contains
two columns of data, ``pendulum.txt``. This file contains the length
of the pendulum in the first column and the corresponding time period
in the second. Note that ``loadtxt`` needs both the columns to have
equal number of rows. 

.. Following is an exercise that you must do. 

.. %%1%% Use the ``cat`` command to view the contents of this file.

.. Please, pause the video here. Do the exercise and then continue. 

.. This is how we look at the contents of the file, ``pendulum.txt``
.. ::

..   cat /home/fossee/pendulum.txt

.. #[Nishanth]: The first column is L values and second is T values
                from a simple pendulum experiment.
                Since you are using the variable names later in the
                script.
                Not necessary but can be included also.

Let us, now, read the data into the variable ``pend``. Again, it is
assumed that the file is in ``/home/fossee/``
::

  pend = loadtxt('/home/fossee/pendulum.txt')

Let us now print the variable ``pend`` and see what's in it. 
::

  print pend

Notice that ``pend`` is not a simple sequence like ``primes``. It has
two sequences, containing both the columns of the data file. Let us
use an additional argument of the ``loadtxt`` command, to read it into
two separate, simple sequences.
::

  L, T = loadtxt('/home/fossee/pendulum.txt', unpack=True)

.. #[Nishanth]: It has a sequence of items in which each item contains
                two values. first is l and second is t

Let us now, print the variables L and T, to see what they contain.
::

  print L
  print T

.. #[Nishanth]: Stress on ``unpack=True`` ??

Notice, that L and T now contain the first and second columns of data
from the data file, ``pendulum.txt``, and they are both simple
sequences. ``unpack=True`` has given us the two columns into two
separate sequences instead of one complex sequence. 

{{{ show the slide with loadtxt --- other features }}}

In this tutorial, we have learnt the basic use of the ``loadtxt``
command, which is capable of doing a lot more than we have used it for
until now. Let us look at an example, but before that do this
exercise. 

%%1%% Read the file ``pendulum_semicolon.txt`` which contains the same
data as ``pendulum.txt``, but the columns are separated by semi-colons
instead of spaces. Use the IPython help to see how to do this. 

Please, pause the video here. Do the exercise and then continue. 

{{{ switch back to the terminal }}}
::

  L, T = loadtxt('/home/fossee/pendulum_semicolon.txt', unpack=True, delimiter=';')

  print L

  print T

This brings us to the end of this tutorial. 

{{{ show the summary slide }}}

You should now be able to do the following, comfortably. 

  + Read data from files, containing a single column of data using the
    ``loadtxt`` command.
  + Read multiple columns of data, separated by spaces or other
    delimiters.

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!

