.. Objectives
.. ----------

.. By the end of this tutorial you will be able to 

..  * Modify the attributes of the plot -- color, line style, linewidth
..  * Add a title to the plot with embedded LaTeX.
..  * Label x and y axes. 
..  * Add annotations to the plot. 
..  * Set and Get the limits of axes. 


.. Prerequisites
.. -------------

..   1. Using the ``plot`` command interactively
     
.. Author              : Nishanth Amuluru
   Internal Reviewer   : Anoop
   External Reviewer   :
   Language Reviewe    : Bhanukiran
   Checklist OK?       : <15-11-2010, Anand, OK> [2010-10-05]

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Welcome to the tutorial on "Embellishing a Plot".

.. L2

{{{ Show the slide containing objectives }}}

.. R2

At the end of this tutorial, you will be able to, 

 1. Modify the attributes of the plot -- color, line style,linewidth.
 #. Add a title to the plot with embedded LaTeX.
 #. Label x and y axes. 
 #. Add annotations to the plot. 
 #. Set and Get the limits of axes.

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Using plot interactively".

Let us start ipython with pylab loaded, open the terminal and type 

.. L3

{{{ Show slide with pre-requisite }}}

{{{ open the terminal and type ipython -pylab }}}
::
   
    ipython -pylab



.. R4

We shall first make a simple plot and start decorating it.

.. L4

::
    
    x = linspace(-2, 4, 20)
    plot(x, sin(x))

.. R5

As we can see, the default colour and the default thickness of the
line is as decided by pylab. Wouldn't it be nice if we could control
these parameters in the plot? This is possible by passing additional
arguments to the plot command.
We shall first clear the figure and plot the same by passing the additional
color argument. Pass the argument 'r' for red color.

.. L5
     
::
   
    clf()
    plot(x, sin(x), 'r')

.. R6

The same plot is seen in red color.

.. L6

{{{Move the mouse pointer on the plot}}}

.. R7

The thickness of the line can be altered by 'linewidth' argument. 

.. L7
{{{ Switch to terminal }}}
    
::
     
    plot(x, cos(x), linewidth=2)

.. R8

A plot with line thickness 2 is produced.

.. L8

{{{ Show the plot and compare the sine and cos plots }}}

.. R9

Pause the video and do this exercise and then resume the video.

Plot sin(x) in blue color along with linewidth as 3.

.. L9

{{{ Show slide with Question1 }}}

.. R10
Switch to terminal for solution
A combination of color and linewidth would do the job for us.

.. L10

{{{ Switch to terminal}}}
::
    
    clf()
    plot(x, sin(x), 'b', linewidth=3)


.. R11 

To get the style of line as bunch of points not joined, pass the linestyle
argument with or without color argument.

.. L11
   
::
   
    clf()
    plot(x, sin(x), '.')

.. R12

We get a plot with only points.

.. L12
 
{{{Point at the dots on the plot}}}

.. R13

To get the same plot in blue color.
 
.. L13
::

    clf()
    plot(x, sin(x), 'b.')

.. R14

Other available options for passing arguments can be seen in the 
documentation of plot.

.. L14
  
::
    
    plot?

{{{ Run through the documentation and show the options available }}}

{{{ Show the options available for line style and colors }}}

.. L15

{{{Show slide containing question 2}}}

.. R15

Pause the video and do this exercise and then resume the video.

 Plot the sine curve with green filled circles.

.. R16

Switch to terminal for solution.
We use a combination of linestyle and color.

.. L16

{{{ Switch to terminal and type the following commands }}}  
::
    
    clf()
    plot(x, cos(x), 'go')

.. L17

{{{Show slide containing question 3}}}

.. R17

Pause the video here, try out the following exercise and resume the video.

Plot the curve of x vs tan(x) in red dash line and linewidth 3.

.. R18

Switch to terminal for solution.
Here we shall use a combination of linewidth argument and linestyle.

.. L18

{{{ Switch to terminal and type the following commands }}}

::
   
    clf()
    plot(x, cos(x), 'r--')

.. R19

Now that we know how to produce a bare minimum plot with color, style
and thickness of our interest, we shall look at further decorating the plot.

.. L19

.. R20

Let us start with a plot for the function -x^2 + 4x - 5.

.. L20

::
   
    plot(x, -x*x + 4*x - 5, 'r', linewidth=2)

{{{ Show the plot window and switch back to terminal }}}

.. R21

As you can see, the figure does not have any description describing the plot.

To add a title to the plot to describe what the plot is,use the ``title`` 
command.

.. L21

{{{ Switch to terminal }}}  
::
   
    title("Parabolic function -x^2+4x-5")

The ``title`` command as you can see, takes a string as an argument 

{{{ Show the plot window and point to the title }}}

.. R22

The figure now has a title. But it is not formatted and does not look clean.

It would look shabby if there were fractions and more complex functions
like log and exp. Wouldn't it be good if the title is seen in LaTeX like
formatting?

This is possible by adding a ``$`` sign before and after the part of the 
string that should be in LaTeX style.

.. L22
  
::
    
    title("Parabolic function $-x^2+4x-5$")

.. R23

As we can see, the polynomial is now formatted.

.. L23

{{{ Point at the polynomial }}}

.. L24

{{{Show slide containing question 4}}}

.. R24

Pause the video here, try out the following exercise and resume the video.

Change the title of the figure such that the whole title is formatted
in LaTeX style.

.. R25

Switch to terminal for solution.
The solution is to enclose the whole string in between $. 

.. L25

{{{ Switch to terminal }}}  
::
    
    title("$Parabolic function -x^2+4x-5$")

.. R26

Although we have title, the plot is not complete without labelling x
and y axes. we shall label x-axis to "x" and y-axis to "f(x)".

.. L26
 
::
    
    xlabel("x")
    ylabel("f(x)")

.. L27

.. R27

As you can see, ``xlabel`` and 'ylabel' command takes a string as an argument. 
xlabel sets the label to x-axis as 'x' and ylabel sets the name to the y-axis
as 'f(x)'.

.. R28

.. L28

::
    
{{{ Show the plot window and point to xlabel and ylabel and 
    switch back to the terminal }}}

.. L29

{{{Show slide containing question 5}}}

.. R29

Pause the video here, try out the following exercise and resume the video.

Set the x and y labels as "x" and "f(x)" in LaTeX style.

Since we need LaTeX style formatting, all we have to do is enclose the string
in between two $. 

.. L30

{{{ Switch to terminal }}}
::

    xlabel("$x$")
    ylabel("$f(x)$")

.. R30

Switch to terminal for solution.

.. L31

{{{ Show the plot window with clean labels }}}

.. R31

The plot is now almost complete. Except that the points are not named. 
For example the point (2, -1) is the local maxima. We would
like to name the point accordingly. To do this use the function ``annotate``.

.. L31

{{{ Switch to terminal }}}
   
::
    
    annotate("local maxima", xy=(2, -1))

{{{ Show the annotation that has appeared on the plot }}}

.. R32

As you can see, the first argument to ``annotate`` command is the name we would
like to mark the point as, and the second argument is the co-ordinates of the
point at which the name should appear. It is a tuple containing two numbers.
The first is x co-ordinate and second is y co-ordinate.

.. L32

{{{ Point at the annotate command while explaining}}}

.. R33

Pause the video, do this exercise and then resume the video.

Make an annotation called "root" at the point (-4, 0).
What happens to the first annotation ?

.. L33

{{{Show slide containing question 6}}}

.. L34

{{{ Switch to the terminal and type the command }}}

::

    annotate("root", xy=(-4,0))  

.. R34

Switch to the terminal for the solution.
As we can see, every annotate command makes a new annotation on the figure.

Now we have everything we need to decorate a plot, but the plot would be
incomplete if we can not set the limits of axes. This can be done using the
button provided on the plot window.

Else limits also can be get and set from the terminal. 
Use "xlim()" and "ylim()" functions to get the limits.

.. L35
  
::
   
    xlim()
    ylim()

.. R35

``xlim`` function returns the current x axis limits and ``ylim``
function returns the current y-axis limits.

Set the limits of x-axis from -4 to 5 by giving command xlim(-4,5).

.. L36

::
    
    xlim(-4, 5)

.. R36

.. R37

Similarly set the limits of y-axis appropriately.

.. L37

::
     
    ylim(-15, 2)

.. L38

{{{Show slide containing question 7 }}}

.. R38

Pause the video, do this exercise and then resume the video.

Set the limits of axes such that the area of interest is the 
rectangle (-1, -15) and (3, 0)

.. R39

Switch to the terminal for the solution.
As we can see, the lower and upper limits of x-axis in the question 
are -1 and 3 respectively.
The lower and upper limits of y-axis are -15 and 0 respectively.

.. L39

{{{ Switch to terminal }}}
::

    xlim(-1, 3)
    ylim(-15, 0)

.. R40

This gives us the required rectangle.

.. L40

.. L41

{{{ Show summary slide }}}

.. R41

Let's quickly revise what we have learnt today. In this tutorial we have learnt to, 

 1. Modify the attributes of plot like color, line width, 
    line style by passing additional arguments.
 #. Add title to a plot using 'title' command.
 #. Incorporate LaTeX style formatting by adding a ``$`` sign 
    before and after the part of the string.
 #. Label x and y axes using xlabel() and ylabel() commands.
 #. Add annotations to a plot using annotate() command.
 #. Get and set the limits of axes using xlim() and ylim() commands.

.. L42

{{{ Show the 'self assessment questions' slide}}}

.. R42

Here are some self assessment questions for you to solve.

1. Draw a plot of cosine graph between -2pi to 2pi with line thickness 4.

2. Read through the documentation and find out, is there a way to modify the
   alignment of text in the command ``ylabel``.

   - Yes
   - No

  
3. How do you set the title as x^2-5x+6 in LaTex style formatting.

.. L43

{{{ solutions for the self assessment questions }}}

.. R43

And the answers,

1. In order to plot a cosine graph between the points -2pi and 2pi with line 
thickness 3,we use the ``linspace`` and ``plot`` command as,
::
        
    x = linspace(-2*pi, 2*pi)
    plot(x, cos(x), linewidth=4)

2. No. We do not have an option to modify the alignment of text in the 
   command ``ylabel``.

3. To set the title in LaTex style formatting,we write the equation between two
   dollar signs as,

::

    title("$x^2-5x+6$")


.. L44

{{{ a thank you slide }}}

.. R44

Hope you have enjoyed this tutorial and found it useful.
Thank you!

