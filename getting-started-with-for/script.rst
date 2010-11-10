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

{{{ show welcome slide }}}

Hello and welcome to the tutorial `Getting started with ``for`` loop`. 

{{{ switch to next slide, outline slide }}}

In this tutorial we will learn about ``for`` loops in python, and also
learn how to write blocks of code in Python.

.. #[Nishanth]: Instead of saying basics of indenting code,
                say How to define code blocks in Python

{{{ switch to next slide, about whitespaces }}}

In Python whitespace is significant, and the blocks are visually
separated.

.. #[nishanth]: Simply tell how blocks are defined in python.
                The details like braces are not used and its
                advantages like neat code can be told after completely
                explaining the indentation

.. #[Amit]: Do you want to do that here. May be its better to talk about 
   this after some initiation into the idea of blocks. 

The best practice is to indent the code using four spaces.

.. #[Nishanth]: Even this detail may be skipped. Simply say use 4 spaces
                for indentation. Do that while typing so that they can
                actually see what is being typed.

As you can see in the slide, ``Block B`` is an inner block and it is
indented using 4 spaces, and after ``Block B`` the next statement in
``Block A`` starts from the same indentation level of other ``Block
A`` statements.

Now let us move straight into ``for`` loop.

{{{ switch to next slide, problem statement of exercise 1 }}}


Write a for loop which iterates through a list of numbers and find the
square root of each number.
::

    numbers are 1369, 7225, 3364, 7056, 5625, 729, 7056, 576, 2916

.. #[nishanth]: making new list with square roots induces extra complication
                like appending which has no use case here

.. #[Nishanth]: The problem focuses more on square root and creation
                of list. The problem must be simple and focusing on 
                nothing more but the indentation and for loop.
                May be change the problem to print squares than to
                print square roots.

For the problem, first we need to create a ``list`` of numbers and
then iterate over the list and find the square root of each element in
it. And let us create a script, rather than typing it out in the
interpreter itself. Create a script called list_roots.py and type the
following.

{{{ open the text editor and paste the following code there }}}
::

    numbers = [1369, 7225, 3364, 7056, 5625, 729, 7056, 576, 2916]
    for each in numbers:
        print "Square root of", each, "is", sqrt(each)
    print "This is not in for loop!"

..  numbers = [1, 12, 3, 4, 21, 17]
    for each in numbers:
        print each, each * each

.. #[nishanth]: I don't see a use case to append the sq_root to
                square_roots. It is only complicating stuff.
                Simply iterate and print.

{{{ switch to next slide, save and run script }}}

{{{ save the script }}}

Now save the script, and run it from your IPython interpreter. I
assume that you have started your IPython interpreter using ``-pylab``
option.

Run the script as,
::

    %run -i list_roots.py

.. #[Nishanth]: you don't have to use the -i option here

{{{ run the script }}}

So that was easy! All what we did was iterate over the list element by
element and then use the element for calculation. Note that here we
used two variables. One the variable ``numbers``, which is a list,
another one ``each``, which is the element of list under consideration
in each cycle of the ``for`` loop. The variable names can be chosen by
you.

.. #[Nishanth]: The details like we didn't have to find the length
                are relevant for people who have programmed in C or
                other languages earlier. But for a newbie it is more
                of confusing extra info. That part may be skipped.
                Simply go ahead and focus on the syntax of for loop.
                And how the variable name is used inside the for loop.
                If you modify the question to only print, the extra 
                variable sq_root can also be avoided. let it be more
                about "each", "numbers" and "for". no other new names.

{{{ show the script which was created }}}

Note that the lines after ``for`` statement, is indented using four
spaces.

{{{ highlight the line after for statement }}}

It means that line is part of the for loop. And it is a block of code,
although it is only a single statement in the block. And the fourth
line or the immediate line after the ``for`` block is not indented,

{{{ highlight the fourth line - the line just after for loop }}}

it means that it is not part of the ``for`` loop and the lines after
that doesn't fall in the scope of the ``for`` loop. Thus each block is
separated by the indentation level and that marks the importance of
white-spaces in Python.

{{{ switch to the slide which shows the problem statement of the first
problem to be tried out }}}

Now a question for you to try, from the given numbers make a list of
perfect squares and a list of those which are not. The numbers are,
::
    
    7225, 3268, 3364, 2966, 7056, 5625, 729, 5547, 7056, 576, 2916

Pause here and try to solve the problem before proceeding further.

{{{ switch to next slide, problem statement of second problem in
solved exercise}}}

Now let us try a simple one, to print the square root of numbers in
the list. And this time let us do it right in the IPython
interpreter. 

{{{ switch to next slide, Indentation in ``ipython`` }}}

{{{ switch focus to the IPython interpreter }}}

So let us start with making a list. Type the following
::

    numbers = [1369, 7225, 3364, 7056, 5625, 729, 7056, 576, 2916]
    for each in numbers:

and now you will notice that, as soon as you press the return key
after for statement, the prompt changes to four dots and the cursor is
not right after the four dots but there are four spaces from the
dots. Please note that IPython automatically indents the block. The
four dots tell you that you are inside a block. Now type the rest of
the ``for`` loop,

{{{ switch to next slide, Indentation in ``ipython`` (cont'd) }}}

.. #[Nishanth]: Tell that IPython does auto indentation.

::

        print "Square root of", each,
	print "is", sqrt(each)

Now we have finished the statements in the block, and still the
interpreter is showing four dots, this means that you are still inside the
block. To exit from the block press the return key or the enter key twice
without entering anything else. It printed the square root of each
number in the list, and that is executed in a ``for`` loop.

{{{ switch to next slide, Indentation in ``python`` interpreter }}}

Now, let us find the cube of all the numbers from one to ten. But this
time let us try it in the vanilla version of Python interpreter.

Start the vanilla version of Python interpreter by issuing the command
``python`` in your terminal.

{{{ open the python interpreter in the terminal using the command
python to start the vanilla Python interpreter }}}

{{{ switch to next slide, Indentation in ``python`` interpreter
(cont'd) }}}

Start with,
::
    
    for i in range(1,11):

and press enter once, and we will see that this time it shows four
dots, but the cursor is close to the dots, so we have to indent the
block. The vanilla version of Python interpreter does not indent the
code automatically. So enter four spaces there and then type the
following
::
    
        print i, "cube is", i**3

Now when we hit enter, we still see the four dots, to get out of the
block, hit enter once again

.. #[Nishanth]: Here also the overhead on print can be reduced.
                Think of a simple print statement. This statement
                will be confusing for a newbie.
                We can focus more on indentation in python.

.. #[nishanth]: Not sure if you must use range here. You can 
                define a list of numbers and iterate on it.
                Then say this list can also be generated using
                the range function and hence introduce range.

{{{ switch to the next slide, ``range()`` function }}}

Okay! so the main thing that we learned here is how to use Python
interpreter and IPython interpreter to specify blocks. But while we
were generating the multiplication table we used something new,
``range()`` function. ``range()`` is an inbuilt function in Python
which can be used to generate a ``list`` of integers from a starting
number to an ending number. Note that the ending number that you
specify will not be included in the ``list``.

.. #[Nishanth]: Show some examples of range without the step argument
                May be give an exercise with negative numbers as arguments

{{{ switch to next slide, problem statement of the next problem in
solved exercises }}}

Now, let us print all the odd numbers from 1 to 50. Pause here and try
to solve the problem yourself.

Let us do it in our IPython interpreter for ease of use.

{{{ switch focus to ipython interpreter }}}

The problem can be solved by just using the ``range()`` function.

It can be solved as,
::

    print range(1,51,2)

This time we passed three parameters to ``range()`` function unlike
the previous case where we passed only two parameters. The first two
parameters are the same in both the cases. The first parameter is the
starting number of the sequence and the second parameter is the end of
the range. Note that the sequence doesn't include the ending
number. The third parameter is for stepping through the sequence. Here
we gave two which means we are skipping every alternate element.

{{{ switch to next slide, summary slide }}}

Thus we come to the end of this tutorial. We learned about blocks in
Python, indentation, blocks in IPython, for loop, iterating over a
list and then the ``range()`` function.

.. #[Amit]: There does seem to too much overhead of details. Should
            the first example be done using script is it necessary. 
	    Do add some things in evolutionary manner. Like introducing 
	    range as a list and doing a very very simple for loop.Like
	    iterating over [1,2,3] .Before getting into a problem.
	    And club details about problem in one paragraph and syntactic details
	    in other.

{{{ switch to next slide, thank you slide }}}

Thank you!
