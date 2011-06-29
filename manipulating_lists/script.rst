.. Objectives
.. ----------

.. Clearly state the objectives of the LO (along with RBT level)

.. Prerequisites
.. -------------

..   1. getting started with lists
..   2. 
..   3. 
     
.. Author              : Madhu
   Internal Reviewer   : Punch
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <16-11-2010, Anand,  OK> [2010-10-05]

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 'Manipulating Lists'. 

.. L2

{{{ Show the slide containing objectives }}}

.. R2

At the end of this tutorial, you will be able to,

  1. Concatenate two lists
  #. Learn the details of slicing and striding of lists
  #. Sort and reverse lists.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with Lists".

.. L4

{{{ Open the terminal and start ipython }}}
::

    ipython

.. R4

let us start ipython on our terminal 

.. R5

We have already learnt about lists in Python, how to access individual
elements in the list and some of the functions that can be run on the
lists like ``max, min, sum, len`` and so on. Now let us learn some of
the basic operations that can be performed on Lists.

We already know how to access individual elements in a List. But what
if we have a scenario where we need to get a part of the entire list
or what we call as a slice of the list? Python supports slicing on
lists. Let us say I have the list,

.. L5
::

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

.. R6

To obtain all the primes between 10 and 20 from the above list of
primes we say

.. L6
::

    primes[4:8]

.. R7

This gives us all the elements in the list starting from the element
with the index 4, which is 11, upto the element with index 8
in the list but not including the eighth element. So we obtain a slice
starting from 11 upto 19th. It is very important to remember that
whenever we specify a range of elements in Python, the start index is
included and end index is not included. So in the above case, 11, which
was the element with the index 4, was included but 23 which was the
element with index 8 was excluded.

Pause the video here, try out the following exercise and resume the video.

.. L7

.. L8

{{{ Show slide with exercise 1 }}}

.. R9

 Obtain the primes less than 10, from the list ``primes``. 

.. R10

Switch to the terminal for solution

.. L10

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    primes[0:4]

.. R11

It give us the primes below 10. 

.. L11

.. L12

{{{ Show the slide containing p[start:stop] }}}

.. R12

Generalizing, we can obtain a slice of the list "p" from the index
"start" upto the index "end" but excluding "end" with the 
syntax ``p[start:stop]``

.. L13

{{{ Switch to terminal }}}

.. R13

By default the slice fetches all the elements between start and stop
including start but not stop. So as to say we obtain all the elements
between start and stop in steps of one. 

.. R14

Python also provides us the functionality to specify the steps in which 
the slice must be obtained. Say we have

.. L14
::

    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

.. R15

If we want to obtain all the odd numbers less than 10 from the list
``num`` we have to start from element with index 1 upto the index 10 in
steps of 2

.. L15
::

    num[1:10:2]

.. R16

When no step is specified, it is assumed to be 1. Similarly, there are
default values for start and stop indices as well. If we don't specify
the start index, it is implicitly taken as the first element of the
list

.. L16
::

    num[:10]

.. R17

This gives us all the elements from the beginning upto the 10th
element but not including the 10th element in the list. Similarly
if the stop index is not specified, it is implicitly assumed to be the
end of the list, including the last element of the list

.. L17
::

    num[10:]

.. R18

This gives all the elements starting from the 10th element in the list
"num" upto the final element including that last element. 


To get all the even numbers in the list "num", we do

.. L18
::

    num[::2]

.. R19

Pause the video here, try out the following exercise and resume the video.

.. L19

.. L20

{{{ Show slide with exercise 2 }}}

.. R20

 Obtain all the multiples of three from the list ``num``.

.. L21

{{{ Show slide with Solution 2 }}}

.. R21

The solution is on your screen.

 ``num[::3]`` gives us all the multiples of 3 from the list, since every 
third element in it, starting from 0, is divisible by 3. 

.. R22

The other basic operation that we can perform on lists is concatenation
of two or more lists. We can combine two lists by using the "plus"
operator. Say we have

.. L22
::

    a = [1, 2, 3, 4]
    b = [4, 5, 6, 7]
    a + b

.. R23

When we concatenate lists using the "plus" operator we get a new
list. We can store this list in a new variable,say c,

.. L23
::

    c = a + b
    c

.. R24

It is important to observe that the "plus" operator always returns a
new list without altering the lists being concatenated in any way. 

We know that a list is a collection of data. Whenever we have a
collection, we run into situations where we want to sort the
collection. Lists support ``sort`` method which sorts the list in place

.. L24
::

    a = [5, 1, 6, 7, 7, 10]
    a.sort()

.. R25

Now the contents of the list ``a`` will be

.. L25
::

    a

.. R26

As the ``sort`` method sorts the elements of a list, the original list 
we had, is overwritten or replaced. We have no way to obtain the 
original list back. One way to avoid this is to keep a copy of the 
original list in another variable and run the sort method on the list. 
However Python also provides a built-in function called sorted which 
sorts the list which is passed as an argument to it and returns a new 
sorted list

.. L26
::

    a = [5, 1, 6, 7, 7, 10]
    sorted(a)

.. R27
  
We can store this sorted list into another list variable

.. L27
::

    sa = sorted(a)

.. R28

Python also provides the ``reverse`` method which reverses
the list in place

.. L28
::

    a = [1, 2, 3, 4, 5]
    a.reverse()

.. R29

the ``reverse`` method reverses the list "a" and stores the reversed 
list in place i.e. in "a" itself. Lets see the list "a"

.. L29
::

    a

.. R30

But again the original list is lost. 

To reverse a list, we could use striding with negative indexing.

.. L30
::

    a[::-1]

.. R31

We can also store this new reversed list in another list variable.

 Pause the video here, try out the following exercise and resume the video.

.. L31

.. L32

{{{ Show slide with exercise 3 }}}

.. R32

 Given a list of marks of students in an examination, obtain a
 list with marks in descending order.
  marks = [99, 67, 47, 100, 50, 75, 62]

.. R33

Switch to terminal for solution.

.. L33

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    sorted(marks)[::-1]

.. R34

OR

.. L34
::
  
    sorted(marks, reverse = True)

.. L35

{{{ Show summary slide }}}

.. R35

This brings us to the end of this tutorial. In this tutorial,
we have learnt to,

  1. Obtain parts of lists using slicing and striding.
  #. Concatenate lists using the ``plus`` operator.
  #. Sort lists using the ``sort`` method. 
  #. Use the method ``reverse`` to reverse the lists.

.. L36

{{{Show self assessment questions slide}}}

.. R36

Here are some self assessment questions for you to solve

1. Given the list primes, ``primes = [2, 3, 5, 7, 11, 13, 17, 19, 23,
   29]``, How do you obtain the last 4 primes?


2. Given a list, p, of unknown length, obtain the first 3 (or all, if
   there are fewer) characters of it. 

  
3. ``reversed`` function reverses a list in place. True or False?

.. L37

{{{solution of self assessment questions on slide}}}

.. R37

And the answers,

1. The last four primes can be obtained from the given list as,
::

    primes[-4:]

2. The first 3 characters can be obtained as,
::

    p[:3]

3. False. The function ``reverse`` will reverse a list in place.

.. L38

{{{ Show the thank you slide }}}

.. R38

Hope you have enjoyed this tutorial and found it useful.
Thank you!
 

