.. Objectives
.. ----------

.. 8.1 LO: getting started with functions (3)

.. At the end of this tutorial, you will be able to 

.. 1. define function
.. #. define functions with arguments
.. #. learn about docstrings
.. #. learn about return values
..     can return multiple values
.. #. read code


.. Prerequisites
.. -------------

..   1. should have ``ipython`` installed. 
..   #. getting started with ``ipython``.

     
.. Author              : Anoop Jacob Thomas <anoop@fossee.in>
   Internal Reviewer   : 
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <put date stamp here, not OK> [2010-10-05]


==============================
Getting started with functions
==============================

{{{ show welcome slide }}}

Hello and welcome to the tutorial getting started with functions.

{{{ switch to next slide, outline slide }}}

In this tutorial we will learn about functions in python, how to
define functions, arguments to functions, docstrings, and function
return value.

{{{ switch to next slide, Function }}}

While writing code, we always want to reduce the number of lines of
code and functions is a way of reusing the code. Thus the same lines
of code can be used as many times as needed. A function is a portion of code
within a larger program that performs a specific task and is
relatively independent of the remaining code. Now let us get more
familiar with functions,

{{{ switch to next slide, f(x) a mathematical function }}}

Consider a mathematical function f(x) = x square. Here x is a variable
and with different values of x the value of function will change. When
x is one f(1) will return the value 1 and f(2) will return us the
value 4. Let us now see how to define the function f(x) in python.

{{{ switch to next slide, define f(x) in Python }}}

In your Ipython interpreter type the following,
::

    def f(x):
    	return x*x

Well that defined the function, so before learning what we did let us
see if it returns the expected values, try,
::

    f(1)
    f(2)

Yes, it returned 1 and 4 respectively. And now let us see what we did.
We wrote two lines: The first line ``def f(x)`` is used to define the
name and the parameters to the function and the second line is used to
fix what the function is supposed to return. ``def`` is a keyword and
``f`` is the name of the function and ``x`` the parameter of the
function.

{{{ switch to next slide, problem statement 1 }}}

%% 1 %% Write a python function named cube which computes the cube of
   a given number n.

Pause here and try to solve the problem yourself.

{{{ switch to next slide, solution }}}

The problem can be solved as,
::

    def cube(n):
    	return n**3

And now let us see how to write functions without arguments.

{{{ switch to next slide, greet function }}}

let us define a new function called ``greet`` which will print ``Hello
World``.
::

    def greet():
    	print "Hello World!"

now try calling the function,
::

    greet()

Well that is a function which takes no arguments. Also note that it is
not mandatory for a function to return values. The function ``greet``
neither takes any argument nor returns any value.

Now let us see how to write functions with more than one argument.

{{{ switch to next slide, exercise 2 }}}

%% 2 %% Write a python function named ``avg`` which computes the
   average of ``a`` and ``b``.

Pause here and try to solve the problem yourself.

{{{ switch to next slide, solution 2 }}}

The problem can be solved as,
::

    def avg(a,b):
    	return (a + b)/2

Thus if we want a function to accept more arguments, we just list them
separated with a comma between the parenthesis after the function's name
in the ``def`` line.

{{{ switch to next slide, docstring }}}

It is always a good practice to document the code that we write, and
for a function we define we should write an abstract of what the
function does, and that is called a docstring. Let us modify the
function ``avg`` and add docstring to it. Do the following,
::

    def avg(a,b):
        """ avg takes two numbers as input (a & b), and
	returns the average of a and b"""
	return (a+b)/2

Note that docstrings are entered in the immediate line after the
function definition and put as a triple quoted string. And here as far
as the code functionality is concerned, we didn't do anything. We just
added an abstract of what the function does.

Now try this in the ipython interpreter.
::

    avg?

It displays the docstring as we gave it. Thus docstring is a good way
of documenting the function we write.

Try to do this,
::

    f?

It doesn't have a docstring associated with it. Also we cannot infer
anything from the function name, and thus we are forced to read the
code to understand about the function.

{{{ switch to next slide, exercise 3 }}}

%% 3 %% Add docstring to the function f.

Pause here and try to do it yourself.

{{{ switch to next slide, solution }}}

We need to define the function again to add docstring to the function
``f`` and we do it as,
::

    def f(x):
    	"""Accepts a number x as argument and,
	returns the square of the number x."""
	return x*x

{{{ switch to next slide, exercise 4 }}}

%% 4 %% Write a python function named ``circle`` which returns the
   area and perimeter of a circle given radius ``r``.

Pause here and try to solve the problem yourself.

{{{ switch to next slide, solution 4 }}}

The problem requires us to return two values instead of one which we
were doing till now. We can solve the problem as,
::

    def circle(r):
    	"""returns area and perimeter of a circle given radius r"""
	pi = 3.14
	area = pi * r * r
	perimeter = 2 * pi * r
	return area, perimeter

A python function can return any number of values. There is no
restriction for it.

Let us call the function ``circle`` as,
::

    a, p = circle(6)
    print a
    print p

Now we have done enough coding, let us do some code reading exercise,

{{{ switch to next slide, what }}}

What does the function ``what`` do?

.. def what( n ):
..     if n < 0: n = -n
..     while n > 0:
..         if n % 2 == 1:
..             return False
..         n /= 10
..     return True

Pause here and try to figure out what the function ``what`` does.

{{{ switch to next slide, even_digits }}}

.. def even_digits( n ):
..    """returns True if all the digits in the number n are even,
..    returns False if all the digits in the number n are not even"""
..     if n < 0: n = -n
..     while n > 0:
..         if n % 2 == 1:
..             return False
..         n /= 10
..     return True

The function returns ``True`` if all the digits of the number ``n``
are even, otherwise it returns ``False``.

Now one more code reading exercise,

{{{ switch to next slide, what }}}

What does the function ``what`` do?

.. def what( n ):
..     i = 1
..     while i * i < n:
..         i += 1
..     return i * i == n, i

Pause here and try to figure out what the function ``what`` does.

{{{ switch to next slide, is_perfect_square }}}

.. def is_perfect_square( n ):
..     """returns True and square root of n, if n is a perfect square,
..     otherwise returns False and the square root of the 
..     next perfect square"""
..     i = 1
..     while i * i < n:
..         i += 1
..     return i * i == n, i


The function returns ``True`` and the square root of ``n`` if n is a
perfect square, otherwise it returns ``False`` and the square root of
the next perfect square.

This brings us to the end of this tutorial, in this tutorial we covered

{{{ switch to next slide, summary }}}

- Functions in Python
- Passing parameters to a function
- Returning values from a function

We also did few code reading exercises.

{{{ switch to next slide, Thank you }}}

Thank you!
