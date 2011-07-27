.. Objectives
.. ----------

.. By the end of this tutorial, you will be able to

.. 1. Defining a list of numbers
.. 2. Squaring a list of numbers
.. 3. Plotting data points.
.. 4. Plotting errorbars.


.. Prerequisites
.. -------------

..   1. getting started with plotting

     
.. Author              : Amit 
   Internal Reviewer   : Anoop Jacob Thomas<anoop@fossee.in> 
   External Reviewer   :
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]

.. #[[Anoop: Add quickref]]
.. #[[Anoop: Slides are incomplete, add summary slide, thank you slide
   etc.]]

===============================
Plotting   Experimental  Data  
===============================   

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1 

Hello Friends and Welcome to this tutorial on 
"Plotting Experimental data".

.. L2
 
{{{ Show the Objectives Slide }}}

.. R2

At the end of this tutorial, you will be able to,

 1. Define a list of numbers.
 #. perform elementwise squaring of the list. 
 #. Plot data points.
 #. plot errorbars.

.. R3

One needs   to  be  familiar  with  the   concepts  of  plotting
mathematical functions in Python.

We will use data from a Simple Pendulum Experiment to illustrate. 

.. L3

{{{ Simple Pendulum data Slide }}} 

.. R4

As we know for a simple pendulum, length L is directly  proportional to 
the square of time T. We shall be plotting L and T^2 values.

First  we will have  to initiate L and  T values. We initiate them as 
sequence of values.  We define a sequence by comma separated values 
inside two square brackets. This is also called a List.
Let's create two sequences L and t.

.. L4
 
::

    L = [0.1, 0.2, 0.3, 0.4, 0.5,0.6, 0.7, 0.8, 0.9]
    
    T= [0.69, 0.90, 1.19,1.30, 1.47, 1.58, 1.77, 1.83, 1.94]

.. R5

To obtain the square of sequence T we will use the function square
with argument T.This is saved into the variable Tsquare.

.. L5

::

    Tsquare=square(T)
    Tsqaure
    array([  0.4761, 0.81 , 1.4161,  1.69 , 2.1609,  2.4964, 3.1329, 
    3.3489, 3.7636])

.. R6  

Now to plot L vs T^2, we will simply type 

.. L6

::

    plot(L,Tsquare,'.')

.. R7

'.' here displays the plot in a dot pattern.
You can also specify 'o' for big dots.For this let us clear the plot first.

.. L7
::
    
    clf()
    plot(L,Tsquare,'o')
    clf()

.. R8

Let us move further.For any experimental there is always an error in 
measurements due to instrumental and human constraints.Now we shall try 
and take these errors into account in our plots . 

.. L8

.. L9

{{{ Show the slide 'Exercise 1' }}}

.. R9

Pause the video here, try out the following exercise and resume the video.

Plot the given experimental data with large dots.The data is
on your screen. 

.. L10

{{{ Show slide 'Exercise 1 data' }}}

.. R10

The error data we will use is on your screen.

.. R11

We shall again initialize the sequence values in the same manner as we 
did for L and T.

.. L11

::

    delta_L= [0.08,0.09,0.07,0.05,0.06,0.00,0.06,0.06,0.01]
    delta_T= [0.04,0.08,0.03,0.05,0.03,0.03,0.04,0.07,0.08]

.. R12
  
Now to plot L vs T^2 with an error bar we use the function ``errorbar()``.

.. L12 
::

    errorbar(L,Tsquare,xerr=delta_L, yerr=delta_T, fmt='bo')

.. R13

This gives a plot with error bar for x and y axis. The dots are of
blue color. The parameters xerr and yerr are error on x and y axis and
fmt is the format of the plot.

similarly we can draw the same error bar with small red dots just change
the parameters of fmt to 'r.'. 

.. L13
::

    clf()
    errorbar(L,Tsquare,xerr=delta_L, yerr=delta_T, fmt='r.')

.. R14

you can explore other options to errorbar using the documentation 
of errorbar.

.. L14

::

    errorbar?

.. L15

{{{ Show slide with 'Exercise 2' }}}

.. R15

Pause the video here, try out the following exercise and resume the video.

Plot the given experimental data with small dots.Also include
the error in your plot. 

.. L16

{{{ Show slide 'Exercise 2 data' }}}

.. R16

The data is on your screen

.. L17

{{{ Show Summary Slide }}}

.. R17

This brings us to the end of the end of this tutorial.In this tutorial, 
we have learnt to, 

1. to declare a sequence of numbers using the function ``array``.
#. to perform elementwise squaring using the ``square`` function.
#. to use the various options available for plotting like dots,lines.
#. to Plot experimental data such that we can also represent error by 
   using the ``errorbar()`` function. 

.. L18
    
{{Show self assessment questions slide}}

.. R18

Here are some self assessment questions for you to solve

1. Square the following sequence. 
   
   distance_values=[2.1,4.6,8.72,9.03]

2. Plot L v/s T in red plusses.

.. L19

{{{ solution of self assessment questions on slide }}}

.. R19

And the answers,

1.  To square a sequence of values, we use the function ``square``
::
 
    square(distance_values)

2. We pass an additional argument stating the desired parameter
::

    plot(L,T,'r+')

.. L20

{{{ Show the Thank you slide }}}

.. R20

Hope you have enjoyed this tutorial and found it useful.
Thank You!

