.. Objectives
.. ----------

.. By the end of this tutorial, you will be able to 

.. * Use if/else blocks 
.. * Use if/elif/else blocks
.. * Use the Ternary conditional statement - C if X else Y

.. to check conditions in your programs. 


.. Prerequisites
.. -------------

..   1. Basic datatypes and operators

     
.. Author              : Madhu
   Internal Reviewer   : 
   External Reviewer   :
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]


Script
------

{{{ Show the slide containing the title }}}

Hello friends. Welcome to this spoken tutorial on Conditionals

{{{ Show the slide containing the outline }}}

In this tutorial, we will learn the basic conditional constructs
available in Python. We learn the if/else, if/elif/else and ternary
conditional constructs available in Python. 

{{{ Shift to terminal and start ipython }}}

To begin with let us start ipython, by typing::

  ipython

on the terminal

Whenever we have two possible states that can occur depending on a
whether a certain condition we can use if/else construct in
Python. 

For example, say, we have a variable ``a`` which stores integers and
we are required to find out whether ``a`` is even or odd.  an even
number or an odd number. Let's say the value of ``a`` is 5, now.
::

  a = 5

In such a case we can write the if/else block as::

  if a % 2 == 0:
      print "Even"
  else:
      print "Odd"

If ``a`` is divisible by 2, i.e., the result of "a modulo 2" is 0, it
prints "Even", otherwise it prints "Odd". 

Note that in such a case, only one of the two blocks gets executed
depending on whether the condition is ``True`` or ``False``.

There is a very important sytactic element to understand here. Every
code block begins with a line that ends with a ``:``, in this example
the ``if`` and the ``else`` lines. Also, all the statements inside a
code block are intended by 4 spaces. Returning to the previous
indentation level, ends the code block. 

The if/else blocks work for a condition, which can take one of two
states. What do we do for conditions, which can take more than two
states? 

Python provides if/elif/else blocks, for such conditions. Let us take
an example. We have a variable ``a`` which holds integer values. We
need to print "positive" if ``a`` is positive, "negative" if
it is negative or "zero" if it is 0. 

Let us use if/elif/else ladder for it. For the purposes of testing our
code let us assume that the value of a is -3::

  a = -3

  if a > 0:
      print "positive"
  elif a < 0:
      print "negative"
  else:
      print "zero"

All the syntax and rules as said for if/else statements hold. The only
addition here is the ``elif`` statement which can have another
condition of its own.

Here too, exactly one block of code is executed -- the block of code
which first evaluates to ``True``. Even if there is a situation where
multiple conditions evaluate to True all the subsequent conditions
other than the first one which evaluates to True are neglected.
Consequently, the else block gets executed if and only if all the
conditions evaluate to False.

Also, the ``else`` block in both if/else statement and if/elif/else is
optional. We can have a single if statement or just if/elif statements
without having else block at all. Also, there can be any number of
elif's within an if/elif/else ladder. For example

{{{ Show slide for this }}}

  if user == 'admin':
      # Do admin operations
  elif user == 'moderator':
      # Do moderator operations
  elif user == 'client':
      # Do customer operations

{{{ end of slide switch to ipython }}}

is completely valid. Note that there are multiple elif blocks and there
is no else block.

Following is an exercise that you must do. 

%% %% Given a number, num. Write an if else block to print num, as is,
      if it is divisible by 10, else print 10 * num.                  

Please, pause the video here. Do the exercise and then continue. 

:: 

  if num%10 == 0:
      print num
  else:
      print 10*num


In addition to these conditional statements, Python provides a very
convenient ternary conditional operator. Let us take the following
example where we read the marks data from a data file which is
obtained as a string as we read a file. The marks can be in the range
of 0 to 100 or 'AA' if the student is absent. In such a case to obtain
the marks as an integer we can use the ternary conditional
operator. Let us say the string score is stored in score_str
variable::

  score_str = 'AA'

Now let us use the ternary conditional operator::

  score = int(score_str) if score_str != 'AA' else 0

This is just the if/else statement block which written in a more
convenient form and is very helpful when we have only one statement
for each block. This conditional statement effectively means as we
would have exactly specified in the English language which will be
like score is integer of score_str is score_str is not 'AA' otherwise
it is 0. This means that we make the scores of the students who were
absent for the exam 0.

Following is an exercise that you must do. 

%% %% Given a number, num. Write a ternary operator to print num, as is,
      if it is divisible by 10, else print 10 * num. 

Please, pause the video here. Do the exercise and then continue. 

:: 

   print num if num%10 == 0 else 10*num

Moving on, there are certain situations where we will have no
operations or statements within a block of code. For example, we have
a code where we are waiting for the keyboard input. If the user enters
"c", "d" or "x" as the input we would perform some operation nothing
otherwise. In such cases "pass" statement comes very handy::

  a = raw_input("Enter 'c' to calculate and exit, 'd' to display the existing
  results exit and 'x' to exit and any other key to continue: ")

  if a == 'c':
     # Calculate the marks and exit
  elif a == 'd':
     # Display the results and exit
  elif a == 'x':
     # Exit the program
  else:
     pass

In this case "pass" statement acts as a place holder for the block of
code. It is equivalent to a null operation. It literally does
nothing. It can used as a place holder when the actual code
implementation for a particular block of code is not known yet but has
to be filled up later.

{{{ Show summary slide }}}

This brings us to the end of the tutorial session on conditional
statements in Python. In this tutorial session we learnt

  * What are conditional statements
  * if/else statement
  * if/elif/else statement
  * Ternary conditional statement - C if X else Y
  * and the "pass" statement

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!
 
