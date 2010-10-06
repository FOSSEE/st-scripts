========
 Script
========

{{{ show the welcome slide }}}

Welcome to the tutorial on advanced feature of functions. 

{{{ show the outline slide }}}

In this tutorial we shall be looking at specifying default arguments
to functions when defining them and calling functions using keyword
arguments. We shall also, look at some of the built-in functions
available in the standard library of Python.

{{{ switch to terminal }}}

We have an ``ipython`` terminal open, which we shall be using through
out this session. 

Let's use the ``round`` function as an example to understand what a
default value of an argument means. Let's type the following
expressions in the terminal. 

::

  round(2.484)

  round(2.484, 2)

Both the first expression and the second are calls to the ``round``
function, but the first calls it with only one argument and the second
calls it with two arguments. By observing the output, we can guess
that the first one is equivalent to call with the second argument
being 0. 0 is the default value of the argument. 

{{{ show a slide with examples of functions showing default values }}}
::

  s.strip() # strips on spaces. 
  s.strip('@') # strips the string of '@' symbols.

  plot(x, y) # plots with x vs. y using default line style. 
  plot(x, y, 'o') # plots x vs. y with circle markers. 

  linspace(0, 2*pi, 100) # returns 100 points between 0 and 2pi
  linspace(0, 2*pi) # returns 50 points between 0 and 2pi

#[punch: all above content goes on to a slide]

{{{ switch back to ipython }}}

Let's now define a simple function that uses default arguments. We
define a simple function that prints a welcome message to a person,
given a greeting and his/her name.

::

  def welcome(greet, name="World"):
      print greet, name

Let us first call the function with two arguments, one for ``greet``
and other for ``name``.

::

  welcome("Hi", "Guido")          

We get the expected welcome message, "Hi Guido". 

Now let us call the function with just one argument "Hello". 
::

  welcome("Hello")

"Hello" is treated as the ``greet`` and we get "Hello World" as
the output. "World" is the default value for the argument ``name``. 

E%% %% Pause the video here and redefine the function ``welcome``, by
interchanging it's arguments. Place the ``name`` argument with it's
default value of "Hello" before the ``greet`` argument. Then, resume
the video. 

::

  def welcome(name="World", greet):
      print greet, name

We get an error that reads ``SyntaxError: non-default argument follows
default argument``. When defining a function all the argument with
default values should come at the end. 

E%% %% Pause the video here and type ``linspace?`` to see the
definition of the command and notice how all the arguments with
default values are towards the end.

::

  linspace?

E%% %% Pause the video here and redefine the function ``welcome`` with
a default value of "Hello" to the ``greet`` argument. Then, call the
function without any arguments. Then, resume the video. 

::

  def welcome(greet="Hello", name="World"):
      print greet, name
 

  welcome()


Let us now learn what keyword arguments are. 

{{{ show a slide with examples using keyword arguments. }}}
::

  legend(['sin(2y)'], loc = 'center')

  plot(y, sin(y), 'g', linewidth = 2)

  annotate('local max', xy = (1.5, 1))

  pie(science.values(), labels = science.keys())

When you are calling functions in Python, you don't need to remember
the order in which to pass the arguments. Instead, you can use the
name of the argument to pass it a value. This slide shows a few
function calls that use keyword arguments. ``loc``, ``linewidth``,
``xy`` and ``labels`` are being called with keyword arguments. 

{{{ switch to ipython terminal }}}

Let us try and understand this better using the ``welcome`` function
that we have been using all along. Let us call it in different ways
and observe the output to see how keyword arguments work. 

::

  welcome()

  welcome("Hello", "James")

  welcome("Hi", name="Guido")

When no keyword is specified, the arguments are allotted based on
their position. So, "Hi" is the value of the argument ``greet`` and
name is passed the value "Guido". 
::

  welcome(name="Guido", greet="Hey! ")

When keyword arguments are used, the arguments can be called in any
order. 

::

  welcome(name="Guido", "Hey")

This call returns an error that reads, ``non keyword arg after keyword
arg``. Python expects all the keyword to be present towards the end. 

That brings us to the end of what we wanted to learn about ``keyword``
arguments. 

{{{ switch to a slide showing variety of functions with uses }}}

Before defining a function of your own, make sure that you check the
standard library, for a similar function. Python is popularly called a
"Batteries included" language, for the huge library that comes along
with it. 

::

  Math functions - abs, sin, ....

#[punch: Need to decide, exactly what to put here. Reviewer comments
 welcome.] 
  

{{{ switch to slide showing classes of functions in pylab, scipy }}}

Apart from the standard library there are other libraries like ``pylab``,
``scipy``, etc which have a huge collection of functions for scientific
purposes. 
::

  pylab
    plot, bar, contour, boxplot, errorbar, log, polar, quiver, semilog

  scipy (modules)
    fftpack, stats, linalg, ndimage, signal, optimize, integrate

{{{ switch slide to summary slide }}}

That brings us to the end of this tutorial. In this tutorial we have
learnt how to use functions with default values and keyword
arguments. We also looked at the range of functions available in the
Python standard library and the Scientific Computing related
packages. 

Thank You!
