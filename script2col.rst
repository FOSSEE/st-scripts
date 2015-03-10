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



+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the  first slide containing title, name of the production               | Hello Friends and Welcome to the spoken tutorial on                              |
| team along with the logo of MHRD }}}                                             | 'Using Python Modules'.                                                          |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ switch to objectives slide }}}                                               | At the end of this tutorial, you will be able to ,                               |
|                                                                                  |                                                                                  |
|                                                                                  |  1. Execute python scripts from command line.                                    |
|                                                                                  |  #. Use import in scripts.                                                       |
|                                                                                  |  #. Import scipy and pylab modules.                                              |
|                                                                                  |  #. Use python standard modules and 3rd party modules.                           |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Switch to the pre-requisite slide }}}                                        | Before beginning this tutorial,we would suggest you to complete the              |
|                                                                                  | tutorial on "Using plot interactively", "Embellishing a plot" and                |
|                                                                                  | "Saving plots".                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ switch to next slide on running python scripts from                          |                                                                                  |
| command line }}}                                                                 |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
|                                                                                  | Let us create a simple python script to print hello world. Open your             |
|                                                                                  | text editor and type the following,                                              |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ open the text editor and type the following }}}                              |                                                                                  |
| ::                                                                               |                                                                                  |
|                                                                                  |                                                                                  |
|     print "Hello world!"                                                         |                                                                                  |
|     print                                                                        |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ save the script as hello.py }}}                                              | Now save this script as ``hello.py``,                                            |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Open the terminal }}}                                                        | Start the ipython interpreter                                                    |
| ::                                                                               |                                                                                  |
|                                                                                  |                                                                                  |
|     ipython                                                                      |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | In the previous tutorials,we have seen how to run a script using                 |
|                                                                                  | the IPython interpreter using ``%run``                                           |
|     %run -i hello.py                                                             |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Close the terminal }}}                                                       | but this is not the correct way of running a python                              |
|                                                                                  | script.                                                                          |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ open terminal and navigate to directory where hello.py was saved }}}         | The correct method is to run it using the Python interpreter. Open the           |
|                                                                                  | terminal and navigate to the directory where hello.py is,                        |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | now run the Python script as,                                                    |
|                                                                                  |                                                                                  |
|     python hello.py                                                              |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
|                                                                                  | It executed the script and we got the output ``Hello World!``.                   |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ switch to next slide }}}                                                     | The syntax is ``python space filename``.                                         |
| {{{ highlight ``python filename`` syntax on slide while narrating }}}            |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ switch to next slide, four plot problem }}}                                  | Now, we have a four plot problem where we have plotted four plots in a           |
|                                                                                  | single figure. Let us run that script from command line.                         |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ open the four_plot.py file in text editor and show }}}                       | If you don't have the script, then make one with the following set of            |
| {{{ Pause for some time and then continue }}}                                    | commands                                                                         |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | Now let us run four_plot.py as a python script.                                  |
|                                                                                  |                                                                                  |
|     python four_plot.py                                                          |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
|                                                                                  | Oops! even though it was supposed to work, it didn't. It gave an error           |
|                                                                                  | ``linspace()`` is not defined, which means that the function                     |
|                                                                                  | ``linspace()`` is not available in the current name-space.                       |
|                                                                                  |                                                                                  |
|                                                                                  | But if you try to run the same script using ``%run -i four_plot.py``             |
|                                                                                  | in your IPython interpreter started with the option ``-pylab`` it will           |
|                                                                                  | work, because the ``-pylab`` option does some work for us by importing           |
|                                                                                  | the required modules to our name-space when ipython interpreter                  |
|                                                                                  | starts. And thus we don't have to explicitly import modules.                     |
|                                                                                  |                                                                                  |
|                                                                                  | So now let us try to fix the problem and run the script in command               |
|                                                                                  | line,                                                                            |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ switch to next slide, fix ``linspace`` problem }}}                           | add this line as the first line in the script,                                   |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ add the line as first line in four_plot.py and save }}}                      |                                                                                  |
| ::                                                                               |                                                                                  |
|                                                                                  |                                                                                  |
|     from scipy import *                                                          |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | Now let us run the script again,                                                 |
|                                                                                  |                                                                                  |
|     python four_plot.py                                                          |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
|                                                                                  | Now it gave another error -- plot not defined,                                   |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ switch to next slide, thank you slide }}}                                    | let us edit the file again and add this line as the                              |
|                                                                                  | second line in our script and save it,                                           |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ add the line as second line in four_plot.py and save }}}                     |                                                                                  |
| ::                                                                               |                                                                                  |
|                                                                                  |                                                                                  |
|     from pylab import *                                                          |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Switch to the terminal }}}                                                   | And now, run the script,                                                         |
| ::                                                                               |                                                                                  |
|                                                                                  |                                                                                  |
|     python four_plot.py                                                          |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
|                                                                                  | Yes! it worked. So what did we do?                                               |
|                                                                                  |                                                                                  |
|                                                                                  | We actually imported the required modules using the keyword ``import``.          |
|                                                                                  | It could also be done as by using,                                               |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ switch to next slide, better way of fixing }}}                               | from scipy import linspace                                                       |
| {{{ highlight the required line while narrating }}}                              |                                                                                  |
|                                                                                  | instead of,                                                                      |
|                                                                                  |                                                                                  |
|                                                                                  |     from scipy import *                                                          |
|                                                                                  |                                                                                  |
|                                                                                  | So in practice it is always good to use function names instead of                |
|                                                                                  | asterisk or star. If we use asterisk to import from a particular                 |
|                                                                                  | module then it will replace any existing functions with the same name            |
|                                                                                  | in our name-space.                                                               |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ switch to next slide, Instead of ``*`` }}}                                   | So let us modify four_plot.py as,                                                |
|                                                                                  | Hence we delete the first two lines of our code which we had added               |
|                                                                                  | and add these lines                                                              |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Switch to script 'four_plot.py' }}}                                          |                                                                                  |
| {{{ delete the first two lines and add the following }}}                         |                                                                                  |
| ::                                                                               |                                                                                  |
|                                                                                  |                                                                                  |
|     from scipy import linspace, pi, sin                                          |                                                                                  |
|     from pylab import plot, legend, annotate                                     |                                                                                  |
|     from pylab import xlim, ylim, title, show                                    |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | Now let us try running the code again as,                                        |
|                                                                                  |                                                                                  |
|     python four_plot.py                                                          |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
|                                                                                  | It works! In this method we actually imported the functions to the               |
|                                                                                  | current name-space.There is one more way of doing it. And that                   |
|                                                                                  | is,                                                                              |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ switch to slide 'another fix' }}}                                            | Notice that we use ``scipy.pi`` instead of just ``pi`` as in the                 |
| {{{ highlight the required line while narrating }}}                              | previous method, and the functions are called as ``pylab.plot()`` and            |
|                                                                                  | ``pylab.annotate()`` and not as ``plot()`` and ``annotate()``.                   |
|                                                                                  |                                                                                  |
|                                                                                  | Pause the video here, try out the following exercise and resume the video.       |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show slide with exercise 1 }}}                                               | Write a script to plot a sine wave from minus two pi to two pi.                  |
|                                                                                  | <Pause>                                                                          |
|                                                                                  | It can solved as,                                                                |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ open sine.py and show it }}}                                                 | The first line we import the required functions ``linspace()`` ,                 |
|                                                                                  | ``sin()`` and constant ``pi`` from the module scipy. The second and              |
|                                                                                  | third line we import the functions ``plot()``, ``legend()``,                     |
|                                                                                  | ``show()``, ``title()``, ``xlabel()`` and ``ylabel()``. And the rest             |
|                                                                                  | the code to generate the plot.                                                   |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Pause for sometime and then continue }}}                                     |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Switch to the terminal }}}                                                   | We can run it as,                                                                |
| ::                                                                               |                                                                                  |
|                                                                                  |                                                                                  |
|     python sine.py                                                               |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
|                                                                                  | As we can see, we our sine plot.Let us move further in our topic.                |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ switch to next slide, What is a module? }}}                                  | Until now we have been learning about importing modules, now what is a           |
|                                                                                  | module?                                                                          |
|                                                                                  |                                                                                  |
|                                                                                  | A module is simply a file containing Python definitions and                      |
|                                                                                  | statements. Definitions from a module can be imported into other                 |
|                                                                                  | modules or into the main module.                                                 |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ switch to next slide, Python standard library }}}                            | Python has a very rich standard library of modules. It is very                   |
|                                                                                  | extensive, offering a wide range of facilities. Some of the standard             |
|                                                                                  | modules are,                                                                     |
|                                                                                  |                                                                                  |
|                                                                                  | for Math: math, random                                                           |
|                                                                                  | for Internet access: urllib2, smtplib                                            |
|                                                                                  | for System, Command line arguments: sys                                          |
|                                                                                  | for Operating system interface: os                                               |
|                                                                                  | for regular expressions: re                                                      |
|                                                                                  | for compression: gzip, zipfile, tarfile                                          |
|                                                                                  | And there are lot more.                                                          |
|                                                                                  |                                                                                  |
|                                                                                  | Find more information at Python Library reference,                               |
|                                                                                  | ``http://docs.python.org/library/``                                              |
|                                                                                  |                                                                                  |
|                                                                                  | There are a lot of other modules like pylab, scipy, Mayavi, etc which            |
|                                                                                  | are not part of the standard python library.                                     |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ switch to next slide, summary }}}                                            | This brings us to the end of this tutorial. In this tutorial, we have            |
|                                                                                  | learnt to,                                                                       |
|                                                                                  |                                                                                  |
|                                                                                  |  1. Run scripts from command line,                                               |
|                                                                                  |  #. Import modules by specifying the module name followed by                     |
|                                                                                  |     an asterisk.                                                                 |
|                                                                                  |  #. Import only the required functions from modules by specifying                |
|                                                                                  |     the function name.                                                           |
|                                                                                  |  #. Use python standard library.                                                 |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Show self assessment questions slide}}}                                       | Here are some self assessment questions for you to solve                         |
|                                                                                  |                                                                                  |
|                                                                                  | 1. Which among this is correct ?                                                 |
|                                                                                  |                                                                                  |
|                                                                                  |    - from scipy import plot                                                      |
|                                                                                  |    - from numpy import plot                                                      |
|                                                                                  |    - from matplotlib import plot                                                 |
|                                                                                  |    - from pylab import plot                                                      |
|                                                                                  |                                                                                  |
|                                                                                  | 2. Which among these libraries is part of python standard library ?              |
|                                                                                  |                                                                                  |
|                                                                                  |    - Mayavi                                                                      |
|                                                                                  |    - scipy                                                                       |
|                                                                                  |    - matplotlib                                                                  |
|                                                                                  |    - urllib2                                                                     |
|                                                                                  |                                                                                  |
|                                                                                  | 3. Functions ``xlim()`` and ``ylim()`` can be imported to the current            |
|                                                                                  |    name-space as,                                                                |
|                                                                                  |                                                                                  |
|                                                                                  |    - from pylab import xlim, ylim                                                |
|                                                                                  |    - import pylab                                                                |
|                                                                                  |    - from scipy import xlim, ylim                                                |
|                                                                                  |    - import scipy                                                                |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{solution of self assessment questions on slide}}}                             | And the answers,                                                                 |
|                                                                                  |                                                                                  |
|                                                                                  | 1. The option ``from pylab import plot`` is the correct one, since plot          |
|                                                                                  |    is a function of module module.                                               |
|                                                                                  |                                                                                  |
|                                                                                  | 2. ``urllib2`` is a part of the python standard library.                         |
|                                                                                  |                                                                                  |
|                                                                                  | 3. Functions ``xlim()`` and ``ylim()`` can be imported to the current            |
|                                                                                  |    name-space as, ``from pylab import xlim, ylim``.                              |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
|                                                                                  | Hope you have enjoyed this tutorial and found it useful.                         |
|                                                                                  | Thank you!                                                                       |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
