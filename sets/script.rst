.. Objectives
.. ----------

.. By the end of this tutorial, you will be able to 

.. * Create sets from lists
.. * Perform union, intersection and symmetric difference operations
.. * Check if a set is a subset of other
.. * understand various similarities with lists like length and containership


.. Prerequisites
.. -------------

..   1. Getting started with lists
     
.. Author              : Nishanth Amuluru
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

Hello friends and welcome to the tutorial on 'Sets'.

.. L2

{{{ Show the slide containing objectives }}}

.. R2

At the end of this tutorial, you will be able to, 

 1. Create sets from lists.
 #. Perform union, intersection and symmetric difference operations.
 #. Check if a set is a subset of other.
 #. Understand various similarities with lists like length and 
    containership.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with Lists"

.. R5

Now, What are sets?
Sets are data structures which contain unique elements. In other words,
duplicates are not allowed in sets.

First let us invoke our ipython interpreter

.. L5
::

    ipython

.. R6

Lets look at how to input sets.
type

.. L6
::
 
    a_list = [1, 2, 1, 4, 5, 6, 2]
    a = set(a_list)
    a
     
.. R7

We can see that duplicates are removed and the set contains only unique
elements. Now let us perform some operations on sets. 
For this, we shall first create a pair of sets

.. L7
::

    f10 = set([1, 2, 3, 5, 8])
    p10 = set([2, 3, 5, 7])

.. R8

f10 is the set of fibonacci numbers from 1 to 10.
p10 is the set of prime numbers from 1 to 10.

Various operations can be performed on sets.For example,
The | (pipe) character stands for union

.. L8
::

    f10 | p10

.. R9

It gave the union of f10 and p10

The '&' character stands for intersection.

.. L9
::

    f10 & p10

.. R10

It gave the intersection of f10 and p10

similarly,f10 - p10 gives all the elements that are 
in f10 but not in p10

.. L10
::

    f10 - p10

.. R11

and f10 ^ p10 gives all the elements in f10 union p10 but not 
in f10 intersection p10.

.. L11
::

    f10 ^ p10

.. R12

In mathematical terms, it gives the symmetric difference.

Sets also support checking of subsets.

.. L12
::

    b = set([1, 2])
    b < f10

.. R13

It gives a ``True`` since b is a proper subset of f10.
Similarly,

.. L13
::

    f10 < f10

.. R14

It gives a ``False`` since f10 is not a proper subset.
hence the right way to do would be

.. L14
::

    f10 <= f10

.. R15

 we get a ``True`` since every set is a subset of itself.

Sets can be iterated upon just like lists and tuples. 

.. L15
::

    for i in f10:
        print i,

.. R16

It prints the elements of f10.

The length and containership check on sets is similar as in lists and 
tuples.

.. L16
::

    len(f10)

.. R17

It shows 5. And

.. L17 
::
    
    1 in f10
    2 in f10

.. R18

prints ``True`` and ``False`` respectively

The order in which elements are organized in a set is not to be relied 
upon, since sets do not support indexing. Hence, slicing and striding 
are not valid on sets.

Pause the video here, try out the following exercise and resume the video.

.. L18

.. L19

{{{ Show slide with exercise 1 }}}

.. R19

 Given a list of marks, marks = [20, 23, 22, 23, 20, 21, 23] 
 list all the duplicates

.. L20

{{{ continue from paused state }}}
{{{ Switch to the terminal }}}

.. R20

Duplicates marks are the marks left out when we remove each element of 
the list exactly one time.

.. L21

::

    marks = [20, 23, 22, 23, 20, 21, 23] 
    marks_set = set(marks)
    for mark in marks_set:
        marks.remove(mark)

.. R21

.. R22

 We are now left with only duplicates in the list ``marks``
Hence,

.. L22
::

    duplicates = set(marks)
    duplicates

.. R23

We obtained our required solution

.. L23

.. L24

{{{ Show summary slide }}}

.. R24

This brings us to the end of the tutorial.In this tutorial,
we have learnt to,

 1. Make sets from lists.
 #. Perform union, intersection and symmetric difference operations.
    by using the operators `|`, `&` and `^` respectively.
 #. Check if a set is a subset of other using the `<` and `<=` operators.
 #. Understand various similarities with lists like length and 
    containership.

.. L25

{{{Show self assessment questions slide}}}

.. R25

Here are some self assessment questions for you to solve

1. If ``a = [1, 1, 2, 3, 3, 5, 5, 8]``. What is set(a)

   - set([1, 1, 2, 3, 3, 5, 5, 8])
   - set([1, 2, 3, 5, 8])
   - set([1, 2, 3, 3, 5, 5])
   - Error

2. ``odd = set([1, 3, 5, 7, 9])`` and ``squares = set([1, 4, 9, 16])``. 
    How do you find the symmetric difference of these two sets?


3. ``a`` is a set. how do you check if a variable ``b`` exists in ``a``?

.. L26

{{{solution of self assessment questions on slide}}}

.. R26

And the answers,

1. set(a) will have all the common elements in the list ``a``, that is
   ``set([1, 2, 3, 5, 8])``.

2. To find the symmetric difference between two sets, we use 
   the operator `^`.
::

    odd ^ squares

3. To check the containership, we say,
::

    b in a

.. L27

{{{ Show the Thank you slide }}}

.. R27

Hope you have enjoyed this tutorial and found it useful.
Thank you!

