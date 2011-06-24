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

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 'Conditionals'.

.. L2

{{{ Show the slide containing objectives }}}

.. R2

At the end of this tutorial, you will be able to, 

 1. Use if/else blocks. 
 #. Use if/elif/else blocks.
 #. Use the Ternary conditional statement - C if X else Y.

.. R3

To begin with let us start ipython,

.. L3

{{{ Shift to terminal and start ipython }}}
::

    ipython

.. R4

Whenever we have two possible states that can occur depending on a
a certain condition, we can use if/else construct in
Python. 

For example, say, we have a variable ``a`` which stores integers and
we are required to find out whether ``a`` is even or odd. 
Let's say the value of ``a`` is 5.

.. L4
::

    a = 5

.. R5

In such a case we can write the if/else block as

.. L5
::

    if a % 2 == 0:
        print "Even"
    else:
        print "Odd"

.. R6

If ``a`` is divisible by 2, i.e., the result of "a modulo 2" is 0, it
prints "Even", otherwise it prints "Odd". 

Note that in such a case, only one of the two blocks gets executed
depending on whether the condition is ``True`` or ``False``.

There is a very important syntactic element to understand here. Every
code block begins with a line that ends with a ``:``, in this example
the ``if`` and the ``else`` lines. Also, all the statements inside a
code block are intended by 4 spaces. Hitting enter twice,
ends the code block. 

The if/else blocks work for a condition, which can take one of two
states. But what do we do for conditions, which can take more than two
states? 

.. L6

.. R7

Python provides if/elif/else blocks, for such conditions.
For example. We have a variable ``a`` which holds integer values. We
need to print "positive" if ``a`` is positive, "negative" if
it is negative or "zero" if it is 0. 

Let us use if/elif/else ladder for it. For the purposes of testing our
code let us assume that the value of a is -3

.. L7
::

    a = -3

    if a > 0:
        print "positive"
    elif a < 0:
        print "negative"
    else:
        print "zero"

.. R8

All the syntax and rules as said for if/else statements hold the same. The only
addition here is the ``elif`` statement which can have another
condition of its own.

Here too, exactly one block of code is executed -- the block of code
which first evaluates to ``True``. Even if there is a situation where
multiple conditions evaluate to True, all the subsequent conditions
other than the first one, which evaluates to True, are neglected.
Consequently, the else block gets executed if and only if all the
conditions evaluate to False.

.. L8

.. R9

Also, the ``else`` block in both if/else statement and if/elif/else is
optional. We can have a single if statement or just if/elif statements
without having else block at all. Also, there can be any number of
elif's within an if/elif/else ladder. For example

.. L9

{{{ Show slide  ~if/elif~ ladder }}}
  
    if user == 'admin':
        # Do admin operations
    elif user == 'moderator':
        # Do moderator operations
    elif user == 'client':
        # Do customer operations

.. R10

Note that there are multiple elif blocks and there
is no else block.

Pause the video here, try out the following exercise and resume the video.

.. L10

.. L11
 
{{{ Show slide with exercise 1 }}}

.. R11

 Given a number, num. Write an if else block to print num, as is,
 if it is divisible by 10, else print 10 * num.                  

.. R12

The solution is on your screen.

.. L12

{{{ Show slide with solution 1 }}} 

    if num%10 == 0:
        print num
    else:
        print 10*num

.. R13

In addition to these conditional statements, Python provides a very
convenient ternary conditional operator. Let us take the following
example where we read the marks from a data file which is
obtained as a string as we read a file. The marks can be in the range
of 0 to 100 or 'AA' if the student is absent. In such a case, to obtain
the marks as an integer, we can use the ternary conditional
operator. Let us say the string score is stored in score_str
variable

.. L13
::

    score_str = 'AA'

.. R14

Now let us use the ternary conditional operator

.. L14
::

    score = int(score_str) if score_str != 'AA' else 0

.. R15

This is just the if/else statement block which written in a more
convenient form and is very helpful when we have only one statement
for each block. In simple terms,this conditional statement effectively means that 
score is integer of ``score_str`` if score_str is not 'AA'; otherwise it is 0.
This means that we make the scores of the students who were
absent for the exam 0.

Pause the video here, try out the following exercise and resume the video.

.. L15

{{{ Show slide with exercise 2 }}}

.. R15

 Given a number, num. Write a ternary operator to print num, as is,
 if it is divisible by 10, else print 10 * num. 

.. L16

{{{ Show slide with Solution 2 }}}

.. R16

The solution is on your screen. 

     print num if num%10 == 0 else 10*num

.. R17

Moving on, there are certain situations where we will have no
operations or statements within a block of code. For example, we have
a code where we are waiting for the keyboard input. If the user enters
"c", "d" or "x" as the input, we would perform some operation; nothing
otherwise. In such cases "pass" statement comes very handy

.. L17

.. L18

{{{ Show slide with pass statement }}}

.. R18

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

.. R19

In this case "pass" statement acts as a place holder for the block of
code. It is equivalent to a null operation. It literally does
nothing. It can used as a place holder when the actual code
implementation for a particular block of code is not known yet but has
to be filled up later.

.. L19

.. L20

{{{ Show summary slide }}}

.. R20

This brings us to the end of the tutorial.In this tutorial, we have learnt to,

  1. Understand the conditional statements in Python.
  #. Use if/else statement.
  #. Use if/elif/else statement.
  #. Apply the ternary conditional statement - C if X else Y.
  #. Use "pass" statement.

.. L21

{{{Show self assessment questions slide}}}

.. R21

Here are some self assessment questions for you to solve

1. Use conditional statements for the following.
   Given a variable ``time``, print ``Good Morning`` if it is less
   than 12, otherwise ``Hello``. 


#. Convert the if else ladder below into a ternary conditional
   statement.
::
   
    x = 20

    if x > 10:
        print x * 100
    else:
        print x

.. L22

{{{solution of self assessment questions on slide}}}

.. R22

And the answers,

1. We can use the if/else statements as
::

    if time < 12:
        print "Good Morning"
    else:
        print "Hello"

2. The if else ladder can be converted to a ternary conditional
   statement as
::

    print x * 100 if x > 10 else x

.. L23

{{{ Show the Thankyou slide }}}

.. R23

Hope you have enjoyed this tutorial and found it useful.
Thank you!
 
