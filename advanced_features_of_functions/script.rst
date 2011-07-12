.. Objectives
.. ----------

.. At the end of this tutorial, you will be able to 

.. 1. Assign default values to arguments, when defining functions
.. 2. Define and call functions with keyword arguments. 
.. 3. Also, you will get a glimpse of the plethora of functions
.. available, in Python standard library and the scientific computing
.. libraries. 


.. Prerequisites
.. -------------

..   1. getting started with ipython
..   #. getting started with functions
     
.. Author              : Puneeth 
   Internal Reviewer   : Anoop Jacob Thomas<anoop@fossee.in>
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 'advanced features of functions'. 

.. L2

{{{ Show the objective slide }}}

.. R2

At the end of this tutorial, you will be able to, 

 1. Assign default values to arguments, when defining functions.
 #. Define and call functions with keyword arguments. 
 #. Learn some of the built-in functions available in Python standard 
    library and the scientific computing libraries.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with functions".

.. R4

Let us Start the ipython interpreter 

.. L4

{{{ Open the terminal }}}
::

    ipython -pylab.

.. R5

Let's use the ``round`` function as an example to understand what a
default value of an argument means. Let's type the following
expressions in the terminal. 

.. L5
::

    round(2.484)

    round(2.484, 2)

.. R6

Both the first expression and the second are calls to the ``round``
function, but the first calls it with only one argument and the second
calls it with two arguments. By observing the output, we can guess
that the first one is equivalent to call with the second argument
being 0. 0 .

.. L6

.. L7

{{{ show a slide with examples of functions showing default values }}}

.. R7

  s.strip() # strips on spaces. 
  s.strip('@') # strips the string of '@' symbols.

Thus it can be said that here, blank space is the default argument.

  plot(x, y) # plots with x vs. y using default line style. 
  plot(x, y, 'o') # plots x vs. y with circle markers. 

Hence, here when third argument is not provided, it shows default line style.

  linspace(0, 2*pi, 100) # returns 100 points between 0 and 2pi
  linspace(0, 2*pi) # returns 50 points between 0 and 2pi

Hence, the default for the third argument is 50.

.. R8

Let's now define a simple function that uses default arguments. We
define a simple function that prints a welcome message to a person,
given a greeting and his/her name.

.. L8

{{{ switch to terminal }}
::

    def welcome(greet, name="World"):
        print greet, name

.. R9

Let us first call the function with two arguments, one for ``greet``
and other for ``name``.

.. L9
::

    welcome("Hi", "Guido")          

.. R10

We get the expected welcome message, "Hi Guido". 

Now let us call the function with just one argument "Hello". 

.. L10
::

    welcome("Hello")

.. R11

"Hello" is treated as the ``greet`` and we get "Hello World" as
the output. "World" is the default value for the argument ``name``. 

Pause the video here, try out the following exercise and resume the video.

.. L11

.. L12

{{{ Show slide with exercise 1 }}}

.. R12

 Redefine the function ``welcome``, by interchanging it's
 arguments. Place the ``name`` argument with it's default value of
 "World" before the ``greet`` argument.

.. R13

Switch to the terminal for solution

.. L13

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    def welcome(name="World", greet):
        print greet, name

.. R14

We get an error that reads ``SyntaxError: non-default argument follows
default argument``. 

.. L14

{{{ Show slide with solution 1 }}}

.. R15

When defining a function all the argument with
default values should come at the end. 

Pause the video here, try out the following exercise and resume the video.

.. L15

.. L16

{{{ Show slide with exercise 2 }}}

.. R16

 See the definition of linspace using ``?`` and make a note of all
 the arguments with default values are towards the end.

.. R17

Switch to the terminal for solution

.. L17

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    linspace?

.. R18

As we go on hitting the enter key, we the the number of arguments this
command has.Please read the content on your terminal.
<pause>

Again, Pause the video here, try out the following exercise and resume the video.

.. L18

.. L19

{{{ Show slide with exercise 3 }}}

.. R19

 Redefine the function ``welcome`` with a default value of
 "Hello" to the ``greet`` argument. Then, call the function without any
 arguments. 

.. R20

Switch to the terminal for solution

.. L20

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    def welcome(greet="Hello", name="World"):
        print greet, name
 
    welcome()

.. R21
 
As we can see, we get the output as ``Hello World``.

Let us now learn what keyword arguments or named arguments are. We
shall refer to them as keyword arguments, henceforth. 

.. L21

.. L22

{{{ show slide keyword arguments examples }}}

  1. legend(['sin(2y)'], loc = 'center')
  #. plot(y, sin(y), 'g', linewidth = 2)
  #. annotate('local max', xy = (1.5, 1))
  #. pie(science.values(), labels = science.keys())

.. R22

When you are calling functions in Python, you don't need to remember
the order in which to pass the arguments. Instead, you can use the
name of the argument to pass it a value. This slide shows a few
function calls that use keyword arguments. ``loc``, ``linewidth``,
``xy`` and ``labels`` are being called with keyword arguments. 

Let us try and understand this better using the ``welcome`` function
that we have been using all along. Let us call it in different ways
and observe the output to see how keyword arguments work. 

.. L22

{{{ switch to ipython terminal }}}
::

    welcome()

    welcome("Hello", "James")

    welcome("Hi", name="Guido")

.. R23

When no keyword is specified, the arguments are allotted based on
their position. So, "Hi" is the value of the argument ``greet`` and
name is passed the value "Guido".If we type, 

.. L23
::

    welcome(name="Guido", greet="Hey! ")

.. R24

When keyword arguments are used, the arguments can be called in any
order. And if we call our function as,

.. L24
::

    welcome(name="Guido", "Hey")

.. R25

This call returns an error that reads, ``non-keyword arg after keyword
arg``. Python expects all the keyword to be present towards the end. 

That brings us to the end of what we wanted to learn about ``keyword``
arguments. 

.. L25

.. L26

{{{ switch to slide built-in functions }}}

.. R26

Before defining a function of your own, make sure that you check the
standard library, for a similar function. Python is popularly called a
"Batteries included" language, for the huge library that comes along
with it. 

  Math functions - abs, sin, ....
  Plot functions - plot, bar, pie ...
  Boolean functions - and, or, not ... 

.. L27
  
{{{ switch to slide showing classes of functions in pylab, scipy }}}

.. R27

Apart from the standard library there are other libraries like ``pylab``,
``scipy``, etc which have a huge collection of functions for scientific
purposes. 

  pylab
    plot, bar, contour, boxplot, errorbar, log, polar, quiver, semilog

  scipy (modules)
    fftpack, stats, linalg, ndimage, signal, optimize, integrate

.. L28

{{{ Show summary slide }}}

.. R28

This brings us to the end of this tutorial. In this tutorial, we 
have learnt to, 

 1. Define functions with default arguments.
 #. Call functions using keyword arguments.
 #. Use the range of functions available in the Python standard library 
    and the Scientific Computing related packages. 

.. L30

{{{Show self assessment questions slide}}}

.. R30

Here are some self assessment questions for you to solve

1. All arguments of a function cannot have default values. 
   - True or False? 

2. The following is a valid function definition. True or False? 
::
   
    def seperator(count=40, char, show=False):
        if show:
            print char * count
        return char * count

3. When calling a function, 

   - the arguments should always be in the order in which they are defined.
   - the arguments can be in any order.
   - only keyword arguments can be in any order, but should be called
      at the beginning.
   - only keyword arguments can be in any order, but should be called
     at the end.

.. L31

{{{solution of self assessment questions on slide}}}

.. R31

And the answers,

1. Flase.All arguments of a Python function can have default values.

2. False. All parameters with default arguments should be
   defined at the end. 

3. When calling a function,only keyword arguments can be in any order, 
   but should be called at the end. 

.. L32

{{{ Show the Thankyou slide }}}

.. R32

Hope you have enjoyed this tutorial and found it useful.
Thank you!

