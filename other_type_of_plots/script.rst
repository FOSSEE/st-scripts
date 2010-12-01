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
Other type of plots
===================

{{{ show the first slide }}}

Hello and welcome to the tutorial ``The other kinds of plots``.

.. #[Puneeth: this sentence doesn't read well]

{{{ show the outline slide }}}

.. #[Puneeth: motivate looking at other plots. Why are we looking at
.. them? Tell that we have only looked at one type of plot all the
.. while, etc.]

Till now we have seen only one kind of plotting, and in this tutorial we
are going to see more kinds of plots such as the scatter plot, the pie chart, the bar chart and
the log-log plot. This tutorial covers the making of other kinds of
plots and also gives an introduction to matplotlib help.

.. #[Puneeth: cover, see and introduce you. be consistent. does, the
.. "We" include the viewer or not?]

Let us start with scatter plot. 

{{{ switch to the next slide, scatter plot }}}

In a scatter plot, the data is displayed as a collection of points,
each having the value of one variable determining the position on the
horizontal axis and the value of the other variable determining the
position on the vertical axis. This kind of plot is also called a
scatter chart, a scatter diagram or a scatter graph.

Before we proceed further, start your IPython interpreter
::

    ipython -pylab

{{{ open the ipython interpreter in the terminal using the command
ipython -pylab }}}

{{{ switch to the next slide having the problem statement of first
exercise }}}

Now, let us plot a scatter plot showing the percentage profit of
a company A from the year 2000-2010. The data for the same is available
in the file ``company-a-data.txt``.

{{{ open the file company-a-data.txt and show the content }}}

The data file has two lines with a set of values in each line, the
first line representing years and the second line representing the
profit percentages.

{{{ close the file and switch to the terminal }}}

To produce the scatter plot, we first need to load the data from the
file using ``loadtxt``. We learned it in one of the previous sessions,
and it can be done as ::

    year,profit =
    loadtxt('/home/fossee/other-plot/company-a-data.txt',dtype=type(int()))

By default loadtxt converts the value to float. The
``dtype=type(int())`` argument in loadtxt converts the value to
integer as we require the data as integer further in the tutorial.

.. #[Puneeth: make a remark about dtype, that has not been covered in
.. the loadtxt tutorial.]

{{{ switch to next slide, ``scatter`` function }}}

Now in-order to generate the scatter graph we will use the function 
``scatter()`` 
::

	scatter(year,profit)

Notice that we passed two arguments to ``scatter()`` function, first
one the values in x-coordinate, year, and the other the values in
y-coordinate, the profit percentage.

{{{ switch to the next slide which has the problem statement of
problem to be tried out }}}

Now here is a question for you to try out, plot the same data with red
diamonds markers. 

.. **Clue** - *try scatter? in your ipython interpreter* 

Pause here and solve the question before moving on.

.. scatter(year,profit,color='r',marker='d')

Now let us see another kind of plot, the pie chart, for the same data.

.. #[Puneeth: instead of just saying that, say that let's plot a pie
.. chart for the same data. continuity, will be good.]

{{{ switch to the slide which says about pie chart }}}

A pie chart or a circle graph is a circular chart divided into
sectors, illustrating proportion.

{{{ switch to the slide showing the problem statement of second
exercise question }}}

Plot a pie chart representing the profit percentage of company A, with
the same data from file ``company-a-data.txt``. So let us reuse the
data we have loaded from the file previously.

.. #[Puneeth, this part can be move above.]

{{{ switch to next slide, ``pie()`` function }}}

We can plot the pie chart using the function ``pie()``.
::

   pie(profit,labels=year)

Notice that we passed two arguments to the function ``pie()``. First
one the values and the next one the set of labels to be used in the
pie chart.

{{{ switch to the next slide which has the problem statement of
problem to be tried out }}}

Now here is a question for you to try out, plot a pie chart with the
same data with colors for each wedges as white, red, black, magenta,
yellow, blue, green, cyan, yellow, magenta and blue respectively.

.. **Clue** - *try pie? in your ipython interpreter* 

Pause here and solve the question before moving on.

.. pie(t,labels=s,colors=('w','r','k','m','y','b','g','c','y','m','b'))

{{{ switch to the slide which says about bar chart }}}

Now let us move on to the bar charts. A bar chart or bar graph is a chart
with rectangular bars with lengths proportional to the values that
they represent.

{{{ switch to the slide showing the problem statement of fifth
exercise question }}}

Plot a bar chart representing the profit percentage of company A, with
the same data from file ``company-a-data.txt``. 

So let us reuse the data we have loaded from the file previously.

{{{ switch to the next slide, ``bar()`` function }}}

We can plot the bar chart using the function ``bar()``.
::

   bar(year,profit)

Note that the function ``bar()`` needs at least two arguments one the
values in x-coordinate and the other values in y-coordinate which is
used to determine the height of the bars.

{{{ switch to the next slide which has the problem statement of
problem to be tried out }}}

Now here is a question for you to try, plot a bar chart which is not
filled and which is hatched with 45\ :sup:`o` slanting lines as shown
in the image in the slide. The data for the chart may be obtained from
the file ``company-a-data.txt``.

.. **Clue** - *try bar? in your ipython interpreter* 

.. bar(year,profit,fill=False,hatch='/')

{{{ switch to the slide which says about log-log graph }}}

Now let us move on to the log-log plot. A log-log graph or a log-log plot is
a two-dimensional graph of numerical data that uses logarithmic scales
on both the horizontal and vertical axes. Because of the nonlinear
scaling of the axes, a function of the form y = ax\ :sup:`b` will
appear as a straight line on a log-log graph

{{{ switch to the slide showing the problem statement of fourth
exercise question }}}


Plot a `log-log` chart of y=5*x\ :sup:`3` for x from 1-20.

Before we actually plot let us calculate the points needed for
that. 
::

    x = linspace(1,20,100)
    y = 5*x**3

{{{ switch to next slide, ``loglog()`` function }}}

Now we can plot the log-log chart using ``loglog()`` function,
::

    loglog(x,y)

To understand the difference between a normal ``plot`` and a ``log-log
plot`` let us create another plot using the function ``plot``.
::

    figure(2)
    plot(x,y)

{{{ show both the plots side by side }}}

So that was ``log-log() plot``.

{{{ switch to the next slide which says: "How to get help on
matplotlib online"}}}

Now we will see few more plots and also see how to access help of
matplotlib over the internet.

Help about matplotlib can be obtained from
matplotlib.sourceforge.net/contents.html


More plots can be seen at
matplotlib.sourceforge.net/users/screenshots.html and also at
matplotlib.sourceforge.net/gallery.html

{{{ switch to summary slide }}}

Now we have come to the end of this tutorial. We have covered scatter
plot, pie chart, bar chart, log-log plot and also saw few other plots
and covered how to access the matplotlib online help.

{{{ switch to the thank you slide }}}

Thank you!
