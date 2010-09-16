Hello and welcome to the tutorial on creating simple plots using
Python.This tutorial is presented by the Fossee group.  
{{{ Show the Title Slide }}} 

I hope you have IPython running on your computer.

In this tutorial we will look at plot command and also how to study
the plot using the UI.

{{{ Show Outline Slide }}}

Lets start ipython on your shell, type :: 

      $ipython -pylab


Pylab is a python library which provides plotting functionality.It
also provides many other important mathematical and scientific
functions. After running IPython -pylab in your shell if at the top of
the result of this command, you see something like ::
 

   `ERROR: matplotlib could NOT be imported!  Starting normal
      IPython.`


{{{ Slide with Error written on it }}}

Then you have to install matplotlib and run this command again.

Now type in your ipython shell ::

             In[]: linpace?



as the documentation says, it returns `num` evenly spaced samples,
calculated over the interval start and stop.  To illustrate this, lets
do it form 1 to 100 and try 100 points.  ::

           In[]: linspace(1,100,100)

As you can see a sequence of numbers from 1 to 100 appears.

Now lets try 200 points between 0 and 1 you do this by typing ::


            In[]: linspace(0,1,200)

0 for start , 1 for stop and 200 for no of points.  In linspace 
the start and stop points can be integers, decimals , or
constants. Let's try and get 100 points between -pi to pi. Type ::
           
            In[]: p = linspace(-pi,pi,100)


'pi' here is constant defined by pylab. Save this to the variable, p
.

If you now ::
     
	   In[]: len(p)

You will get the no. of points. len function gives the no of elements
of a sequence.


Let's try and plot a cosine curve between -pi and pi using these
points.  Simply type :: 


       	  In[]: plot(p,cos(points))

Here cos(points) gets the cosine value at every corresponding point to
p.


We can also save cos(points) to variable cosine and plot it using
plot.::

           In[]: cosine=cos(points) 

	   In[]: plot(p,cosine)

 

Now do ::
       	 
	   In[]: clf()

this will clear the plot.

This is done because any other plot we try to make shall come on the
same drawing area. As we do not wish to clutter the area with
overlaid plots , we just clear it with clf().  Now lets try a sine
plot. ::


    	 In []: plot(p,sin(p))



 
The Window on which the plot appears can be used to study it better.

First of all moving the mouse around gives us the point where mouse
points at.  

Also we have some buttons the right most among them is
for saving the file. 

Just click on it specifying the name of the file.  We will save the plot 
by the name sin_curve in pdf format.

{{{ Action corelating with the words }}}

As you can see I can specify format of file.  
Left to the save button is the slider button to specify the margins.  

{{{ Action corelating with the words  }}}

Left to this is zoom button to zoom into the plot. Just specify the 
region to zoom into.  
The button left to it can be used to move the axes of the plot.  

{{{ Action corelating with the words }}}
 
The next two buttons with a left and right arrow icons change the state of the 
plot and take it to the previous state it was in. It more or less acts like a
back and forward button in the browser.  

{{{ Action corelating with the words }}}

The last one is 'home' referring to the initial plot.

{{{ Action corelating with the words}}}



{{{ Summary Slide }}}


In this tutorial we have looked at 

1. Starting Ipython with pylab 

2. Using linspace function to create `num` equaly spaced points in a region.

3. Finding length of sequnces using  len.
 
4. Plotting mathematical functions using plot.

4. Clearing drawing area using clf 
 
5. Using the UI of plot for studying it better . Using functionalities like save , zoom , moving the plots on x and y axis 

etc ..
 


{{{ Show the "sponsored by FOSSEE" slide }}}

 

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

 

 Hope you have enjoyed and found it useful.

 Thankyou

 

Author              : Amit Sethi
Internal Reviewer   :
Internal Reviewer 2 : 
