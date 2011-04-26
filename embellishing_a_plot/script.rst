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

Hello friends and welcome to the tutorial on Embellishing Plots.


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

Let us start ipython with pylab loaded,open the terminal and type 
::
   
    ipython -pylab

.. L3

{{{ open the terminal and type ipython -pylab }}}

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
The additional argument that we shall be passing in here now is the
colour argument. We shall first clear the figure and plot the same now in
red colour. 

.. L5
     
::
   
    clf()
    plot(x, sin(x), 'r')

.. R6

As we can see we have the same plot but now in red colour.

.. L6

{{{Move the mouse pointer on the plot}}}

.. R7

To alter the thickness of the line, we use the ``linewidth`` argument
in the plot command. 

.. L7
    
::
     
    plot(x, cos(x), linewidth=2)

.. R8

This produces a plot with a thicker line, to be more precise plot with line
thickness 2.

.. L8

{{{ Show the plot and compare the sine and cos plots }}}

.. R9

Let's try out the following exercise

Plot sin(x) in blue colour and with linewidth as 3.

.. L9

{{{ Show slide with Question1 }}}

.. R10

A combination of colour and linewidth would do the job for us.

.. L10

::
    
    clf()
    plot(x, sin(x), 'b', linewidth=3)


.. R11 

Occasionally we would also want to alter the style of line. Sometimes
all we want is just a bunch of points not joined. This is possible by
passing the linestyle argument along with or instead of the colour
argument.

.. L11
   
::
   
    clf()
    plot(x, sin(x), '.')

.. R12

Hence we get a plot with only points.

.. L12
 
{{{Point at the dots on the plot}}}

.. R13

We can produce the same plot but now in blue colour.
 
.. L13
 
  ::
    clf()
    plot(x, sin(x), 'b.')

.. R14
Other available options can be seen in the documentation of plot.

.. L14
  
::
    
    plot?

{{{ Run through the documentation and show the options available }}}

{{{ Show the options available for line style and colors }}}


.. L15

{{{Show slide containing question 2}}}

.. R15

Try out the following exercises

Plot the sine curve with green filled circles.


.. R16

All we have to do is use a combination of linestyle and colour to acheive this.

.. L16

{{{ Switch to terminal and type the following commands }}}  
::
    
    clf()
    plot(x, cos(x), 'go')

.. L17

{{{Show slide containing question 3}}}

.. R17 

Let us try out one more exercise 
 
Plot the curve of x vs tan(x) in red dashed line and linewidth 3.

.. L18

{{{ Switch to terminal and type the following commands }}}
::
   
    clf()
    plot(x, cos(x), 'r--')

.. R19

Now that we know how to produce a bare minimum plot with colour, style
and thickness of our interest, we shall look at decorating the plot.

.. R20

Let us start with a plot for the function -x^2 + 4x - 5.

.. L20

::
   
    plot(x, -x*x + 4*x - 5, 'r', linewidth=2)

{{{ Show the plot window and switch back to terminal }}}

.. R21

We now have the plot in a colour and linewidth of our interest. As you
can see, the figure does not have any description describing the plot.

We will now add a title to the plot by using the ``title`` command.

.. L21
  
::
   
    title("Parabolic function -x^2+4x-5") 

{{{ Show the plot window and point to the title }}}

.. R22

The figure now has a title which describes what the plot is. The
``title`` command as you can see, takes a string as an argument and sets
the title accordingly.

The formatting in the title is messed and it does not look clean. You can imagine
what would be the situation if there were fractions and more complex functions
like log and exp. Wouldn't it be good if there was LaTeX like formatting?

That is also possible by adding a ``$`` sign before and after the part of the 
string that should be in LaTeX style.

.. L22
  
::
    
    title("Parabolic function $-x^2+4x-5$")

.. R23

As we can see we get the polynomial formatted properly.

.. L23

{{{ Point at the polynomial }}}

.. L24

{{{Show slide containing question 4}}}

.. R24

{{{ Let us try out the following exercise }}}

Change the title of the figure such that the whole title is formatted
in LaTeX style.

.. R25

The solution is to enclose the whole string in between $. 

.. L25
  
::
    
    title("$Parabolic function -x^2+4x-5$")

.. R26

Hence it gives a title that looks neatly formatted.

Although we have title, the plot is not complete without labelling x
and y axes. Hence we shall label x-axis to "x" and y-axis to "f(x)".

.. L26
 
::
    
    xlabel("x")

.. L27

{{{ Switch to plot window and show the xlabel }}}

.. R27

As you can see, ``xlabel`` command takes a string as an argument,
similar to the ``title`` command and sets it as the label to x-axis.

.. R28

Similarly, ``ylabel("f(x)")`` sets the name of the y-axis as "f(x)"

.. L28

::
    
    ylabel("f(x)")

{{{ Show the plot window and point to ylabel and switch back to the terminal }}}

.. L29

{{{Show slide containing question 5}}}

.. R29

Now lets try out this exercise.

Set the x and y labels as "x" and "f(x)" in LaTeX style.

Since we need LaTeX style formatting, all we have to do is enclose the string
in between two $. 

.. L30

{{{ Pause for some time and then Show slide with answer 5 }}}

.. R30

{{{ Read out the commands on the slides }}}

    xlabel("$x$")
    ylabel("$f(x)$")

does the job for us.

.. L31

{{{ Show the plot window with clean labels }}}

.. R31

The plot is now almost complete. Except that we have still not seen how to 
name the points. For example the point (2, -1) is the local maxima. We would
like to name the point accordingly. We can do this by using the function ``annotate``.

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

Let's try out this exercise.

Make an annotation called "root" at the point (-4, 0).
What happens to the first annotation ?

.. L33

{{{Show slide containing question 6}}}

.. L34

{{{Show slide with answer 6}}}
{{{ Switch to the terminal and type the command }}}
::

    annotate("root", xy=(-4,0))  

.. R34

As we can see, every annotate command makes a new annotation on the figure.

Now we have everything we need to decorate a plot. but the plot would be
incomplete if we can not set the limits of axes. This is possible using the
button on the plot window.

we shall look at how to get and set them from the terminal.We use "xlim()" and "ylim()" functions.

.. L35
  
::
   
    xlim()
    ylim()

.. R35

We see that ``xlim`` function returns the current x axis limits and ``ylim``
function returns the current y-axis limits.

Let us look at how to set the limits.

.. L36

::
    
    xlim(-4, 5)

.. R36

We see the limits of x-axis are now set to -4 and 5.

.. R37

Similarly we set the limits of y-axis appropriately.

.. L37

::
     
    ylim(-15, 2)


.. L38

{{{ Pause here and try out the following exercises }}}

{{{Show slide containing question 7 and read it out }}}

Set the limits of axes such that the area of interest is the rectangle (-1, -15) and (3, 0)

{{{ continue from paused state }}}

.. R38

As we can see, the lower upper limits of x-axis in the question are -1 and 3.
The limits of y-axis are -15 and 0.

.. L39

{{{Show slide with answer 7}}}

::

    xlim(-1, 3)
    ylim(-15, 0)

.. R39

Hence xlim with limits -1 & 3 and ylim with limits -15 & 0 gives us the required rectangle.

.. L40

{{{ Show summary slide }}}

.. R40

let's revise quickly what we have learnt today. 

 1. to Modify the attributes of plot by passing additional arguments.
 #. to add title to a plot.
 #. to incorporate LaTeX style formatting.
 #. to label x and y axes.
 #. to add annotations to a plot.
 #. to set the limits of axes.

.. L41

{{{ Show the 'self assesment questions' slide}}}

.. R41

Here are some self assessment questions for you to solve.

1. Draw a plot of cosine graph between -2pi to 2pi with line thickness 4.

2. Read thorugh the documentation and find out is there a way to modify the
   alignment of text in the command ``ylabel``.

   - Yes
   - No

  
3. How do you set the title as x^2-5x+6 in LaTex style formatting.

    
.. L42

{{{ solutions for the self assessment questions }}}

.. R42

And the answers,

1. In order to plot a cosine graph between the points -2pi and 2pi with line thickness 3,we use
the ``linspace`` and ``plot`` command as,
::
        
    x = linspace(-2*pi, 2*pi)
    plot(x, cos(x), linewidth=4)

2. No. We do not have an option to modify the alignment of text in the command ``ylabel``.

3. To set the title in LaTex style formatting,we write the equation between two dollar signs as,
::

    title("$x^2-5x+6$")


.. L43

{{{ a thank you slide }}}

.. R43

Hope you have enjoyed and found it useful.
Thankyou!

