.. Objectives
.. ----------

.. By the end of this tutorial, you will be able to

.. 1. Defining symbolic expressions in sage.  
.. # Using built-in constants and functions. 
.. # Performing Integration, differentiation using sage. 
.. # Defining matrices. 
.. # Defining Symbolic functions.  
.. # Simplifying and solving symbolic expressions and functions.


.. Prerequisites
.. -------------

..   1. getting started with sage notebook

     
.. Author              : Amit 
   Internal Reviewer   :  
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <, if OK> [2010-10-05]

Symbolics with Sage
-------------------

Hello friends and welcome to the tutorial on Symbolics with Sage.

{{{ Show welcome slide }}}

During the course of the tutorial we will learn

{{{ Show outline slide  }}}

* Defining symbolic expressions in Sage.  
* Using built-in constants and functions. 
* Performing Integration, differentiation using Sage. 
* Defining matrices. 
* Defining symbolic functions.  
* Simplifying and solving symbolic expressions and functions.

In addtion to a lot of other things, Sage can do Symbolic Math and we shall
start with defining symbolic expressions in Sage. 

Have your Sage notebook opened. If not, pause the video and
start you Sage notebook right now. 

On the sage notebook type::
   
    sin(y)

It raises a name error saying that ``y`` is not defined. We need to
declare ``y`` as a symbol. We do it using the ``var`` function. 
::

    var('y')
   
Now if you type::

    sin(y)

Sage simply returns the expression.

Sage treats ``sin(y)`` as a symbolic expression. We can use this to do
symbolic math using Sage's built-in constants and expressions.

Let us try out a few examples. ::
   
   var('x,alpha,y,beta') 
   x^2/alpha^2+y^2/beta^2

We have defined 4 variables, ``x``, ``y``, ``alpha`` and ``beta`` and
have defined a symbolic expression using them.
 
Here is an expression in ``theta``  ::
   
   var('theta')
   sin(theta)*sin(theta)+cos(theta)*cos(theta)

Now that you know how to define symbolic expressions in Sage, here is
an exercise. 

{{ show slide showing question 1 }}

%% %% Define following expressions as symbolic expressions in Sage. 
   
   1. x^2+y^2
   #. y^2-4ax
  
Please, pause the video here. Do the exercise and then continue. 

The solution is on your screen.

{{ show slide showing solution 1 }}

Sage also provides built-in constants which are commonly used in
mathematics, for instance pi, e, infinity. The function ``n`` gives
the numerical values of all these constants.
:: 
    n(pi) 
    n(e) 
    n(oo)
   
If you look into the documentation of function ``n`` by doing

::
   n(<Tab>

You will see what all arguments it takes and what it returns. It will
be very helpful if you look at the documentation of all functions
introduced in the course of this script.

Also we can define the number of digits we wish to have in the
constants. For this we have to pass an argument -- digits.  Type

::

   n(pi, digits = 10)

Apart from the constants Sage also has a lot of built-in functions
like ``sin``, ``cos``, ``log``, ``factorial``, ``gamma``, ``exp``,
``arcsin`` etc ...

Lets try some of them out on the Sage notebook.
::
     
   sin(pi/2)
   
   arctan(oo)
     
   log(e,e)

Following are exercises that you must do. 

{{ show slide showing question 2 }}

%% %% Find the values of the following constants upto 6 digits
      precision
   
   1. pi^2
   #. euler_gamma^2


%% %% Find the value of the following.

   1. sin(pi/4)
   #. ln(23)  

Please, pause the video here. Do the exercises and then continue.

The solutions are on your screen

{{ show slide showing solution 2 }}

Given that we have defined variables like x, y etc., we can define an
arbitrary function with desired name in the following way.::

       var('x') 
       function('f',x)

Here f is the name of the function and x is the independent variable .
Now we can define f(x) to be ::

     f(x) = x/2 + sin(x)

Evaluating this function f for the value x=pi returns pi/2.::
	   
	   f(pi)

We can also define functions that are not continuous but defined
piecewise.  Let us define a function which is a parabola between 0
to 1 and a constant from 1 to 2 .  Type the following 
::
      

      var('x') 
      h(x)=x^2 
      g(x)=1 

      f=Piecewise([[(0,1),h(x)],[(1,2),g(x)]],x) 
      f

We can also define functions convergent series and other series. 

We first define a function f(n) in the way discussed above.::

   var('n') 
   function('f', n)


To sum the function for a range of discrete values of n, we use the
sage function sum.

For a convergent series , f(n)=1/n^2 we can say ::
   
   var('n') 
   function('f', n)
   f(n) = 1/n^2
   sum(f(n), n, 1, oo)

 
Lets us now try another series ::


    f(n) = (-1)^(n-1)*1/(2*n - 1)
    sum(f(n), n, 1, oo)

This series converges to pi/4. 

Following  are exercises that you must do. 

{{ show slide showing question 3 }}

%% %% Define the piecewise function. 
   f(x)=3x+2 
   when x is in the closed interval 0 to 4.
   f(x)=4x^2
   between 4 to 6. 
   
%% %% Sum  of 1/(n^2-1) where n ranges from 1 to infinity. 

Please, pause the video here. Do the exercise(s) and then continue. 

{{ show slide showing solution 3 }}

Moving on let us see how to perform simple calculus operations using Sage

For example lets try an expression first ::

    diff(x**2+sin(x),x) 

The diff function differentiates an expression or a function. It's
first argument is expression or function and second argument is the
independent variable.

We have already tried an expression now lets try a function ::

   f=exp(x^2)+arcsin(x) 
   diff(f(x),x)

To get a higher order differential we need to add an extra third argument
for order ::
 
   diff(f(x),x,3)

in this case it is 3.

Just like differentiation of expression you can also integrate them ::

     x = var('x') 
     s = integral(1/(1 + (tan(x))**2),x) 
     s

Many a times we need to find factors of an expression, we can use the
"factor" function

::

    y = (x^100 - x^70)*(cos(x)^2 + cos(x)^2*tan(x)^2) 
    f = factor(y)

One can simplify complicated expression ::
    
    f.simplify_full()

This simplifies the expression fully. We can also do simplification of
just the algebraic part and the trigonometric part ::

    f.simplify_exp() 
    f.simplify_trig()
    
One can also find roots of an equation by using ``find_root`` function::

    phi = var('phi') 
    find_root(cos(phi)==sin(phi),0,pi/2)

Let's substitute this solution into the equation and see we were
correct ::

     var('phi') 
     f(phi)=cos(phi)-sin(phi)
     root=find_root(f(phi)==0,0,pi/2) 
     f.substitute(phi=root)

as we can see when we substitute the value the answer is almost = 0 showing 
the solution we got was correct.

Following are a few exercises that you must do. 

%% %% Differentiate the following. 
      
      1. sin(x^3)+log(3x)  , degree=2
      #. x^5*log(x^7)      , degree=4 

%% %% Integrate the given expression 
      
      sin(x^2)+exp(x^3) 

%% %% Find x
      cos(x^2)-log(x)=0
      Does the equation have a root between 1,2. 

Please, pause the video here. Do the exercises and then continue. 


Lets us now try some matrix algebra symbolically ::

   var('a,b,c,d') 
   A=matrix([[a,1,0],[0,b,0],[0,c,d]]) 
   A

Now lets do some of the matrix operations on this matrix
::
    A.det() 
    A.inverse()


Following is an (are) exercise(s) that you must do. 

%% %% Find the determinant and inverse of :

      A=[[x,0,1][y,1,0][z,0,y]]

Please, pause the video here. Do the exercise(s) and then continue. 


{{{ Show the summary slide }}}

That brings us to the end of this tutorial. In this tutorial we learnt
how to

* define symbolic expression and functions
* use built-in constants and functions  
* use <Tab> to see the documentation of a function  
* do simple calculus
* substitute values in expressions using ``substitute`` function
* create symbolic matrices and perform operations on them

