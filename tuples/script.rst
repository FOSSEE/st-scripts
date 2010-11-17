.. Objectives
.. ----------

.. At the end of the tutorial, you will
.. #. have a clear understand of what tuples are
.. #. be able to compare them with lists
.. #. know why they are needed and where to use them 


.. Prerequisites
.. -------------

..   1. Getting started with lists
     
.. Author              : Nishanth Amuluru
   Internal Reviewer   : Punch
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <put date stamp here, not OK> [2010-10-05]

Script
------

Hello friends and welcome to the tutorial on getting started with
tuples. 

{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline slide }}}

In this tutorial, we shall learn

 * what are tuples
 * their similarities and dissimilarities with lists
 * why are they needed

Let's get started by defining a tuple. A tuple is defined by enclosing
parentheses around a sequence of items seperated by commas. It is
similar to defining a list except that parentheses are used instead of
square brackets.  
::

    t = (1, 2.5, "hello", -4, "world", 1.24, 5)
    t

defines a tuple. The items in the tuple are indexed using numbers and can be 
accessed by using their position.
::

    t[3]

prints -4 which is the fourth item of the tuple.

::

    t[1:5:2]

prints the corresponding slice

This is the behaviour similar as to lists. But the difference can be seen when
we try to change an element in the tuple.
::

    t[2] = "Hello"

We can see that, it raises an error saying tuple does not support item
assignment. Tuples are immutable, and cannot be changed after
creation. 

Then, what's the use of tuples?

We shall understand that soon. But let us look at a simple problem of swapping
values.

{{{ Pause here and try out the following exercises }}}

%% 1 %% a = 5 and b = 7. swap the values of a and b

{{{ continue from paused state }}}
::

    a = 5
    b = 7

    a
    b

We define the two values
::

    temp = a
    a = b
    b = temp

    a
    b

This is the traditional approach

Now let us do it the python way
::

    a
    b

    a, b = b, a

    a
    b

We see that the values are swapped.  This idiom works for different
data-types also.  

::

    a = 2.5
    b = "hello"

    a
    b

Moreover this type of behaviour is something that feels natural and
you'd expect to happen. 

This is possible because of the immutability of tuples. This process is called
tuple packing and unpacking.

Let us first see what is tuple packing. Type
::

    5,

What we see is a tuple with one element.
::

    5, "hello", 2.5

Now it is a tuple with three elements.

So when we are actually typing two or more elements seperated by commas, those
elements are packed into a tuple. 

When you type
::

    a, b = b, a

First the values of b and a are packed into a tuple on the right side and then
unpacked into the variables a and b.

Immutability of tuples ensures that the values are not changed during the
packing and unpacking.

{{{ Show summary slide }}}

This brings us to the end of the tutorial.
we have learnt

 * How to define tuples
 * The similarities of tuples with lists, like indexing and iterability
 * The immutability of tuples
 * The value swapping idiom in Python
 * packing and unpacking of tuples

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you

