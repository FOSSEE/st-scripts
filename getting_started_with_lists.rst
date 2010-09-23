.. #[Nishanth]: liststart is not a good name. there is no consistency.
                Use underscores or hyphens instead of spaces and 
                make the filename from LO name
                Ex: getting_started_with_lists (or)
                getting_started_lists

Hello friends and welcome to the tutorial on getting started with
lists.

 {{{ Show the slide containing title }}}

 {{{ Show the slide containing the outline slide }}}

In this tutorial we will be getting acquainted with a python data
structure called lists.  We will learn :
 * How to create lists
 * Structure of lists
 * Access list elements
 * Append elements to lists
 * Deleting elements from lists

.. #[Nishanth]: Did you compile this??
                There must an empty before the bulleted list

I hope you have ipython running on your system.

.. #[Nishanth]: need not specify. Implicit that IPython is running

List is a compound data type, it can contain data of other data
types. List is also a sequence data type, all the elements are in
order and there order has a meaning.

We will first create an empty list with no elements. On your IPython
shell type ::

   empty = [] 
   type(empty)
   

This is an empty list without any elements.

* Filled lists

Lets now define a list, nonempty and fill it with some random elements.

nonempty = ['spam', 'eggs', 100, 1.234]

Thus the simplest way of creating a list is typing out a sequence 
of comma-separated values (items) between square brackets. 
All the list items need not have the same data type.

.. #[Nishanth]: do not use "You" or anything else. Stick to "We"

As we can see lists can contain different kinds of data. In the
previous example 'spam' and 'eggs' are strings and 100 and 1.234
integer and float. Thus we can put elements of heterogenous types in
lists. Thus list themselves can be one of the element types possible
in lists. Thus lists can also contain other lists.  Example ::

      list_in_list=[[4,2,3,4],'and', 1, 2, 3, 4]

We access list elements using the number of index. The
index begins from 0. So for list nonempty, nonempty[0] gives the
first element, nonempty[1] the second element and so on and
nonempty[3] the last element.::

	    nonempty[0] 
	    nonempty[1] 
	    nonempty[3]

We can also access the elememts from the end using negative indices ::
   
   nonempty[-1] 
   nonempty[-2] 
   nonempty[-4]

-1 being the last element , -2 second to last and -4 being the first
element.

.. #[Nishanth]: -1 being last element sounds like -1 is the last element
                Instead say -1 gives the last element which is 4

.. #[Nishanth]: Instead of saying -4 being the first, say -4 gives 4th 
                from the last which is the first element.

* =append= elements 
We can append elements to the end of a list using append command. ::

   nonempty.append('onemore') 
   nonempty.append(6) 
   nonempty
   
As we can see non empty appends 'onemore' and 6 at the end.

.. #[Nishanth]: First show an example with only one append.
                may be show the value of a after first append
                then show what happens after second append 

Using len function we can check the number of elements in the list
nonempty. Because we just appended two elements at the end this
returns us 6.::
	 
	 len(nonempty)

.. #[Nishanth]: the "because ..." can be removed. You can simply
                say len gives the no.of elements which is 6 here

Just like we can append elements to a list we can also remove them.
There are two ways of doing. One is by using index. ::

      del(nonempty[1])

.. #[Nishanth]: do not use "You" or anything else. Stick to We

deletes the element at index 1, i.e the second element of the
list, 'eggs'. The other way is removing element by content. Lets say
one wishes to delete 100 from nonempty list the syntax of the command
should be :: 
      
      a.remove(100)

but what if their were two 100's. To check that lets do a small
experiment. ::

	   a.append('spam') 
	   a 
	   a.remove('spam') 
	   a

If we check a now we will see that the first occurence 'spam' is removed
thus remove removes the first occurence of the element in the sequence
and leaves others untouched.


{{{Slide for Summary }}}


In this tutorial we came across a sequence data type called lists. ::

 * We learned how to create lists.  
 * Append elements to list.
 * Delete Element from list.  
 * And Checking list length.

.. #[Nishanth]: See the diff. I have corrected punctuation in many places.
                The first thing you do before committing is compile the script.
                I have corrected syntax errors also in many places.

{{{ Sponsored by Fossee Slide }}}

This tutorial was created as a part of FOSSEE project.

I hope you found this tutorial useful.

Thank You


Author : Amit Sethi 
First Reviewer : 
Second Reviewer : Nishanth
