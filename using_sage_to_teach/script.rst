.. Objectives
.. ----------

.. By the end of this tutorial you will be able to

..  * use ``@interact`` feature of SAGE
..  * learn to share, publish and edit SAGE worksheets

.. Prerequisites
.. -------------

..   1. Getting started with Sage
     #. Getting started with Symbolics
     
.. Author              : Nishanth Amuluru
   Internal Reviewer   : 
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <put date stamp here, not OK> [2010-10-05]

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to the tutorial on 'Using SAGE to teach'.

.. L2

{{{ Show the slide containing the objectives }}}

.. R2

At the end of this tutorial, you will be able to,

 1. Use ``@interact`` feature of SAGE for better demonstration.
 #. Share, publish and edit SAGE worksheets for collaborative learning.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with Sage" and 
"Getting started with Symbolics."

.. R4

Let us start by looking at a typical example of demonstrating a 
damped oscillation.

.. L4

{{{ Open sage notebook }}}
::

    t = var('t')
    p1 = plot( e^(-t) * sin(2*t), (t, 0, 15))
    show(p1)

.. R5

Now let us reduce the damping factor by half

.. L5
::

    t = var('t')
    p1 = plot(e^(-t/2) * sin(2*t), (t, 0, 15))
    show(p1)

.. R6

Now if we want to reduce the damping factor even more, we would be using
e^(-t/3). We can observe that every time we have to change, all we do is 
change something very small and re-evaluate the cell.

This process can be simplified, using the ``@interact`` feature of SAGE.

.. L6
::

    @interact
    def plot_damped(n=1):
        t = var('t')
        p1 = plot( e^(-t/n) * sin(2*t), (t, 0, 20))
        show(p1)

.. R7

We can see that the function is evaluated and the plot is shown. 
We can also see that there is a field to enter the value of ``n`` and 
it is currently set to ``1``. Let us change it to 2 and hit enter.

.. L7
::

    2<enter>

.. R8

We see that the new plot with reduced damping factor is shown. 
Similarly we can change ``n`` to any desired value and hit enter and the 
function will be evaluated. 

This is a very handy tool while demonstrating or teaching.

Pause the video here, try out the following exercise and resume the video.

.. L8

.. L9

{{{ Show slide with exercise 1 }}}

.. R9

 Plot the sine curve and vary its frequency using the ``@interact`` 
 feature.

.. R10

Switch to your worksheet for solution.

.. L10

{{{ continue from paused state }}}
{{{ Switch to the sage worksheet }}}
::

    @interact
    def sine_plot(n=1):
        x = var('x')
        p2 = plot(sin(n*x), (x, 0, 2*pi))
        show(p2)

.. R11

Often we would want to vary a parameter over range instead of taking it 
as an input from the user. For instance we do not want the user to 
give ``n`` as 0 for the damping oscillation we discussed. In such cases 
we use a range of values as the default argument.

.. L11
::

    @interact
    def plot_damped(n=(1..10)):
        t = var('t')
        p1 = plot( e^(-t/n) * sin(2*t)), (t, 0, 20))
        show(p1)

.. R12

We get similar plot but the only difference is the input widget. 
Here it is a slider unlike an input field. 

.. L12

.. L13

{{{ Move the slider two times and show the plot obtained }}}

.. R13

We can see that as the slider is moved, the
function is evaluated and plotted accordingly.

Pause the video here, try out the following exercise and resume the video.

.. L14

{{{ Show slide with exercise 2 }}}

.. R14

 Take a string as input from user and circular shift it to the left and
 vary the shift length using a slider.

.. R15

For this problem, again we will use the ``@interact`` feature of sage.
We shall first assign a string say 'MADAM' to a variable and then shift 
the alphabets one by one.

.. L15

{{{ continue from paused state }}}
{{{ Switch to the sage worksheet }}}
::

    @interact
    def str_shift(s="MADAM", shift=(0..8)):
        shift_len = shift % len(s)
        chars = list(s)
        shifted_chars = chars[shift_len:] + chars[:shift_len]
        print "Actual String:", s
        print "Shifted String:", "".join(shifted_chars)

.. L16

{{{ Move the slider 2 times and show the output }}}

.. R16

As we move the slider, we see that shifting is taking place.

.. R17

Sometimes we want the user to have only a given set of options. 
We use a list of items as the default argument in such situations.

.. L17
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

.. R18

We can see that buttons are displayed which enables us to select from a 
given set of options.

.. L18

.. L19

{{{ Demonstrate the use of left and right buttons }}}
{{{ press 'left' button and move the slider to show the output
    then press 'right' button and move the slider to show the output }}}

.. R19

We see that, as we select the left or right button, the shifting takes 
place appropriately. 

Thus, we have learnt how to use the ``@interact`` feature of SAGE for better
demonstration. Now we shall look at how to use SAGE worksheets for 
collaborative learning.

.. R20

The first feature we shall see is the ``publish`` feature. Open a worksheet 
and in the top right, we can see a button called ``publish``. 
Click on that and we get a confirmation page with an option for 
re-publishing.

.. L20

{{{ Open a new worksheet and click on the 'publish' button }}}

.. L21

{{{ Demonstrate the actions }}}

.. R21

For now lets forget that option and simply publish by clicking ``yes``. 
The worksheet is now published. 

Now lets sign out and go to the sage notebook home. We see link to browse
published worksheets. Lets click on it and we can see the worksheet. 
This does not require login and anyone can view the worksheet.

Alternatively, if one wants to edit the sheet, there is a link on top 
left corner that enables the user to download a copy of the sheet onto 
their home. This way they can edit a copy of the worksheet.

We have learnt how to publish the worksheets to enable users to edit a 
copy.Next, we shall look at how to enable users to edit the actual 
worksheet itself.

.. L22

{{{ Open a worksheet }}}

.. R22

Let us open the worksheet and we see a link called ``share`` on the 
top right corner of the worksheet. Click the link and we get a box 
where we can type the usernames of users whom we want to share the 
worksheet with. We can even specify multiple users by separating their 
names using commas. Once we have shared the worksheet, the worksheet 
appears on the home of shared users.

.. L23

{{{ Show summary slide }}}

.. R23

This brings us to the end of this tutorial.In this tutorial,
we have learnt to,

 1. Use interactive features of SAGE using ``@interact``.
 #. Publish our work.
 #. Edit a copy of one of the published worksheets.
 #. Share the worksheets with fellow users.

.. L24

{{{Show self assessment questions slide}}}

.. R24

Here are some self assessment questions for you to solve

1. Which default argument, when used with ``@interact`` gives a slider 
   starting at 0 and ending in 10.

   - (0..11)
   - range(0, 11)
   - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   - (0..10)

 2. What is the input widget resulted by using ``n = [2, 4, 5, 9]`` in 
   the default arguments along with ``@interact``.

    - input field
    - set of buttons
    - slider
    - None

.. L25

{{{solution of self assessment questions on slide}}}

.. R25

And the answers,

1. The default argument, used with ``@interact`` which gives a slider 
   starting at 0 and ending in 10 is (0..10).

2. The input widget resulted by using ``n = [2, 4, 5, 9]`` in the
   default arguments along with ``@interact`` will be a set of buttons.

.. L26

{{{ Show the Thank you slide }}}

.. R26

Hope you have enjoyed this tutorial and found it useful.
Thank you!

