.. Objectives
.. ----------

.. By the end of this tutorial you will be able to 

..  * Use SAGE for 2D plotting
..  * Use SAGE for 3D plotting

.. Prerequisites
.. -------------

..   1. Getting started with lists
     
.. Author              : Nishanth Amuluru
   Internal Reviewer   : 
   External Reviewer   :
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]

Script
------

Hello friends, welcome to the tutorial on "Plotting using SAGE".

{{{ Show the outline slide }}}

In this tutorial we shall look at 
 
 * 2D plotting in SAGE
 * 3D plotting in SAGE

We shall first create a symbolic variable ``x``
::

    x = var('x')

We shall plot the function ``sin(x) - cos(x) ^ 2`` in the range (-5, 5).
::

    plot(sin(x) - cos(x) ^ 2, (x, -5, 5))

As we can see, the plot is shown.

``plot`` command takes the symbolic function as the first argument and the
range as the second argument.

{{{ Pause here and try out the following exercises }}}

%% 1 %% Define a variable ``y`` and plot the function ``y^2 + 5y - 7`` in the
        range (-3, 3)

{{{ continue from paused state }}}

::

    y = var('y')
    plot(y^2 + 5*y -7, (y, -3, 3))

We have seen that plot command plots the given function on a linear range.

What if the x and y values are functions of another variable.
For instance, lets plot the trajectory of a projectile.

A projectile was thrown at 50 m/s^2 and at an angle of 45 degrees from the 
ground. We shall plot the trajectory of the particle for 5 seconds.

These types of plots can be drawn using the parametric_plot function.
We first define the time variable.
::

    t = var('t')

Then we define the x and y as functions of t.
::

    f_x = 50 * cos(pi/4)
    f_y = 50 * sin(pi/4) * t - 1/2 * 9.81 * t^2 )

We then call the ``parametric_plot`` function as
::

    parametric_plot((f_x, f_y), (t, 0, 5))

And we can see the trajectory of the projectile.

The ``parametric_plot`` funciton takes a tuple of two functions as the first
argument and the range over which the independent variable varies as the second
argument.

{{{ Pause here and try out the following exercises }}}

%% 2 %% A particle is thrown into the air at 10 m/s^2 and at angle of 60 degrees
        from the top of a 100 m tower. Plot the trajectory of the particle.

{{{ continue from paused state }}}

::

    t = var('t')
    f_x = 10 * cos(pi/3) * t
    f_y = 100 + 10 * sin(pi/3) * t - 1/2 * 9.81 * t^2
    parametric_plot((f_x, f_y), (t,0,5))

Now we shall look at how to plot a set of points.

We have the ``line`` function to acheive this.

We shall plot sin(x) at few points and join them.

First we need the set of points.
::

    points = [ (x, sin(x)) for x in srange(-2*float(pi), 2*float(pi), 0.75) ]

``srange`` takes a start, a stop and a step argument and returns a list of
point. We generate list of tuples in which the first value is ``x`` and second
is ``sin(x)``.

::

    line(points)

plots the points and joins them with a line.

{{{ Pause here and try out the following exercises }}}

%% 3 %% Plot the cosine function using line function.

{{{ continue from paused state }}}

::

    points = [ (x, cos(x)) for x in srange(-2*float(pi), 2*float(pi), 0.75) ]
    line(points)

The ``line`` function behaves like the plot command in matplotlib. The
difference is that ``plot`` command takes two sequences while line command
expects a sequence of co-ordinates.

As we can see, the axes limits are set by SAGE. Often we would want to set them
ourselves. Moreover, the plot is shown here since the last command that is
executed produces a plot. 

Let us try this example
::

    plot(cos(x), (x,0,2*pi))
    # Does the plot show up??

As we can see here, the plot is not shown since the last command does not
produce a plot.

The actual way of showing a plot is to use the ``show`` command.

::

    p1 = plot(cos(x), (x,0,2*pi))
    show(p1)
    # What happens now??

As we can see the plot is shown since we used it with ``show`` command.

``show`` command is also used set the axes limits.

::

    p1 = plot(cos(x), (x,0,2*pi))
    show(p1, xmin=0, xmax=2*pi, ymin=-1.2, ymax=1.2)

As we can see, we just have to pass the right keyword arguments to the ``show``
command to set the axes limits.

{{{ Pause here and try out the following exercises }}}

%% 4 %% Plot the cosine function in the range (-2pi, 2pi) and set the x-axis
        limits to (-5, 5) and y-axis limits to (-2, 2) respectively.

{{{ continue from paused state }}}

::

    p1 = plot(cos(x), (x, 0, 2*pi))
    show(p1, xmin=-5, xmax=5, ymin=-2, ymax=2)

The ``show`` command can also be used to show multiple plots.
::

    p1 = plot(cos(x), (x, 0, 2*pi))
    p2 = plot(sin(x), (x, 0, 2*pi))
    show(p1+p2)

As we can see, we can add the plots and use them in the ``show`` command.

{{{ Pause here and try out the following exercises }}}

%% 5 %% Plot sin(x) and sin(2*x) in the range (0, 2pi)

{{{ continue from paused state }}}

::

    p1 = plot(sin(x), (x, 0, 2*pi))
    p2 = plot(sin(2*x), (x, 0, 2*pi))
    show(p1+p2)

Now we shall look at 3D plotting in SAGE.

We have the ``plot3d`` function that takes a function in terms of two 
independent variables and the range over which they vary.

::

    x, y = var('x y')
    plot3d(x^2 + y^2, (x, 0, 2), (y, 0, 2))

We get a 3D plot which can be rotated and zoomed using the mouse.

{{{ Pause here and try out the following exercises }}}

%% 6 %% Plot the function sin(x)^2 + cos(y)^2 for x in range (0,2) and y in
        range (-2, 2)

{{{ continue from paused state }}}

::

    x, y = var("x y")
    plot3d( sin(x)^2 + cos(y)^2, (x, 0, 2), (y, -2, 2))

``parametric_plot3d`` function plots the surface in which x, y and z are
functions of another variable.

::

   u, v = var("u v")
   f_x = u
   f_y = v
   f_z = u^2 + v^2
   parametric_plot3d((f_x, f_y, f_z), (u, 0, 2), (v, 0, 2))

{{{ Show summary slide }}}

This brings us to the end of the tutorial.
we have learnt

 * How to draw 2D plots using plot comand
 * How to use the parametric_plot and line functions
 * How to use show command for multiple plots and setting axes limits
 * How to draw 3D plots

{{{ Show the "sponsored by FOSSEE" slide }}}

#[Nishanth]: Will add this line after all of us fix on one.
This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thankyou

