.. Objectives
.. ----------

.. By the end of this tutorial, you will be able to

.. Create Lists.
.. Access List elements.
.. Append elemets to list
.. Delete list elemets

.. 1. getting started with ipython 



.. Prerequisites
.. -------------

..   1. getting started with strings
..   #. getting started with lists
..   #. basic datatypes
     
.. Author              : Amit 
   Internal Reviewer   : Anoop Jacob Thomas <anoop@fossee.in>
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <12-11-2010, Anand, OK> [2010-10-05]


Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to the tutorial on "Getting started with
lists".

.. L2

{{{ Show slide with objectives }}}

.. R2

In this tutorial we will be getting acquainted with a python data
structure called lists.  
At the end of this tutorial, you will be able to, 
 
 1. Create lists
 #. Access list elements
 #. Append elements to lists
 #. Delete elements from lists

.. R3

List is a compound data type, it can contain data of mutually
different datatypes. List is also a sequence data type where all the
elements are arranged in a specific order.

Start the ipython interpreter and first create an empty list with no 
elements. 

.. L3
::   
   
    ipython
    empty = [] 
    type(empty)

.. R4
  
This is an empty list without any elements.

Lets define a non-empty list as: 

.. L4
::

    nonempty = ['spam', 'eggs', 100, 1.234]

.. R5

Thus, the simplest way of creating a list is typing out a sequence 
of comma-separated values (or items) between two square brackets. 

As we can see, lists can contain different kinds of data. In the
previous example 'spam' and 'eggs' are strings whereas 100 and 1.234 are
integer and float respectively. Thus, we can put elements of different 
datatypes in lists including lists itself. This property makes lists 
heterogeneous data structures.

Let us include a list within a list. 

.. L5
::

    listinlist=[[4,2,3,4],'and', 1, 2, 3, 4]

.. R6

We access an element of a list using its corresponding index. Index of
the first element of a list is 0. So for the list nonempty, nonempty[0] 
gives the first element, nonempty[1] the second element and so on and 
nonempty[3] the last element. 

.. L6
::

    nonempty[0] 
    nonempty[1] 
    nonempty[3]

.. L7

{{{ Switch to the slide exercise 1 }}}

.. R7

Pause the video here, try out the following exercise and resume the video.

What happens when you do nonempty[-1]. 

.. L8

{{{ Switch to the terminal }}}
::

    nonempty[-1]

.. R8

As you can see you get the last element which is 1.234.

.. L9
::
    
    nonempty[-2] 
    nonempty[-4]

.. R9

In python negative indices are used to access elements from the end.
-1 gives the last element which is the 4th element , -2 gives second 
element to last and -4 gives the fourth from the last which, in this case,
is the first element.

.. R10

We can also append elements to the end of a list using the ``append`` 
function. 

.. L10
::

    nonempty.append('onemore') 
    nonempty
    nonempty.append(6) 
    nonempty

.. L11

{{{ Switch to slide exercise 2 }}}

.. R11
   
Please, pause the video here. Do the exercise and then continue.

1. What is the syntax to get the element 'and' in the list,listinlist ?
2. How would you get 'and' using negative indices?

.. L12

{{{ Switch to slide Solution 2 }}}

.. R12

The solution is on your screen
As we can see nonempty is appended with 'onemore' and 6 at the end.

.. R13

Let us move further.We can use ``len`` function to check the number of 
elements in the list.
Let us find out the length of the list 'nonempty'.

.. L13
::
	 
    len(nonempty)

.. R14

Just like we can append elements to a list, we can also remove them.
There are two ways of doing it. One is by using index. 

.. L14
::

    del(nonempty[1])

.. R15

The function ``del`` deletes the element at index 1, i.e the second 
element of the list, 'eggs'. 

The other way is removing element by content. Lets say
one wishes to delete 100 from nonempty list.For this, one could use 
the function ``remove``.

.. L15
::

    nonempty.remove(100)

.. R16

But what if there were two 100's. To check that lets do a small
experiment. 

.. L16
::

    nonempty.append('spam') 
    nonempty
    nonempty.remove('spam') 
    nonempty

.. R17

If we now check, we will see that the first occurence 'spam' is removed
and therefore the function `remove` removes the first occurence of the 
element in the sequence and leaves others untouched.

One should remember this, that while ``del`` removes by index number,
`remove` removes on the basis of content being passed on.Let us take 
an example.

.. L17

.. L18
::
       
    k = [1,2,1,3] 
    del([k[2])

.. R18

del gives us [1,2,3]. 

.. L19
::

    k.remove(x[2])

.. R19

remove will give us [2,1,3]. Since it deletes the first occurrence of 
what is returned by x[2] which is 1.      

.. L20

{{{ Switch to the slide exercise 3 }}}

.. R20

Pause the video here, try out the following exercise and resume the video.

1. Remove the third element from the list, listinlist.   
2. Remove 'and' from the list, listinlist.

.. L21

{{{ Switch to slide Solution 3 }}}

.. R21

The solution is on your screen.

.. L22

{{{Slide for Summary }}}

.. R22

This brings us to the end of this tutorial.
In this tutorial, we have learnt to,

 1. Create lists.  
 #. Access lists using their index numbers.
 #. Append elements to list using the function ``append``.
 #. Delete Element from lists by specifying the index number of the
    element to be deleted in the ``del`` function.  
 #. Delete element from list by content using ``remove`` function.
 #. Find out the list length using ``len`` function.

.. L23
 
{{Show self assessment questions slide}}

.. R23

Here are some self assessment questions for you to solve

1. How do you create an empty list? 
2. Can you have a list inside a list ? 
3. How would you access the end of a list without finding its length?

.. L24

{{{solution of self assessment questions on slide}}}

.. R24

And the answers,

1. We create an empty list just by leaving the space inside the square 
brackets empty.
::

    empty=[]

2. Yes.List can contain all the other data types, including list.
   Here is an example
::

    list_in_list=[2.3,[2,4,6],'string,'all datatypes can be there']

3. Using negative indices, we can access the list from the end using 
   negative indices.
   This is an example
::

    nonempty = ['spam', 'eggs', 100, 1.234]
    nonempty[-1]

.. L25

{{{ Show Thankyou Slide }}}

.. R25

Hope you have enjoyed this tutorial and found it useful.
Thank you!

