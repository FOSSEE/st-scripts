Hello friends and welcome to the tutorial on Tuples

{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline slide }}}

In this tutorial, we shall learn

 * what are tuples
 * their similarities and dissimilarities with lists
 * why are they needed

Let`s get started by defining a tuple. A tuple is defined by enclosing
parantheses around a sequence of items seperated by commas. It is similar to
defining a list except that parantheses are used instead of square brackets.
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
assignment. It only implies that tuples are immutable or in simple words,
tuples cannot be changed.

But what is the use of tuples!!!

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

We see that the values are swapped.
This idiom works for different datatypes also.
::

    a = 2.5
    b = "hello"

    a
    b

Moreover this type of behaviour is straight forward and what you would expect
should happen naturally.

This is possible because of the immutability of tuples. This process is called
tuple packing and unpacking.

Let us first see what is tuple packing. Type
::

    5,

What we see is a tuple with one element.
::

    5, "hello", 2.5

Now it is a tuple with two elements.

So when we are actually typing two or more elements seperated by commas, those
elements are packed and a tuple is made from them.

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

 1. Define a tuple containing two values. The first being integer 4 and second
    is a float 2.5

   Answer: (4, 2.5)

 2. If ``a = (5, "Hello", 3.2)``. what is the value of a[2]

   Answer: 3.2

 3. If ``a = 5,`` then what is the type of a

   a. int
   #. float
   #. tuple
   #. string

   Answer: tuple

 4. if ``a = (2, 3)``. What does ``a[0], a[1] = (3, 4)`` produce

   Answer: Error

 5. If ``a = ([2, 3], 4, 5)``. What is the value of ``a`` after doing
    ``a[0].append(6)``

    a. ([2, 3, 6], 4, 5)
    #. Raises an error
    #. ([2, 3], 4, 5)
    #. [2, 3, 4, 5, 6]

    Answer: ([2, 3, 6], 4, 5)

 6. What does the following code produce::

      a = 5
      b = "Hello"
      a, b = b, a
      print a
      print b

    Answer: Hello
            5

 7. ``a = ("hello", "world", 5, 6, 8)``. What is the value of a[1:4]

    Answer: ("world", 5, 6)

 8. ``a = (1, 2, 3, 4, 5, 6, 7, 8)``. What is the value of a[1::3]

    Answer: (2, 5, 8)


