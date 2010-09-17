.. 3.2 LO: getting started with =for= (2) [anoop] 
.. -----------------------------------------------
.. * blocks in python 
..   + (indentation) 
.. * blocks in ipython 
..   + ... prompt 
..   + hitting enter 
.. * =for= with a list 
.. * =range= function 

=============================
Getting started with for loop
=============================

{{{ show welcome slide }}}

Hello and welcome to the tutorial getting started with ``for`` loop. 

{{{ switch to next slide, outline slide }}}

In this tutorial we will see ``for`` loops in python, and also cover
the basics of indenting code in python.

{{{ switch to next slide, about whitespaces }}}

In Python whitespace is significant, and the blocks are visually
separated rather than using braces or any other mechanisms for
defining blocks. And by this method Python forces the programmers to
stick on to one way of writing or beautifying the code rather than
debating over where to place the braces. This way it produces uniform
code than obscure or unreadable code.

A block may be defined by a suitable indentation level which can be
either be a tab or few spaces. And the best practice is to indent the
code using four spaces.

Now let us move straight into ``for`` loop.

{{{ switch to next slide,  problem statement of exercise 1 }}}

Write a for loop which iterates through a list of numbers and find the
square root of each number. Also make a new list with the square roots
and print it at the end.
::

    numbers are 1369, 7225, 3364, 7056, 5625, 729, 7056, 576, 2916

For the problem, first we need to create a ``list`` of numbers and
then iterate over the list and find the square root of each element in
it. And let us create a script, rather than typing it out in the
interpreter itself. Create a script called list_roots.py and type the
following.

{{{ open the text editor and paste the following code there }}}
::

    numbers = [1369, 7225, 3364, 7056, 5625, 729, 7056, 576, 2916]
    square_roots = []
    for each in numbers:
        sq_root = sqrt(each)
        print "Square root of", each, "is", sq_root
        square_roots.append(sq_root)
    print 
    print square_roots

{{{ save the script }}}

Now save the script, and run it from your IPython interpreter. I
assume that you have started your IPython interpreter using ``-pylab``
option.

Run the script as,
::

    %run -i list_roots.py

{{{ run the script }}}

So that was easy! We didn't have to find the length of the string nor
address of each element of the list one by one. All what we did was
iterate over the list element by element and then use the element for
calculation. Note that here we used three variables. One the variable
``numbers``, which is a list, another one ``each``, which is the
element of list under consideration in each cycle of the ``for`` loop,
and then a variable ``sq_root`` for storing the square root in each
cycle of the ``for`` loop. The variable names can be chosen by you.

{{{ show the script which was created }}}

Note that three lines after ``for`` statement, are indented using four
spaces.

{{{ highlight the threee lines after for statement }}}

It means that those three lines are part of the for loop. And it is
called a block of statements. And the seventh line or the immediate
line after the third line in the ``for`` loop is not indented, 

{{{ highlight the seventh line - the line just after for loop }}}

it means that it is not part of the ``for`` loop and the lines after
that doesn't fall in the scope of the ``for`` loop. Thus each block is
separated by the indentation level. Thus marking the importance of
white-spaces in Python.

{{{ switch to the slide which shows the problem statement of the first
problem to be tried out }}}

Now a question for you to try, from the given numbers make a list of
perfect squares and a list of those which are not. The numbers are,
::
    
    7225, 3268, 3364, 2966, 7056, 5625, 729, 5547, 7056, 576, 2916

{{{ switch to next slide, problem statement of second problem in
solved exercie}}}

Now let us try a simple one, to print the square root of numbers in
the list. And this time let us do it right in the IPython
interpreter. 

{{{ switch focus to the IPython interpreter }}}

So let us start with making a list. Type the following
::

    numbers = [1369, 7225, 3364, 7056, 5625, 729, 7056, 576, 2916]
    for each in numbers:

and now you will notice that, as soon as you press the return key
after for statement, the prompt changes to four dots and the cursor is
not right after the four dots but there are four spaces from the
dots. The four dots tell you that you are inside a block. Now type the
rest of the ``for`` loop,
::

        sq_root = sqrt(each)
        print "Square root of", each, "is", sq_root

Now we have finished the statements in the block, and still the
interpreter is showing four dots, which means you are still inside the
block. To exit from the block press return key or the enter key twice
without entering anything else. It printed the square root of each
number in the list, and that is executed in a ``for`` loop.

Now, let us generate the multiplication table of 10 from one to
ten. But this time let us try it in the vanilla version of Python
interpreter.

Start the vanilla version of Python interpreter by issuing the command
``python`` in your terminal.

{{{ open the python interpreter in the terminal using the command
python to start the vanilla Python interpreter }}}

Start with,
::
    
    for i in range(1,11):

and press enter once, and we will see that this time it shows four
dots, but the cursor is close to the dots, so we have to intend the
block. So enter four spaces there and then type the following
::
    
    
        print "10 *",i,"=",i*10

Now when we hit enter, we still see the four dots, to get out of the
block type enter once.

Okay! so the main thing here we learned is how to use Python
interpreter and IPython interpreter to specify blocks. But while we
were generating the multiplication table we used something new,
``range()`` function. ``range()`` is an inbuilt function in Python
which can be used to generate a ``list`` of integers from a starting
range to an ending range. Note that the ending number that you specify
will not be included in the ``list``.

Now, let us print all the odd numbers from 1 to 50. Let us do it in
our IPython interpreter for ease of use.

{{{ switch focus to ipython interpreter }}}

{{{ switch to next slide, problem statement of the next problem in
solved exercises }}}

Print the list of odd numbers from 1 to 50. It will be better if
you can try it out yourself.

It is a very trivial problem and can be solved as,
::

    print range(1,51,2)

This time we passed three parameters to ``range()`` function unlike
the previous case where we passed only two parameters. The first two
parameters are the same in both the cases. The first parameter is the
starting number of the sequence and the second parameter is the end of
the range. Note that the sequence doesn't include the ending
number. The third parameter is for stepping through the sequence. Here
we gave two which means we are skipping every alternate element.

{{{ switch to next slide, recap slide }}}

Thus we come to the end of this tutorial. We learned about blocks in
Python, indentation, blocks in IPython, for loop, iterating over a
list and then the ``range()`` function.

{{{ switch to next slide, thank you slide }}}

Thank you!

..  Author: Anoop Jacob Thomas <anoop@fossee.in>
    Reviewer 1:
    Reviewer 2:
    External reviewer:
