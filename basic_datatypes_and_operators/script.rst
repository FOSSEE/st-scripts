.. Objectives
.. ----------

.. At the end of this tutorial, you should know --

.. 1. Learn about Python Data Structures and Operators.(Remembering)
.. #.Use them to do basic operations.(Applying)

.. Prerequisites
.. -------------

.. None
     
.. Author              : Amit Sethi
   Internal Reviewer   : 
   External Reviewer   :
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]

Hello friends and welcome to the tutorial on Basic Data types and operators
in Python.

{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline slide }}}

In this tutorial, we shall look at

* Datatypes in Python
    * Numbers
    * Boolean
    * Sequence
* Operators in Python
  * Arithmetic Operators
  * Boolean Operators

* Python Sequence Data types
  * list
  * string
  * tuple

First we will explore python data structures in the domain of numbers.
There are three built-in data types in python to represent numbers.

{{{ A slide to make a memory note of the different datatypes }}}

These are:

  * int 
  * float 
  * complex 

Lets first talk about int. ::

   a = 13
   a


Now, we have our first int variable a.


If we now see ::
     
   type(a)
   <type 'int'>

This means that a is a type of int. There are lot of functions associated
with the int datatype, to manipulate it in different ways. These can be
explored by doing, ::

  a.<Tab>

*int* datatype can hold integers of any size lets see this by an example.
::

  b = 99999999999999999999
  b

As you can see even when we put a value of 9 repeated 20 times python did
not complain. This is because python's int data-type can hold integers of any
size.

Let us now look at the float data-type. 

Decimal numbers in python are represented by the float data-type ::

  p = 3.141592
  p

If you notice the value of output of ``p`` isn't exactly equal to ``p``.
This is because computer saves floating point values in a specific format.
There is always an approximation. This is why we should never rely on
equality of floating point numbers in a program.

The last data type in the list is complex number ::

  c = 3.2+4.6j

as simple as that so essentialy its just a combination of two floats the
imaginary part being defined by j notation instead of i. Complex numbers
have a lot of functions specific to them. Let us look at these ::

  c.<Tab>

Lets try some of them ::

  c.real
  c.imag

c.real gives the real part of the number and c.imag the imaginary.

We can get the absolute value using the function ::
 
  abs(c)


Following is are exercises that you must do. 

%% %% Find the absolute value of 3+4j 
::

        abs(3+4j)

%% %% What is the datatype of number 999999999999999999? Is it
not int?
::

        Long
        Big integers are internally stored in python
        as Long datatype.  

Please, pause the video here. Do the exercises and then continue. 


{{ Slide for showing Boolean datatypes }} 

Python also has Boolean as a built-in type.

Try it out just type ::  

  t = True

note that T in true is capitalized.
  
You can apply different Boolean operations on t now for example ::

  f = not t 
  f
  f or t
  f and t 


The results are self explanatory.

What if you want to apply one operator before another.

Well you can use parenthesis for precedence.

Lets write some piece of code to check this out.::

  a=False 
  b=True 
  c=True


To check how precedence changes with parenthesis, we will try two
expressions and their evaluation.

one ::
 
  (a and b) or c
 
This expression gives the value True

where as the expression :: 
  
  a and (b or c) 

gives the value False.


Let's now look at some operators available in Python to manipulate
these data types.

Python uses '+' for addition ::

  23 + 74

'-' for subtraction ::

  23 - 56

'*' for multiplication ::
 
  45*76

'/' for division ::
    
  384/16
  8/3 
  8.0/3

When we did 8/3 the first case results in am integer 
output as both the operands are integer however when 
8.0/3 is used the answer is float as one of the operands is
float. 


'%' for modulo operation ::

    87 % 6

and two stars for a exponent. ::

    7**8


In case one wishes to use the current value of variable in which the result
is stored in the expression one can do that by putting the operator before
`equal to`. ::

   a=73
   a*=34

is same as ::
   
   a=a*34

and ::

    a/=23

is same as ::

   a=a/23

Following is are exercises that you must do. 

%% %% Using python find sqaure root of 3?

%% %% Is 3**1/2 and 3**0.5 same

Please, pause the video here. Do the exercises and then continue.

::

   3**0.5

::
    No,One gives an int answer and the other float        


Lets now discuss sequence data types in Python. Sequence data types
are those in which elements are kept in a sequential order and all the 
elements are accessed using index numbers.

{{{ slide introducing sequence datatype }}}

The sequence datatypes in Python are ::

 * list
 * string
 * tuple

The list type is a container that holds a number of other objects, in the
given order.

We create our first list by typing :: 
  
  num_list = [1, 2, 3, 4]
  num_list


Items enclosed in square brackets separated by comma constitutes a list.

Lists can store data of any type in them.

We can have a list something like ::

 var_list = [1, 1.2, [1,2]]	
 var_list

Lets look at another sequence data type, strings

type :: 

  greeting_string="hello"


greeting_string is now a string variable with the value "hello"

{{{ All the different types of strings shown }}}

Python strings can actually be defined in three different ways ::

   k='Single quote'
   l="Let's see how to include a single quote"
   m='''"Let's see how to include both"'''

As you can see, single quotes are used as delimiters usually.

When a string contains a single quote, double quotes are used as
delimiters. When a string quote contains both single and double quotes,
triple quotes are used as delimiters.

The last in the list of sequence data types is tuple.

To create a tuple we use normal brackets '(' unlike '[' for lists.::

   num_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
  
Because of their sequential property there are certain functions and
operations we can apply to all of them.



The first one is accessing.

They can be accessed using index numbers ::

   num_list[2]
   num_list[-1]
   greeting_string[1]
   greeting_string[3]
   greeting_string[-2]
   num_tuple[2]
   num_tuple[-3]


Indexing starts from 0 from left to right and from -1 when accessing lists
in reverse. Thus num_list[2] refers to the third element 3. and greetings
[-2] is the second element from the end , that is 'l'.



Addition gives a new sequence containing both sequences ::

      num_list+var_list
      a_string="another string"
      greeting_string+a_string
      t2=(3,4,6,7)
      num_tuple+t2

len function gives the length ::

   len(num_list)
   len(greeting_string)
   len(num_tuple)

Prints the length the variable.

We can check the containership of an element using the 'in' keyword ::

   3 in num_list
   'H' in greeting_string
   2 in num_tuple

We see that it gives True and False accordingly.

Find maximum using max function and minimum using min::

   max(num_tuple)
   min(greeting_string)

Get a sorted list  ::

   sorted(num_list)
   

As a consequence of their order, we can access a group of elements in a
sequence, together. This is called slicing and striding.

First lets discuss Slicing, 

Given a list ::

  j=[1,2,3,4,5,6]

Lets say we want elements starting from 2 and ending in 5.

For this we can do ::

   j[1:4]

The syntax for slicing is, sequence variable name square bracket first
element index, colon, second element index. The last element however is not
included in the resultant list::


   j[:4]

If first element is left blank default is from beginning and if last
element is left blank it means till the end.

::

  j[1:]

  j[:]

This effectively is the whole list.

Striding is similar to slicing except that the step size here is not one.

Lets see by example ::

  new_num_list=[1,2,3,4,5,6,7,8,9,10]
  new_num_list[1:8:2]
  [2, 4, 6, 8]

The colon two added in the end signifies all the alternate elements. This
is why we call this concept striding because we move through the list with
a particular stride or step. The step in this example being 2.

We have talked about many similar features of lists, strings and tuples.
But there are many important features in lists that differ from strings and
tuples. Lets see this by example.::

   new_num_list[1]=9
   greeting_string[1]='k'

{{{ slide to show the error }}}



As you can see while the first command executes with out a problem there is
an error on the second one.
  
Now lets try ::

   new_tuple[1]=5

Its the same error. This is because strings and tuples share the property
of being immutable. We cannot change the value at a particular index just
by assigning a new value at that position.


We have looked at different types but we need to convert one data type into
another. Well lets one by one go through methods by which we can convert
one data type to other:

We can convert all the number data types to one another ::

  i=34
  d=float(i)
  d  

Python has built in functions int, float and complex to convert one number
type data structure to another.

::

  dec=2.34
  dec_con=int(dec)
  dec_con


As you can see the decimal part of the number is simply stripped to get the
integer.::

  com=2.3+4.2j
  float(com)
  com

In case of complex number to floating point only the real value of complex
number is taken.

Similarly we can convert list to tuple and tuple to list ::
  
  lst=[3,4,5,6]
  tup=tuple(lst)
  tupl=(3,23,4,56)
  lst=list(tuple)

However converting a string to a list and a list to a string is an
interesting problem. Let's say we have a string ::

  In: somestring="Is there a way to split on these spaces."
  In: somestring.split()


This produces a list with the string split at whitespace. Similarly we can
split on some other character.

::

  In: otherstring="Tim,Amy,Stewy,Boss"

How do we split on comma , simply pass it as argument ::

  In: otherstring.split(',')

join function does the opposite. Joins a list to make a string.::

  ','.join['List','joined','on','commas']

Thus we get a list joined on commas. Similarly we can do spaces.::

  ' '.join['Now','on','spaces']

Note that the list has to be a list of strings to apply join operation.

With this we come to the end of this tutorial .

Following is an (are) exercise(s) that you must do. 



%% %% Check if 3 is an element of the list [1,7,5,3,4]. In case
it is change it to 21.
::
        l=[1,7,5,3,4]
        3 in l
        l[3]=21
        l

%% %% Convert the string "Elizabeth is queen of england" to 
"Elizabeth is queen"
::

           s="Elizabeth is queen of england"
           stemp=s.split()
           ' '.join(stemp[:3])
   
Please, pause the video here. Do the exercise(s) and then continue. 


This brings us to the end of the tutorial. In this tutorial we have
discussed

1. Number Datatypes , integer,float and complex 
2. Boolean and datatype and operators
3. Sequence data types ,List,String and Tuple
4. Accesing sequence
5. Slicing sequences
6. Finding length , sorting and reversing operations on sequences.
7. Immutability.

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.

Thank You.


.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 75
   End:
