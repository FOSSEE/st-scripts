.. Objectives
.. ----------

.. At the end of this tutorial, you will be able to 

.. 1. Create scatter plot
.. #. Create pie charts
.. #. Create bar charts
.. #. Create log-log plots.

.. Prerequisites
.. -------------

..   1. should have ``ipython`` and ``pylab`` installed. 
..   #. getting started with ``ipython``.
..   #. loading data from files
..   #. plotting the data

     
.. Author              : Anoop Jacob Thomas <anoop@fossee.in>
   Internal Reviewer   : Puneeth
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <10-11-2010, Anand, OK> [2010-10-05]


===================
Types of plots
===================

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello Friends and welcome to the tutorial on ``Types of plots``.

.. L2

{{{ Show slide with objectives }}}

.. R2

Till now we have seen only one kind of plotting.Hence in this tutorial 
we will be looking atn some more kinds of plots. 

At the end of this tutorial, you will be able to 

 1. Create scatter plot
 #. Create pie charts
 #. Create bar charts
 #. Create log-log plots
 #. Use the matplotlib help

.. L3

{{{ Show slide with pre-requisite }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Loading data from files" and "Plotting data".

.. R4

Before we start with the topic, let us start our IPython interpreter

.. L4

{{{ open the ipython interpreter in the terminal using the command
ipython -pylab }}}
::

    ipython -pylab

.. L5

{{{ switch to the next slide, scatter plot }}}

.. R5

In a scatter plot, the data is displayed as a collection of points,
where each point determines it's position on the horizontal axis and the 
vertical axis respectively.This kind of plot is also called a
scatter chart, a scatter diagram or a scatter graph.
Let us now generate a scatter plot with the help of an exercise

.. L6

{{{ switch to the slide having exercise 1 }}}

.. R6

Plot a scatter plot showing the percentage profit of
a company A from the year 2000-2010. The data for the same is available
in the file ``company-a-data.txt``.

.. L7

{{{ open the file company-a-data.txt and show the content }}}

.. R7

The data file has two lines with a set of values in each line, the
first line representing years and the second line representing the
profit percentages.

.. R8

To produce the scatter plot, we first need to load the data from the
file using ``loadtxt`` command.  

.. L8

{{{ close the file and switch to the terminal }}}

::

    year,profit =
    loadtxt('/home/fossee/other-plot/company-a-data.txt',dtype=type(int()))


.. R9

By default loadtxt converts the value to float. The
``dtype=type(int())`` argument in loadtxt converts the value to
integer, as we require the data as integer further in the tutorial.

.. L9

.. R10

Now in-order to generate the scatter graph we will use the function 
``scatter()`` 

.. L10

::

    scatter(year,profit)

.. L11

{{{ switch to next slide, ``scatter`` function }}}

.. R11

Notice that we passed two arguments to ``scatter()`` function, first
one the values in x-coordinate, year, and the other the values in
y-coordinate, the profit percentage.

.. L12

{{{ switch to the next slide exercise 2 }}}

.. R12

Plot a scatter plot of the same data in company-a-data.txt with red
diamond markers.
Pause the video here, try out the following exercise and resume the video.

.. L13

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::
  
    clf()
    scatter(year,profit,color='r',marker='d')

.. R13

Thus, we got our scatter plot.
It is always a good practice to clear the previous figure before 
creating another one.
Now let us see another kind of plot, the pie chart, for the same data.

.. L14

{{{ switch to the slide which says about pie chart }}}

.. R14

A pie chart or a circle graph is a circular chart divided into
sectors, illustrating proportion.

.. L15

{{{ switch to the slide showing exercise 3 }}}

.. R15

Plot a pie chart representing the profit percentage of company A, with
the same data from file ``company-a-data.txt``. 

So let us reuse the data we have loaded from the file previously.

.. R16

We can plot the pie chart using the function ``pie()``.

.. L16

{{{ Switch to the terminal }}}
::

    clf()
    pie(profit,labels=year)

.. L17

{{{ switch to next slide, ``pie()`` function }}}

.. R17

Notice that we passed two arguments to the function ``pie()``. First
one the values and the next one the set of labels to be used in the
pie chart.

Pause the video here, try out the following exercise and resume the video.

.. L18

{{{ switch to the next slide with exercise 4 }}}

.. R18

Plot a pie chart with the same data with colors for each wedges 
as white, red, black, magenta,yellow, blue, green, cyan, yellow, magenta 
and blue respectively.

.. L19

{{{ Switch to the terminal }}}
::

    clf()
    pie(t,labels=s,colors=('w','r','k','m','y','b','g','c','y','m','b'))

.. R19

.. L20

{{{ switch to the slide which says about bar chart }}}

.. R20

Now let us move on to the bar charts. A bar chart or bar graph is a chart
with rectangular bars with lengths proportional to the values that
they represent.

.. L21

{{{ switch to the slide showing exercise 5 }}}

.. R21

Plot a bar chart representing the profit percentage of company A, with
the same data from file ``company-a-data.txt``. 

So let us reuse the data we have loaded from the file previously.

.. R22

We can plot the bar chart using the function ``bar()``.

.. L22

{{{ Switch to the terminal }}}
::

    clf()
    bar(year,profit)

.. R23

{{{ switch to the next slide, ``bar()`` function }}}

.. R23
 
Note that the function ``bar()`` needs at least two arguments one the
values in x-coordinate and the other values in y-coordinate which is
used to determine the height of the bars.

.. L24

{{{ switch to the next slide with exercise 6 }}}

.. R24

Plot a bar chart which is not filled and which is hatched 
with 45\ :sup:`o` slanting lines as shown in the image.The data for the 
chart may be obtained from the file ``company-a-data.txt``.

.. L25

::

    clf()
    bar(year,profit,fill=False,hatch='/')

.. R25

.. L26

{{{ switch to the slide which says about log-log graph }}}

.. R26

Now let us move on to the log-log plot. A log-log graph or a log-log plot
is a two-dimensional graph of numerical data that uses logarithmic scales
on both the horizontal and vertical axes. Because of the nonlinear
scaling of the axes, a function of the form y = ax\ :sup:`b` will
appear as a straight line on a log-log graph

.. L27

{{{ switch to the slide showing exercise 7 }}}

.. R27

Plot a `log-log` chart of y=5*x\ :sup:`3` for x from 1-20.

.. R28

Before we actually plot let us calculate the points needed for
that. 

.. L28

{{{ Switch to the terminal }}}
::

    x = linspace(1,20,100)
    y = 5*x**3

.. L29

{{{ switch to next slide, ``loglog()`` function }}}

.. R29

Here is the syntax of the log-log function.
Now we can plot the log-log chart using ``loglog()`` function,

.. L30

{{{ Switch to the terminal }}}
::

    clf()
    loglog(x,y)

.. R30

.. R31

To understand the difference between a normal ``plot`` and a ``log-log
plot`` let us create another plot using the function ``plot``.

.. L31

::

    figure(2)
    plot(x,y)

.. L32

{{{ show both the plots side by side }}}

.. R32

The difference is clear.So that was ``log-log() plot``.

.. L33

{{{ switch to the next slide which says: "How to get help on
matplotlib online"}}}

.. R33

Now we will see few more plots and also see how to access help of
matplotlib over the Internet.

Help about matplotlib can be obtained from
matplotlib.sourceforge.net/contents.html


More plots can be seen at
matplotlib.sourceforge.net/users/screenshots.html and also at
matplotlib.sourceforge.net/gallery.html

.. L34

{{{ switch to summary slide }}}

.. R34

This brings us to the end of this tutorial. 
In this tutorial we learnt to,
 
  1. Plot a scatter plot using ``scatter()`` function
  #. Plot a pie chart using ``pie()`` function
  #. Plot a bar chart using ``bar()`` function
  #. Plot a log-log graph using ``loglog()`` function
  #. Access the matplotlib online help.

.. L35

{{Show self assessment questions slide}}

.. R35

Here are some self assessment questions for you to solve.

1. ``scatter(x, y, color='blue', marker='d')`` and ``plot(x, y,
   color='b', marker='d')`` does exactly the same.

   - True
   - False

2. What statement can be issued to generate a bar chart with vertical
   line hatching.

   - bar(x, y, color='w', hatch='/')
   - bar(x, y, fill=False, hatch='//')
   - bar(x, y, fill=False, hatch='|')
   - bar(x, y, color='w', hatch='\')

.. L36

{{{solution of self assessment questions on slide}}}

.. R36

And the answers,

1. False. Both functions do not produce the same kind of plot.

2. ``bar(x, y, fill=False, hatch='|')`` is the correct option to generate 
   a bar chart with vertical line hatching.

.. L37

{{{ switch to the thank you slide }}}

.. R37

Hope you have enjoyed this tutorial and found it useful.
Thank you!

