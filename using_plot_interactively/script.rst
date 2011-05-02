.. Objectives
.. ----------

.. By the end of this tutorial you will --

.. 1. Create simple plots of mathematical functions
.. 2. Use features of graphical window to manipulate plots



.. Prerequisites
.. -------------

.. Installation of required tools
.. Ipython
     
.. Author              : Amit Sethi
   Internal Reviewer   : 
   External Reviewer   :
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]

Script
-------
.. L1

{{{ Show the first slide containing title, name of the production
team along with the logo of MHRD }}} 

.. R1

Hello Friends and welcome to the tutorial on creating simple plots using
iPython.
I hope you have IPython installed on your computer if not, then refer to the spoken tutorial 
on instaling ipython.

.. L2

{{{ Show Objective Slide }}}

At the end of this tutorial, you will be able to, 

   1. Create simple plots of mathematical functions.
   2. Use features of graphical window to manipulate plots


.. R2



.. R3 

To start ipython, Open the terminal and type  
ipython -pylab and hit enter.

.. L3

:: 
  
    ipython -pylab

.. R4 

Pylab is a python library which provides plotting functionality.It
provides many other important mathematical and scientific
functions.
After running IPython -pylab in your shell, 
the screen will look like this.

.. Pause the video for 2 sec then continue. 

But instead if you get the following error like::

- show the error slide

   `ERROR: matplotlib could NOT be imported!  Starting normal
      IPython.`

Then you will have to install the matplotlib and run this command again.

.. Add some instruction to help user to install matplotlib.

.. L4

{{{ Slide with Error written on it }}}

.. R5

To get array of numbers we use linspace command. 
Type 'linspace' followed by a '?' mark to get detailed documentation/help of it
             
.. L5

:: 
   
    linspace?

.. R6

As the documentation says, it returns `num` evenly spaced samples,
calculated over the interval start and stop.  To illustrate this, lets
try to generate 100 points.Type ``linspace(1,100,100)`` and hit enter.

.. L6

::
    
    linspace(1,100,100)

As you can see a sequence of numbers from 1 to 100 appears.

.. R7

To generate 200 points between 0 and 1, type linspace(0,1,200).

.. L7

::

    linspace(0,1,200)

.. R8

Here,0 is the start , 1 is the stop and 200 is the number of points. In linspace 
the start and stop points can be integers, decimals , or constants.  
To get 100 points between -pi to pi where 'pi' is a constant 
defined by pylab and save the result to the variable,say p. Type p=linspace(-pi,pi,100).
           
.. L8

::

    p = linspace(-pi,pi,100)

.. R9

To get the number of elements or points of a sequence say p type ''len(p)''

.. L9
 
:: 

    len(p)


.. R10

To plot a cosine curve between -pi and pi, we use the plot command.
Here cos(p) gets the cosine value at every point
corresponding to point p. 

.. L10

:: 
     
    plot(p,cos(p)) 

.. R11

We can save cos(p) to variable cosine and then plot it using the
plot function.

.. L11

::

    cosine=cos(p) 
    plot(p,cosine)

.. R12

To clear the plot, use the ``clf()`` function 

.. L12 
     
:: 

    clf()

.. R13

If the plot is not cleared, then any new plot will overlap the previous plot. Hence to avoid 
cluttering the area with overlaid plots use clf() function.
 
Now lets try a sine plot. 

.. L13

:: 

    plot(p,sin(p))

.. R14 

We can manipulate the plot in the graphical window.

.. L14

{{{ Show the slide with all the buttons on it }}}

.. R15

The location of the mouse pointer on the window is displayed in bottom right corner of the window.
By moving the mouse pointer the location of each point is seen.

.. L15

{{Move the mouse along the plot}}

.. R16

To the bottom left of the window,there are a few buttons.The right most among them is
for saving the file. 
Just click on it and type the file name in the box provided. We will save the plot 
by the name `sin_curve` in pdf format.As you can see we can specify the format 
of file from the dropdown. Formats like png ,eps ,pdf, ps are also available.

.. L16

{{{ Save the plot as ``sin_curve`` in pdf format }}}

.. R17

Left to the save button is the slider button by which we can specify the margins.

.. L17

{{{Point the mouse on the slider button}}}

.. L18

{{{ Show how to zoom. Press zoom button and specify region to zoom }}}

.. R18

Left to this is the zoom button by which we can zoom into the plot. Just specify the 
region to zoom into.  

.. L19

{{{ Press Move button and move the axes. }}}

.. R19

The button to the left of it can be used to move the axes of the plot.  

.. L20

{{{ Press Back and Forward Button }}}

.. R20

The next two buttons with left and right arrow icons change the state of the 
plot and take it to the previous state it was in. It more or less acts like the
back and forward button in a browser.  

.. L21

{{{ Press home button }}}

.. R21

The last one is 'home' referring to the initial plot.

.. L22

{{{Show slide with question 1}}}

.. R22

Pause the video and do this exercise. Resume the video once done.


      Plot (sin(x)*sin(x))/x.

      1. Save the plot by the sinsquarebyx.pdf in pdf format.
      #. Zoom and find the maxima.
      #. Bring it back to initial position.

.. L23

{{{ Summary Slide }}}

.. R23

Let's revise quickly what we have learnt today 

  1. To Start Ipython with pylab. 
  #. To Use the linspace function to create `num` equally spaced points in a region.
  #. To Find the length of sequnces using len function.
  #. To Plot mathematical functions using plot function.
  #. To Clear drawing area using clf function. 
  #. Manipulate the plot in the window itself by using functionalities like save, zoom, move, home, arrow buttons. 

.. L24

{{Show self assessment questions slide}}

.. R24

1. Create 100 equally spaced points between -pi/2 and pi/2?

2. How do you clear a figure in ipython?

3. How do find the length of a sequence?

.. L25

{{{ Show solution of self assessment questions slide}}}

.. R25

And the answers,

1. We use the command `linspace(-pi/2,pi/2,100)` to create 100 eually spaced lines between the points -pi/2 and pi/2.

2. We use `clf()` function to clear a figure.
    
3. `len(sequence\_name)` is the function used to find out the length of a sequence.

.. L26

{{{ A thank you slide }}}

.. R26 

Hope you have enjoyed and found it useful.
Thankyou!

