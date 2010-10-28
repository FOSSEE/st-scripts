.. Objectives
.. ----------

.. By the end of this tutorial, you will be able to

.. 1. Defining symbolic expressions in sage.  
.. # Using built-in costants and functions. 
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
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]

Symbolics with Sage
-------------------

Hello friends and welcome to the tutorial on symbolics with sage.

{{{ Show welcome slide }}}


.. #[Madhu: What is this line doing here. I don't see much use of it]

During the course of the tutorial we will learn

{{{ Show outline slide  }}}

* Defining symbolic expressions in sage.  
* Using built-in costants and functions. 
* Performing Integration, differentiation using sage. 
* Defining matrices. 
* Defining Symbolic functions.  
* Simplifying and solving symbolic expressions and functions.

We can use Sage for symbolic maths. 

On the sage notebook type::
   
    sin(y)

It raises a name error saying that y is not defined. But in sage we
can declare y as a symbol using var function.


::
    var('y')
   
Now if you type::

    sin(y)

sage simply returns the expression.


Thus sage treats sin(y) as a symbolic expression . We can use
this to do  symbolic maths using sage's built-in constants and
expressions..


So let us try ::
   
   var('x,alpha,y,beta') 
   x^2/alpha^2+y^2/beta^2
 
taking another example
   
   var('theta')
   sin^2(theta)+cos^2(theta)


Similarly, we can define many algebraic and trigonometric expressions
using sage .


Sage also provides a few built-in constants which are commonly used in
mathematics .

example : pi,e,infinity , Function n gives the numerical values of all these
    constants.

{{{ Type n(pi)
   	n(e)
	n(oo) 
    On the sage notebook }}}  



If you look into the documentation of function "n" by doing

.. #[Madhu: "documentation of the function "n"?]

::
   n(<Tab>

You will see what all arguments it takes and what it returns. It will be very
helpful if you look at the documentation of all functions introduced through
this script.



Also we can define the no. of digits we wish to use in the numerical
value . For this we have to pass an argument digits.  Type

.. #[Madhu: "no of digits"? Also "We wish to obtain" than "we wish to
     use"?]
::

   n(pi, digits = 10)

Apart from the constants sage also has a lot of builtin functions like
sin,cos,log,factorial,gamma,exp,arcsin etc ...
lets try some of them out on the sage notebook.


::
     
   sin(pi/2)
   
   arctan(oo)
     
   log(e,e)


Given that we have defined variables like x,y etc .. , We can define
an arbitrary function with desired name in the following way.::

       var('x') 
       function('f',x)


Here f is the name of the function and x is the independent variable .
Now we can define f(x) to be ::

     f(x) = x/2 + sin(x)

Evaluating this function f for the value x=pi returns pi/2.::
	   
	   f(pi)

We can also define functions that are not continuous but defined
piecewise.  Let us define a function which is a parabola between 0
to 1 and a constant from 1 to 2 .  Type the following as given on the
screen

::
      

      var('x') 
      h(x)=x^2 g(x)=1 
      f=Piecewise(<Tab>

{{{ Show the documentation of Piecewise }}} 
    
::
      f=Piecewise([[(0,1),h(x)],[(1,2),g(x)]],x) f




We can also define functions which are series 


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


Moving on let us see how to perform simple calculus operations using Sage

For example lets try an expression first ::

    diff(x**2+sin(x),x) 
    2x+cos(x)

The diff function differentiates an expression or a function. Its
first argument is expression or function and second argument is the
independent variable.

We have already tried an expression now lets try a function ::

   f=exp(x^2)+arcsin(x) 
   diff(f(x),x)

To get a higher order differential we need to add an extra third argument
for order ::
 
   diff(<tab> diff(f(x),x,3)

in this case it is 3.


Just like differentiation of expression you can also integrate them ::

     x = var('x') 
     s = integral(1/(1 + (tan(x))**2),x) 
     s



Many a times we need to find factors of an expression ,we can use the "factor" function

::
    factor(<tab> 
    y = (x^100 - x^70)*(cos(x)^2 + cos(x)^2*tan(x)^2) 
    f = factor(y)

One can  simplify complicated expression ::
    
    f.simplify_full()

This simplifies the expression fully . We can also do simplification
of just the algebraic part and the trigonometric part ::

    f.simplify_exp() 
    f.simplify_trig()
    


One can also find roots of an equation by using find_root function::

    phi = var('phi') 
    find_root(cos(phi)==sin(phi),0,pi/2)

Lets substitute this solution into the equation and see we were
correct ::

     var('phi') 
     f(phi)=cos(phi)-sin(phi)
     root=find_root(f(phi)==0,0,pi/2) 
     f.substitute(phi=root)

as we can see when we substitute the value the answer is almost = 0 showing 
the solution we got was correct.




Lets us now try some matrix algebra symbolically ::



   var('a,b,c,d') 
   A=matrix([[a,1,0],[0,b,0],[0,c,d]]) 
   A

Now lets do some of the matrix operations on this matrix


::
    A.det() 
    A.inverse()



{{{ Part of the notebook with summary }}}

So in this tutorial we learnt how to


* We learnt about defining symbolic expression and functions.  
* Using built-in constants and functions.  
* Using <Tab>  to see the documentation of a function.  
* Simple calculus operations .  
* Substituting values in expression using substitute function.
* Creating symbolic matrices and performing operation on them .

