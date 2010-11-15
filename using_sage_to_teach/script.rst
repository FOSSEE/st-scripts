.. Objectives
.. ----------

.. By the end of this tutorial you will be able to

..  * use ``@interact`` feature of SAGE
..  * learn to share, publish and edit SAGE worksheets

.. Prerequisites
.. -------------

..   1. Getting started with lists
     
.. Author              : Nishanth Amuluru
   Internal Reviewer   : 
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <put date stamp here, not OK> [2010-10-05]

Script
------

{{{ Show the slide containing title }}}

Hello friends and welcome to the tutorial on Using SAGE to teach

{{{ Show the slide containing the outline slide }}}

In this tutorial, we shall learn

 * How to use the "@interact" feature of SAGE for better demonstration
 * How to use SAGE for collaborative learning

Let us look at a typical example of demonstrating a damped oscillation.
::

    t = var('t')
    p1 = plot( e^(-t) * sin(2*t), (t, 0, 15))
    show(p1)

Now let us reduce the damping factor
::

    t = var('t')
    p1 = plot(e^(-t/2) * sin(2*t), (t, 0, 15))
    show(p1)

Now if we want to reduce the damping factor even more, we would be using
e^(-t/3). We can observe that every time we have to change, all we do is change
something very small and re evaluate the cell.

This process can be simplified, using the ``@interact`` feature of SAGE.

::

    @interact
    def plot_damped(n=1):
        t = var('t')
        p1 = plot( e^(-t/n) * sin(2*t), (t, 0, 20))
        show(p1)

We can see that the function is evaluated and the plot is shown. We can also
see that there is a field to enter the value of ``n`` and it is currently set
to ``1``. Let us change it to 2 and hit enter.

We see that the new plot with reduced damping factor is shown. Similarly we can
change ``n`` to any desired value and hit enter and the function will be
evaluated. 

This is a very handy tool while demonstrating or teaching.

{{{ Pause here and try out the following exercises }}}

%% 1 %% Plot the sine curve and vary its frequency using the ``@interact``

{{{ continue from paused state }}}

::

    @interact
    def sine_plot(n=1):
        x = var('x')
        p2 = plot(sin(n*x), (x, 0, 2*pi))
        show(p2)

Often we would want to vary a parameter over range instead of taking it as an
input from the user. For instance we do not want the user to give ``n`` as 0
for the damping oscillation we discussed. In such cases we use a range of
values as the default argument.
::

    @interact
    def plot_damped(n=(1..10)):
        t = var('t')
        p1 = plot( e^(-t/n) * sin(2*t), (t, 0, 20))
        show(p1)

We get similar plot but the only difference is the input widget. Here it is a
slider unlike an input field. We can see that as the slider is moved, the
function is evaluated and plotted accordingly.

{{{ Pause here and try out the following exercises }}}

%% 2 %% Take a string as input from user and circular shift it to the left and
        vary the shift length using a slider

{{{ continue from paused state }}}

::

    @interact
    def str_shift(s="MADAM", shift=(0..8)):
        shift_len = shift % len(s)
        chars = list(s)
        shifted_chars = chars[shift_len:] + chars[:shift_len]
        print "Actual String:", s
        print "Shifted String:", "".join(shifted_chars)

Sometimes we want the user to have only a given set of options. We use a list
of items as the default argument in such situations.
::

    @interact
    def str_shift(s="STRING", shift=(0..8), direction=["Left", "Right"]):
        shift_len = shift % len(s)
        chars = list(s)
        if direction == "Right":
            shifted_chars = chars[-shift_len:] + chars[:-shift_len]
        else:
            shifted_chars = chars[shift_len:] + chars[:shift_len]
        print "Actual String:", s
        print "Shifted String:", "".join(shifted_chars)

We can see that buttons are displayed which enables us to select from a given
set of options.

We have learnt how to use the ``@interact`` feature of SAGE for better
demonstration. We shall look at how to use SAGE worksheets for collaborative
learning.

The first feature we shall see is the ``publish`` feature. Open a worksheet and
in the top right, we can see a button called ``publish``. Click on that and we
get a confirmation page with an option for re publishing.

For now lets forget that option and simply publish by clicking ``yes``. The
worksheet is now published. 

Now lets sign out and go to the sage notebook home. We see link to browse
published worksheets. Lets click on it and we can see the worksheet. This does
not require login and anyone can view the worksheet.

Alternatively, if one wants to edit the sheet, there is a link on top left
corner that enables the user to download a copy of the sheet onto their home.
This way they can edit a copy of the worksheet.

We have learnt how to publish the worksheets to enable users to edit a copy.
Next, we shall look at how to enable users to edit the actual worksheet itself.

Let us open the worksheet and we see a link called ``share`` on the top right
corner of the worksheet. Click the link and we get a box where we can type the
usernames of users whom we want to share the worksheet with. We can even
specify multiple users by seperating their names using commas. Once we have
shared the worksheet, the worksheet appears on the home of shared users.

{{{ Show summary slide }}}

This brings us to the end of the tutorial.
we have learnt

 * How to user interactive feaures of SAGE
 * How to publish our work
 * How to edit a copy of one of the published worksheets
 * How to share the worksheets with fellow users

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!

