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

-------
Script
-------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to the tutorial on 'Basic Data types and operators'
in Python.

.. L2

{{{ Show the slide containing the objectives }}}

.. R2

At the end of this tutorial, you will be able to,

1. Know the Datatypes in Python
    - Numbers
    - Boolean
    - Sequence
#. Learn about the Operators in Python
    - Arithmetic Operators
    - Boolean Operators
#. Know the Python Sequence Data types
    - list
    - string
    - tuple

.. R3

First we will explore python data structures in the domain of numbers.
There are three built-in data types in python to represent numbers.

.. L3

.. L4

{{{ Show the slide 'numbers' }}}

.. R4

These are:

  - int 
  - float 
  - complex 

.. R5

Let us first invoke our ipython interpreter

.. L5
::

    ipython

.. R6

Lets first talk about int. 

.. L6
::

    a = 13
    a

.. R7

Now, we have our first int variable a.
If we now see 

.. L7
::
     
    type(a)
    <type 'int'>

.. R8

This means that 'a' is a type of int. There are lot of functions associated
with the int datatype, to manipulate it in different ways. These can be
explored by doing, 

.. L8
::

    a.<Tab>

.. R9	

*int* datatype can hold integers of any size lets see this by an example.

.. L9
::

    b = 99999999999999999999
    b

.. R10

As you can see, even when we put a value of 9 repeated 20 times, python did
not complain. This is because python's int data-type can hold integers of any
size.

Let us now look at the float data-type. 
Decimal numbers in python are represented by the float data-type 

.. L10
::

    p = 3.141592
    p

.. R11

If you notice the value of output of ``p`` isn't exactly equal to ``p``.
This is because computer saves floating point values in a specific format.
There is always an approximation. This is why we should never rely on
equality of floating point numbers in a program.

The last data type in the list is complex number 

.. L11
::

    c = 3.2+4.6j

.. R12

it's just a combination of two floats the
imaginary part being defined by j notation instead of i. Complex numbers
have a lot of functions specific to them. Let us look at these 

.. L12
::

    c.<Tab>

.. R13

Lets try some of them 

.. L13
::

    c.real
    c.imag

.. R14

c.real gives the real part of the number and c.imag the imaginary.

We can get the absolute value using the function 

.. L14
::
 
    abs(c)

.. R15

Pause the video here, try out the following exercise and resume the video.

.. L15

.. L16

{{{ Show slide with exercise 1 }}}

.. R16

 Find the absolute value of 3+4j 
<pause>
Switch to your terminal for solution

.. L17

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    abs(3+4j)

.. R17

Thus we get the absolute value of the expression.

Let us do 1 more exercise of a similar type.
Pause the video here, try out the following exercise and resume the video.

.. L18

{{{ Show slide with exercise 2 }}} 

.. R18

 What is the datatype of number 999999999999999999? Is it not int?

.. L19

{{{ Switch to slide solution 2 }}}

.. R19

The solution is on your screen.
The data type of this number is long though it is an integer.    
Big integers are internally stored in python as Long datatype.  

Python also has Boolean as a built-in type.
To Try it out, just type 

.. L20

{{{ Switch to terminal }}}
::  

    t = True

.. R20

note that T in true is capitalized.
  
.. R21

You can apply different Boolean operations on t now for example 

.. L21
::

    f = not t 
    f
    f or t
    f and t 

.. R22

The results are self explanatory.

What if you want to apply one operator before another.
Well you can use parenthesis for precedence.

Lets write some piece of code to check this out.

.. L22
::

    a=False 
    b=True 
    c=True

.. R23

To check how precedence changes with parenthesis, we will try two
expressions and their evaluation.The first one

.. L23
::
 
    (a and b) or c

.. R24
 
This expression gives the value True
where as the expression 

.. L24
:: 
  
    a and (b or c) 

.. R25

gives the value False.

Let's now look at some operators available in Python to manipulate
these data types.

.. L25

.. R26

Python uses '+' sign for addition 

.. L26
::

    23 + 74

.. R27

'-' sign for subtraction  

.. L27
::

    23 - 56

.. R28

'*' (star) sign for multiplication 

.. L28
::
 
    45*76

.. R29

'/'(back slash) for division 

.. L29
::
    
    384/16
    8/3 
    8.0/3

.. R30

Note that, when we did 8/3 the first case results in an integer 
output as both the operands are integer however when 
8.0/3 is used the answer is float as one of the operands is
float. 

.. L30

.. R31

Let us move ahead with the operators.
'%' (percentage) sign for modulo operation 

.. L31
::

    87 % 6

.. R32

and two stars for a exponent. 

.. L32
::

    7**8

.. R33

In case one wishes to use the current value of variable in which the result
is stored in the expression, one can do that by putting the operator before
`equal to`. 

.. L33
::

    a=73
    a*=34

.. R34

The above expression is same as 

.. L34
::
   
    a=a*34

.. R35

and 

.. L35
::

    a/=23

.. R36

is same as 

.. L36
::

    a=a/23

.. R37

Pause the video here, try out the following exercise and resume the video.

.. L37

.. L38

{{{ Show slide with exercise 3 }}}

.. R38
 
 Using python find sqaure root of 3.

.. L39

{{{ Switch to slide solution 3 }}}

.. R39

The solution is on your screen.
3**0.5 gives the square root of 3.

.. L40

{{{ Show slide with exercise 4 }}}

.. R40

 Now, Is 3**1/2 and 3**0.5 same?
<Pause>

.. R41

Switch to your terminal for solution
Let us try both these operations.

.. L41

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    3**0.5
    3**1/2

.. R42

As you can see,the first operation gives an integer,whereas the second one gives a float.
Hence,though both mean the same,they give different outputs.

Let us now discuss sequence data types in Python. Sequence data types
are those in which elements are kept in a sequential order and all the 
elements are accessed using index numbers.

.. L42

.. L43

{{{ slide introducing sequence datatype }}}

.. R43

The sequence datatypes in Python are 

   * list
   * string
   * tuple

The list type is a container that holds a number of other objects, in the
given order.

.. R44

We create our first list by typing 

.. L44

{{{ Switch to terminal }}}
:: 
  
    num_list = [1, 2, 3, 4]
    num_list

.. R45

Items enclosed in square brackets separated by comma constitutes a list.
Lists can store data of any type in them.

We can have a list something like 

.. L45
::

    var_list = [1, 1.2, [1,2]]	
    var_list

.. R46

Lets look at another sequence data type, strings

.. L46
:: 

    greeting_string="hello"

.. R47

greeting_string is now a string variable with the value "hello"

Python strings can actually be defined in three different ways 

.. L47
::

    k='Single quote'
    l="Let's see how to include a single quote"
    m='''"Let's see how to include both"'''

.. R48

As you can see, single quotes are used as delimiters usually.

When a string contains a single quote, double quotes are used as
delimiters. When a string quote contains both single and double quotes,
triple quotes are used as delimiters.

The last in the list of sequence data types is tuple.

To create a tuple we use normal brackets '(' unlike '[' for lists.

.. L48
::

    num_tuple = (1, 2, 3, 4, 5, 6, 7, 8)

.. R49
  
Because of their sequential property there are certain functions and
operations we can apply to all of them.
The first one is accessing.

They can be accessed using index numbers 

.. L49
::

    num_list[2]
    num_list[-1]
    greeting_string[1]
    greeting_string[3]
    greeting_string[-2]
    num_tuple[2]
    num_tuple[-3]

.. R50

Indexing starts from 0, from left to right and from -1 when accessing lists
in reverse. Thus num_list[2] refers to the third element 3. and greetings
[-2] is the second element from the end , that is 'l'.

Addition gives a new sequence containing both sequences 

.. L50
::

    num_list+var_list
    a_string="another string"
    greeting_string+a_string
    t2=(3,4,6,7)
    num_tuple+t2

.. R51

len function gives the length 

.. L51
::

    len(num_list)
    len(greeting_string)
    len(num_tuple)

.. R52

We can check the containership of an element using the 'in' keyword 

.. L52
::

    3 in num_list
    'H' in greeting_string
    2 in num_tuple

.. R53

We see that it gives True and False accordingly.

Find maximum using max function and minimum using min

.. L53
::

    max(num_tuple)
    min(greeting_string)

.. R54

Get a sorted list  

.. L54
::

    sorted(num_list)

.. R55
   
As a consequence of their order, we can access a group of elements in a
sequence, together. This is called slicing and striding.

First lets discuss Slicing, 

Given a list 

.. L55
::

    j=[1,2,3,4,5,6]

.. R56

Lets say we want elements starting from 2 and ending in 5.

For this we can do 

.. L56
::

    j[1:4]

.. R57

The syntax for slicing is, sequence variable name, square bracket, first
element index, colon, second element index. The last element however is not
included in the resultant list

.. L57
::

    j[:4]

.. R58

If first element is left blank default is from beginning and if last
element is left blank it means till the end.

.. L58
::

    j[1:]
    j[:]

.. R59
This effectively is the whole list.

Striding is similar to slicing except that the step size here is not one.

Let us see an example 

.. L59
::

    new_num_list=[1,2,3,4,5,6,7,8,9,10]
    new_num_list[1:8:2]
    [2, 4, 6, 8]

.. R60

The, colon two, added in the end signifies all the alternate elements. This
is why we call this concept striding because we move through the list with
a particular stride or step. The step in this example being 2.

We have talked about many similar features of lists, strings and tuples.
But there are many important features in lists that differ from strings and
tuples. Lets see this by example.

.. L60
::

    new_num_list[1]=9
    greeting_string[1]='k'

.. R61

As you can see while the first command executes with out a problem there is
an error on the second one.
  
Now lets try 

.. L61
::

    new_tuple[1]=5

.. R62

Its the same error. This is because strings and tuples share the property
of being immutable. We cannot change the value at a particular index just
by assigning a new value at that position.

We have looked at different types but we need to convert one data type into
another. Well lets one by one go through methods by which we can convert
one data type to other

.. L62
::

    i=34
    d=float(i)
    d  

.. R63

Python has built in functions int, float and complex to convert one number
type data structure to another.

.. L63
::

    dec=2.34
    dec_con=int(dec)
    dec_con

.. R64

As you can see the decimal part of the number is simply stripped to get the
integer.

.. L64
::

    com=2.3+4.2j
    float(com)
    com

.. R65

In case of complex number to floating point only the real value of complex
number is taken.

Similarly we can convert list to tuple and tuple to list 

.. L65
::
  
    lst=[3,4,5,6]
    tup=tuple(lst)
    lst
    tupl=(3,23,4,56)
    lst=list(tupl)
    tupl

.. R66

However converting a string to a list and a list to a string is an
interesting problem. Let's say we have a string 

.. L66
::

    somestring="Is there a way to split on these spaces."
    somestring.split()

.. R67

This produces a list with the string split at whitespace. Similarly we can
split on some other character.

.. L67
::

    otherstring="Tim,Amy,Stewy,Boss"

.. R68

How do we split on comma , simply pass it as argument 

.. L68
::

    otherstring.split(',')

.. R69

join function does the opposite. Joins a list to make a string.

.. L69
::

    l1=['List','joined','on','commas']
    ','.join(l1)

.. R70

Thus we get a list joined on commas. Similarly we can do spaces.

.. L70
::
 
    l2=['Now','on','spaces']
    ' '.join(l2)

.. R71

Note that the list has to be a list of strings to apply join operation.

Pause the video here, try out the following exercise and resume the video.

.. L71

.. L72

{{{ Show slide with exercise 5 }}}

.. R72

 Check if 3 is an element of the list [1,7,5,3,4]. In case
 it is change it to 21.

.. R73

Switch to the terminal for solution

.. L73

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::
        
    l=[1,7,5,3,4]
    3 in l
    l[3]=21
    l

.. R74

Let us solve one more exercise.
Pause the video here, do the exercise and resume the video.

.. L74

.. L75

{{{ Show slide with exercise 6 }}}

.. R75

 Convert the string "Elizabeth is queen of england" to 
"Elizabeth is queen"

.. R76

Switch to the terminal for solution

.. L76

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    s="Elizabeth is queen of england"
    stemp=s.split()
    ' '.join(stemp[:3])

.. R77

As you can see, we have easily removed the unwanted words.

.. L77

.. L78

{{{ Show summary slide }}}

.. R78

This brings us to the end of the tutorial. In this tutorial, we have
learnt to,

1. Understand the number Datatypes -- integer,float and complex. 
#. Know the boolean datatype and operators -- +, *, /, **, % .
#. use the sequence data types -- List,String and Tuple.
#. Slice sequences by using the row and column numbers.
#. Split and join a list using ``split()`` and ``join()`` function respectively.
#. Convert to string to tuple and vice-versa.

.. L79

{{{Show self assessment questions slide}}}

.. R79

Here are some self assessment questions for you to solve

1. What is the major diffence between tuples and lists?

2. Split this string on whitespaces
::

    string="Split this string on whitespaces"

.. L80

{{{solution of self assessment questions on slide}}}

.. R80

And the answers,

1. The major diffence between tuples and lists is that Tuples are immutable while lists are not.

2. To split the string on whitespace, we use the function `` split`` without any argument
::

    string.split()

.. L81

{{{ Show the thankyou slide }}}

.. R81

Hope you have enjoyed this tutorial and found it useful.
Thank You.
