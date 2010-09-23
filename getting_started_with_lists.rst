Hello friends and welcome to the tutorial on getting started with
lists.

 {{{ Show the slide containing title }}}

 {{{ Show the slide containing the outline slide }}}

In this tutorial we will be getting acquainted with a python data
structure called lists.  We will learn ::
 
 * How to create lists
 * Structure of lists
 * Access list elements
 * Append elements to lists
 * Deleting elements from lists

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



As we can see lists can contain different kinds of data. In the
previous example 'spam' and 'eggs' are strings and 100 and 1.234
integer and float. Thus we can put elements of heterogenous types in
lists. Thus list themselves can be one of the element types possible
in lists. Thus lists can also contain other lists.  Example ::

      list_in_list=[[4,2,3,4],'and', 1, 2, 3, 4]

We access list elements using the number of index. The
index begins from 0. So for list nonempty, nonempty[0] gives the
first element, nonempty[1] the second element and so on and
nonempty[3] the last element. ::

	    nonempty[0] 
	    nonempty[1] 
	    nonempty[3]

We can also access the elememts from the end using negative indices ::
   
   nonempty[-1] 
   nonempty[-2] 
   nonempty[-4]

-1 gives the last element which is the 4th element , -2 second to last and -4 gives the fourth
from last element which is first element.

We can append elements to the end of a list using append command. ::

   nonempty.append('onemore') 
   nonempty
   nonempty.append(6) 
   nonempty
   
As we can see non empty appends 'onemore' and 6 at the end.



Using len function we can check the number of elements in the list
nonempty. In this case it being 6 ::
	 
	 len(nonempty)



Just like we can append elements to a list we can also remove them.
There are two ways of doing it. One is by using index. ::

      del(nonempty[1])



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



{{{ Sponsored by Fossee Slide }}}

This tutorial was created as a part of FOSSEE project.

I hope you found this tutorial useful.

Thank You


 * Author : Amit Sethi 
 * First Reviewer : 
 * Second Reviewer : Nishanth
