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

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to the tutorial on "Symbolics with Sage".

.. L2

{{{ Show objectives slide  }}}

.. R2

At the end of this tutorial, you will be able to,

 1. Define symbolic expressions in sage.  
 #. Use built-in constants and functions. 
 #. Perform Integration, differentiation using sage. 
 #. Define matrices. 
 #. Define Symbolic functions.  
 #. Simplify and solve symbolic expressions and functions.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with sage notebook".

In addition to a lot of other things, Sage can do Symbolic Math and 
we shall start with defining symbolic expressions in Sage. 

.. L4

{{{ Open the sage notebook }}}

.. R4

Have your Sage notebook opened. If not, pause the video and
start you Sage notebook. 

.. R5

On the sage notebook type

.. L5
::
   
    sin(y)

.. R6

It raises a name error saying that ``y`` is not defined. We need to
declare ``y`` as a symbol. We do it using the ``var`` function. 

.. L6
::

    var('y')

.. R7
   
Now if you type sin(y),Sage simply returns the expression.

.. L7
::

    sin(y)

.. R8

Sage treats ``sin(y)`` as a symbolic expression. We can use this to do
symbolic math using Sage's built-in constants and expressions.

Let us try out a few examples. 

.. L8
::
   
    var('x,alpha,y,beta') 
    x^2/alpha^2+y^2/beta^2

.. R9

We have defined 4 variables, ``x``, ``y``, ``alpha`` and ``beta`` and have 
defined a symbolic expression using them.
 
Here is an expression in ``theta``  

.. L9
::
   
    var('theta')
    sin(theta)*sin(theta)+cos(theta)*cos(theta)

.. R10

Now that you know how to define symbolic expressions in Sage, here is
an exercise. 

Pause the video here, try out the following exercise and resume the video.

.. L10

.. L11

{{{ show slide showing exercise 1 }}}

.. R11

Define following expressions as symbolic expressions in Sage. 
   
   1. x^2+y^2
   #. y^2-4ax

.. L12

{{{continue from paused state}}}
{{{ show slide showing solution 1 }}}

.. R12

The solution is on your screen.

 var('x,y')
 x^2+y^2
 var('a,x,y')
 y^2-4*a*x

<pause for sometime,then continue>

.. R13

Sage also provides built-in constants which are commonly used in mathematics, 
for instance pi, e, infinity. The function ``n`` gives the numerical values of 
all these constants.

.. L13
:: 

    n(pi) 
    n(e) 
    n(oo)

.. R14
   
If you look into the documentation of function ``n`` by doing n<tab>, You 
will see what all arguments it takes and what it returns.

.. L14
::

    n<Tab>

.. R15

It will be very helpful if you look at the documentation of all functions 
introduced in the course of this script.
Also we can define the number of digits we wish to have in the
constants. For this we have to pass an argument -- digits.

.. L15
::

    n(pi, digits = 10)

.. R16

Apart from the constants Sage also has a lot of built-in functions
like ``sin``, ``cos``, ``log``, ``factorial``, ``gamma``, ``exp``,
``arctan`` which stands for arctangent etc ...

Lets try some of them out on the Sage notebook.

.. L16
::
     
    sin(pi/2)
    arctan(oo)
    log(e,e)

.. R17

Pause the video here, try out the following exercise and resume the video.

.. L17

.. L18

{{{ show slide showing exercise 2 }}}

.. R18

Find the values of the following constants upto 6 digits precision
   
   1. pi^2
   #. euler_gamma^2


Find the value of the following.

   1. sin(pi/4)
   #. ln(23)  

.. L19

{{{continue from paused state}}}
{{{ show slide showing solution 2 }}}
 
.. R19

The solutions are on your screen.

  n(pi^2,digits=6)
  n(sin(pi/4))
  n(log(23,e))
 
<pause for sometime,then continue>

.. R20

Given that we have defined variables like x, y etc., we can define an
arbitrary function with desired name in the following way.

.. L20
::

    var('x') 
    function('f',x)

.. R21

Here f is the name of the function and x is the independent variable .
Now we can define f(x)  

.. L21
::

    f(x) = x/2 + sin(x)

.. R22

Evaluating this function f for the value x=pi returns pi/2.

.. L22
::

    f(pi)

.. R23

We can also define functions that are not continuous but defined
piecewise.  Let us define a function which is a parabola between 0
to 1 and a constant from 1 to 2 .We shall use the function ``Piecewise`` 
which returns a piecewise function from a list of pairs. 
Type the following 

.. L23
::
      
    var('x') 
    h(x)=x^2 
    g(x)=1 
    f=Piecewise([[(0,1),h(x)],[(1,2),g(x)]],x) 
    f

.. R24

We can also define functions convergent series and other series. 
We first define a function f(n) in the way discussed before.

.. L24
::

    var('n') 
    function('f', n)

.. R25

To sum the function for a range of discrete values of n, we use the
sage function sum.
For a convergent series , f(n)=1/n^2 we can say 

.. L25
::
   
    var('n') 
    function('f', n)
    f(n) = 1/n^2
    sum(f(n), n, 1, oo)

.. R26

Let us now try another series 

.. L26
::

    f(n) = (-1)^(n-1)*1/(2*n - 1)
    sum(f(n), n, 1, oo)

.. R27

This series converges to pi/4. 
Pause the video here, try out the following exercise and resume the video. 

.. L27

.. L28

{{{ show slide showing exercise 3 }}}

.. R28

Define the piecewise function

::
  
    f(x)=3x+2 when x is in the closed interval 0 to 4.  
    f(x)=4x^2 between 4 to 6.
   
Sum  of 1/(n^2-1) where n ranges from 1 to infinity. 

.. L29

{{{continue from paused state}}}
{{{ show slide showing solution 3 }}}

.. R29

The solution is on your screen

 var('x')
 h(x) = 3*x+2
 g(x) = 4*x^2
 f = Piecewise([[(0,4),h(x)],[(4,6),g(x)]],x)
 f

 var('n')
 f = 1/(n^2-1)
 sum(f(n), n, 1, oo)

<pause for sometime,then continue>

.. R30

Moving on let us see how to perform simple calculus operations 
using Sage
For example lets try an expression first 

.. L30
::

    diff(x**2+sin(x),x) 

.. R31

The ``diff`` function differentiates an expression or a function. It's
first argument is expression or function and second argument is the
independent variable.
We have already tried an expression now lets try a function 

.. L31
::

    f = exp(x^2) + arcsin(x) 
    diff(f(x),x)

.. R32

To get a higher order differential we need to add an extra third argument
for order 

.. L32
::
 
    diff(f(x),x,3)

.. R33

in this case it is 3.
Just like differentiation of expression you can also integrate them 

.. L33
::

    x = var('x') 
    s = integral(1/(1 + (tan(x))**2),x) 
    s

.. R34

Many a times we need to find factors of an expression, we can use the
"factor" function

.. L34
::

    y = (x^100 - x^70)*(cos(x)^2 + cos(x)^2*tan(x)^2) 
    f = factor(y)

.. R35

One can simplify complicated expression by using the 
function ``simplify``. 

.. L35
::
    
    f.simplify_full()

.. R36

This simplifies the expression fully. We can also do simplification of
just the algebraic part and the trigonometric part 

.. L36
::

    f.simplify_exp() 
    f.simplify_trig()

.. R37
    
One can also find roots of an equation by using ``find_root`` function

.. L37
::

    phi = var('phi') 
    find_root(cos(phi) == sin(phi),0,pi/2)

.. R38

Let's substitute this solution into the equation and see we were
correct 

.. L38
::

    var('phi') 
    f(phi) = cos(phi)-sin(phi)
    root = find_root(f(phi) == 0,0,pi/2) 
    f.substitute(phi=root)

.. R39

As we can see when we substitute the value the answer is almost = 0 showing 
the solution we got was correct.
Pause the video here, try out the following exercise and resume the video. 

.. L39

.. L40

{{{ show slide showing exercise 4 }}}

.. R40

Differentiate the following. 
      
  1. sin(x^3)+log(3x)  , degree=2
  #. x^5*log(x^7)      , degree=4 

Integrate the given expression 
      
  sin(x^2)+exp(x^3) 

Find x
  cos(x^2)-log(x)=0
  Does the equation have a root between 1,2. 

.. L41

{{{continue from paused state}}}
{{{ show slide showing solution 4 }}}

.. R41

The solution is on your screen

 var('x')
 f(x)= x^5*log(x^7)
 diff(f(x),x,5)

 var('x')
 integral(x*sin(x^2),x)

 var('x')
 f=cos(x^2)-log(x)
 find_root(f(x)==0,1,2)

<pause for sometime,then continue>

.. R42

Lets us now try some matrix algebra symbolically 

.. L42
::

    var('a,b,c,d') 
    A=matrix([[a,1,0],[0,b,0],[0,c,d]]) 
    A

.. R43

Now lets do some of the matrix operations on this matrix

.. L43
::
    
    A.det() 
    A.inverse()

.. R44

As we can see, we got the determinant and the inverse of the matrix 
respectively.
Pause the video here, try out the following exercise and resume the video.

.. L44

.. L45

{{{ show slide showing exercise 5 }}} 

.. R45

 Find the determinant and inverse of 

      A = [[x,0,1][y,1,0][z,0,y]]

.. L46

{{{continue from paused state}}}
{{{ show slide showing solution 5 }}}

.. R47

The solution is on your screen

 var('x,y,z')
 A = matrix([[x,0,1],[y,1,0],[z,0,y]])
 A.det()
 A.inverse()

<pause for sometime,then continue>

.. L48

{{{ Show the summary slide }}}

.. R48

This brings us to the end of this tutorial. In this tutorial, 
we have learnt to,

1. Define symbolic expression and functions using the method ``var``.
#. Use built-in constants like pi,e,oo and functions like 
   sum,sin,cos,log,exp and many more.  
#. Use <Tab> to see the documentation of a function. 
#. Do simple calculus using functions
   - diff()--to find a differential of a function
   - integral()--to integrate an expression
   - simplify--to simplify complicated expression. 
#. Substitute values in expressions using ``substitute`` function.
#. Create symbolic matrices and perform operations on them like--
   - det()--to find out the determinant of a matrix
   - inverse()--to find out the inverse of a matrix.

.. L49

{{{Show self assessment questions slide}}}

.. R49

Here are some self assessment questions for you to solve

1. How do you define a name 'y' as a symbol?


2. Get the value of pi upto precision 5 digits using sage?


3. Find third order differential function of

   f(x) = sin(x^2)+exp(x^3)
 
.. L50

{{{solution of self assessment questions on slide}}}

.. R50

And the answers,

1. We define a symbol using the function ``var``.In this case it will be
   ::

    var('y')

2. The value of pi upto precision 5 digits is given as,
   ::

    n(pi,5)

3. The third order differential function can be found out by adding the 
   third argument which states the order.The syntax will be,
   ::

    diff(f(x),x,3)

.. L51

{{{Show thank you slide}}}

.. R51

Hope you have enjoyed this tutorial and found it useful.
Thank You!

