.. Objectives
.. ----------

.. A - Students and teachers from Science and engineering backgrounds
   B - 
   C - 
   D - 

.. Prerequisites
.. -------------

..   1. Loops
     
.. Author              : Nishanth Amuluru
   Internal Reviewer   : 
   External Reviewer   :
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]

Script
------

Hello friends and welcome to the tutorial on Input/Output

{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline slide }}}

Input and Output are used in almost every program we use.
In this tutorial, we shall learn

 * Outputting data
 * Taking input from the user

type
::
 
    a = "This is a string"
    a
    print a
     
print a prints the value of a which is obvious.
As you can see, even when you type just a, the value of a is shown.
But there is a difference.

Typing a shows the value of a while print a prints the string. This difference
becomes more evident when we use strings with newlines in them.
type
::

    b = "A line \n New line"
    b
    print b

As you can see, just typing b shows that b contains a newline character.
While typing print b prints the string and hence the newline.

Moreover when we type just a, the value a is shown only in interactive mode and
does not have any effect on the program while running it as a script.

We shall look at different ways of outputting the data.

print statement also accepts the syntax of C's printf statement.
Various arguments can be passed to print using modifiers.
type
::

    x = 1.5
    y = 2
    z = "zed"
    print "x is %2.1f y is %d z is %s"%(x,y)

As you can see, the values of x and y are substituted in place of %2.1f and %d

{{{ Pause here and try out the following exercises }}}

%% 1 %% What happens when you do print "x is %d y is %f"%(x)

{{{ continue from paused state }}}

We see that the int value of x and float value of y are printed corresponding
to the modifiers used in the print statement.

We can also see that print statement prints a new line character at the end of
line, everytime it is called. This can be suppressed by using a "," at the end
print statement.

Let us see this by typing out following code on an editor as print_example.py

{{{ open an editor }}}
type
::

    print "Hello"
    print "World"

    print "Hello",
    print "World"

Now we run the script using %run /home/fossee/print_example.py

As we can see, the print statement when used with comma in the end, prints a
space instead of a new line.

Now we shall look at taking input from the user.
We will use the ~~raw_input~~ for this.
type
::

    ip = raw_input()

The cursor is blinking indicating that it is waiting for input    
type
::

    an input

and hit enter.
Now let us see what is the value of ip by typing.
::

    ip

We can see that it contains the string "an input"

{{{ Pause here and try out the following exercises }}}

%% 2 %% enter the number 5.6 as input and store it in a variable called c.

{{{ continue from paused state }}}

We have to use the raw_input command with variable c.
type
::

    c = raw_input()
    5.6
    c

Now let us see the type of c.

::

    type(c)

We see that c is a string. This implies that anything you enter as input, will
be taken as a string no matter what you enter.

{{{ Pause here and try out the following exercises }}}

%% 3 %% What happens when you do not enter anything and hit enter

{{{ continue from paused state }}}

::

    d = raw_input()
    <RET>
    d

We see that when nothing is entered, an empty string is considered as input.

raw_input also can display a prompt to assist the user.
::

    name = raw_input("Please enter your name: ")

prints the string given as argument and then waits for the user input.

{{{ Pause here and try out the following exercises }}}

%% 4 %% How do you display a prompt and let the user enter input in a new line

{{{ continue from paused state }}}

The trick is to include a newline character at the end of the prompt string.
::

    ip = raw_input("Please enter a number in the next line\n> ")

prints the newline character and hence the user enters input in the new line

{{{ Show summary slide }}}

This brings us to the end of the tutorial.
we have learnt

 * How to print some value
 * How to print using modifiers
 * How to take input from user
 * How to display a prompt to the user before taking the input

{{{ Show the "sponsored by FOSSEE" slide }}}

#[Nishanth]: Will add this line after all of us fix on one.
This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thankyou
 
