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

     
.. Author              : Puneeth
   Internal Reviewer   : Anoop Jacob Thomas<anoop@fossee.in>
   External Reviewer   :
   Langauge Reviewer   : Bhanukiran
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello Friends and Welcome to the tutorial on 'loops' in Python. 

.. L2

{{{ Show the objectives slide }}}

.. R2

At the end of this tutorial, you will be able to,

 1. use the ``for`` loop
 #. use the ``while`` loop
 #. Use ``break``, ``continue`` and ``pass`` statements to play around
    with loops.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with for" and "Conditionals".

.. R4

Let us start our ipython interpreter.

.. L4

{{{ switch to the ipython terminal }}}
::

    ipython

.. R5

We shall first begin with the ``while`` loop. The ``while`` loop is
used for repeated execution as long as a condition is ``True``. 

Let us print the squares of all the odd numbers less than 10, using
the ``while`` loop.

.. L5
::

    i = 1

    while i<10:
        print i*i
        i += 2

.. R6

This loop prints the squares of the odd numbers below 10. 

The ``while`` loop, repeatedly checks if the condition is true and
executes the block of code within the loop, if it is. As with any
other block in Python, the code within the ``while`` block is indented
to the right by 4 spaces. 

Pause the video here, try out the following exercise and resume the video.

.. L6

.. L7

{{{ Show slide with exercise 1 }}}

.. R7

 Write a ``while`` loop to print the squares of all the even
 numbers below 10. 

.. R8

Switch to the terminal for solution.

.. L8

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    i = 2

    while i<10:
        print i*i
        i += 2

.. R9

Let us now solve the same problem of printing the squares of all odd
numbers less than 10, using the ``for`` loop. As we know, the ``for``
loop iterates over a list or any other sequential data type. So, we
use the ``range`` function to get a list of odd numbers below 10, and
then iterate over it and print the required stuff. 

.. L9
::

    for n in range(1, 10, 2):
        print n*n

.. R10

We can see that we got the same output as before.Note that the lines of code
are less.

Pause the video here, try out the following exercise and resume the video.

.. L10

.. L11

{{{ Show slide with exercise 2 }}}

.. R11

 Write a ``for`` loop to print the squares of all the even
 numbers below 10. 

.. R12

Switch to the terminal for solution.

.. L12

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    for n in range(2, 10, 2):
        print n*n

.. R13

Let us now look at how to use the keywords, ``pass``, ``break`` and
``continue``.

As we already know, ``pass`` is just a syntactic filler. It is used
for the sake of completion of blocks, that do not have any code within
them. 

.. L13
::

    for n in range(2, 10, 2):
        pass

.. R14

``break`` is used to break out of the innermost loop. The ``while``
loop to print the squares of all the odd numbers below 10, can be
modified using the ``break`` statement, as follows

.. L14
::

    i = 1

    while True:
        print i*i
        i += 2
        if i<10:
            break

.. R15

``continue`` is used to skip execution of the rest of the loop on this
iteration and continue to the end of this iteration. 

Say, we wish to print the squares of all the odd numbers below 10,
which are not multiples of 3, we would modify the ``for`` loop as
follows.  

.. L15
::

    for n in range(1, 10, 2):
        if n%3 == 0:
            continue      
        print n*n

.. R16
  
Pause the video here, try out the following exercise and resume the video.

.. L16

.. L17

{{{ Show slide with exercise 3 }}}

.. R17

Using the ``continue`` keyword modify the ``for`` loop, with the
``range(2, 10, 2)``, to print the squares of even numbers below 10,
which are multiples of 4.
(Do not modify the range function call.)

.. R18

Switch to the terminal for solution.

.. L18

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    for n in range(2, 10, 2):
        if n%4:
            continue      
        print n*n

.. L19

{{{ Show summary slide }}}

.. R19

This brings us to the end of this tutorial. In this tutorial, we have learnt to,

  1. Iterate over a sequence using ``for'' and ``while'' loops.
  #. Break out of loops using ``break'' statement.
  #. Skip iterations using ``continue'' statement.
  #. Use the ``pass'' statement in a loop. 

.. L20

{{{Show self assessment questions slide}}}

.. R20

Here are some self assessment questions for you to solve

 1. Given ``range(1,4)``; Write a code to print only the number 1.

 2. Which statement do you use to skip iterations.
    - break
    - pass
    - continue

.. L21

{{{solution of self assessment questions on slide}}}

.. R21

And the answers,

1. We can use the break statement in a for loop as,

::
    for i in range(1, 4):
        print i 
        break

2. In order to skip iterations,we make use of the ``continue`` statement.

.. L22

{{{ Show the thankyou slide }}}

.. R22

Hope you have enjoyed this tutorial and found it useful.
Thank you!
