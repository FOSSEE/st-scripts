.. Objectives
.. ----------

.. At the end of this tutorial, you will be able to 

.. 1. Create arrays using data
.. #. Create arrays from lists
.. #. Basic array operations
.. #. Creating identity matrix using ``identity()`` function.
.. #. Learn about ``zeros()``, ``zeros_like()``, ``ones()``,
      ``ones_like()`` functions.

.. Prerequisites
.. -------------

..   1. should have ``ipython`` and ``pylab`` installed. 
..   #. getting started with ``ipython``.
..   #. getting started with lists.

.. #[sushma: the software required to open the ogg files in windows
.. should also be given in the prerequisites]

..  Author: Anoop Jacob Thomas <anoop@fossee.in>
    Internal Reviewer   : Puneeth 
    External Reviewer   :
    Language Reviewer   : Bhanukiran
    Checklist OK?       : <11-11-2010,Anand, OK > [2010-10-05]

===========================
Getting started with Arrays
===========================

.. #[Puneeth: Prerequisites and Objectives are missing. Fill them in]

{{{ show the welcome slide }}}

Welcome to the spoken tutorial on getting started with arrays.

{{{ switch to next slide, outline slide }}}

In this tutorial, we will learn about the data structure called an array, how to convert
a list into an array, operations on arrays and also why an array is preferred
to lists.

.. #[Puneeth: Fix the grammar above.]

{{{ switch to next slide on overview of array }}}

Arrays are homogeneous data structures. Unlike lists, arrays cannot have
heterogeneous data elements, that is, they can have only one type of data 
as their entries, be them all integers, strings, or maybe floats, but not a mix.

.. #[Puneeth: Use multiple short sentences, rather than one long sentence
   I would've written something like this. 

   Unlike lists, arrays are homogeneous data structures. They can have only
   type of data, ....]

Arrays of a given length are comparatively much faster in mathematical
operations than lists of the same length, because of the fact that they are
homogeneous data structures.

.. #[Puneeth: For what size of an array is that the comparison?

{{{ switch to the next slide, creating arrays }}}

Now let us see how to create arrays.

Run your IPython interpreter with ``-pylab`` option, to load the required
modules to work with arrays.
{{{ take terminal and run the following command }}}
::

        ipython -pylab

.. #[Puneeth: 'I am assuming' doesn't sound right. Ask them to open if it
.. is not open?]

To create an array we will use the function ``array()`` as,

::

    a1 = array([1,2,3,4])

Notice that we created a one dimensional array here. Also notice the object
we passed to create an array. We passed a list to create an array. 

Now let us see how to create a two dimensional array. Pause here and try to
do it yourself before looking at the solution.

{{{ switch to next slide, creating two dimensional arrays }}}

.. #[Puneeth: I don't think this question can be solved by an average
.. viewer. Questions during the tutorial, should generally be to re-iterate
.. concepts learnt? ]

.. #[Puneeth: Also, you didn't even point out that we are converting a
.. list, using the ``array`` function. Bring the later section about
.. converting a list, here. A separate section is not necessary, IMHO.]

We create two dimensional array by converting a list of lists to an array
as,

::

    a2 = array([[1,2,3,4],[5,6,7,8]])

.. #[Puneeth: Again, you could explain a bit about the fact that we are
.. converting a list of lists.]

Now let us use ``arange()`` function to create the same array as before.

::

    ar = arange(1,9)

.. #[Puneeth: say, creating the same array as before. for some time I got
.. confused .]

And we obtained a one dimensional array with elements from 1 to 8.

::

    print ar

.. #[Puneeth: be consistent with voice. say, we obtained... or something.]

And how can we make it a two dimensional array of order 2 by 4? Pause here
and try to do it yourself, try ``ar.tab`` and find a suitable method for
that.

{{{ switch to next slide, reshape() method }}}

We can use the function ``reshape()`` for that purpose and it can be done
as,

::

    ar.reshape(2,4)
    ar.reshape(4,2)
    ar = ar.reshape(2,4)

{{{ switch to next slide, creating array from list}}}

Now, let us see how to convert a list object to an array. As you have
already seen, in both of the previous statements we have passed a list, so
creating an array can be done so, first let us create a list ``l1``

::

    l1 = [1,2,3,4]

Now we can convert the list to an array as, 

::

    a3 = array(l1)


{{{ switch to the next slide, problem statement of unsolved exercise 1 }}}

Create a three dimensional array of the shape (2,2,4).

.. #[Puneeth: s/order/shape or size ?]

{{{ switch to the next slide, shape of an array }}}

To find the shape of an array we can use the method ``.shape``, let us
check the shape of the arrays we have created so far,

.. #[Puneeth: s/object/method ?]

::

    a2.shape

``a2.shape`` object is a tuple, and it returned a tuple (2, 4).

.. #[Puneeth: first show a 2D array, so that it becomes easier to explain.
.. Also, the word ``tuple`` need not be mentioned. ]

{{{ switch to the next slide, unsolved exercise 2 }}}

Find out the shape of the other arrays that we have created.

.. #[Puneeth: solution missing.]

It can be done as,
::

    a1.shape
    a3.shape
    ar.shape

{{{ Array can have only a single type of data }}}

.. #[Puneeth: I guess, this whole section can be skipped. If you want to
.. keep this, just briefly mention that arrays are homogeneous in the
.. intro, don't explain it there.]

Now let us try to create a new array with a mix of elements and see what
will happen,

::

    a4 = array([1,2,3,'a string'])

Well, we would expect an error as it has been previously mentioned that arrays handle
elements with the same datatype, but it didn't raise an error. Let us check the values
in the new array created. In your IPython terminal type, 
::

    a4

Did you notice it,

{{{ switch to next slide, implicit type casting }}}

.. #[Puneeth: typecasting may be unnecessary. (Also too advanced?) an
.. average guy wouldn't use arrays with strings.]

.. #[Puneeth: You may want to mention that float is the default dtype.]

{{{ highlight all the array elements one by one using mouse movements }}}

all the elements have been implicitly type casted as strings, though our
first three elements were meant to be integers.

.. #[Puneeth: when I type a4 it says some ``dtype`` etc. I don't understand
.. what it is, can you explain? ;)]

{{{ switch to the next slide, identity & zeros methods }}}

.. #[Puneeth: something needs to motivate this. why are we suddenly talking
.. of an identity matrix?]

Now let us see how to create an identity matrix of a given size, that is a
two-dimensional array  in  which all the diagonal elements are ones and rest of the
elements are zeros. We can create an identity matrix using the function
``identity()``.

The function ``identity()`` takes an integer argument which specifies the
size of the desired matrix,

::

    identity(3)

As you can see the identity function returned a three by three square matrix
with all the diagonal elements as ones and the rest of the elements as zeros.

.. #[Puneeth: You say array here, matrix there -- it's a bit messed up.
.. Clarify, explicitly.]

``zeros()`` function accepts a tuple, which is the order of the array that we
want to create, and it generates an array with all elements as zeros.

{{{ switch to the next slide, problem statement of solved exercise 1 }}}

Let us creates an array of the order four by five with all the elements
zero. We can do it using the method zeros, ::

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

We can use all the mathematical operations with arrays, Now let us try this
::

   a1 = array([1,2,3,4])
   a2 = array([1,2,3,4])
   a1 + a2

Returns an array with element by element addition,
::

    a1 * a2

Returns an array with element by element multiplication, notice that it
does not perform matrix multiplication.

{{{ switch to next slide, summary slide }}}

So this brings us to the end of this tutorial, in this tutorial we covered
basics of arrays, learned how to create an array, saw how to convert a list
to an array, and basic array operations etc.

.. #[Puneeth: s/how to create an array/creating an array]

{{{ switch to next slide, thank you }}}

Thank you!

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 75
   End:
