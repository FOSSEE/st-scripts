.. Objectives
.. ----------

.. At the end of this tutorial, you will be able to 

.. 1. Create arrays using data
.. #. Create arrays from lists
.. #. Basic array operations
.. #. Creating identity matrix using ``identity()`` function.
.. #. Use functions zeros(), zeros_like(), ones(), ones_like().
.. #. Perform basic operations with arrays.

.. Prerequisites
.. -------------

..   1. should have ``ipython`` and ``pylab`` installed. 
..   #. getting started with ``ipython``.
..   #. getting started with lists.


..  Author: Anoop Jacob Thomas <anoop@fossee.in>
    Internal Reviewer   : Puneeth 
    External Reviewer   :
    Language Reviewer   : Bhanukiran
    Checklist OK?       : <11-11-2010,Anand, OK > [2010-10-05]

===========================
Getting started with Arrays
===========================

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to the spoken tutorial on 
'Getting started with arrays'.

.. L2

{{{ switch to objectives slide }}}

.. R2

At the end of this tutorial, you will be able to, 

 1. Create arrays using data.
 #. Create arrays from lists.
 #. Perform basic array operations.
 #. Create identity matrix.
 #. Use functions zeros(), zeros_like(), ones(), ones_like().

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with Lists".

.. L4

{{{ switch to next slide on overview of array }}}

.. R4

Arrays are homogeneous data structures. Unlike lists, arrays cannot have
heterogeneous data elements.They can have only one type of data 
as their entries, be them all integers, strings, or maybe floats, 
but not a mix.

Arrays of a given length are comparatively much faster in mathematical
operations than lists of the same length, because of the fact that they 
are homogeneous data structures.

Now let us see how to create arrays.

.. R5

Run your IPython interpreter with ``-pylab`` option, to load the 
required modules to work with arrays.

.. L5

{{{ open the terminal and run the following command }}}
::

    ipython -pylab

.. R6

To create an array we will use the function ``array()`` as,

.. L6
::

    a1 = array([1,2,3,4])

.. R7

Notice that we created a one dimensional array here. Also notice that 
the object we passed to create an array is a list. 

Now let us see how to create a two dimensional array. 

We create two dimensional array by converting a list of lists to an 
array as,

.. L7
::

    a2 = array([[1,2,3,4],[5,6,7,8]])

.. R8

Now let us use ``arange()`` function to create the same array as before.

.. L8
::

    ar = arange(1,9)
    print ar

.. R9

As you can see, we obtained a one dimensional array with elements from 
1 to 8.
 
Now can we make it a two dimensional array of order 2 by 4? 
Yes,we can.For this we will have to use the function ``reshape()``,

.. L9
::

    ar.reshape(2,4)
    ar.reshape(4,2)
    ar = ar.reshape(2,4)

.. R10

Hence,we got our two-dimensional array.

Now, let us see how to convert a list object to an array. We define a 
list,say l1

.. L10
::

    l1 = [1,2,3,4]

.. R11

Now to convert this list to an array,we use the array function as,

.. L11
::

    a3 = array(l1)

.. L12

{{{ switch to the next slide, shape of an array }}}

.. R12

To find the shape of an array we can use the method ``.shape``, let us
check the shape of the arrays we have created so far,

.. L13

{{{ Switch to the terminal }}}
::

    a2.shape

.. R13

``a2.shape`` object is a tuple, and it returned a tuple (2, 4).A tuple 
is nothing but an ordered list of elements.

Pause the video here, try out the following exercise and resume the video.

.. L14

{{{ switch to the next slide,exercise 1 }}}

.. R14

Find out the shape of the other arrays i.e. a1, a3, ar that we have 
created.

.. R15

Switch to the terminal for solution

.. L15

{{{ Continue from paused state }}}
{{{ Switch to the terminal }}}
::

    a1.shape
    a3.shape
    ar.shape

.. R16

Now let us try to create a new array with a mix of elements and see what
will happen,

.. L16
::

    a4 = array([1,2,3,'a string'])

.. R17

Well, we would expect an error as it has been previously mentioned that 
arrays handle elements with the same datatype, but it didn't raise an 
error. Let us check the values in the new array created. 
Type a4 in the terminal,

.. L17
::

    a4

{{{ highlight all the array elements one by one using mouse movements 
accordingly }}}

.. R18

Did you notice it, all the elements have been implicitly type casted as 
strings, though our first three elements were meant to be integers.
Also,if you have noticed,we got something like 'dtype S8' in the output.
dtype is nothing but the datatype which is the minimum type required
to hold the objects in the sequence.

.. L18

.. L19

{{{ switch to the next slide, identity & zeros methods }}}

.. R19

Let us now move on to study functions like zeros() and ones().
For this ,we will have to create a matrix.
let us see how to create an identity matrix of a given size, that is a
two-dimensional array  in  which all the diagonal elements are ones and 
rest of the elements are zeros. We can create an identity matrix using 
the function ``identity()``.

The function ``identity()`` takes an integer argument which specifies the
size of the desired matrix,

.. L20

{{{ Switch to the terminal }}}
::

    identity(3)

.. R20

As you can see the identity function returned a three by three square 
matrix with all the diagonal elements as one and the rest of the elements
as zeros.

``zeros()`` function accepts a tuple, which is the order of the array that 
we want to create, and it generates an array with all elements as zeros.

Let us create an array of the order four by five with all the elements
zero. We can do it using the method zeros(), 

.. L21
::

    zeros((4,5))

.. R21

Notice that we passed a tuple to the function zeros.
Pause the video here, try out the following exercise and resume the video.

.. L22

{{{ switch to next slide, learning exercise }}}

.. R22

Find out about the functions 
    - zeros_like()
    - ones()
    - ones_like()

< pause for some time and then continue >

.. R23

Try the following, first check the value of a1,

.. L23
::

    a1

.. R24

We see that ``a1`` is a single dimensional array, 
Let us now try a1*2

.. L24
::

    a1 * 2

.. R25

It returned a new array with all the elements multiplied by 2.
Now let us again check the contents of a1

.. L25
::

    a1

.. R26

note that the value of a1 still remains the same.

Similarly with addition,

.. L26
::

    a1 + 2
    a1

.. R27

it returns a new array, with all the elements summed with two. But
again notice that the value of a1 has not been changed.

You may change the value of a1 by simply assigning the newly returned
array as,

.. L27
::

    a1 += 2

.. R28

Notice the change in elements of a by typing 'a'

.. L28
::

    a

.. R29

We can use all the mathematical operations with arrays, Now let us try 
this

.. L29
::

   a1 = array([1,2,3,4])
   a2 = array([1,2,3,4])
   a1 + a2

.. R30

This returns an array with element by element addition

.. L30
::

    a1 * a2

.. R31

a1*a2 returns an array with element by element multiplication, notice 
that it does not perform matrix multiplication.

.. L31

.. L32

{{{ switch to summary slide }}}

.. R32

This brings us to the end of the end of this tutorial.In this tutorial, 
we have learnt to, 

 1. Create an array using the ``array()`` function.
 #. Convert a list to an array.
 #. Perform some basic operations on arrays like addition,multiplication.
 #. Use functions like 
    - .shape
    - arrange()
    - .reshape
    - zeros() & zeros_like()
    - ones() & ones_like()

.. L33

{{{Show self assessment questions slide}}}

.. R33

Here are some self assessment questions for you to solve

1. ``x = array([1, 2, 3], [5, 6, 7])`` is a valid statement

   - True
   - False


2. What does the ``ones_like()`` function do?
   
   (A) Returns an array of ones with the same shape and type as a
       given array.
   (B) Return a new array of given shape and type, filled with ones.

   Read the statements and answer,

   - Only statement A is correct.
   - Only statement B is correct.
   - Both statement A and B are correct.
   - Both statement A and B are incorrect.

.. L34

{{{solution of self assessment questions on slide}}}

.. R34

And the answers,

1. False.
   The correct way would be to assign the elements as a list of lists 
   and then convert it to an array
::

    x = array([[1, 2, 3], [5, 6, 7]])

2. The function ``ones_like()`` returns an array of ones with the same 
   shape and type as a given array.

.. L35
    
{{{ switch to thank you slide }}}

.. R35

Hope you have enjoyed this tutorial and found it useful.
Thank you!

