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

.. #[Puneeth: Quickref missing]

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

Till now we have seen only one kind of plotting.Hence in this tutorial we will be looking at
some more kinds of plots. 

At the end of this tutorial, you will be able to 

 1. Create scatter plot
 #. Create pie charts
 #. Create bar charts
 #. Create log-log plots
 #. Use the matplotlib help

Let us begin with the scatter plot. 

.. L3

{{{ switch to the next slide, scatter plot }}}

.. R3

In a scatter plot, the data is displayed as a collection of points,
where each point determines it's position on the horizontal axis and the vertical axis 
respectively.This kind of plot is also called a
scatter chart, a scatter diagram or a scatter graph.

.. R4

Before we proceed further, start your IPython interpreter

.. L4

{{{ open the ipython interpreter in the terminal using the command
ipython -pylab }}}
::

    ipython -pylab


.. L5

{{{ switch to the slide having Question 1 }}}

.. R5

Plot a scatter plot showing the percentage profit of
a company A from the year 2000-2010. The data for the same is available
in the file ``company-a-data.txt``.

.. L6

{{{ open the file company-a-data.txt and show the content }}}

.. R6

The data file has two lines with a set of values in each line, the
first line representing years and the second line representing the
profit percentages.

.. R7

To produce the scatter plot, we first need to load the data from the
file using ``loadtxt`` command.  

.. L7

{{{ close the file and switch to the terminal }}}

::

    year,profit =
    loadtxt('/home/fossee/other-plot/company-a-data.txt',dtype=type(int()))


.. R8

By default loadtxt converts the value to float. The
``dtype=type(int())`` argument in loadtxt converts the value to
integer, as we require the data as integer further in the tutorial.

.. L8

.. R9

Now in-order to generate the scatter graph we will use the function 
``scatter()`` 

.. L9

::

    scatter(year,profit)

.. L10

{{{ switch to next slide, ``scatter`` function }}}

.. R10

Notice that we passed two arguments to ``scatter()`` function, first
one the values in x-coordinate, year, and the other the values in
y-coordinate, the profit percentage.

.. L11

{{{ switch to the next slide Question 2 }}}

.. R11

Plot a scatter plot of the same data in company-a-data.txt with red
diamond markers.
Pause the video here, try out the following exercise and resume the video.

.. L12

::
  
    scatter(year,profit,color='r',marker='d')

.. R12

Now let us see another kind of plot, the pie chart, for the same data.

.. L13

{{{ switch to the slide which says about pie chart }}}

.. R13

A pie chart or a circle graph is a circular chart divided into
sectors, illustrating proportion.

.. L14

{{{ switch to the slide showing Question 3 }}}

.. R14

Plot a pie chart representing the profit percentage of company A, with
the same data from file ``company-a-data.txt``. So let us reuse the
data we have loaded from the file previously.

.. R15

We can plot the pie chart using the function ``pie()``.

.. L15

::

    pie(profit,labels=year)

.. L16

{{{ switch to next slide, ``pie()`` function }}}

.. R16

Notice that we passed two arguments to the function ``pie()``. First
one the values and the next one the set of labels to be used in the
pie chart.

.. L17

{{{ switch to the next slide with Question 4 }}}

.. R17

Plot a pie chart with the same data with colors for each wedges 
as white, red, black, magenta,yellow, blue, green, cyan, yellow, magenta and blue respectively.

Pause the video here, try out the following exercise and resume the video.

.. L18

::

    pie(t,labels=s,colors=('w','r','k','m','y','b','g','c','y','m','b'))

.. R18

.. L19

{{{ switch to the slide which says about bar chart }}}

.. R19

Now let us move on to the bar charts. A bar chart or bar graph is a chart
with rectangular bars with lengths proportional to the values that
they represent.

.. L20

{{{ switch to the slide showing Question 5 }}}

.. R20

Plot a bar chart representing the profit percentage of company A, with
the same data from file ``company-a-data.txt``. 

So let us reuse the data we have loaded from the file previously.

.. R21

We can plot the bar chart using the function ``bar()``.

.. L21

::

   bar(year,profit)

.. R22

{{{ switch to the next slide, ``bar()`` function }}}

.. R22
 
Note that the function ``bar()`` needs at least two arguments one the
values in x-coordinate and the other values in y-coordinate which is
used to determine the height of the bars.

.. L23

{{{ switch to the next slide with Question 6 }}}

.. R23

Plot a bar chart which is not filled and which is hatched with 45\ :sup:`o` 
slanting lines as shown in the image.The data for the chart may be obtained from
the file ``company-a-data.txt``.

.. L24

::

   bar(year,profit,fill=False,hatch='/')

.. R24


.. L25

{{{ switch to the slide which says about log-log graph }}}

.. R25

Now let us move on to the log-log plot. A log-log graph or a log-log plot is
a two-dimensional graph of numerical data that uses logarithmic scales
on both the horizontal and vertical axes. Because of the nonlinear
scaling of the axes, a function of the form y = ax\ :sup:`b` will
appear as a straight line on a log-log graph

.. L26

{{{ switch to the slide showing Question 7 }}}

.. R26

Plot a `log-log` chart of y=5*x\ :sup:`3` for x from 1-20.

.. R27

Before we actually plot let us calculate the points needed for
that. 

.. L27

::

    x = linspace(1,20,100)
    y = 5*x**3

.. L28

{{{ switch to next slide, ``loglog()`` function }}}

.. R28

Here is the syntax of the log-lof function.
Now we can plot the log-log chart using ``loglog()`` function,

.. L29

::

    loglog(x,y)

.. R29

.. R30

To understand the difference between a normal ``plot`` and a ``log-log
plot`` let us create another plot using the function ``plot``.

.. L30

::

    figure(2)
    plot(x,y)

.. L31

{{{ show both the plots side by side }}}

.. R31

The differnce is clear.So that was ``log-log() plot``.

.. L32

{{{ switch to the next slide which says: "How to get help on
matplotlib online"}}}

.. R32

Now we will see few more plots and also see how to access help of
matplotlib over the internet.

Help about matplotlib can be obtained from
matplotlib.sourceforge.net/contents.html


More plots can be seen at
matplotlib.sourceforge.net/users/screenshots.html and also at
matplotlib.sourceforge.net/gallery.html

.. L33

{{{ switch to summary slide }}}

.. R33

This brings us to the end of this tutorial. 
In this tutorial we learnt to,
 
  1. Plot a scatter plot using ``scatter()`` function
  #. Plot a pie chart using ``pie()`` function
  #. Plot a bar chart using ``bar()`` function
  #. Plot a log-log graph using ``loglog()`` function
  #. Access the matplotlib online help.

.. L34

{{Show self assessment questions slide}}

.. R34

Here are some self assessment questions for you to solve.

1. ``scatter(x, y, color='blue', marker='d')`` and ``plot(x, y,
   color='b', marker='d')`` does exactly the same.

   a. True
   #. False

2. What statement can be issued to generate a bar chart with vertical
   line hatching.

   a. bar(x, y, color='w', hatch='/')
   #. bar(x, y, fill=False, hatch='\\')
   #. bar(x, y, fill=False, hatch='|')
   #. bar(x, y, color='w', hatch='\')

.. L35

{{{solution of self assessment questions on slide}}}

.. R35

And the answers,

1. False. Both functions do not produce the same kind of plot.
2. ``bar(x, y, fill=False, hatch='|')`` is the correct option to generate a bar 
   chart with vertical line hatching.

.. L36

{{{ switch to the thank you slide }}}

.. R36
Hope you have enjoyed and found it useful.
Thank you!
