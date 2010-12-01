Plotting   Experimental  Data  
=============================   
Hello  and welcome , this tutorial on  Plotting Experimental data is 
presented by the fossee  team.  

{{{ Show the slide containing title }}}


{{{ Show the Outline Slide }}}

Here  we will discuss plotting  Experimental data. 

1.We will see how we can represent a sequence of numbers in Python. 

2.We will also become fimiliar with  elementwise squaring of such a
sequence. 

3. We will also see how we can use our graph to indicate Error.

One needs   to  be  fimiliar  with  the   concepts  of  plotting
mathematical functions in Python.

We will use  data from a Simple Pendulum  Experiment to illustrate our
points. 

{{{ Simple Pendulum data Slide }}} 

  
  
  
As we know for a simple pendulum length,L is directly  proportional to 
the square of time,T. We shall be plotting L and T^2 values.


First  we will have  to initiate L and  T values. We initiate them as sequence 
of values.  To tell ipython a sequence of values we  write the sequence in 
comma  seperated values inside two square brackets.  This is also  called List 
so to create two sequences

L,t type in ipython shell. ::

    In []: L = [0.1, 0.2, 0.3, 0.4, 0.5,0.6, 0.7, 0.8, 0.9]
    
    In []: t= [0.69, 0.90, 1.19,1.30, 1.47, 1.58, 1.77, 1.83, 1.94]


  
To obtain the  square of sequence t we will  use the function square
with argument t.This is saved into the variable tsquare.::

   In []: tsquare=square(t)
  
   array([  0.4761, 0.81 , 1.4161,  1.69 , 2.1609,  2.4964, 3.1329, 
   3.3489, 3.7636])

  
Now to plot L vs T^2 we will simply type ::

  In []: plot(L,t,.)

'.' here represents to plot use small dots for the point. ::

  In []: clf()

You can also specify 'o' for big dots.::
 
  In []: plot(L,t,o)

  In []: clf()


{{{ Slide with Error data included }}}


Now we  shall try  and take into  account error  into our plots . The
Error values for L and T  are on your screen.We shall again intialize
the sequence values in the same manner as we did for L and t ::

  In []: delta_L= [0.08,0.09,0.07,0.05,0.06,0.00,0.06,0.06,0.01]
  
  In []: delta_T= [0.04,0.08,0.11,0.05,0.03,0.03,0.01,0.07,0.01]


  
Now to plot L vs T^2 with an error bar we use the function errorbar()

The syntax of the command is as given on the screen. ::

    
    In []: errorbar(L,tsquare,xerr=delta_L, yerr=delta_T, fmt='b.')

This gives a  plot with error bar for  x and y axis. The  dots are of
blue color.


similarly we can draw the same error bar with big red dots just change 
the parameters to fmt to 'ro'. ::

    In []: clf()
    In []: errorbar(L,tsquare,xerr=delta_L, yerr=delta_T, fmt='ro')



thats it. you can explore other options to errorbar using the documentation 
of errorbar.::

   In []: errorbar?


{{{ Summary Slides }}}

In this tutorial we have learnt : 

1. How to declare a sequence of number , specifically the kind of sequence we learned was a list.

2. Plotting experimental data extending our knowledge from mathematical functions. 

3. The various options available for plotting dots instead of lines.

4. Plotting experimental data such that we can also represent error. We did this using the errorbar() function.


 {{{ Show the "sponsored by FOSSEE" slide }}}



This tutorial was created as a part of FOSSEE project.

Hope you have enjoyed and found it useful.

 Thankyou

 

Author              : Amit Sethi
Internal Reviewer   :
Internal Reviewer 2 : 
