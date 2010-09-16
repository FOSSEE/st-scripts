========
 Script
========

Welcome to this tutorial on loading data from files. 

{{{ Screen shows welcome slide }}}

Until now, all the plots we have made use analytic functions. We have
been using analytic functions to generate a sequence of points and
plotting them, against another sequence of points. But, this is not
what we do most often. We often require to plot points obtained from
experimental observations.

#[punch: the initial part of the paragraph may be removed, to make
this a more generic LO?]

In this tutorial we shall learn to read data from files and save it
into sequences that can later be used to plot.

{{{ Show the outline for this tutorial }}} 

We shall use the ``loadtxt`` command to load data from files. We will
be looking at how to get multiple columns of data into multiple
sequences.

{{{ switch back to the terminal }}}

As usual, let us start IPython, using 
::

  ipython -pylab 

Now, Let us begin with reading the file primes.txt, which contains
just a list of primes listed in a column, using the loadtxt command.
The file, in our case, is present in ``/home/fossee/primes.txt``.

#[punch: do we need a slide for showing the path?]

We use the ``cat`` command to see the contents of this file. 

#[punch: should we show the cat command here? seems like a good place
to do it] ::

  cat /home/fossee/primes.txt

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
in the second.

%%1%% Pause the video here, and use the ``cat`` command to view the
contents of this file and then resume the video.

This is how we look at the contents of the file, ``pendulum.txt``
::

  cat /home/fossee/pendulum.txt

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

Let us now, print the variables L and T, to see what they contain.
::

  print L
  print T

Notice, that L and T now contain the first and second columns of data
from the data file, ``pendulum.txt``, and they are both simple
sequences.

{{{ show the slide with loadtxt --- other features }}}

In this tutorial, we have learnt the basic use of the ``loadtxt``
command, which is capable of doing a lot more than we have used it for
until now, for example

%%2%% Pause the video here, and read the file
``pendulum_semicolon.txt`` which contains the same data as
``pendulum.txt``, but the columns are separated by semi-colons instead
of spaces. Use the IPython help to see how to do this. Once you have
finished, resume the video to look at the solution.

{{{ switch back to the terminal }}}
::

  L, T = loadtxt('/home/fossee/pendulum.txt', unpack``True, delimiter``';')

  print L

  print T

This brings us to the end of this tutorial. 

{{{ show the summary slide }}}

You should now be able to do the following, comfortably. 

  + Read data from files, containing a single column of data using the
    ``loadtxt`` command.
  + Read multiple columns of data, separated by spaces or other
    delimiters.

Thank you!   


