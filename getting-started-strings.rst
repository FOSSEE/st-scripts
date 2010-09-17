3.3 LO: getting started with strings (2) [madhu] 
-------------------------------------------------
* strings 
  + single, double, triple quoted 
* accessing elements 
* show immutability 
* tell that there are methods for manipulation 


Hello friends. Welcome to this spoken tutorial on Getting started with
strings.

{{{ Show the slide containing the title }}}

{{{ Show the slide containing the outline }}}

In this tutorial, we will learn what do we actually mean by strings in
python, how python supports the use of strings. We will also learn
some of the operations that can be performed on strings.

{{{ Shift to terminal and start ipython }}}

To begin with let us start ipython, by typing::

  ipython

on the terminal

So what are strings? In Python anything within either single quotes
or double quotes or triple single quotes or triple double quotes are
strings. This is true whatsoever, even if there is only one character
within the quotes

{{{ Type in ipython the following and read them as you type }}}::

  'This is a string'
  "This is a string too'
  '''This is a string as well'''
  """This is also a string"""
  'p'

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






{{{ Show summary slide }}}

This brings us to the end of another session. In this tutorial session
we learnt

  *


{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thankyou
 
.. Author              : Madhu
   Internal Reviewer 1 :         [potential reviewer: Nishanth]
   Internal Reviewer 2 :         [potential reviewer: Amit]
   External Reviewer   :

