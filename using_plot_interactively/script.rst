.. Objectives
.. ----------

.. By the end of this tutorial you will --

.. 1. Create simple plots of mathematical functions
.. #. Use the Figure window to study plots better



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
I hope you have IPython running on your computer.

.. L2

{{{ Show Objective Slide }}}

.. R2

At the end of this tutorial, you will be able to, 

   1. Create simple plots of mathematical functions.
   #. Use the Figure window to study plots better.

.. R3 

Lets start ipython.Open the terminal and type  
ipython -pylab and hit enter.

.. L3

:: 
  
    ipython -pylab

.. R4 

Pylab is a python library which provides plotting functionality.It
provides many other important mathematical and scientific
functions. After running IPython -pylab in the shell you will see some 
information about ipython and pylab followed by the In[1] prompt.
But if you get an error like ::

   `ERROR: matplotlib could NOT be imported!  Starting normal
      IPython.`

Then you will have to install the matplotlib and run this command again.

.. L4

{{{ Slide with Error written on it }}}

.. R5

Now type 'linspace' followed by a '?' mark in your ipython shell 
             
.. L5

:: 
   
    linspace?

.. R6

as the documentation says, it returns `num` evenly spaced samples,
calculated over the interval start and stop.  To illustrate this, lets
try to generate 100 points.Type ``linspace(1,100,100)`` and hit enter.
As you can see a sequence of numbers from 1 to 100 appears.

.. L6

::
    
    linspace(1,100,100)

.. R7

Now lets try to generate 200 points between 0 and 1,we do that by typing  
linspace(0,1,200).

.. L7

::

    linspace(0,1,200)

.. R8

Here,0 is the start , 1 the stop and 200 the number of points.In linspace 
the start and stop points can be integers, decimals , or constants.  
Let's try and get 100 points between -pi to pi.Here 'pi' is a constant 
defined by pylab. Save this to the variable,say p.
           
.. L8

::

    p = linspace(-pi,pi,100)

.. R9

If we now type ``len(p)``we will get the no. of points.
``len`` function gives the no of elements of a sequence.

.. L9
 
:: 

    len(p)


.. R10

Let's try and plot a cosine curve between -pi and pi.
For this we use the plot command.
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

Now to clear the plot ,we use the ``clf()`` function 

.. L12 
     
:: 

    clf()

.. R13

This is done because if we wish to make another plot,
it will overlap the previous plot.
As we do not wish to clutter the area with overlaid plots ,
we just clear it with clf().  
Now lets try a sine plot. 

.. L13

:: 

    plot(p,sin(p))

.. R14 

We can study the plot better on the plot window by using the 
various options available on it.Let us have a look at these options.

.. L14

{{{ Show the slide 'Plot UI' }}}

.. R15

As we can observe, moving the mouse pointer along the plot gives us 
the location of each point on the plot 

.. L15

{{Move the mouse along the plot}}

.. R16

To the bottom left of the window,there are a few buttons.
The right most among them is for saving the file. 
Just click on it and type the file name. We will save the plot 
by the name `sin_curve` in pdf format.
As you can see we can specify the format of file from the dropdown.
Formats like png ,eps ,pdf, ps are available.

.. L16

{{{ Save the plot as ``sin_curve`` in pdf format }}}

.. R17

Left to the save button is the slider button by which we can 
specify the margins.

.. L17

{{{Point the mouse on the slider button}}}

.. L18

{{{ Show how to zoom. Press zoom button and specify region to zoom }}}

.. R18

Left to this is the zoom button by which we can zoom into the plot.
Just specify the region to zoom into.  

.. L19

{{{ Press Move button and move the axes. }}}

.. R19

The button to the left of it can be used to move the axes of the plot.  

.. L20

{{{ Press Back and Forward Button }}}

.. R20

The next two buttons with left and right arrow icons change the 
state of the plot and take it to the previous state it was in.
It more or less acts like the back and forward button in a browser.  

.. L21

{{{ Press home button }}}

.. R21

The last one is 'home' referring to the initial plot.

.. L22

{{{Show slide with question 1}}}

.. R22

Pause the video here, try out the following exercise and resume the video.

      Plot (sin(x)*sin(x))/x.

      1. Save the plot by the sinsquarebyx.pdf in pdf format.
      #. Zoom and find the maxima.
      #. Bring it back to initial position.

.. L23

{{{ Switch to the Summary Slide }}}

.. R23

Let's revise quickly what we have learnt today 

  1. To Start Ipython with pylab. 
  #. To Use the linspace function to create `num` equally spaced points 
     in a region.
  #. To Find the length of sequences using len function.
  #. To Plot mathematical functions using plot.
  #. To Clear drawing area using clf. 
  #. To Use the UI of plot for studying it better and using functionalities 
     like save,zoom and moving the plots on x and y axis. 

.. L24

{{Show self assessment questions slide}}

.. R24

1. Create 100 equally spaced points between -pi/2 and pi/2?

2. What will the command ''linspace(-pi,pi,100)'' do.
   - returns 100 evenly spaced samples from -pi to pi
   - returns 100 evenly spaced samples from -pi to pi excluding pi but 
     including -pi  
   - returns 100 evenly spaced samples from -pi to pi excluding -pi but 
     including pi
   - returns 100 evenly spaced samples from -pi to pi including both -pi
     and pi

3. How do you find the length of a sequence?

.. L25

{{{ Show solution of self assessment questions slide}}}

.. R25

And the answers,

1. We use the command `linspace(-pi/2,pi/2,100)` to create 100 eually spaced 
   lines between the points -pi/2 and pi/2.

2. The command ''linspace(-pi,pi,100)'' will return 100 evenly spaced samples 
   from -pi to pi including both -pi and pi.
    
3. `len(sequence_name)` is the function used to find out the length of a sequence.

.. L26

{{{ Show thank you slide }}}

.. R26 

Hope you have enjoyed and found it useful.
Thank you!

