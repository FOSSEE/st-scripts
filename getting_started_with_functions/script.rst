.. Objectives
.. ----------

.. 8.1 LO: getting started with functions (3)

.. At the end of this tutorial, you will be able to 

.. 1. define function
.. #. define functions with arguments
.. #. learn about docstrings
.. #. learn about return values
..    can return multiple values
.. #. read code


.. Prerequisites
.. -------------

..   1. should have ``ipython`` installed. 
..   #. getting started with ``ipython``.
..   #. Conditionals
..   #. Loops 

     
.. Author              : Anoop Jacob Thomas <anoop@fossee.in>
   Internal Reviewer   : 
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <put date stamp here, not OK> [2010-10-05]


==============================
Getting started with functions
==============================

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to the tutorial on 
'Getting started with functions'.

.. L2

{{{ switch to slide containing objectives }}}

.. R2

At the end of this tutorial, you will be able to, 

 1. Define a function.
 #. Define functions with arguments.
 #. Learn about docstrings.
 #. Learn about function return value.
 #. Read code.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Conditionals".

.. L4

{{{ switch to next slide, Function }}}

.. R4

While writing code, we always want to reduce the number of lines of
code, and functions is a way of reusing the code. Thus the same lines
of code can be used as many times as needed. A function is a portion of 
code within a larger program that performs a specific task and is
relatively independent of the remaining code. Now let us get more
familiar with functions,

.. L5

{{{ switch to next slide, f(x) a mathematical function }}}

.. R5

Consider a mathematical function f(x) = x square. Here x is a variable
and with different values of x the value of function will change. When
x is one, f(1) will return the value 1 and f(2) will return us the
value 4. Let us now see how to define the function f(x) in python.

.. R6

Start your ipython interpreter by typing,

.. L6

{{{ Open the terminal }}}
::

    ipython

.. R7

Let us define our function f(x)

.. L7
::

    def f(x):
    	return x*x

.. R8

Well that defined the function, so before learning what we did let us
see if it returns the expected values, try,

.. L8
::

    f(1)
    f(2)

.. R9

Yes, it returned 1 and 4 respectively. And now let us see what we did.
We wrote two lines: The first line ``def f(x)`` is used to define the
name and the parameters to the function, and the second line is used to
fix what the function is supposed to return. ``def`` is a keyword and
``f`` is the name of the function and ``x`` the parameter of the
function.

Pause the video here, try out the following exercise and resume the video.

.. L9

.. L10

{{{ Show slide with exercise 1 }}}

.. R10

 Write a python function named ``cube`` which computes the cube of
 a given number n.

.. R11

Switch to your terminal for solution.The problem can be solved as,

.. L11

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    def cube(n):
    	return n**3

.. R12

Let us check whether our function returns the cube of a number or not

.. L12
::

    cube(2) 

.. R13

It returned 8,which means we have defined our function,the right way.
And now let us see how to write functions without arguments.

let us define a new function called ``greet`` which will print ``Hello
World``.

.. L13
::

    def greet():
    	print "Hello World!"

.. R14

Now we call the function as,

.. L14
::

    greet()

.. R15

Well that is a function which takes no arguments. Also note that it is
not mandatory for a function to return values. The function ``greet``
neither takes any argument nor returns any value.

Now let us see how to write functions with more than one argument.

Pause the video here, try out the following exercise and resume the video.

.. L15

.. L16

{{{ Show slide with exercise 2 }}}

.. R16

 Write a python function named ``avg`` which computes the
 average of ``a`` and ``b``.

.. R17

Switch to your terminal for solution.

.. L17

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    def avg(a,b):
    	return (a + b)/2

.. R18

Let us test our function

.. L18
::

    avg(20, 30)

.. R19

We get the correct average, 25.
Thus if we want a function to accept more arguments, we just list them
separated with a comma between the parenthesis after the function's name
in the ``def`` line.

It is always a good practice to document the code that we write, and
for a function we define, we should write an abstract of what the
function does, and that is called a docstring. Let us modify the
function ``avg`` and add docstring to it. Do the following,

.. L19
::

    def avg(a,b):
        """ avg takes two numbers as input (a & b), and
	returns the average of a and b"""
	return (a+b)/2

.. L20

{{{ switch to next slide, docstring }}}

.. R20

Note that docstrings are entered in the immediate line after the
function definition and put as a triple quoted string. And here as far
as the code functionality is concerned, we didn't do anything. We just
added an abstract of what the function does.

.. R21

Now try this in the ipython interpreter.

.. L21

{{{ Switch to the terminal }}}
::

    avg?

.. R22

It displays the docstring as we gave it. Thus docstring is a good way
of documenting the function we write.

 Now type,

.. L22
::

    f?

.. R23

It doesn't have a docstring associated with it. Also we cannot infer
anything from the function name, and thus we are forced to read the
code to understand about the function.

Pause the video here, try out the following exercise and resume the video.

.. L23

.. L24

{{{ Show slide with exercise 3 }}}

.. R24

 Add docstring to the function f.

.. L25

{{{ Show slide with solution 3 }}}

.. R25

We need to define the function again to add docstring to the function
``f`` and we do it as,
::

    def f(x):
    	"""Accepts a number x as argument and,
	returns the square of the number x."""
	return x*x

Let us solve one more exercise
Pause the video here, try out the following exercise and resume the video.

.. L27

{{{ Show slide with exercise 4 }}}

.. R27

 Write a python function named ``circle`` which returns the
 area and perimeter of a circle given radius ``r``.

.. R28

Switch to the terminal for solution.

The problem requires us to return two values instead of one which we
were doing till now. We can solve the problem as,

.. L28

{{{ Switch to the terminal }}}
::

    def circle(r):
    	"""returns area and perimeter of a circle given radius r"""
	pi = 3.14
	area = pi * r * r
	perimeter = 2 * pi * r
	return area, perimeter

.. R29

A python function can return any number of values. There is no
restriction for it.

Let us call the function ``circle`` as,

.. L29
::

    a, p = circle(6)
    print a
    print p

.. R30

Now we have done enough coding, let us do some code reading exercise,

.. L30

{{{ switch to next slide, what }}}

.. R31

Pause here and try to figure out what the function ``what`` does.

 def what( n ):
     if n < 0: n = -n
     while n > 0:
         if n % 2 == 1:
             return False
         n /= 10
     return True

{{{continue from paused state}}}
It will return true if ``n % 2`` is not equal to 1 and will return 
false, otherwise.

.. L31

.. L32

{{{ switch to next slide, even_digits }}}

 def even_digits( n ):
     """returns True if all the digits in the number n are even,
     returns False if all the digits in the number n are not even"""
     if n < 0: n = -n
     while n > 0:
         if n % 2 == 1:
             return False
         n /= 10
     return True

.. R32

The function here returns ``True`` if all the digits of the number ``n``
are even, otherwise it returns ``False``.

Now one more code reading exercise,

.. L33

{{{ switch to next slide, what }}}

.. R33

Pause here and try to figure out what the function ``what`` does.

 def what( n ):
     i = 1
     while i * i < n:
         i += 1
     return i * i == n, i

{{{continue from paused state}}}
The function returns two values. One it returns the result of the while 
statement whether true of false, and second it prints the value that `i`` 
currently holds.

.. L34

{{{ switch to next slide, is_perfect_square }}}

 def is_perfect_square( n ):
     """returns True and square root of n, if n is a perfect square,
     otherwise returns False and the square root of the 
     next perfect square"""
     i = 1
     while i * i < n:
         i += 1
     return i * i == n, i

.. R34

Here, the function returns ``True`` and the square root of ``n`` if n is 
a perfect square, otherwise it returns ``False`` and the square root of
the next perfect square.

.. L35

{{{ switch to summary slide }}}

.. R35

This brings us to the end of this tutorial. In this tutorial,
we have learnt to,

  1. Define functions in Python by using the keyword ``def``.
  #. Call the function by specifying the function name.
  #. Assign a docstring to a function by putting it as a triple quoted 
     string.
  #. Pass parameters to a function.
  #. Return values from a function.

.. L26

{{{Show self assessment questions slide}}}

.. R36

Here are some self assessment questions for you to solve

1. What will the function do?
::

    def what(x)
        return x*x

   - Returns the square of x
   - Returns x
   - Function doesn't have docstring
   - Error	   

2. How many arguments can be passed to a python function?

   - None
   - One
   - Two
   - Any

3. Write a function which calculates the area of a rectangle.
   
.. L37

{{{solution of self assessment questions on slide}}}

.. R37

And the answers,

1. The function will result into an error due to the use of wrong 
   syntax in defining the function.The function line should always 
   end with a colon

2. Any number of arguments can be passed to a python function.

3. As we know, area of a rectangle is product of it's length and breadth.
   Hence, we define our function as,
::

    def area(l,b):
        return l * b

.. L38
  
{{{ switch to Thank you slide }}}

.. R38

Hope you have enjoyed this tutorial and found it useful.
Thank you!

