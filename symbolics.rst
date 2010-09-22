Symbolics with Sage
-------------------

This tutorial on using Sage for symbolic calculation is brought to you
by Fossee group.

{{{ Part of Notebook with title }}}

We would be using simple mathematical functions on the sage notebook
for this tutorial.

During the course of the tutorial we will learn

{{{ Part of Notebook with outline }}}

To define symbolic expressions in sage.  Use built-in costants and
function. Integration, differentiation using sage. Defining
matrices. Defining Symbolic functions. Simplifying and solving
symbolic expressions and functions.

.. #[Nishanth]: The formatting is all messed up
                First fix the formatting and compile the rst
                The I shall review

Using sage we can perform mathematical operations on symbols .

On the sage notebook type::
   
    sin(y)

It raises a name error saying that y is not defined . But in sage we
can declare y as a symbol using var function. ::
   
    var('y')
   
Now if you type::

    sin(y)

     sage simply returns the expression .

thus now sage treats sin(y) as a symbolic expression . You can use
this to do a lot of symbolic maths using sage's built-in constants and
expressions .

Try out ::
   
   var('x,alpha,y,beta') x^2/alpha^2+y^2/beta^2
 
Similarly , we can define many algebraic and trigonometric expressions
using sage .



Sage also provides a few built-in constants which are commonly used in
mathematics .

example : pi,e,oo , Function n gives the numerical values of all these
    constants.

For instance::

   n(e)
   
   2.71828182845905

gives numerical value of e.

If you look into the documentation of n by doing ::

   n(<Tab>

You will see what all arguments it can take etc .. It will be very
helpful if you look at the documentation of all functions introduced
      

Also we can define the no of digits we wish to use in the numerical
value . For this we have to pass an argument digits.  Type::
  
   n(pi, digits = 10)

Apart from the constants sage also has a lot of builtin functions like
sin,cos,sinh,cosh,log,factorial,gamma,exp,arcsin,arccos,arctan etc ...
lets try some out on the sage notebook. ::
     
   sin(pi/2)
   
   arctan(oo)
     
   log(e,e)


Given that we have defined variables like x,y etc .. , We can define
an arbitrary function with desired name in the following way.::

       var('x') function(<tab> {{{ Just to show the documentation
       extend this line }}} function('f',x)

Here f is the name of the function and x is the independent variable .
Now we can define f(x) to be ::

     f(x) = x/2 + sin(x)

Evaluating this function f for the value x=pi returns pi/2.::
	   
	   f(pi)

We can also define function that are not continuous but defined
piecewise.  We will be using a function which is a parabola between 0
to 1 and a constant from 1 to 2 .  type the following as given on the
screen::
      

      var('x') h(x)=x^2 g(x)=1 f=Piecewise(<Tab> {{{ Just to show the
      documentation extend this line }}}
      f=Piecewise([[(0,1),h(x)],[(1,2),g(x)]],x) f

Checking f at 0.4, 1.4 and 3 :: f(0.4) f(1.4) f(3)

for f(3) it raises a value not defined in domain error .


Apart from operations on expressions and functions one can also use
them for series .

We first define a function f(n) in the way discussed above.::

   var('n') function('f', n)


To sum the function for a range of discrete values of n, we use the
sage function sum.

 For a convergent series , f(n)=1/n^2 we can say ::
   
   var('n') function('f', n)

   f(n) = 1/n^2

   sum(f(n), n, 1, oo)

For the famous Madhava series :: var('n') function('f', n)

    f(n) = (-1)^(n-1)*1/(2*n - 1)

This series converges to pi/4. It was used by ancient Indians to
interpret pi.

For a divergent series, sum would raise a an error 'Sum is
divergent' :: 
	
	var('n') 
	function('f', n) 
	f(n) = 1/n sum(f(n), n,1, oo)




We can perform simple calculus operation using sage

For example lets try an expression first ::

    diff(x**2+sin(x),x) 2x+cos(x)

The diff function differentiates an expression or a function . Its
first argument is expression or function and second argument is the
independent variable .

We have already tried an expression now lets try a function ::

   f=exp(x^2)+arcsin(x) diff(f(x),x)

To get a higher order differentiation we need to add an extra argument
for order ::
 
   diff(<tab> diff(f(x),x,3)


in this case it is 3.


Just like differentiation of expression you can also integrate them ::

     x = var('x') s = integral(1/(1 + (tan(x))**2),x) s



To find factors of an expression use the function factor

    factor(<tab> y = (x^100 - x^70)*(cos(x)^2 + cos(x)^2*tan(x)^2) f =
    factor(y)

One can also simplify complicated expression using sage ::
    f.simplify_full()

This simplifies the expression fully . You can also do simplification
of just the algebraic part and the trigonometric part ::

    f.simplify_exp() f.simplify_trig()
    

One can also find roots of an equation by using find_root function::

    phi = var('phi') find_root(cos(phi)==sin(phi),0,pi/2)

Lets substitute this solution into the equation and see we were
correct ::

     var('phi') f(phi)=cos(phi)-sin(phi)
     root=find_root(f(phi)==0,0,pi/2) f.substitute(phi=root)


as we can see the solution is almost equal to zero .


We can also define symbolic matrices ::



   var('a,b,c,d') A=matrix([[a,1,0],[0,b,0],[0,c,d]]) A


Now lets do some of the matrix operations on this matrix ::


    A.det() A.inverse()

You can do ::
    
    A.<Tab>

To see what all operations are available


{{{ Part of the notebook with summary }}}

So in this tutorial we learnt how to


We learnt about defining symbolic expression and functions .  
And some built-in constants and functions .  
Getting value of built-in constants using n function.  
Using Tab to see the documentation.  
Also we learnt how to sum a series using sum function.  
diff() and integrate() for calculus operations .  
Finding roots , factors and simplifying expression using find_root(), 
factor() , simplify_full, simplify_exp , simplify_trig .
Substituting values in expression using substitute function.
And finally creating symbolic matrices and performing operation on them .
