.. Objectives
.. ----------

.. At the end of this tutorial, you will be able to 

.. 1. Write blocks of code in python.
.. #. Use for loop.
.. #. Use ``range()`` function.
.. #. Write blocks in python interpreter
.. #. Write blocks in ipython interpreter.


.. Prerequisites
.. -------------

..   1. should have ``ipython`` and ``pylab`` installed. 
..   #. getting started with ``ipython``.
..   #. getting started with lists.

     
.. Author              : Anoop Jacob Thomas <anoop@fossee.in>
   Internal Reviewer   : Nishanth
   Internal Reviewer(2): Amit
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <10-11-2010, Anand, OK> [2010-10-05]


=============================
Getting started with for loop
=============================

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello and welcome to the tutorial on `Getting started with ``for`` loop`. 

.. L2

{{{ Show slide with objectives }}}

.. R2

At the end of this tutorial, you will be able to, 

 1. Write blocks of code in python using indentation.
 #. Use the ``for`` loop.
 #. Use ``range()`` function.
 #. Write blocks in python interpreter
 #. Write blocks in ipython interpreter.

.. L3

{{{ Show slide with pre-requisite }}}

{{{ switch to next slide, 'Whitespace in python' }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with Lists".

In Python whitespace is significant, and the blocks are visually
separated.The best practice is to indent the code using four spaces.

As you can see in the slide, “Block B” is an inner block, indented by 
4 spaces.
After “Block B” the next statement in ”Block A” starts from the same 
indentation level of other ”Block A” Statements.

.. R4

Start the ipython interpreter using ipython -pylab.

.. L4
::

    ipython -pylab

.. R5

Now let us move straight into ``for`` loop.

.. L5

.. L6

{{{ switch to slide showing exercise 1 }}}

.. R6

Write a for loop which iterates through a list of numbers and find the
square root of each number.
numbers are 1369, 7225, 3364, 7056, 5625, 729, 7056, 576, 2916

.. R7

For the problem, first we need to create a ``list`` of numbers and
then iterate over the list and find the square root of each element in
it. And let us create a script, rather than typing it out in the
interpreter itself. Open your text editor and type the following code 
shown on the slide.

.. L7

{{{ Switch to the slide Solution 1 }}}

.. L8

{{{ switch to next slide, save & run script }}}

.. R8

Now switch to your terminal and run the script as,

.. L9
::

    %run -i list_roots.py

.. R9

So that was easy! All what we did was iterate over the list element by
element and then use the element for calculation. Note that here we
used two variables,the variable ``numbers``, which is a list,and the
other variable ``each``, which is the element of list under consideration
in each cycle of the ``for`` loop. The variable names can be chosen by
you.

.. L10

{{{ show the script which was created }}}

.. R10

Note that the lines after ``for`` statement, is indented using four
spaces.

.. L11

{{{ highlight the line after ``for`` statement }}}

.. R11

It means that line is a part of the for loop. And it is a block of code,
although it is only a single statement in the block. Also, the fourth
line or the immediate line after the ``for`` block is not indented.

.. L12

{{{ Highlight the fourth line - the line just after for loop }}}

.. R12

It means that it is not a part of the ``for`` loop and the lines after
that dont fall in the scope of the ``for`` loop. Thus each block is
separated by the indentation level and that marks the importance of
white-spaces in Python.

.. L13

{{{ switch to slide showing exercise 2 }}}

.. R13

Print the square root of numbers in the list. 
And this time let us do it right in the IPython interpreter. 
So let us create a list. 

.. L14

{{{ switch focus to the IPython interpreter }}}
::

    numbers = [1369, 7225, 3364, 7056, 5625, 729, 7056, 576, 2916]
    for each in numbers:

{{{ Hit enter }}}

.. R14

You will notice that, as soon as you press the enter key
after for statement, the prompt changes to four dots and the cursor is
not right after the four dots but there are four spaces from the
dots.

.. L15

{{{ Higlight the four dots }}}

.. R15

Please note that IPython automatically indents the block. The
four dots tell you that you are inside a block.

.. R16

Now type the rest of the ``for`` loop,

.. L16
::

    print "Square root of", each,
    print "is", sqrt(each)

.. R17

Now we have finished the statements in the block, and still the
interpreter is showing four dots, this means that you are still inside the
block. To exit from the block press the return key or the enter key twice
without entering anything else.

.. L17

{{{ Hit enter twice }}}

.. R18

It printed the square root of each
number in the list, which was executed in the ``for`` loop.

.. L18

.. L19

{{{ switch to slide exercise 3 }}}

.. R19

Find the cube of all the numbers from one to ten. 
But this time let us try it in the vanilla version of Python interpreter.

.. R20

Start the vanilla version of Python interpreter by issuing the command
``python`` in your terminal.

.. L20

{{{ Switch to the terminal }}}
::

    python
    
    for i in range(1,11):

{{{ Hit enter }}}

.. R21

press enter once, and we will see that this time it shows four
dots, but the cursor is close to the dots, so we have to indent the
block.

.. L21

{{{ Highlight the cursor }}}

.. R22

The vanilla version of Python interpreter does not indent the
code automatically. So enter four spaces there and then type the
following

.. L22
::
    
    print i, "cube is", i**3

.. R23

Now when we hit enter, we still see the four dots.To get out of the
block, hit enter once again.

.. L23

{{{ Hit enter }}}

.. L24

{{{ switch to the next slide, ``range()`` function }}}

.. R24

Okay! so the main thing we learnt here is how to use the Python
interpreter and the IPython interpreter to specify blocks. But while we
were generating the multiplication table we used something new,
``range()`` function. ``range()`` is an inbuilt function in Python
which can be used to generate a ``list`` of integers from a starting
number to an ending number. Note that the ending number that you
specify will not be included in the ``list``.

.. L25

{{{ switch to next slide exercise 4 }}}

.. R25

Print all the odd numbers from 1 to 50. 
Let us do it in our IPython interpreter for ease of use.

.. L26

{{{ switch focus to ipython interpreter }}}
::

    ipython 

.. R26

The problem can be solved by just using the ``range()`` function.

It can be solved as,

.. L27
::

    print range(1,51,2)

.. R27

This time we passed three parameters to ``range()`` function unlike
the previous case where we passed only two parameters. The first two
parameters are same in both the cases. The first parameter is the
starting number of the sequence and the second parameter is the end of
the range. Note that the sequence does not include the ending
number. The third parameter is for stepping through the sequence. Here
we gave two which means we are skipping every alternate element.

.. L28

{{{ switch to Summary slide }}}

.. R28

This brings us to the end of the tutorial.In this tutorial,we learnt to,

 1. create blocks in python using ``for`` loop
 #. indent the blocks of code
 #. iterate over a list using ``for`` loop
 #. use the ``range()`` function

.. L29

{{Show self assessment questions slide}}

.. R29

Here are some self assessment questions for you to solve

1. Indentation is not mandatory in Python

   - True
   - False

2. Write a code using ``for`` loop to print the product of all 
   natural numbers from 1 to 20.


3. What will be the output of-
::

    range(1,5)

.. L30

{{{ solution of self assessment questions on slide }}}

.. R30

And the answers,

1. False.Indentation is essential in python.

2. We use the ``for`` loop in the following manner.
::

    y = 1
    for x in range(1,21):
        y*=x
    print y

3. ``range(1,5)`` will produce a list of integers from 1 to 4.
   [1,2,3,4]

.. L31

{{{ switch to Thank you slide }}}

.. R31

Hope you have enjoyed this tutorial and found it useful.
Thank you!

