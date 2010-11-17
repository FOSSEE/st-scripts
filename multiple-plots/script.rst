.. Objectives
.. ----------

..  * How to draw multiple plots which are overlaid
..  * the figure command
..  * the legend command
..  * how to switch between the plots and perform some operations on each
..    of them like saving the plots and
..  * creating and switching between subplots


.. Prerequisites
.. -------------

.. 1. using the plot command interactively
.. 2. embellishing a plot
.. 3. saving plots
     
.. Author              : Madhu
   Internal Reviewer 1 :         [potential reviewer: Puneeth]
   Internal Reviewer 2 : Nishanth
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <, not OK> []


Script
------

{{{ Show the slide containing the title }}}

Hello friends. Welcome to this spoken tutorial on Multiple plots.

{{{ Show the slide containing the outline }}}

In this tutorial, we will learn how to draw more than one plot, how to
add legends to each plot to indicate what each plot represents. We
will also learn how to switch between the plots and create multiple
plots with different regular axes which are also called as subplots.

.. #[Nishanth]: See diff - edited a grammatical mistake
.. #[Madhu: Done]

{{{ Shift to terminal and start ipython -pylab }}}

To begin with let us start ipython with pylab, by typing::

  ipython -pylab

on the terminal

Let us first create set of points for our plot. For this we will use
the command called linspace::

  x = linspace(0, 50, 10)

linspace command creates 10 points in the interval between 0 and 50
both inclusive. We assign these values to a variable called x.

.. #[Nishanth]: pre requisite for this LO is basic plotting which
                covers linspace and plot. So you may not need to 
                specify all that again. But not a problem if it is
                there also.
.. #[Madhu: Since I thought the LOs are disconnected, I thought it is
     better to give a very short intro to it]

Now let us draw a plot simple sine plot using these points::

  plot(x, sin(x))

This should give us a nice sine plot.

{{{ Switch to the plot window }}}

Oh! wait! Is that a nice sine plot? Does a sine plot actually look
like that? We know that a sine plot is a smooth curve. Is it not? What
really caused this?

.. #[Nishanth]: See diff
.. #[Madhu: Done]

{{{ pause for a while }}}

A small investigation on linspace tells us that we chose too few
points in a large interval between 0 and 50 for the curve to be
smooth. This should also indicate that the plot command actually plots
the set of points given by x and sin(x) and it doesn't plot the
analytical function itself i.e. it plots the points given by
Analytical functions. So now let us use linspace again to get 500
points between 0 and 100 and draw the sine plot

.. #[Nishanth]: Here specify that when we do plot(x, sin(x) 
                it is actually plotting two sets of points
                and not analytical functions. Hence the sharp 
                curve.
.. #[Madhu: Incorporated]

{{{ Switch to ipython andtype }}} ::

  y = linspace(0, 50, 500)
  plot(y, sin(y))

{{{ Change to the plot window }}}

Now we see what we remember as a sine plot. A smooth curve. If we
carefully notice we also have two plots now one overlaid upon
another. In pylab, by default all the plots are overlaid.

Since we have two plots now overlaid upon each other we would like to
have a way to indicate what each plot represents to distinguish
between them. This is accomplished using legends. Equivalently, the
legend command does this for us

{{{ Switch to ipython }}}::

  legend(['sin(x)', 'cos(x)'])

.. #[Nishanth]: This legend may go up in the script. May be before 
                introducing the figure command itself.
.. #[Madhu: brought up]

The legend command takes a single list of parameters where each
parameter is the text indicating the plots in the order of their
serial number.

{{{ Switch to plot window }}}

Now we can see the legends being displayed for the respective sine and
cosine plots on the plot area.

We have learnt quite a lot of things now, so let us take up an
exercise problem.

%% 1 %% Draw two plots overlaid upon each other, with the first plot
   being a parabola of the form y = 4(x ^ 2) and the second being a
   straight line of the form y = 2x + 3 in the interval -5 to 5. Use
   colors to differentiate between the plots and use legends to
   indicate what each plot is doing.

{{{ pause for a while and continue from paused state }}}

We can obtain the two plots in different colors using the following
commands::

  x = linspace(-5, 5, 100)
  plot(x, 4 * (x * x), 'b')
  plot(x, (2 * x) + 3, 'g')

Now we can use the legend command as::

  legend(['Parabola', 'Straight Line'])

Or we can also just give the equations of the plot::

  legend(['y = 4(x ^ 2)', 'y = 2x + 3'])

We now know how to draw multiple plots and use legends to indicate
which plot represents what function, but we would like to have more
control over the plots we draw. Like switch between them, perform some
operations or labelling on them individually and so on. Let us see how
to accomplish this. Before we move on, let us clear our screen.

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

Now we have two plots, a sine plot and a cosine plot in two different
figures.

.. #[Nishanth]: figure(1) and figure(2) give two different plots.
                The remaining script moves on the fact that they 
                give overlaid plots which is not the case.
                So clear the figure and plot cos and sin without
                introducing figure command. Then introduce legend
                and finish off the everything on legend.
                Then introduce figure command.

.. #[Madhu: I have just moved up the text about legend command. I
     think that should take care of what you suggested. If there is
     some mistake with it, Punch please let me know in your next
     review.]

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

We also titled our first plot as 'sin(y)' which we did not do for
the second plot.

Let us attempt another exercise problem

%% 2 %% Draw a line of the form y = x as one figure and another line
   of the form y = 2x + 3. Switch back to the first figure, annotate
   the x and y intercepts. Now switch to the second figure and
   annotate its x and y intercepts. Save each of them.

{{{ Pause for a while and continue from the paused state }}}

To solve this problem we should first create the first figure using
the figure command. Before that, let us first run clf command to make
sure all the previous plots are cleared::

  clf()
  figure(1)
  x = linspace(-5, 5, 100)
  plot(x, x)

Now we can use figure command to create second plotting area and plot
the figure::

  figure(2)
  plot(x, ((2 * x) + 3))

Now to switch between the figures we can use figure command. So let us
switch to figure 1. We are asked to annotate x and y intercepts of the
figure 1 but since figure 1 passes through origin we will have to
annotate the origin. We will annotate the intercepts for the second
figure and save them as follows::

  figure(1)
  annotate('Origin', xy=(0.0, 0.0)
  figure(2)
  annotate('x-intercept', xy=(0, 3))
  annotate('y-intercept', xy=(0, -1.5))
  savefig('/home/fossee/plot2.png')
  figure(1)
  savefig('/home/fossee/plot1.png')

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

in this case we have 2 as the first argument so it spilts the plotting area horizontally for
two subplots. The second argument specifies the number of coloumns of
subplots that must be created. We passed 1 as the argument so the
plotting area won't be split vertically and the last argument
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

.. #[Nishanth]: stress on the similarity between subplot and figure
     commands

.. #[Madhu: I think they are not really similar. Trying to bring in
     the similarity will confuse people I think.]

%% 3 %% We know that the Pressure, Volume and Temperatures are held by
the equation PV = nRT where nR is a constant. Let us assume nR = .01
Joules/Kelvin and T = 200K. V can be in the range from 21cc to
100cc. Draw two different plots as subplots, one being the Pressure
versus Volume plot and the other being Pressure versus Temparature
plot.

{{{ Pause for a while and continue }}}

To start with, we have been given the range of Volume using which we
can define the variable V::

  V = linspace(21, 100, 500)

Now we can create first subplot and draw Pressure versus Volume graph
using this V. We know that nRT is a constant which is equal to 2.0
since nR = 0.01 Joules/Kelvin and T = 200 Kelvin::

  subplot(2, 1, 1)
  plot(V, 2.0/V)

Now we can create the second subplot and draw the Pressure versus
Temparature plot as follows::

  subplot(2, 1, 2)
  plot(200, 2.0/V)

Unfortunately we have an error now, telling x and y dimensions don't
match. This is because our V contains a set of values as returned by
linspace and hence 2.0/V which is the pressure also contains a set of
values. But the first argument to the plot command is a single
value. So to plot this data we need to create as many points as there
are in Pressure or Volume data for Temperature too, all having the
same value. This can be accomplished using::

  T = linspace(200, 200, 500)

We now have 500 values in T each with the value 200 Kelvin. Plotting
this data we get the required plot::

  plot(T, 2.0/V)

It is left as a homework to label both X and Y axes for each of the
two subplots. 

{{{ Show summary slide }}}

.. #[Nishanth]: Exercises are missing in the script
                one exercise for overlaid plot and legend
                one for figure command
                one for subplot must do

This brings us to the end of another session. In this tutorial session
we learnt

 * How to draw multiple plots which are overlaid
 * the figure command
 * the legend command
 * how to switch between the plots and perform some operations on each
   of them like saving the plots and
 * creating and switching between subplots

.. #[Nishanth]: legend command can be told right after overlaid plots
.. #[Madhu: Incorporated]

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!
 
