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

{{{ Show the slide containing the title }}}

Hello friends. Welcome to this spoken tutorial on Manipulating Lists. 

{{{ Show the slide containing the outline }}}

We have already learnt about Lists in Python. In this tutorial,
we will learn about more advanced features of Lists in Python like how
to concatenate two lists, details of slicing and striding of lists, 
methods to sort and reverse lists.

{{{ Shift to terminal and start ipython }}}

To begin with let us start ipython, by typing::

  ipython

on the terminal

We already know what Lists are in Python, how to access individual
elements in the list and some of the functions that can be run on the
lists like ``max, min, sum, len`` and so on. Now let us learn some of
the basic operations that can be performed on Lists.

We already know how to access individual elements in a List. But what
if we have a scenario where we need to get a part of the entire list
or what we call as a slice of the list? Python supports slicing on
lists. Let us say I have the list::

  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

To obtain all the primes between 10 and 20 from the above list of
primes we say::

  primes[4:8]

This gives us all the elements in the list starting from the element
with the index 4, which is 11 in our list, upto the element with index 8
in the list but not including the eigth element. So we obtain a slice
starting from 11 upto 19th. It is a very important to remember that
whenever we specify a range of elements in Python the start index is
included and end index is not included. So in the above case, 11 which
was the element with the index 4 was included but 23 which was the
element with index 8 was excluded.

Following is an exercise you must do. 

%% %% Obtain the primes less than 10, from the list ``primes``. 

Please, pause the video here, do the exercise and then resume. 

::

  primes[0:4]

will give us the primes below 10. 

Generalizing, we can obtain a slice of the list "p" from the index
"start" upto the index "end" but excluding "end" with the following
syntax

{{{ Show the slide containing p[start:stop] }}}

By default the slice fetches all the elements between start and stop
including start but not stop. So as to say we obtain all the elements
between start and stop in steps of one. Python also provides us the
functionality to specify the steps in which the slice must be
obtained. Say we have::

  num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

If we want to obtain all the odd numbers less than 10 from the list
``num`` we have to start from element with index 1 upto the index 10 in
steps of 2::

  num[1:10:2]

When no step is specified, it is assumed to be 1. Similarly, there are
default values for start and stop indices as well. If we don't specify
the start index it is implicitly taken as the first element of the
list::

  num[:10]

This gives us all the elements from the beginning upto the 10th
element but not including the 10th element in the list "num". Similary
if the stop index is not specified it is implicitly assumed to be the
end of the list, including the last element of the list::

  num[10:]

gives all the elements starting from the 10th element in the list
"num" upto the final element including that last element. Now::

  num[::2]

gives us all the even numbers in the list "num".

Following is an exercise that you must do. 

%% %% Obtain all the multiples of three from the list ``num``.

Please, pause the video here. Do the exercise and then continue. 

::

  num[::3]

gives us all the multiples of 3 from the list, since every third
element in it, starting from 0, is divisible by 3. 

The other basic operation that we can perform on lists is concatenation
of two or more lists. We can combine two lists by using the "plus"
operator. Say we have

{{{ Read as you type }}}::

  a = [1, 2, 3, 4]
  b = [4, 5, 6, 7]
  a + b

When we concatenate lists using the "plus" operator we get a new
list. We can store this list in a new variable::

  c = a + b
  c

It is important to observe that the "plus" operator always returns a
new list without altering the lists being concatenated in any way. 

We know that a list is a collection of data. Whenever we have a
collection we run into situations where we want to sort the
collection. Lists support sort method which sorts the list inplace::

  a = [5, 1, 6, 7, 7, 10]
  a.sort()

Now the contents of the list ``a`` will be::

  a
  [1, 5, 6, 7, 7, 10]

As the sort method sorts the elements of a list, the original list we had
is overwritten or replaced. We have no way to obtain the original list
back. One way to avoid this is to keep a copy of the original list in
another variable and run the sort method on the list. However Python
also provides a built-in function called sorted which sorts the list
which is passed as an argument to it and returns a new sorted list::

  a = [5, 1, 6, 7, 7, 10]
  sorted(a)
  
We can store this sorted list another list variable::

  sa = sorted(a)

Python also provides the reverse method which reverses
the list inplace::

  a = [1, 2, 3, 4, 5]
  a.reverse()

reverses the list "a" and stores the reversed list inplace i.e. in "a"
itself. Lets see the list "a"::

  a
  [5, 4, 3, 2, 1]

But again the original list is lost. 
.. #[punch: removed reversed, since it returns an iterator]

To reverse a list, we could use striding with negative indexing.::

   a[::-1]

We can also store this new reversed list in another list variable.

Following is an (are) exercise(s) that you must do. 

%% %% Given a list of marks of students in an examination, obtain a
      list with marks in descending order.
      ::

            marks = [99, 67, 47, 100, 50, 75, 62]

Please, pause the video here. Do the exercise(s) and then continue. 

::

  sorted(marks)[::-1]

OR

::

  sorted(marks, reverse = True)



{{{ Show summary slide }}}

This brings us to the end of another session. In this tutorial session
we learnt

  * Obtaining parts of lists using slicing and striding
  * List concatenation
  * Sorting lists 
  * Reversing lists

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!
 

