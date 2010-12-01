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
{{{ show the welcome slide }}}

Welcome to the spoken tutorial on Using Python Modules.

{{{ switch to next slide, outline slide }}}

In this tutorial, we will see how to run python scripts from command
line. We'll see how to import modules, importing scipy and pylab
modules and have a look at the Python standard library.

{{{ switch to next slide on executing python scripts from command line }}}

Let us create a simple python script to print hello world. Open your
text editor and type the following,

{{{ open the text editor and type the following }}}
::

    print "Hello world!"
    print

and save the script as ``hello.py``,

{{{ save the script as hello.py }}}

Till now we saw how to run a script using the IPython interpreter
using the
::

    %run -i hello.py

option, but that is not the correct way of running a python
script. 

The correct method is to run it using the Python interpreter. Open the
terminal and navigate to the directory where hello.py is,

{{{ open terminal and navigate to directory where hello.py was saved }}}

{{{ switch to next slide }}}

now run the Python script as,
::

    python hello.py

It executed the script and we got the output ``Hello World!``.

{{{ highlight ``python filename`` syntax on slide while narrating }}}

The syntax is python space filename.

{{{ switch to next slide, four plot problem }}}

Now recall the four plot problem where we plotted four plots in a single
figure. Let us run that script from command line.

If you don't have the script, 

{{{ open the four_plot.py file in text editor }}}

just pause here and create a python script with the following lines
and save it as four_plot.py.

Now let us run four_plot.py as a python script.
::

    python four_plot.py

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

{{{ switch to next slide, fix ``linspace`` problem }}}

add the following line as the first line in the script,
{{{ add the line as first line in four_plot.py and save }}}
::

    from scipy import *

Now let us run the script again,
::

    python four_plot.py

Now it gave another error -- plot not defined, let us edit the file
again and add the line below the line we just added,

{{{ switch to next slide, fix ``plot`` problem }}}

{{{ add the line as second line in four_plot.py and save }}}
::

    from pylab import *

And run the script,
::

    python four_plot.py

Yes! it worked. So what did we do?

We actually imported the required modules using the keyword ``import``.
It could have also be done as,

{{{ switch to next slide, better way of fixing }}}

{{{ highlight the following in slide and say it loud }}}
::

    from scipy import linspace

instead of,
::

    from scipy import *

So in practice it is always good to use function names instead of
asterisk or star. If we use asterisk to import from a particular
module then it will replace any existing functions with the same name
in our name-space.

{{{ switch to next slide, Instead of ``*`` }}}

So let us modify four_plot.py as,
{{{ delete the first two lines and add the following }}}
::

    from scipy import linspace, pi, sin
    from pylab import plot, legend, annotate
    from pylab import xlim, ylim, title, show

Now let us try running the code again as,
::

    python four_plot.py

It works! In this method we actually imported the functions to the
current name-space, and there is another method of doing it. And that
is,

{{{ switch to next slide }}}

Notice that we use ``scipy.pi`` instead of just ``pi`` as in the
previous method, and the functions are called as ``pylab.plot()`` and
``pylab.annotate()`` and not as ``plot()`` and ``annotate()``.

{{{ switch to next slide, problem statement }}}

%% %% Write a script to plot a sine wave from minus two pi to two pi.

Pause here and try to solve the problem yourself before looking at the
solution.

It can solved as,

{{{ open sine.py and show it }}}

the first line we import the required functions ``linspace()`` and
``sin()`` and constant ``pi`` from the module scipy. the second and
third line we import the functions ``plot()``, ``legend()``,
``show()``, ``title()``, ``xlabel()`` and ``ylabel()``. And the rest
the code to generate the plot.

We can run it as,
{{{ now switch focus to terminal and run the script }}}
::

    python sine.py

{{{ switch to next slide, What is a module? }}}

Until now we have been learning about importing modules, now what is a
module?

A module is simply a file containing Python definitions and
statements. Definitions from a module can be imported into other
modules or into the main module.

{{{ switch to next slide, Python standard library }}}

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

{{{ switch to next slide, summary }}}

This brings us to the end of this tutorial, in this tutorial we
learned running scripts from command line, learned about modules, saw
the python standard library.

{{{ switch to next slide, thank you slide }}}

Thank you!
