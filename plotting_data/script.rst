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

{{{ Show the slide containing title }}}

Hello  and welcome , this tutorial on  Plotting Experimental data is 
presented by the fossee  team.  

{{{ Show the Outline Slide }}}

.. #[[Anoop: outline slide is missing]]

Here  we will discuss plotting  Experimental data. 

1. We will see how we can represent a sequence of numbers in Python. 

2. We will also become familiar with  elementwise squaring of such a
sequence. 

3. How to plot data points using python.

4. We will also see how we can use our graph to indicate Error.

One needs   to  be  familiar  with  the   concepts  of  plotting
mathematical functions in Python.

We will use  data from a Simple Pendulum Experiment to illustrate. 

.. #[[Anoop: what do you mean by points here? if you mean the
   points/numbered list in outline slide, then remove the usage point
   from here.]]

{{{ Simple Pendulum data Slide }}} 

.. #[[Anoop: slides are incomplete, work on slides and context
   switches]]
  
  
As we know for a simple pendulum length,L is directly  proportional to 
the square of time,T. We shall be plotting L and T^2 values.


First  we will have  to initiate L and  T values. We initiate them as sequence 
of values.  We define a sequence by comma seperated values inside two square brackets.  
This is also  called List.Lets create two sequences L and t.

.. #[[Anoop: instead of saying "to tell ipython a sequence of values"
   and make it complicated, we can tell, we define a sequence as]]

.. #[[Anoop: sentence is incomplete, can be removed]]

{{{ Show the initializing L&T slide }}}

Type in ipython shell ::

    L = [0.1, 0.2, 0.3, 0.4, 0.5,0.6, 0.7, 0.8, 0.9]
    
    t= [0.69, 0.90, 1.19,1.30, 1.47, 1.58, 1.77, 1.83, 1.94]

 
To obtain the square of sequence t we will use the function square
with argument t.This is saved into the variable tsquare.::

   tsquare=square(t)
   tsqaure
   array([  0.4761, 0.81 , 1.4161,  1.69 , 2.1609,  2.4964, 3.1329, 
   3.3489, 3.7636])

.. #[[Anoop: how do you get the array([ 0.4761 ....]) output?]]

  
Now to plot L vs T^2 we will simply type ::

  plot(L,tsquare,'.')

.. #[[Anoop: be consistent with the spacing and all.]]

'.' here represents to plot use small dots for the point. ::

  clf()

You can also specify 'o' for big dots.::
 
  plot(L,tsquare,'o')

  clf()


Following are exercises that you must do.

%% %% Plot the given experimental data with large dots.The data is
on your screen. 
 
%% %% Plot the given experimental data with small dots.
The data is on your screen


Please, pause the video here. Do the exercises and then continue. 





.. #[[Anoop: Make sure code is correct, corrected plot(L,t,o) to
   plot(L,t,'o')]]



.. #[[Anoop: again slides are incomplete.]]

For any experimental there is always an error in measurements due to
instrumental and human constaraints.Now we shall try and take into
account error into our plots . The Error values for L and T are on
your screen.We shall again intialize the sequence values in the same
manner as we did for L and t

The error data we will use is on your screen.

{{{ Show the Adding Error Slide }}}
.. #[[Anoop: give introduction to error and say what we are going to
   do]]

::

    delta_L= [0.08,0.09,0.07,0.05,0.06,0.00,0.06,0.06,0.01]
    delta_T= [0.04,0.08,0.03,0.05,0.03,0.03,0.04,0.07,0.08]
  
Now to plot L vs T^2 with an error bar we use the function errorbar()

The syntax of the command is as given on the screen. ::

    
    errorbar(L,tsquare,xerr=delta_L, yerr=delta_T, fmt='b.')

This gives a plot with error bar for x and y axis. The dots are of
blue color. The parameters xerr and yerr are error on x and y axis and
fmt is the format of the plot.


similarly we can draw the same error bar with big red dots just change
the parameters to fmt to 'ro'. ::

    clf()
    errorbar(L,tsquare,xerr=delta_L, yerr=delta_T, fmt='ro')



thats it. you can explore other options to errorbar using the documentation 
of errorbar.::

   errorbar?

Following is an  exercise that you must do.

%% %% Plot the given experimental data with large green dots.Also include
the error in your plot. 

Please, pause the video here. Do the exercise and then continue. 







{{{ Show Summary Slide }}}

In this tutorial we have learnt :



1. How to declare a sequence of numbers.

2. Plotting experimental data.

#. The various options available for plotting dots instead of lines.

#. Plotting experimental data such that we can also represent error. 



 {{{ Show the "sponsored by FOSSEE" slide }}}

.. #[[Anoop: again slides are incomplete]]

This tutorial was created as a part of FOSSEE project.

Hope you have enjoyed and found it useful.

Thank You!

