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

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to the tutorial on "getting started with
tuples". 

.. L2

{{{ Show the slide containing the objectives }}}

.. R2

At the end of the tutorial, you will be able to,

 1. Understand of what tuples are.
 #. Compare them with lists.
 #. Know why they are needed and where to use them.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with lists".

.. R4

Let us start our ipython interpreter.

.. L4

{{{ Open the terminal }}}
::

    ipython

.. R5

Let's get started by defining a tuple. A tuple is defined by enclosing
parentheses around a sequence of items seperated by commas. It is
similar to defining a list except that parentheses are used instead of
square brackets.  

.. L5
::

    t = (1, 2.5, "hello", -4, "world", 1.24, 5)
    t

.. R6

The items in the tuple are indexed using numbers and can be 
accessed by using their position.For example,

.. L6
::

    t[3]

.. R7

It prints -4 which is the fourth item of the tuple
Similarly,

.. L7
::

    t[1:5:2]

.. R8

It prints the corresponding slice

This behaviour is similar to that of lists. But the difference can be 
seen when we try to change an element in the tuple.

.. L8
::

    t[2] = "Hello"

.. R9

We can see that, it raises an error saying 'tuple object does not support 
item assignment'. Tuples are immutable, and hence cannot be changed after
creation. 

Then, what is the use of tuples?
We shall understand that soon. But let us look at a simple problem of 
swapping values.

Pause the video here, try out the following exercise and resume the video.

.. L9

.. L10

{{{ Show slide with exercise 1 }}}

.. R10

 Given, a = 5 and b = 7. Swap the values of a and b.

.. R11

Switch to terminal fo solution

.. L11

{{{ continue from paused state }}}
{{{ Switch to the terminal }}}
::

    a = 5
    b = 7

    a
    b

.. R12

We now create a variable say, temp and swap the values using this variable

.. L12
::

    temp = a
    a = b
    b = temp

    a
    b

.. R13

This is the traditional approach
Now let us do it the python way

.. L13
::

    a
    b

    a, b = b, a

    a
    b

.. R14

We see that the values are swapped.  This idiom works for different
data-types also.  

.. L14
::

    a = 2.5
    b = "hello"
    a, b = b, a
    a
    b

.. R15

Moreover this type of behaviour is something that feels natural and
you'd expect to happen. 

This is possible because of the immutability of tuples. This process is 
called tuple packing and unpacking.

Let us first see what is tuple packing. Type

.. L15
::

    5,

.. R16

What we see is a tuple with one element.

.. L16
::

    5, "hello", 2.5

.. R17

Now it is a tuple with three elements.

So when we are actually typing two or more elements seperated by commas, 
those elements are packed into a tuple. 

When you type

    a, b = b, a

First the values of b and a are packed into a tuple on the right side 
and then unpacked into the variables a and b.

Immutability of tuples ensures that the values are not changed during the
packing and unpacking.

.. L17

.. L18

{{{ Show summary slide }}}

.. R18

This brings us to the end of this tutorial.In this tutorial,
we have learnt to,

 1. Define tuples.
 #. Understand the similarities of tuples with lists, like indexing and 
    iterability.
 #. Know about the immutability of tuples.
 #. Swap values, the python way.
 #. Understand the concept of packing and unpacking of tuples.

.. L19

{{{Show self assessment questions slide}}}

.. R19

Here are some self assessment questions for you to solve

1. Define a tuple containing two values. The first being integer 4 and 
   second is a float 2.5

2. If ``a = 5,`` then what is the type of a ?

   - int
   - float
   - tuple
   - string

3. if ``a = (2, 3)``. What does ``a[0], a[1] = (3, 4)`` produce

.. L20

{{{solution of self assessment questions on slide}}}

.. R20

And the answers,

1. A tuple is defined by enclosing parentheses around a sequence of 
   items seperated by commas.Hence, we write our tuple as,
::

    (4, 2.5)

2. Since the given data is 5 followed by a comma, it means that it is 
   a tuple

3. The operation a[0], a[1] = (3, 4) will result in an error because 
   tuples are immutable.

.. L21

{{{ Show the thankyou slide }}}

.. R21

Hope you have enjoyed this tutorial and found it useful.
Thank you!

