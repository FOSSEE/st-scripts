Hello friends and welcome to the tutorial on getting started with
lists

 {{{ Show the slide containing title }}}

 {{{ Show the slide containing the outline slide }}}

In this tutorial we will be getting acquainted with a python data
structure called lists .  We will learn :
How to create lists. 
Structure of lists .
Access list elements 
Append elements to lists 
Deleting elements from lists

I hope you have ipython running on your system .




List is a compound data type,it can contain data of other data
types.List is also a sequence data type , all the elements are in
order and there order has a meaning .




We will first create an empty list with no elements . On your ipython
shell type ::

   In []: empty = [] In []: type(empty)
   
   <type 'list'>

This is an empty list without any elements .

* filled lists

Lets now define a list nonempty and fill it with some random elements.

nonempty = ['spam','eggs', 100, 1.234]

Thus the simplest way of creating a list is typing out a sequence 
of comma-separated values (items) between square brackets. 
List items need not all have the same data type.


As you can see lists can contain different kinds of data . In the
previous example 'spam' and 'eggs' are strings and 100 and 1.234
integer and float . Thus you can put elements of heterogenous types in
lists.  Thus list themselves can be one of the element types possible
in lists.  Thus lists can also contain other lists in it .  Example ::

      list_in_list=[[4,2,3,4],'and', 1,2,3,4]


We access list elements using the number of index . The
index begins from 0 . So for list,  nonempty , nonempty[0] gives the
first element , nonempty[1] the second element and so on and
nonempty[3] the last element .::


	    nonempty[0] 
	    nonempty[1] 
	    nonempty[3]

We can also access the elememts from the end using negative indices ::
   
   nonempty[-1] 
   nonempty[-2] 
   nonempty[-4]

-1 being the last element , -2 second to last and -4 being the first
 element .

* =append= elements We can append elements to the end of a list using
append command .::

   nonempty.append('onemore') 
   nonempty.append(6) 
   nonempty
   
As you can see non empty appends 'onemore' and 6 at the end

Using len function we can check the number of elements in the list
nonempty .Because we just appended two elements at the end this
returns us 6.::
	 
	 len(nonempty)

Just like you can append elements to a list you can also remove them .
Their are two ways of doing one is by index no. ::

      del(nonempty[1])

deletes the element at index no.1 , i.e the second element of the
list, 'eggs'. The other way is removing element by content. Lets say
one wishes to delete 100 from nonempty list the syntax of the command
shall be :: a.remove(100)

but what if their were two 100 's . To check that lets do a small
experiment . ::

	   a.append('spam') 
	   a 
	   a.remove('spam') 
	   a

If we check a now we will see that the first element spam is remove
thus remove removes only the first instance of the element by sequence
and leaves others untouched .


{{{Slide for Summary }}}


In this tutorial we came across a sequence data type called lists 
We learned how to create lists .  
Append elements to list .
Delete Element from list.  
And Checking list length.


{{{ Sponsored by Fossee Slide }}}

This tutorial was created as a part of FOSSEE project.

I hope you found this tutorial useful.

Thank You


Author : Amit Sethi 
First Reviewer :
