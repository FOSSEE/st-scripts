.. Objectives
.. ----------

.. By the end of this tutorial, you will be able to

.. 1. use the ``for`` loop 
.. #. use the ``while`` loop
.. #. Use ``break``, ``continue`` and ``pass`` statements to play around
..    with loops.

.. Prerequisites
.. -------------

.. 1. getting started with ipython
.. #. getting started with for
.. #. conditionals

     
.. Author              : 
   Internal Reviewer   : 
   External Reviewer   :
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]

Script
------

{{{ Show the slide containing title }}}

Hello Friends. Welcome this tutorial on loops in Python. 

{{{ Show the outline slide }}}

In this tutorial, we shall look at ``while`` and ``for`` loops. We
shall then look at the ``break``, ``continue`` and ``pass`` keywords
and how to use them. 

{{{ switch to the ipython terminal }}}

We have an ``ipython`` terminal, that we shall use through out this
tutorial. 

We shall first begin with the ``while`` loop. The ``while`` loop is
used for repeated execution as long as a condition is ``True``. 

Let us print the squares of all the odd numbers less than 10, using
the ``while`` loop.

::

  i = 1

  while i<10:
      print i*i
      i += 2

This loop prints the squares of the odd numbers below 10. 

The ``while`` loop, repeatedly checks if the condition is true and
executes the block of code within the loop, if it is. As with any
other block in Python, the code within the ``while`` block is indented
to the right by 4 spaces. 

Following is an exercise that you must do. 

%%1%% Write a ``while`` loop to print the squares of all the even
numbers below 10. 

Please, pause the video here. Do the exercise and then continue. 

::

  i = 2

  while i<10:
      print i*i
      i += 2

Let us now solve the same problem of printing the squares of all odd
numbers less than 10, using the ``for`` loop. As we know, the ``for``
loop iterates over a list or any other sequential data type. So, we
use the ``range`` function to get a list of odd numbers below 10, and
then iterate over it and print the required stuff. 

::

  for n in range(1, 10, 2):
      print n*n

Following is an exercise that you must do. 

%%2%% Write a ``for`` loop to print the squares of all the even
numbers below 10. 

Please, pause the video here. Do the exercise and then continue. 

::

  for n in range(2, 10, 2):
      print n*n

Let us now look at how to use the keywords, ``pass``, ``break`` and
``continue``.

As we already know, ``pass`` is just a syntactic filler. It is used
for the sake of completion of blocks, that do not have any code within
them. 

::

  for n in range(2, 10, 2):
      pass

``break`` is used to break out of the innermost loop. The ``while``
loop to print the squares of all the odd numbers below 10, can be
modified using the ``break`` statement, as follows
::

  i = 1

  while True:
      print i*i
      i += 2
      if i<10:
          break

``continue`` is used to skip execution of the rest of the loop on this
iteration and continue to the end of this iteration. 

Say, we wish to print the squares of all the odd numbers below 10,
which are not multiples of 3, we would modify the for loop as follows.
::

  for n in range(1, 10, 2):
      if n%3 == 0:
          continue      
      print n*n
  

Following is an exercise that you must do. 

%%3%%Using the ``continue`` keyword modify the ``for`` loop to print
the squares of even numbers below 10, to print the squares of only
multiples of 4. (Do not modify the range function call.) 

Please, pause the video here. Do the exercise and then continue. 
::

  for n in range(2, 10, 2):
      if n%4:
          continue      
      print n*n

{{{ Show summary slide }}}

That brings us to the end of this tutorial. In this tutorial, we have
learnt about looping structures in Python and the use of the keywords
``pass``, ``break`` and ``continue``. 

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!
