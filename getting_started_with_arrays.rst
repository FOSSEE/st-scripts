.. 4.1 LO: getting started with arrays (2) [anoop] 
.. ------------------------------------------------
.. * why arrays 
..   + speed - simply say 
..   + array level operations 
.. * creating arrays 
..   + direct data 
..   + list conversion 
..   + homogeneous 
..   + builtins - identitiy, zeros, 
.. * array operations 
..   + =+ - * /= 

===========================
Getting started with Arrays
===========================

{{{ show the welcome slide }}}

Welcome to the spoken tutorial on getting started with arrays.

{{{ switch to next slide, outline slide }}}

In this tutorial, we will learn about arrays, how to convert a list
into an array and also why an array is preferred over lists. And array
operations.

{{{ switch to next slide on overview of array }}}

Arrays are homogeneous data structures, unlike lists, arrays cannot
have heterogeneous data elements, that is, it can have only one type
of data type, either all integers, or strings, or float, and not a
mix.

Arrays are really fast in mathematical operations when compared to
lists, it is at least 80 to 100 times faster than lists.

{{{ switch to the next slide, creating arrays }}}

I am assuming that you have your IPython interpreter running with the
``-pylab`` option, so that you have the required modules loaded.

To create an array we will use the function ``array()`` as,
::

    a1 = array([1,2,3,4])

Notice that here we created a one dimensional array. Also notice the
object we passed to create an array. Now let us see how to create a
two dimensional array.
::

    a2 = array([[1,2,3,4],[5,6,7,8]])

Now, let us see how to convert a list object to an array. As you have
already seen, in both of the previous statements we have passed a
list, so creating an array can be done so, first let us create a list
``l1``
::

    l1 = [1,2,3,4]

Now we can convert the list to an array as,
::

    a3 = array(l1)


{{{ switch to the next slide, problem statement of unsolved exercise 1 }}}

Create a three dimensional array of the order (2,2,4).

{{{ switch to the next slide, shape of an array }}}

To find the shape of an array we can use the object ``.shape``, let us
check the shape of the arrays we have created so far,
::

    a1.shape

``a1.shape`` object is a tuple, and since a1 is a single dimensional
array, it returned a tuple (4,).

{{{ switch to the next slide, unsolved exercise 2 }}}

Find out the shape of the other two arrays that we have created.

{{{ Array can have only a single type of data }}}

Now let us try to create a new array with a mix of elements and see
what will happen,
::

    a4 = array([1,2,3,'a string'])

Well, we expected an error as previously I said that an array can have
only homogeneous elements, but it didn't give an error. Let us check
the values in the new array created. In your IPython terminal type,
::

    a4

Did you notice it, 

{{{ highlight all the array elements one by one using mouse 
movements }}}

all the elements have been implicitly type casted as string, though
our first three elements were integers.

{{{ switch to the next slide, identity & zeros methods }}}

An identity matrix is a square matrix in which all the diagonal
elements are one and rest of the elements zero. We can create an
identity matrix using the method ``identity()``.

The function ``identity()`` takes an integer argument,
::

    identity(3)

As you can see the identity method returned a three by three square
array with all the diagonal elements as one and the rest of the
elements as zero.

``zeros()`` function accepts a tuple, which is the order of the array
we want to create, and it generates an array with all elements zero.

{{{ switch to the next slide, problem statement of the solved exercise
1 }}}

Let us creates an array of the order four by five with all the
elements zero. We can do it using the method zeros,
::

    zeros((4,5))

Notice that we passed a tuple to the function zeros.

{{{ switch to next slide, learning exercise }}}

We learned two functions ``identity()`` and ``zeros()``, find out more
about the functions ``zeros_like()``, ``ones()``, ``ones_like()``.

{{{ switch to next slide, array operations }}}

Try the following, first check the value of a1,
::

    a1

``a1`` is a single dimensional array, and now try,
::

    a1 * 2

It returned a new array with all the elements multiplied by 2.
::

    a1

note that the value of a1 still remains the same.

Similarly with addition,
::

    a1 + 2

it returns a new array, with all the elements summed with two. But
again notice that the value of a1 has not been changed.
::

    a1

You may change the value of a1 by simply assigning the newly returned
array as,
::

    a1 += 2

Notice the change in elements of a,
::

    a

We can use all the mathematical operations with arrays, Now let us try
this
::

   a1 = array([1,2,3,4])
   a2 = array([1,2,3,4])
   a1 + a2

Returns an array with element by element addition,
::

    a1 * a2

Returns an array with element by element multiplication, notice that
it does not perform matrix multiplication.

{{{ switch to next slide, recap slide }}}

So this brings us to the end of this tutorial, in this tutorial we covered basics of arrays, how to create an array, converting a list to an array, basic array operations etc.

{{{ switch to next slide, thank you }}}

Thank you!

..  Author: Anoop Jacob Thomas <anoop@fossee.in>
    Reviewer 1:
    Reviewer 2:
    External reviewer:
