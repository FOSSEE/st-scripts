Hello friends. Welcome to this spoken tutorial on Multiple plots.

{{{ Show the slide containing the title }}}

{{{ Show the slide containing the outline }}}

In this tutorial, we will learn how to draw more than one plot, how to
add legends to each plot to indicate what each plot represents. We
will also learn how to switch between the plots and creating multiple
plots with different regular axes which are also called as subplots.

{{{ Shift to terminal and start ipython -pylab }}}

To begin with let us start ipython with pylab, by typing::

  ipython -pylab

on the terminal

Let us first create set of points for our plot. For this we will use
the command called linspace::

  x = linspace(0, 50, 10)

linspace command creates 10 points in the interval between 0 and 50
both inclusive. We assign these values to a variable called x.

Now let us draw a plot simple sine plot using these points::

  plot(x, sin(x))

This should give us a nice sine plot.

{{{ Switch to the plot window }}}

Oh! wait! Is that a nice sine plot? Does a sine plot actually look
like that? We know that a sine plot is a smooth curve is it not? What
really caused this?

{{{ pause for a while }}}

A small investigation on linspace tells us that we chose too few
points in a large interval between 0 and 50 for the curve to be
smooth. So now let us use linspace again to get 500 points between 0
and 100 and draw the sine plot

{{{ Switch to ipython andtype }}} ::

  y = linspace(0, 50, 500)
  plot(y, sin(y))

{{{ Change to the plot window }}}

Now we see what we remember as a sine plot. A smooth curve. If we
carefully notice we also have two plots now one overlaid upon
another. In pylab, by default all the plots are overlaid.

We now know how to draw multiple plots but we would like to have more
control over it. Like switch between them, perform some operations or
labelling on them individually and so on. Let us see how to accomplish
this. Before we move on, let us clear our screen.

{{{ Switch to ipython }}}::

  clf()

To accomplishing more control over individual plots we use the figure
command::

  x = linspace(0, 50, 500)
  figure(1)
  plot(x, sin(x), 'b')
  figure(2)
  plot(x, cos(x), 'g')

{{{ Switch to plot window }}}

Now we have two plots, a sine plot and a cosine plot one overlaid upon
the other.

{{{ Have both plot window and ipython side by side }}}

The figure command takes an integer as an argument which is the serial
number of the plot. This selects the corresponding plot. All the plot
commands we run after this are applied to the selected plot. In this
example figure 1 is the sine plot and figure 2 is the cosine plot. We
can, for example, save each plot separately

{{{ Switch to ipython }}}::

  savefig('/home/user/cosine.png')
  figure(1)
  title('sin(y)')
  savefig('/home/user/sine.png')

{{{ Have both plot window and ipython side by side }}}

We also titled the our first plot as 'sin(y)' which we did not do for
the second plot.

Since we have two plots now overlaid upon each other we would like to
have a way to indicate what each plot represents to distinguish
between them. This is accomplished using legends. Equivalently, the
legend command does this for us

{{{ Switch to ipython }}}::

  legend(['sin(x)', 'cos(x)'])

The legend command takes a single list of parameters where each
parameter is the text indicating the plots in the order of their
serial number.

{{{ Switch to plot window }}}

Now we can see the legends being displayed for the respective sine and
cosine plots on the plot area.

At times we run into situations where we want to compare two plots and
in such cases we want to draw both the plots in the same plotting
area. The situation is such that the two plots have different regular
axes which means we cannot draw overlaid plots. In such cases we can
draw subplots.

We use subplot command to accomplish this

{{{ Switch to ipython }}}::

  subplot(2, 1, 1)

subplot command takes three arguments, the first being the number of
rows of subplots that must be created,

{{{ Have both plot window and ipython side by side }}}

in this case we have 2 so it spilts the plotting area horizontally for
two subplots. The second argument specifies the number of coloumns of
subplots that must be created. We passed 1 as the argument so the
plotting area won't be split horizontally and the last argument
specifies what subplot must be created now in the order of the serial
number. In this case we passed 1 as the argument, so the first subplot
that is top half is created. If we execute the subplot command as

{{{ Switch to ipython }}}::

  subplot(2, 1, 2)

{{{ Switch to plot window }}}

The lower subplot is created. Now we can draw plots in each of the
subplot area using the plot command.

{{{ Switch to ipython }}}::

  x = linspace(0, 50, 500)
  plot(x, cos(x))
  subplot(2, 1, 1)
  y = linspace(0, 5, 100)
  plot(y, y ** 2)

{{{ Have both plot window and ipython side by side }}}

This created two plots one in each of the subplot area. The top
subplot holds a parabola and the bottom subplot holds a cosine
curve.

As seen here we can use subplot command to switch between the subplot
as well, but we have to use the same arguments as we used to create
that subplot, otherwise the previous subplot at that place will be
automatically erased. It is clear from the two subplots that both have
different regular axes. For the cosine plot x-axis varies from 0 to
100 and y-axis varies from 0 to 1 where as for the parabolic plot the
x-axis varies from 0 to 10 and y-axis varies from 0 to 100

{{{ Show summary slide }}}

This brings us to the end of another session. In this tutorial session
we learnt

 * How to draw multiple plots which are overlaid
 * the figure command
 * how to switch between the plots and perform some operations on each
   of them like saving the plots
 * the legend command and
 * creating and switching between subplots

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thankyou
 
.. Author              : Madhu
   Internal Reviewer 1 :         [potential reviewer: Puneeth]
   Internal Reviewer 2 :         [potential reviewer: Nishanth]
   External Reviewer   :

