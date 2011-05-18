.. Objectives
.. ----------

.. At the end of this tutorial, you should know --

..   1. How to define strings
..   #. Different ways of defining a string
..   #. How to concatenate strings 
..   #. How to print a string repeatedly 
..   #. Accessing individual elements of the string
..   #. Immutability of strings

.. Prerequisites
.. -------------

.. 1. getting started with ipython
     
.. Author              : Madhu
   Internal Reviewer   : Punch
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <15-11-2010, Anand, OK> [2010-10-05]

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on "Getting started with
strings".

.. L2

{{{ Show slide with objectives }}}

.. R2

At the end of this tutorial, you will be able to,

   1. Define strings in differnt ways.
   #. Concatenate strings. 
   #. Print a string repeatedly. 
   #. Access individual elements of the string.
   #. Learn immutability of strings.

.. L3

{{{ Shift to terminal and start ipython }}}
::

    ipython

.. R3

Open the terminal and invoke the ipython interpreter by typing ipython

.. R4

So, what are strings? In Python anything within either single quotes
or double quotes or triple single quotes or triple double quotes are
strings. 

.. L4

{{{ Type in ipython the following and read them as you type }}}
::

    'This is a string'
    "This is a string too"
    '''This is a string as well'''
    """This is also a string"""
    'p'
    ""

.. R5

Note that it really doesn't matter how many characters are present in
the string. The last example is a null string or an empty string. 

Having more than one control character to define strings is handy when
one of the control characters itself is part of the string. For example

.. L5

::

    "Python's string manipulation functions are very useful"

.. R6

By having multiple control characters, we avoid the need for
escaping characters -- in this case the apostrophe. 

Let us now move on to the triple quoted strings. Let us define multi-line 
strings without using any escaping. Everything within the triple quotes is a 
single string no matter how many lines it extends

.. L6
::

     """Having more than one control character to define
     strings come as very handy when one of the control
     characters itself is part of the string."""

.. R7

We can assign this string to any variable

.. L7
::

    a = 'Hello, World!'

.. R8

Now 'a' is a string variable. String is a collection of characters. In
addition string is an immutable collection which means that the string cannot 
be modified after it is created.So all the operations that are applicable to any
other immutable collection in Python, works on strings as well.
Hence we can add two strings

.. L8
::

    a = 'Hello'
    b = 'World'
    c = a + ', ' + b + '!'
    print c

.. R9

We can add string variables as well as the strings themselves all in
the same statement. The addition operation performs the concatenation
of two strings.

.. L9

.. R10

Similarly we can multiply a string with an integer

.. L10
::

    a = 'Hello'
    a * 5

.. R11

It gives another string in which the original string 'Hello' is repeated
5 times.

.. L11

.. L12

{{{ Show slide with Question 1 }}}

.. R12

Pause the video here, try out the following exercise and resume the video.

 Obtain the string ``%% -------------------- %%`` (20 hyphens)
 without typing out all the twenty hyphens. 

.. L13

{{{ Switch to terminal }}}

::

    s = "%% " + "-"*20 + " %%"
    print s

.. R13

Let's now look at accessing individual elements of strings. Since,
strings are collections, we can access individual items in the string
using the subscripts

.. L14
::

    a[0]

.. R14

a[0] gives us the first character in the string. The indexing starts from 0
for the first character and goes up to (n-1) for the last character,where 'n' is
the total number of characters in a string. 
We can access the strings from the end using negative indices

.. L15
::

    a[-1]
    a[-2]

.. R15

a[-1] gives us the last element of the string and 
a[-2] gives us second element from the end of the string.

.. L16

{{{ Show slide with Question 2 }}}

.. R16

Pause the video here, try out the following exercise and resume the video.

Given a string, ``s = "Hello World"``, what is the output of::

    s[-5] 
    s[-10]
    s[-15]

.. L17

{{{ Switch to terminal }}}
::

    s[-5] 

.. R17

s[-5] gives us 'W'

.. L18
::

    s[-10] 

.. R18

s[-10] gives us 'e' and 

.. L19
::

    s[-15] 

.. R19

s[-15] gives us an ``IndexError``, as should be expected, since the string
given to us is only 11 characters long. 

.. R20

Let us attempt to change one of the characters in a string

.. L20
::

    a = 'hello'
    a[0] = 'H'

.. R21

As said earlier, strings are immutable. We cannot manipulate a
string. Although there are some methods which let us manipulate
strings, we will look at them in the advanced session on strings. In
addition to the methods that let us manipulate the strings we have
methods like split which lets us break the string on the specified
separator, the join method which lets us combine the list of strings
into a single string based on the specified separator.

.. L21

.. L22

{{{ Show summary slide }}}

.. R22

Let's revise quickly what we have learnt today.In this tutorial we have learnt to,

  1. Define strings in differnt ways.
  #. Concatenate strings by performing addition.
  #. Repeat a string 'n' number of times by doing multiplication.
  #. Access individual elements of the string by using their subscripts.
  #. Use the concept of immutability of strings.

.. L23

{{{Show self assessment questions slide}}}

.. R23

Here are some self assessment questions for you to solve

1. Write code to assign s, the string ``' is called the apostrophe``

2. Given strings s and t, ``s = "Hello"`` and ``t = "World"`` and an
   integer r, ``r = 2``. What is the output of s * r + s * t?

3. How will you change s='hello' to s='Hello'.

   - s[0]= H
   - s[0]='H'
   - strings are immutable,hence cannot be manipulated

.. L24

{{{ solution of self assessment questions on slide }}}

.. R24

And the answers,

1. The given string can be assigned in this manner
::

    s = "` is called the apostrophe"

2. The operation ``s * r + s * t`` will print each of the two words twice
   
   HelloHelloWorldWorld

3. Strings are immutable.Therefore they cannot be manipulated.

.. L25

{{{ Show the Thankyou slide }}}

.. R25

Hope you have enjoyed and found it useful.
Thank you!

