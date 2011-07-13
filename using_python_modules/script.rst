.. Objectives
.. ----------

.. At the end of this tutorial, you will be able to 

.. 1. Execute python scripts from command line.
.. #. Use import in scripts.
.. #. Import scipy and pylab modules
.. #. Use python standard modules and 3rd party modules.


.. Prerequisites
.. -------------

..   1. should have ``pylab`` installed. 
..   #. using plot command interactively.
..   #. embellishing a plot.
..   #. saving plots.
     
.. Author              : Anoop Jacob Thomas <anoop@fossee.in>
   Internal Reviewer   : Puneeth
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <11-11-2010, Anand, OK> [2010-10-05]


====================
Using Python modules
====================

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello Friends and Welcome to the spoken tutorial on 
'Using Python Modules'.

.. L2

{{{ switch to objectives slide }}}

.. R2

At the end of this tutorial, you will be able to ,

 1. Execute python scripts from command line.
 #. Use import in scripts.
 #. Import scipy and pylab modules.
 #. Use python standard modules and 3rd party modules.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Using plot interactively", "Embellishing a plot" and 
"Saving plots".

.. L4

{{{ switch to next slide on running python scripts from 
command line }}}

.. R5

Let us create a simple python script to print hello world. Open your
text editor and type the following,

.. L6

{{{ open the text editor and type the following }}}
::

    print "Hello world!"
    print

.. R6

.. R7

Now save this script as ``hello.py``,

.. L7

{{{ save the script as hello.py }}}

.. R8

Start the ipython interpreter

.. L8

{{{ Open the terminal }}}
::

    ipython

.. R9

In the previous tutorials,we have seen how to run a script using 
the IPython interpreter using ``%run``

.. L9
::

    %run -i hello.py

.. R10

but this is not the correct way of running a python
script. 

.. L10

{{{ Close the terminal }}}

.. R11

The correct method is to run it using the Python interpreter. Open the
terminal and navigate to the directory where hello.py is,

.. L11

{{{ open terminal and navigate to directory where hello.py was saved }}}

.. R12

now run the Python script as,

.. L12
::

    python hello.py

.. R13

It executed the script and we got the output ``Hello World!``.

.. L13

.. L14

{{{ switch to next slide }}}
{{{ highlight ``python filename`` syntax on slide while narrating }}}

.. R14

The syntax is ``python space filename``.

.. L15

{{{ switch to next slide, four plot problem }}}

.. R15

Now, we have a four plot problem where we have plotted four plots in a 
single figure. Let us run that script from command line.

.. R16

If you don't have the script, then make one with the following set of 
commands

.. L16

{{{ open the four_plot.py file in text editor and show }}}
{{{ Pause for some time and then continue }}}

.. R17

Now let us run four_plot.py as a python script.

.. L17
::

    python four_plot.py

.. R18

Oops! even though it was supposed to work, it didn't. It gave an error
``linspace()`` is not defined, which means that the function
``linspace()`` is not available in the current name-space.

But if you try to run the same script using ``%run -i four_plot.py``
in your IPython interpreter started with the option ``-pylab`` it will
work, because the ``-pylab`` option does some work for us by importing
the required modules to our name-space when ipython interpreter
starts. And thus we don't have to explicitly import modules.

So now let us try to fix the problem and run the script in command
line,

.. L18

.. L19

{{{ switch to next slide, fix ``linspace`` problem }}}

.. R19

add this line as the first line in the script,

.. L20

{{{ add the line as first line in four_plot.py and save }}}
::

    from scipy import *

.. R20

.. R21

Now let us run the script again,

.. L21
::

    python four_plot.py

.. R22

Now it gave another error -- plot not defined, 

.. L22

.. L23

{{{ switch to next slide, fix ``plot`` problem }}}

.. R23

let us edit the file again and add this line as the 
second line in our script and save it,

.. L24

{{{ add the line as second line in four_plot.py and save }}}
::

    from pylab import *

.. R24

.. R25

And now, run the script,

.. L25

{{{ Switch to the terminal }}}
::

    python four_plot.py

.. R26

Yes! it worked. So what did we do?

We actually imported the required modules using the keyword ``import``.
It could also be done as by using,

.. L26

.. L27

{{{ switch to next slide, better way of fixing }}}
{{{ highlight the required line while narrating }}}

.. R27

    from scipy import linspace

instead of,

    from scipy import *

So in practice it is always good to use function names instead of
asterisk or star. If we use asterisk to import from a particular
module then it will replace any existing functions with the same name
in our name-space.

.. L28

{{{ switch to next slide, Instead of ``*`` }}}

.. R28

So let us modify four_plot.py as,
Hence we delete the first two lines of our code which we had added
and add these lines

.. L29

{{{ Switch to script 'four_plot.py' }}}
{{{ delete the first two lines and add the following }}}
::

    from scipy import linspace, pi, sin
    from pylab import plot, legend, annotate
    from pylab import xlim, ylim, title, show

.. R29

.. R30

Now let us try running the code again as,

.. L30
::

    python four_plot.py

.. R31

It works! In this method we actually imported the functions to the
current name-space.There is one more way of doing it. And that
is,

.. L31

.. L32

{{{ switch to slide 'another fix' }}}
{{{ highlight the required line while narrating }}}

.. R32

Notice that we use ``scipy.pi`` instead of just ``pi`` as in the
previous method, and the functions are called as ``pylab.plot()`` and
``pylab.annotate()`` and not as ``plot()`` and ``annotate()``.

Pause the video here, try out the following exercise and resume the video.

.. L33

{{{ Show slide with exercise 1 }}}

.. R33

 Write a script to plot a sine wave from minus two pi to two pi.
<Pause>
It can solved as,

.. L34

{{{ open sine.py and show it }}}

.. R34

The first line we import the required functions ``linspace()`` ,
``sin()`` and constant ``pi`` from the module scipy. The second and
third line we import the functions ``plot()``, ``legend()``,
``show()``, ``title()``, ``xlabel()`` and ``ylabel()``. And the rest
the code to generate the plot.

.. L35

{{{ Pause for sometime and then continue }}}

.. R35

.. R36

We can run it as,

.. L36

{{{ Switch to the terminal }}}
::

    python sine.py

.. R37

As we can see, we our sine plot.Let us move further in our topic.

.. L37

.. L38

{{{ switch to next slide, What is a module? }}}

.. R38

Until now we have been learning about importing modules, now what is a
module?

A module is simply a file containing Python definitions and
statements. Definitions from a module can be imported into other
modules or into the main module.

.. L39

{{{ switch to next slide, Python standard library }}}

.. R39

Python has a very rich standard library of modules. It is very
extensive, offering a wide range of facilities. Some of the standard
modules are,

for Math: math, random
for Internet access: urllib2, smtplib
for System, Command line arguments: sys
for Operating system interface: os
for regular expressions: re
for compression: gzip, zipfile, tarfile
And there are lot more.

Find more information at Python Library reference,
``http://docs.python.org/library/``

There are a lot of other modules like pylab, scipy, Mayavi, etc which
are not part of the standard python library.

.. L40

{{{ switch to next slide, summary }}}

.. R40

This brings us to the end of this tutorial. In this tutorial, we have
learnt to,

 1. Run scripts from command line, 
 #. Import modules by specifying the module name followed by  
    an asterisk. 
 #. Import only the required functions from modules by specifying 
    the function name.
 #. Use python standard library.

.. L41

{{{Show self assessment questions slide}}}

.. R41

Here are some self assessment questions for you to solve

1. Which among this is correct ? 

   - from scipy import plot
   - from numpy import plot
   - from matplotlib import plot
   - from pylab import plot
   
2. Which among these libraries is part of python standard library ?

   - Mayavi
   - scipy
   - matplotlib
   - urllib2

3. Functions ``xlim()`` and ``ylim()`` can be imported to the current
   name-space as,

   - from pylab import xlim, ylim
   - import pylab
   - from scipy import xlim, ylim
   - import scipy

.. L42

{{{solution of self assessment questions on slide}}}

.. R42

And the answers,

1. The option ``from pylab import plot`` is the correct one, since plot 
   is a function of module module.

2. ``urllib2`` is a part of the python standard library.

3. Functions ``xlim()`` and ``ylim()`` can be imported to the current
   name-space as, ``from pylab import xlim, ylim``.

.. L23

{{{ switch to next slide, thank you slide }}}

.. R43

Hope you have enjoyed this tutorial and found it useful.
Thank you!
