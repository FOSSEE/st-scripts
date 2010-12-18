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

Hello friends and welcome to the tutorial on Embellishing Plots.

{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline }}}

In this tutorial, we shall look at how to modify the colour, thickness and 
linestyle of a plot. We shall then learn how to add title to a plot and 
then look at adding labels to x and y axes. we shall also look at adding 
annotations to the plot and setting the limits on the axes.

Let us start ipython with pylab loaded, by typing on the terminal

{{{ shift to terminal and type ipython -pylab }}}

::

    ipython -pylab

.. #[madhu: I feel the instructions should precede the actual action,

since while recording we need to know before hand what we need to do]

We shall first make a simple plot and start decorating it.

.. #[madhu: start decorating it should be fine, with is not necessary]

::

    x = linspace(-2, 4, 20)
    plot(x, sin(x))

.. #[madhu: Standard is to choose between -50 to 50 or 0 to 50 with 100
     points right?]

As we can see, the default colour and the default thickness of the
line is as decided by pylab. Wouldn't it be nice if we could control
these parameters in the plot? This is possible by passing additional
arguments to the plot command.

.. #[[Anoop: I think it will be good to rephrase the sentence]]
.. #[madhu: Why "you" here? Shouldn't this be "we" as decided? Also I
     added "the default" check the diff]

The additional argument that we shall be passing in here now is the
colour argument. We shall first clear the figure and plot the same in
red colour. Hence

.. #[Madhu: Note the diff for changes]

::

    clf()
    plot(x, sin(x), 'r')

As we can see we have the same plot but now in red colour.

.. #[Madhu: diff again]

To alter the thickness of the line, we use the ``linewidth`` argument
in the plot command. Hence ::

    plot(x, cos(x), linewidth=2)

produces a plot with a thicker line, to be more precise plot with line
thickness 2.

.. #[[Anoop: I guess it will be good if you say that it affects the
   same plot, as you have not cleared the figure]]
.. #[Madhu: To Anoop, not necessary I feel since they can see it?]

{{{ Show the plot and compare the sine and cos plots }}}

Pause here and try out the following exercises,

.. #[[Anoop: is the above a context switch for the person who does the
   recording, other wise if it an instruction to the person viewing
   the video, then I guess the three braces can be removed.]]

%% 1 %% Plot sin(x) in blue colour and with linewidth as 3

{{{ continue from paused state }}}

A combination of colour and linewidth would do the job for us. Hence
::

    clf()
    plot(x, sin(x), 'b', linewidth=3)

.. #[[Anoop: add clf()]]

produces the required plot

.. #[Nishanth]: I could not think of a SIMPLE recipe approach for
             introducing linestyle. Hence the naive approach.

.. #[[Anoop: I guess the recipe is fine, but would be better if you
   add the problem statement rather than just saying "let's do a simple
   plot"]]

.. #[Madhu: It is good enough.]

Occasionally we would also want to alter the style of line. Sometimes
all we want is just a bunch of points not joined. This is possible by
passing the linestyle argument along with or instead of the colour
argument. Hence ::

    clf()
    plot(x, sin(x), '.')

produces a plot with only points.

To produce the same plot but now in blue colour, we do
::

    clf()
    plot(x, sin(x), 'b.')

Other available options can be seen in the documentation of plot.
::

    plot?

{{{ Run through the documentation and show the options available }}}

{{{ Show the options available for line style and colors }}}

.. #[Madhu: The script needs to tell what needs to be shown or
     explained.]

Pause here and try out the following exercises

.. #[[Anoop: same question as above, should it be read out?]]

%% 2 %% Plot the sine curve with green filled circles.

{{{ continue from paused state }}}

All we have to do is use a combination of linestyle and colour to acheive this.
Hence
::

    clf()
    plot(x, cos(x), 'go')

produces the required plot.

{{{ Pause here and try out the following exercises }}}

%% 3 %% Plot the curve of x vs tan(x) in red dashed line and linewidth 3

{{{ continue from paused state }}}

.. #[Madhu: I did not understand the question]

::
    clf()
    plot(x, cos(x), 'r--')

Now that we know how to produce a bare minimum plot with colour, style
and thickness of our interest, we shall look at decorating the plot.

Let us start with a plot of the function -x^2 + 4x - 5.
::

    plot(x, -x*x + 4*x - 5, 'r', linewidth=2)

{{{ Show the plot window and switch back to terminal }}}

We now have the plot in a colour and linewidth of our interest. As you
can see, the figure does not have any description describing the plot.

.. #[Madhu: Added "not". See the diff]

We will now add a title to the plot by using the ``title`` command.
::

    title("Parabolic function -x^2+4x-5") 

{{{ Show the plot window and point to the title }}}

The figure now has a title which describes what the plot is. The
``title`` command as you can see, takes a string as an argument and sets
the title accordingly.

.. #[Madhu: See the diff]

The formatting in title is messed and it does not look clean. You can imagine
what would be the situation if there were fractions and more complex functions
like log and exp. Wouldn't it be good if there was LaTeX like formatting?

That is also possible by adding a $ sign before and after the part of the 
string that should be in LaTeX style.

for instance, we can use
::

    title("Parabolic function $-x^2+4x-5$")

and we get the polynomial formatted properly.

.. #[Nishanth]: Unsure if I have to give this exercise since enclosing the whole
             string in LaTeX style is not good

.. #[[Anoop: I guess you can go ahead with the LaTeX thing, it's
     cool!]]
.. #[Madhu: Instead of saying LaTeX style you can say Typeset math
     since that is how it is called as. I am not sure as well. It
     doesn't really solve the purpose]

{{{ Pause here and try out the following exercises }}}

%% 4 %% Change the title of the figure such that the whole title is formatted
        in LaTeX style

{{{ continue from the paused state }}}

The solution is to enclose the whole string in between $. Hence,
::

    title("Parabolic function $-x^2+4x-5$")

.. #[[Bhanu: Dollar sign should enclose only the math-expression. change
   made.]]

gives a title that looks neatly formatted.

Although we have title, the plot is not complete without labelling x
and y axes. Hence we shall label x-axis to "x" and y-axis to "f(x)" ::

    xlabel("x")

{{{ Switch to plot window and show the xlabel }}}

As you can see, ``xlabel`` command takes a string as an argument,
similar to the ``title`` command and sets it as the label to x-axis.

.. #[See the diff]

Similarly,
::

    ylabel("f(x)")

sets the name of the y-axis as "f(x)"

{{{ Show the plot window and point to ylabel and switch back to the terminal }}}

{{{ Pause here and try out the following exercises }}}

%% 5 %% Set the x and y labels as "x" and "f(x)" in LaTeX style.

{{{ continue from paused state }}}

Since we need LaTeX style formatting, all we have to do is enclose the string
in between two $. Hence,
::

    xlabel("$x$")
    yalbel("$f(x)$")

does the job for us.

{{{ Show the plot window with clean labels }}}

The plot is now almost complete. Except that we have still not seen how to 
name the points. For example the point (2, -1) is the local maxima. We would
like to name the point accordingly. We can do this by using
::

    annotate("local maxima", xy=(2, -1))

{{{ Show the annotation that has appeared on the plot }}}

As you can see, the first argument to ``annotate`` command is the name we would
like to mark the point as and the second argument is the co-ordinates of the
point at which the name should appear. It is a sequence containing two numbers.
The first is x co-ordinate and second is y co-ordinate.

.. #[[Anoop: I think we should tell explicitely that xy takes a
   sequence or a tuple]]
.. #[Madhu: Agreed to what anoop says and also that xy= is the point
     part should be rephrased I think.]

{{{ Pause here and try out the following exercises }}}

%% 6 %% Make an annotation called "root" at the point (-4, 0)
        What happens to the first annotation ?

{{{ continue from paused state }}}

::

  annotate("root", xy=(-4,0))  

As we can see, every annotate command makes a new annotation on the figure.

Now we have everything we need to decorate a plot. but the plot would be
incomplete if we can not set the limits of axes. This is possible using the
button on the plot window.

we shall look at how to get and set them from the script.
::

    xlim()
    ylim()

We see that ``xlim`` function returns the current x axis limits and ylim
function returns the current y-axis limits.

Let us look at how to set the limits.
::

    xlim(-4, 5)

We see the limits of x-axis are now set to -4 and 5.
Similarly
::

    ylim(-15, 2)

sets the limits of y-axis appropriately.

{{{ Pause here and try out the following exercises }}}

%% 7 %% Set the limits of axes such that the area of interest is the rectangle
        (-1, -15) and (3, 0)

{{{ continue from paused state }}}

As we can see, the lower upper limits of x-axis in the question are -1 and 3.
The limits of y-axis are -15 and 0.

::

    xlim(-1, 3)
    ylim(-15, 0)

Gives us the required rectangle.

{{{ Show summary slide }}}

we have looked at 

 * Modifying the attributes of plot by passing additional arguments
 * How to add title
 * How to incorporate LaTeX style formatting
 * How to label x and y axes
 * How to add annotations
 * How to set the limits of axes

{{{ Show the "sponsored by FOSSEE" slide }}}

.. #[Nishanth]: Will add this line after all of us fix on one.

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thankyou


