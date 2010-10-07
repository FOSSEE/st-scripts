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
 
.. Author              : Nishanth
   Internal Reviewer 1 : 
   Internal Reviewer 2 : 
   External Reviewer   :

Questions
=========

 1. ``a = 2.5``. What is the output of ``print "a is %d"%(a)``

   a. a is 2.5
   #. a is 2.0
   #. 2.0
   #. a is 2

   Answer: a is 2

 2. What does ``print "This is",     "a line ", "with  spaces"`` print?

   a. This is a line with spaces
   #. This is a line with  spaces
   #. This is     a line   with   spaces
   #. This is a line  with  spaces

   Answer: This is a line  with  spaces

 3. What does ``print "%2.5f"%(1.2)`` print?

   a. 1.2
   #. 1.20
   #. 1.20000
   #. 00001.2

   Answer: 1.20000

 4. What is the output of the following code::

     for i in range(1,10,2):
         print i,

    Answer::

      1 3 5 7 9

 5. ``a = 2`` and ``b = 4.5``. What does ``print "a is %d and b is %2.1f"%(b, a)``
    print?

   a. a is 2 and b is 4.5
   #. a is 4 and b is 2
   #. a is 4 and b is 2.0
   #. a is 4.5 and b is 2

   Answer: a is 4 and b is 2.0

 6. What is the prompt displayed by ``raw_input("Say something\nType here:")``

   Answer::

     Say something 
     Type here:

 6. What is the prompt displayed by ``raw_input("value of a is %d\nInput b
    value:"a)`` and ``a = 2.5``

   Answer::

     value of a is 2
     Input ba value:

 7. ``a = raw_input()`` and user enters ``2.5``. What is the type of a?

   a. str
   #. int
   #. float
   #. char

   Answer: str

 8. ``a = int(raw_input())`` and user enters ``4.5``. What happens?

   a. a = 4.5
   #. a = 4
   #. a = 4.0
   #. Error

   Answer: Error

 9. ``a = raw_input()`` and user enters ``"this is a string"``. What does 
    ``print a`` produce?

   a. 'this is a string'
   b. 'this is a string"
   c. "this is a string"
   #. this is a string

   Answer: "this is a string"

Problems
========

 1. Answer to universe and everything. Keep taking input from user and print it
    back until the input is 42.

  Answer::

    ip = raw_input()
    while ip != "42":
        print ip

 2. 
