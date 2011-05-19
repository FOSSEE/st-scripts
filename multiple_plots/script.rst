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

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to this spoken tutorial on "Multiple plots".

.. L2

{{{ Show slide with objectives }}}

.. R2

At the end of this tutorial, you will be able to,

 1. draw multiple plots which are overlaid. 
 #. use the figure command. 
 #. use the legend command 
 #. switch between the plots and perform some operations on each of them 
    like saving the plots.
 #. create and switch between subplots
 
.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Using plot interactively" , "Embellishing a plot" and "Saving plots".

To begin with let us start ipython with pylab, by typing ipython -pylab
on the terminal.

.. L3

{{{ Show slide with pre-requisite }}}

{{{ Shift to terminal and start ipython -pylab }}}

::

    ipython -pylab

.. R4

Let us first create set of points for our plot. For this we will use
the command called linspace

.. L4

::

    x = linspace(0, 50, 10)

.. R5

linspace command creates 10 points in the interval between 0 and 50
both inclusive. We assign these values to a variable called x.

Now let us draw a simple sine plot using these points

.. L5

::

    plot(x, sin(x))

.. L6

{{{ Switch to the plot window }}}

.. R6

Oh! wait! Is that a good sine plot? Does a sine plot actually look
like that? We know that a sine plot is a smooth curve. Is it not? What
really caused this?

.. L7

{{{ pause for a while }}}

.. R7

A small investigation on linspace tells us that we chose too few
points in a large interval between 0 and 50 for the curve to be
smooth. This also indicates that the plot command actually plots
the set of points given by x and sin(x) and it doesn't plot the
analytical function itself rather it plots the points given by
Analytical functions. So now let us use linspace again to get 500
points between 0 and 100 and draw the sine plot again.

.. L8

{{{ Switch to terminal and type }}}

::

    y = linspace(0, 50, 500)
    plot(y, sin(y))

{{{ Switch to the plot window }}}

.. R8

Now we see a sine plot with a smooth curve, just as we wanted.If we
carefully notice we also have two plots now one overlaid upon
another. In pylab, by default all the plots are overlaid.

Since we have two plots now overlaid upon each other we would like to
have a way to indicate what each plot represents to distinguish
between them. This is accomplished using legends. Equivalently, the
legend command does this for us.

.. L9

{{{ Switch to terminal }}}

::

    legend(['sin(x)', 'cos(x)'])

.. R9

The legend command takes a single list of parameters where each
parameter is the text indicating the plots in the order of their
serial number.

.. L10

{{{ Switch to plot window }}}

.. R10

Now we can see the legends being displayed for the respective sine and
cosine plots on the plot area.

.. L11

{{{ Show slide with exercise 1 }}}

.. R11

We have learnt quite a lot of things now, so let us take up an
exercise.Pause the video here,do the exercise and resume the video.

   Draw two plots overlaid upon each other, with the first plot
   being a parabola of the form y = 4(x ^ 2) and the second being a
   straight line of the form y = 2x + 3 in the interval -5 to 5. Use
   colors to differentiate between the plots and use legends to
   indicate what each plot is doing.

.. R12

Switch to the terminal for solution.
We can obtain the two plots in different colors using the following
commands

.. L12

{{{ pause for a while and continue from paused state }}}

::

    x = linspace(-5, 5, 100)
    plot(x, 4 * (x * x), 'b')
    plot(x, (2 * x) + 3, 'g')

.. R13

Now we can use the legend command as

.. L13

::

    legend(['Parabola', 'Straight Line'])

.. R14

Or we can also just give the equations of the plot

.. L14

::

    legend(['y = 4(x ^ 2)', 'y = 2x + 3'])

.. R15

We now know how to draw multiple plots and use legends to indicate
which plot represents what function, but we would like to have more
control over the plots we draw. Like switch between them, perform some
operations or labelling them individually and so on. Let us see how
to accomplish this.But before we move on, let us clear our screen.

.. L15

{{{ Switch to terminal }}}

::

    clf()

.. R16

To accomplishing more control over individual plots we use the figure
command

.. L16

::

    x = linspace(0, 50, 500)
    figure(1)
    plot(x, sin(x), 'b')
    figure(2)
    plot(x, cos(x), 'g')

.. L17

{{{ Switch to plot window }}}

.. R17

Now we have two plots, a sine plot and a cosine plot in two different
figures.

.. L18

{{{ Show both plot window and terminal side by side }}}

.. R18

The figure command takes an integer as an argument which is the serial
number of the plot. This selects the corresponding plot. All the plot
commands we run hereafter are applied to the selected plot. In this
example figure 1 is the sine plot and figure 2 is the cosine plot.
For example,we cansave each plot separately

.. L19

{{{ Switch to terminal }}}

::

    savefig('/home/user/cosine.png')
    figure(1)
    title('sin(y)')
    savefig('/home/user/sine.png')

{{{ Have both plot window and ipython side by side }}}

.. R19

We also titled our first plot as 'sin(y)' which we did not do for
the second plot.

.. R20

Let us attempt another exercise problem.Pause here,try to solve the 
problem and resume the video.

   Draw a line of the form y = x as one figure and another line
   of the form y = 2x + 3. Switch back to the first figure,annotate
   the x and y intercepts. Now switch to the second figure and
   annotate its x and y intercepts. Save each of them.

.. L20

{{{ Show slide with exercise 2 }}}
 
.. R21

Switch to the terminal for solution.
To solve this problem we should first create the first figure using
the figure command. Before that, let us first run clf command to make
sure all the previous plots are cleared

.. L21

{{{ Pause for a while and continue from the paused state }}}

::

    clf()
    figure(1)
    x = linspace(-5, 5, 100)
    plot(x, x)

.. R22

Now use the figure command to create second plotting area and plot
the figure

.. L22

::

    figure(2)
    plot(x, ((2 * x) + 3))

.. R23

Now to switch between the figures we can use figure command. So let us 
now switch to figure 1. We are asked to annotate x and y intercepts of 
the figure 1, but since figure 1 passes through origin,this means, we
will have to annotate the origin. We will annotate the intercepts for 
the second figure and save them as follows

.. L23

::

    figure(1)
    annotate('Origin', xy=(0.0, 0.0)
    figure(2)
    annotate('x-intercept', xy=(0, 3))
    annotate('y-intercept', xy=(0, -1.5))
    savefig('/home/fossee/plot2.png')
    figure(1)
    savefig('/home/fossee/plot1.png')

.. R24

At times we run into situations where we want to compare two plots and
in such cases we want to draw both the plots in the same plotting
area. The situation is such that the two plots have different regular
axes which means we cannot draw overlaid plots. In such cases we can
draw subplots.

We use subplot command to accomplish this

.. L24

{{{ Switch to terminal }}}

::

    subplot(2, 1, 1)

{{{ Have both plot window and ipython side by side }}}

.. R25

As we can see subplot command takes three arguments, the first being 
the number ofrows of subplots that must be created,in this case we have 
2 as the first argument so it spilts the plotting area horizontally for
two subplots. The second argument specifies the number of coloumns of
subplots that must be created. We passed 1 as the argument so the
plotting area won't be split vertically and the last argument
specifies what subplot must be created now in the order of the serial
number. In this case we passed 1 as the argument, so the first subplot
that is top half is created. If we execute the subplot command as

.. L25

{{{ Switch to terminal }}}

::

    subplot(2, 1, 2)

{{{ Switch to plot window }}}

.. R26

The lower subplot is created. Now we can draw plots in each of the
subplot area using the plot command.

.. L26

{{{ Switch to terminal }}}

::

    x = linspace(0, 50, 500)
    plot(x, cos(x))
    subplot(2, 1, 1)
    y = linspace(0, 5, 100)
    plot(y, y ** 2)

.. L27
 
{{{ Have both plot window and ipython side by side }}}

.. R27

This created two plots one in each of the subplot area. The top
subplot holds a parabola and the bottom subplot holds a cosine
curve.

As seen here we can use subplot command to switch between the subplots
as well, but we have to use the same arguments as we used to create
that subplot, otherwise the previous subplot at that place will be
automatically erased. It is clear from the two subplots that both have
different regular axes. For the cosine plot x-axis varies from 0 to
100 and y-axis varies from 0 to 1 where as for the parabolic plot the
x-axis varies from 0 to 10 and y-axis varies from 0 to 100.

.. L28

{{{ Show slide with exercise 3 }}}

.. R28

Let us try one more exercise.Pause the video here, try out the exercise 
and resume the video.

  We know that the Pressure, Volume and Temperatures are held by
  the equation PV = nRT where nR is a constant. Let us assume nR =0.01
  Joules/Kelvin and T = 200K. V can be in the range from 21cc to
  100cc. Draw two different plots as subplots, one being the Pressure
  versus Volume plot and the other being Pressure versus Temperature
  plot.

.. R29

Switch to the terminal for solution.
To start with, we have been given the range of Volume using which we
can define the variable V

.. L29

{{{ Pause for a while and continue }}}

::

    V = linspace(21, 100, 500)

.. R30

Now we can create first subplot and draw Pressure versus Volume graph
using this V. We know that nRT is a constant which is equal to 2.0
since nR = 0.01 Joules/Kelvin and T = 200 Kelvin

.. L30

::

    subplot(2, 1, 1)
    plot(V, 2.0/V)

.. R31

Now we can create the second subplot and draw the Pressure versus
Temparature plot as follows

.. L31

::

    subplot(2, 1, 2)
    plot(200, 2.0/V)

.. R32

Unfortunately we have an error now, telling x and y dimensions don't
match. This is because our V contains a set of values as returned by
linspace and hence 2.0/V which is the pressure also contains a set of
values. But the first argument to the plot command is a single
value. So to plot this data we need to create as many points as there
are in Pressure or Volume data for Temperature too, all having the
same value.Hence we do this,

.. L32

::

    T = linspace(200, 200, 500)

.. R33

We now have 500 values in T each with the value 200 Kelvin. Plotting
this data, we get the required plot

.. L33

::

    plot(T, 2.0/V)

.. L34
 
{{{ Show summary slide }}}

.. R34

This brings us to the end of this tutorial.In this tutorial,we have learnt to,

 1. Draw multiple plots which are overlaid.
 #. Use the figure command.
 #. Use the legend command.
 #. Switch between the plots and perform some operations on each
    of them like saving the plots.
 #. Create subplots and to switch between them.

.. L35

{{Show self assessment questions slide}}

.. R35

Here are some self assessment questions for you to solve

1. What command is used to get individual plots separately?.

2. Which of the following is correct.

   - subplot(numRows, numCols, plotNum)
   - subplot(numRows, numCols)
   - subplot(numCols, numRows)

.. L36

{{{solution of self assessment questions on slide}}}

.. R36

And the answers,

1. The command "figure()" can get us the individual plots seperately.

2. The subplot command takes three arguments namely the number of 
   rows followed by the number of columns and the plot number.
   Hence the first option is correct.

.. L37

{{{ a thank you slide }}}

.. R37

Hope you have enjoyed and found it useful.
Thank you!
 
