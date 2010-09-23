Hello friends and welcome to the tutorial on Basic Data types and
operators in Python.  
{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline slide }}}

In this tutorial, we shall look at::

 * Various Datatypes in Python
 * Operators with a little hands-on on how they can be applied to 
   the different data types.



First we will explore python data structures in the domain of numbers.
There are three built-in data types in python to represent numbers.

{{{ A slide to make a memory note of this }}}

These are:

  * Integers 
  * Complex and 
  * Boolean 

Lets first talk about integers. ::

   a = 13
   a


Thats it, there we have our first integer variable a.



If we now see ::
     
   type(a)
   <type 'int'>

This means that a is a type of int. Being an int data structure 
in python means that there are various functions that this variable
has to manipulate it different ways. You can explore these by doing,

  a.<Tab>



Lets see the limits of this int.

  b = 99999999999999999999
  b

As you can see even when we put a value of 9 repeated 20 times 
python did not complain. However when you asked python to print
the number again it put a capital L at the end. Now if you check
the type of this variable b, ::

  type(b)
  <type 'long'>


The reason for this is that python recognizes large integer numbers
by the data type long. However long type and integer type share there 
functions and properties.

Lets now try out the second type in list called float.

Decimal numbers in python are recognized by the term float ::

  p = 3.141592
  p

If you notice the value of output of p isn't exactly equal to p. This
is because computer saves floating point values in a specific
format. There is always an aproximationation. This is why we should
never rely on equality of floating point numbers in a program.

The last data type in the list is complex number ::

  c = 3.2+4.6j

as simple as that so essentialy its just a combination of two floats the 
imaginary part being define by j notation instead of i. Complex numbers have a lot of functions specific to them.
Lets check these ::

  c.<Tab>

Lets try some of them ::

  c.real
  c.imag

c.real gives the real part of the number and c.imag the imaginary.

We can get the absolute value using the function ::
 
  abs(c)

Python also has Boolean as a built-in type.

Try it out just type ::  

  t = True

note that T in true is capitalized.
  
You can apply different Boolean operations on t now for example ::

  f = not t 
  f
  f or t
  f and t 


  
The results are explanotary in themselves.

The usage of boolean brings us to an interesting question of precendence.
What if you want to apply one operator before another. 

Well you can use parenthesis for precedence.

Lets write some piece of code to check this out.

  In[]: a=False 
  In[]: b=True 
  In[]: c=True

To check how precedence changes with parenthesis. We will try two
expressions and their evaluation.

one ::
 
  (a and b) or c
 
This expression gives the value True

where as the expression :: 
  
  a and (b or c) 

gives the value False.

Lets now discuss sequence data structures in python. Sequence 
datatypes are those in which elements are kept in a sequential 
order. All the elements accessed using index. 

{{{ slide to for memory aid }}}

The sequence datatypes in python are ::

 * list
 * string
 * tuple

The list type is a container that holds a number of other 
objects, in the given order.

We create our first list by typing :: 
  
  num_list = [1, 2, 3, 4]
  num_list


Items enclosed in square brackets separated by comma 
constitutes a list.

Lists can store data of any type in them. 

We can have a list something like ::

 var_list = [1, 1.2, [1,2]]	
 var_list



Now we will have a look at strings 

type :: 

 In[]: greeting_string="hello"


greeting_string is now a string variable with the value "hello"

{{{ Memory Aid Slide }}}

Python strings can actually be defined in three different ways ::

  In[]: k='Single quote'
  In[]: l="Double quote contain's single quote"
  In[]: m='''"Contain's both"'''

Thus, single quotes are used as delimiters usually.
When a string contains a single quote, double quotes are used as delimiters.
When a string quote contains both single and double quotes, triple quotes are
used as delimiters.

The last in the list of sequence data types is tuple.

To create a tuple  we use normal brackets '('
unlike '[' for lists.::

  In[]: num_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
  
Because of their sequential property there are certain functions and 
operations we can apply to all of them. 

{{{ Slide for memory aid }}}

The first one is accessing.

They can be accessed using index numbers ::

  In[]: num_list[2]
  In[]: num_list[-1]
  In[]: greeting_string[1]
  In[]: greeting_string[3]
  In[]: greeting_string[-2]
  In[]: num_tuple[2]
  In[]: num_tuple[-3]


Indexing starts from 0 from left to right and from -1 when accessing
lists in reverse. Thus num_list[2] refers to the third element 3. 
and greetings [-2] is the second element from the end , that is 'l'. 



Addition gives a new sequence containing both sequences ::

     In[]: num_list+var_list
     In[]: a_string="another string"
     In[]: greeting_string+a_string
     In[]: t2=(3,4,6,7)
     In[]: num_tuple+t2

len function gives the length  ::

  In[]: len(num_list)
  In[]: len(greeting_string)
  In[]: len(num_tuple)

Prints the length the variable.

We can check the containership of an element using the 'in' keyword ::

  In[]: 3 in num_list
  In[]: 'H' in greeting_string
  In[]: 2 in num_tuple

We see that it gives True and False accordingly.

Find maximum using max function and minimum using min:: 

  In[]: max(num_tuple)
  In[]: min(greeting_string)

Get a sorted list and reversed list using sorted and reversed function ::

  In[]: sorted(num_list)
  In[]: reversed(greeting_string)

As a consequence of the order one we access a group of elements together.
This is called slicing and striding.

First Slicing 

Given a list ::

  In[]:j=[1,2,3,4,5,6]

Lets say we want elements starting from 2 and ending in 5.

For this we can do ::

  In[]: j[1:4]

The syntax for slicing is sequence variable name square bracket
first element index, colon, second element index.The last element however is notincluded in the resultant list::


  In[]: j[:4]

If first element is left blank default is from beginning and if last
element is left blank it means till the end.

 In[]: j[1:]

 In[]: j[:]

This effectively is the whole list.

Striding is similar to slicing except that the step size here is not one.

Lets see by example ::

  new_num_list=[1,2,3,4,5,6,7,8,9,10]
  new_num_list[1:8:2]
  [2, 4, 6, 8]

The colon two added in the end signifies all the alternate elements. This is why we call this concept
striding because we move through the list with a particular stride or step. The step in this example
being 2. 

We have talked about many similar features of lists, strings and tuples. But there are many important
features in lists that differ from strings and tuples. Lets see this by example.::

  In[]: new_num_list[1]=9
  In[]: greeting_string[1]='k'

{{{ slide to show the error }}}



As you can see while the first command executes with out a problem there is an error on the second one.
  
Now lets try ::

  In[]: new_tuple[1]=5

Its the same error. This is because strings and tuples share the property of being immutable.
We cannot change the value at a particular index just by assigning a new value at that position.


We have looked at different types but we need to convert one data type into another. Well lets one
by one go through methods by which we can convert one data type to other:

We can convert all the number data types to one another ::

  i=34
  d=float(i)
  d  

Python has built in functions int, float and complex to convert one number type
data structure to another.

  dec=2.34
  dec_con=int(dec)
  dec_con


As you can see the decimal part of the number is simply stripped to get the integer.::

  com=2.3+4.2j
  float(com)
  com

In case of complex number to floating point only the real value of complex number is taken.

Similarly we can convert list to tuple and tuple to list ::
  
  lst=[3,4,5,6]
  tup=tuple(lst)
  tupl=(3,23,4,56)
  lst=list(tuple)

However string to list and list to string is an interesting problem.
Lets say we have a string ::

  In: somestring="Is there a way to split on these spaces."
  In: somestring.split()


This produces a list with the string split at whitespace.
similarly we can split on some other character.

  In: otherstring="Tim,Amy,Stewy,Boss"

How do we split on comma , simply pass it as argument ::

  In: otherstring.split(',')

join function does the opposite. Joins a list to make a string.::

  In[]:','.join['List','joined','on','commas']

Thus we get a list joined on commas. Similarly we can do spaces.::

  In[]:' '.join['Now','on','spaces']

Note that the list has to be a list of strings to apply join operation.

.. #[Nishanth]: string to list is fine. But list to string can be left for
                string manipulations. Just say it requires some string 
                manipulations and leave it there.

.. #[Nishanth]: Where is the summary
                There are no exercises in the script

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.

Thank You.



Author              : Amit Sethi
Internal Reviewer 1 : Nishanth
Internal Reviewer 2 : 
External Reviewer
