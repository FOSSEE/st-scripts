.. Objectives
.. ----------

.. #. How to print some value
.. #. How to print using modifiers
.. #. How to take input from user
.. #. How to display a prompt to the user before taking the input

.. Prerequisites
.. -------------

..  none
     
.. Author              : Nishanth Amuluru
   Internal Reviewer   : Puneeth 
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <put date stamp here, not OK> [2010-10-05]

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to this tutorial on 'Input/Output'.

.. L2

{{{ Show the slide containing the objectives }}}

.. R2

At the end of this tutorial,you will be able to, 

 1. Print some value.
 #. Print using modifiers.
 #. Take input from user.
 #. Display a prompt to the user before taking the input.

.. L3

Let us first start ipython on our teminal

.. R3
::

    ipython

.. L4

Let us start this tutorial by typing a string

.. R4
::
 
    a = "This is a string"
    a
    print a
     
.. R5

``print a``, obviously, prints the value of ``a``.

As you can see, even when you type just a, the value of a is shown.
But there is a difference.

Typing just ``a`` displays the content of ``a`` whereas the 
statement ``print a`` prints the string itself.This difference becomes 
more evident when we use strings with newlines in them.

.. L5
::

    b = "A line \n New line"
    b
    print b

.. R6

As you can see, just typing ``b`` shows that b contains a newline 
character but While typing ``print b``,it prints the string and hence 
the newline.

Moreover when we type just ``a``, the value a is shown only in 
interactive mode and does not have any effect on the program while 
running it as a script.

We shall look at different ways of outputting the data.

print statement  in python supports string formatting.
Various arguments can be passed to print using modifiers.

type

.. L6
::

    x = 1.5
    y = 2
    z = "red"
    print "x is %2.1f, y is %d, z is %s"%(x,y,z)

.. R7

As you can see, the values of x, y and z are substituted in place of 
the modifiers ``%2.1f``, ``%d`` and ``%s`` respectively.

Pause the video here, try out the following exercise and resume the video.

.. L7

.. L8

{{{ Show slide with exercise 1 }}}

.. R8

 What happens when you do ``print "x is %d, y is %f" %(x, y)``

.. R9

Switch to the terminal for solution.

.. L9

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::
    
    print "x is %d, y is %f" %(x, y)

.. R10
    
We see that the ``int`` value of x and ``float`` value of y are
printed corresponding to the modifiers used in the print statement.

We have seen that ``print`` statement prints a new line character
everytime it is called. This can be suppressed
by using a "," at the end of the ``print`` statement.

Let us see this by typing out following code on an editor as 
print_example.py

.. L10

{{{ open an editor }}}
::

    print "Hello"
    print "World"

    print "Hello",
    print "World"

.. R11

Save the script as 'print_example.py' and run it using 
%run /home/fossee/print_example.py

As we can see, the print statement when used with comma in the 
end, prints a space instead of a new line.

Now we shall look at taking input from the user.
We will use the ~~raw_input~~ for this.
type

.. L11
::

    ip = raw_input()

.. R12

The cursor is blinking indicating that it is waiting for input    
type something and hit enter.

.. L12
::

    an input

.. R13

Now let us see what is the value of ip by typing it.

.. L13
::

    ip

.. R14

We can see that it contains the string "an input"

Pause the video here, try out the following exercise and resume the video.

.. L14

.. L15

{{{ Show slide with exercise 2 }}}

.. R15

 Enter the number 5.6 as input and store it in a variable called c.

.. R16

Switch to the terminal for solution.

.. L16

{{{continue from paused state}}}
{{{ Switch to the terminal }}}

.. R17

We have to use the raw_input command with variable c.
type

.. L17
::

    c = raw_input()
    5.6
    c

.. R18

Now let us see the type of c.

.. L18
::

    type(c)

.. R19

We see that c is a string. This implies that anything you enter as input,
it will be taken as a string no matter what you enter.

Pause the video here, try out the following exercise and resume the video.

.. L19

.. L20

{{{ Show slide with exercise 3 }}}

.. R20

 What happens when you do not enter anything and hit enter.

.. R21

Switch to the terminal for solution.

.. L21

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    d = raw_input()
    <RET>
    d

.. R22

We see that when nothing is entered, an empty string is considered 
as input.

raw_input also can display a prompt to assist the user.

.. L22
::

    name = raw_input("Please enter your name: ")

.. R23

It prints the string given as argument and then waits for the user input.

Let us do one more exercise.
Pause the video here, try out the following exercise and resume the video.

.. L23

.. L24

{{{ Show slide with exercise 3 }}}

.. R24

 How do you display a prompt and let the user enter input in next line.

.. R25

Switch to the terminal for solution.
The trick is to include a newline character at the end of the 
prompt string.

.. L25

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    ip = raw_input("Please enter a number in the next line\n> ")

.. R26

It prints the newline character and hence the user enters input in the 
next line

.. L26

.. L27

{{{ Show summary slide }}}

.. R27

This brings us to the end of the tutorial.
In this totorial, we have learnt to,

 1. Use the print statement.
 #. Use the modifiers %d, %f, %s in the print statement.
 #. Take input from user by using ``raw_input()``. 
 #. Display a prompt to the user before taking the input by passing 
    a string as an argument to ``raw_input``.

.. L28

{{{Show self assessment questions slide}}}

.. R28

Here are some self assessment questions for you to solve

1. ``a = raw_input()`` and user enters ``2.5``. What is the type of a?

    - str
    - int
    - float
    - char

2. ``a = 2`` and ``b = 4.5``. What does ``print "a is %d and b is %2.
    1f" %(b, a)`` print?

   - a is 2 and b is 4.5
   - a is 4 and b is 2
   - a is 4 and b is 2.0
   - a is 4.5 and b is 2

.. L29

{{{solution of self assessment questions on slide}}}

.. R29

And the answers,

1. No matter what you enter, it will be taken as a string.Hence 2.5 is 
   a string.

2. Since 'b' is called first, It will display  integer value of 'a' 
   because the modifier used is %d. Similarly, 'b' will get the float 
   value of 'a' due to it's modifier %2.1f. Hence 'a' will be 4 
   and 'b' 2.0 . 

.. L30

{{{ Show the Thankyou slide }}}

.. R30

Hope you have enjoyed this tutorial and found it useful.
Thank You!
 
