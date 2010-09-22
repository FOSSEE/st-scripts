Hello friends and welcome to the tutorial on Basic Data types and
operators in Python.  
{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline slide }}}


In this tutorial, we shall look at 
 * Various Datatypes in Python
 * Operators with a little hands-on on how they can be applied to 
   the different data types.

Since this a hands on session, you will require python installed in your 
computer. 


First we will explore python data structures in the domain of numbers.
There are three built-in data structures in python to represent numbers.

{{{ A slide to make a memory note of this }}}

These are:

  * Integers 
  * Complex and 
  * Boolean 



Lets first talk about integers. ::

   In[]: a=13


Thats it , there we have our first integer variable a.

If we now see ::
     
   In[]: type(a)
   Out[]: <type 'int'>

   This means  that a is a type of int. Being an int data structure 
in python means that there are various functions that this variable
has to manipulate it different ways. You can explore these by doing,

  In[]: a.<Tab>


Lets see the limits of this int.

  In[]: b=99999999999999999999
  In[]: b

As you can see even when we put a value of 9 repeated 20 times 
python did not complain. However when you asked python to print
the number again it put a capital L at the end. Now if you check
the type of this variable b, ::

  In[]: type(b)
  <type 'long'>


The reason for this is that python recognizes large integer numbers
by a data type long. However long type and integer type share there 
functions and properties.

Lets now try out the second type in list called float.


Decimal numbers in python are recognized by the term float ::

  In[]: p=3.141592
  In[]: p

If you notice the value of output of p isn't exactly equal to p. This
is because computer saves floating point values in a specific
format. This is always an aproximationation. This is why we should
never rely on equality of floating point numbers in a program.


The last data structure in the list is complex number ::

  In: c=3.2+4.6j

as simple as that so essentialy its just a combination of two floats the 
imaginary part being define by j notation usually used in electrical 
engineering. Complex numbers have a lot of functions specific to them.
Lets check these ::

  In[]: c.<Tab>

Lets try some of them ::

  In[]: c.real
  In[]: c.imag

c.real gives the real part of the number and c.imag the imaginary.

We can get the absolute value using the function ::
 
  In[]: abs(c)


Python also has Boolean as a built-in type.

Try it out just type ::  

  In[]: t=True

note that T in true is capitalized.
  
You can apply different Boolean operations on t now for example ::

  In[]: f=not t 
  In[]: f
  In[]: f or t
  In[]: f and t 
  
The results explanotary in themselves.

The usage of boolean brings us to an interesting question of precendence.
What if you want to apply one operator before another. 

Well you can use parenthesis for precedence ,

Lets write some piece of code to check this out.

  In[]: a=False 
  In[]: b=True 
  In[]: c=True

To check how precedence changes with parenthesis. We will try two
expressions and their evaluation.

one ::
 
  In[]: (a and b) or c
 
This expression gives the value True

where as the expression :: 
  
  In[]: a and (b or c) 

gives the value False.


Lets now discuss sequence data structures in python. Sequence 
datatypes are those in which elements are kept in a sequential 
order.All the elements accessed using index. 

{{{ slide to for memory aid }}}

The sequence datatypes in python are ::
 * list
 * string
 * tuple


The list type is a container that holds a number of other 
objects, in the given order.


We create our first list by typing :: 
  
  In[]: num = [1, 2, 3, 4]

Items enclosed in square brackets separated by comma 
constitutes a list.

Lists  can store data of any type in them. 

We can have a list something like ::
 In[]: var = [1, 1.2, [1,2]]	
print var

Now we will have a look at strings 

type :: 

 In[]: w="hello"

w is now a string variable with the value "hello"

{{{ Memory Aid Slide }}}

Python strings can actually be defined in three different ways ::



  In[]: k='Single quote'
  In[]: l="Double quote contain's single quote"
  In[]: m='''"Contain's both"'''

Thus while single quote string may not contain another single quote
double quote can do that. While triple quoted strings can contain both.

The last in the list of sequence data types is tuple.

To create a tuple  we use normal brackets '('
unlike '[' for lists.::

  In[]: t = (1, 2, 3, 4, 5, 6, 7, 8)

  
Because of their sequential property there are certain functions and 
operations we can apply to all of them. 

{{{ Slide for memory aid }}}

The first one is accessing.

They can be accessed using index numbers ::

  In[]: num[2]
  In[]: num[-1]
  In[]: w[1]
  In[]: w[3]
  In[]: w[-2]
  In[]: t[2]
  In[]: t[-3]

Negative indices can be used to access in reverse

Addition gives a new sequence containing both sequences ::

     In[]: num+var
     In[]: p="another string"
     In[]: w+p
     In[]: t2=(3,4,6,7)
     In[]: t+t2

len function gives the length  ::

  In[]: len(num)
  In[]: len(w)
  In[]: len(t)

We can check whether an element is there with 'in' keyword ::

  In[]: 3 in num
  In[]: 'H' in w
  In[]: 2 in t

Find maximum using max function  and minimum using min:: 

  In[]: max(t)
  In[]: min(w)

Get a sorted list and reversed list using sorted and reversed function ::

  In[]: sorted(num)
  In[]: reversed(w)

As a consequence of the order one can access a group of elements together 
The methods for this are called slicing and striding 

First Slicing 

Given a list ::

  In[]:j=[1,2,3,4,5,6]

Lets say we want elements 2 to 5.

For this we can do ::

  In[]: j[1:4]

The syntax for slicing is sequence variable name square bracket
first element index ,colon,second element index.

  In[]: j[:4]

If first element is left blank default is from beginning and if last
element is left blank it means till the end.

 In[]: j[1:]

 In[]: j[:]

This effectively is the whole list.

Striding is a concept similar to slicing with the concept of skiping elements
at regular intervals added.

Lets see by example ::

  In[]: z=[1,2,3,4,5,6,7,8,9,10]
  In[]: z[1:8:2]
  Out[]:[2, 4, 6, 8]

The colon two added in the end signifies all the second elemets. This is why we call this concept
striding because we move through the list with a particular stride or step. The step in this example
being 2. 

We have talked about many similar features of lists,strings and tuples but there are many is an important
way in which lists differ from strings and tuples. Lets see this by example.::

  In[]: z[1]=9
  In[]: w[1]='k'


{{{ slide to show the error }}}
As you can see while the first command executes with out a problem there is an error on the second one.
  
Now lets try ::
  In[]: t[1]=5

Its the same error. This is because strings and tuples share the property of being immutable.
We cannot change the value at a particular index just by assigning a new value at that position.
In case of strings we have special functions to appy relacement and other things while tuples cannot
be changed at all. 

We have looked at different types but we need to convert one data type into another. Well lets one
by one go through methods by which we can convert one data type to other:

We can convert all the number data types to one another ::

  In[]: i=34
  In[]: d=float(i)

Python has built in functions int , float and complex to convert one number type
data structure to another.

  In[]: dec=2.34
  In[]: dec_con=int(dec)
  
As you can see the decimal part of the number is simply stripped  to get the integer.::

  In[]: com=2.3+4.2j
  In[]: float(com)
  In case of complex number to floating point only the real value of complex number is taken.

Similarly we can convert list to tuple and tuple to list ::
  
  In[]: lst=[3,4,5,6]
  In[]: tup=tuple(lst)
  In[]: tupl=(3,23,4,56)
  In[]: lst=list(tuple)

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

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India


Hope you have enjoyed and found it useful.

Thank You.



Author              : Amit Sethi

Internal Reviewer 1 : 

Internal Reviewer 2 : 

External Reviewer
