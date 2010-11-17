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

{{{ Show the slide containing the title }}}

Hello friends. Welcome to this spoken tutorial on Getting started with
strings.

{{{ Show the slide containing the outline }}}

In this tutorial, we will look at what we really mean by strings, how
Python supports the use of strings and some of the operations that can
be performed on strings. 

{{{ Shift to terminal and start ipython }}}

To begin with let us start ipython, by typing::

  ipython

on the terminal

So, what are strings? In Python anything within either single quotes
or double quotes or triple single quotes or triple double quotes are
strings. 

{{{ Type in ipython the following and read them as you type }}}::

  'This is a string'
  "This is a string too'
  '''This is a string as well'''
  """This is also a string"""
  'p'
  ""

Note that it really doesn't matter how many characters are present in
the string. The last example is a null string or an empty string. 

Having more than one control character to define strings is handy when
one of the control characters itself is part of the string. For
example::

  "Python's string manipulation functions are very useful"

By having multiple control characters, we avoid the need for
escaping characters -- in this case the apostrophe. 

The triple quoted strings let us define multi-line strings without
using any escaping. Everything within the triple quotes is a single
string no matter how many lines it extends::

   """Having more than one control character to define
   strings come as very handy when one of the control
   characters itself is part of the string."""

We can assign this string to any variable::

  a = 'Hello, World!'

Now 'a' is a string variable. String is a collection of characters. In
addition string is an immutable collection. So all the operations that
are applicable to any other immutable collection in Python works on
string as well. So we can add two strings::

  a = 'Hello'
  b = 'World'
  c = a + ', ' + b + '!'

We can add string variables as well as the strings themselves all in
the same statement. The addition operation performs the concatenation
of two strings.

Similarly we can multiply a string with an integer::

  a = 'Hello'
  a * 5

gives another string in which the original string 'Hello' is repeated
5 times.

Following is an exercise that you must do. 

%% %% Obtain the string ``%% -------------------- %%`` (20 hyphens)
      without typing out all the twenty hyphens. 

Please, pause the video here. Do the exercise and then continue. 

::

  s = "%% " + "-"*20 + " %%"

Let's now look at accessing individual elements of strings. Since,
strings are collections we can access individual items in the string
using the subscripts::

  a[0]

gives us the first character in the string. The indexing starts from 0
for the first character and goes up to n-1 for the last character. We
can access the strings from the end using negative indices::

  a[-1]

gives us the last element of the string and 
::

    a[-2]

gives us second element from the end of the string

Following is an exercise that you must do. 

%% %% Given a string, ``s = "Hello World"``, what is the output of::

      s[-5] 
      s[-10]
      s[-15]

Please, pause the video here. Do the exercise and then continue. 

::

  s[-5] 

gives us 'W'
::

  s[-10] 

gives us 'e' and 
::

  s[-15] 

gives us an ``IndexError``, as should be expected, since the string
given to us is only 11 characters long. 

Let us attempt to change one of the characters in a string::

  a = 'hello'
  a[0] = 'H'

As said earlier, strings are immutable. We cannot manipulate a
string. Although there are some methods which let us manipulate
strings, we will look at them in the advanced session on strings. In
addition to the methods that let us manipulate the strings we have
methods like split which lets us break the string on the specified
separator, the join method which lets us combine the list of strings
into a single string based on the specified separator.

{{{ Show summary slide }}}

This brings us to the end of another session. In this tutorial session
we learnt

  * How to define strings
  * Different ways of defining a string
  * String concatenation and repetition
  * Accessing individual elements of the string
  * Immutability of strings

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!

