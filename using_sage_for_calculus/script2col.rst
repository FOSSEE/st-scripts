.. Objectives
.. ----------

.. By the end of this tutorial you will --

.. 1. Get an idea of the range of things for which Sage can be used. 
.. #. Know some of the functions for Calculus
.. #. Get some insight into Graphs in Sage. 


.. Prerequisites
.. -------------

.. Getting Started -- Sage  
     
Script
------



+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the title slide }}}                                                     | Hello Friends and  Welcome to the tutorial on 'Using Sage for Calculus'.         |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ show the 'objectives' slide }}}                                              | At the end of this tutorial, you will be able to,                                |
|                                                                                  |                                                                                  |
|                                                                                  |  1. Learn the range of things for which Sage can be used.                        |
|                                                                                  |  #. Perform integrations & other Calculus in Sage.                               |
|                                                                                  |  #. Perform matrix algebra in sage.                                              |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ show the 'pre-requisite' slide }}}                                           | Before beginning this tutorial,we would suggest you to complete the              |
|                                                                                  | tutorial on "Getting started with Sage".                                         |
|                                                                                  |                                                                                  |
|                                                                                  | Let us begin with Calculus. We shall be looking at limits,                       |
|                                                                                  | differentiation, integration, and Taylor polynomial.                             |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ open sage notebook }}}                                                       | We have our Sage notebook running. In case, you don't have it running,           |
|                                                                                  | start is using the command, ``sage --notebook``.                                 |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | To begin with, let us find the limit of the function x*sin(1/x), at x=0.         |
|                                                                                  | To do this we say                                                                |
|     lim(x*sin(1/x), x=0)                                                         |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | As expected, we get the limit to be 0.                                           |
|                                                                                  |                                                                                  |
|     lim(1/x, x=0, dir='right')                                                   | It is also possible to limit a point from one direction. For                     |
|                                                                                  | example, let us find the limit of 1/x at x=0, when approaching from              |
|                                                                                  | the positive side.                                                               |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | We get the limit from positive side.                                             |
|                                                                                  | To find the limit from the negative side, we say,                                |
|     lim(1/x, x=0, dir='left')                                                    |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the 'differential expression' slide }}}                                 | Let us now see how to perform differentiation, using Sage. We shall              |
|                                                                                  | find the differential of the expression ``exp(sin(x^2))/x`` w.r.t ``x``.         |
|                                                                                  | For this, we shall first define the expression, and then use the ``diff``        |
|                                                                                  | function to obtain the differential of the expression. So, switch to the sage    |
|                                                                                  | notebook and type                                                                |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | And we get the expected differential of the expression.                          |
|                                                                                  |                                                                                  |
|     var('x')                                                                     |                                                                                  |
|     f = exp(sin(x^2))/x                                                          |                                                                                  |
|     diff(f, x)                                                                   |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the slide 'Partial Differentiation' }}}                                 | We can also obtain the partial differentiation of an expression with one of the  |
|                                                                                  | vriables. Let us differentiate the expression                                    |
|                                                                                  | ``exp(sin(y - x^2))/x`` w.r.t x and y. Switch to sage notebook and type          |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | Thus we get our partial differential solution.                                   |
|                                                                                  |                                                                                  |
|     var('x y')                                                                   |                                                                                  |
|     f = exp(sin(y - x^2))/x                                                      |                                                                                  |
|     diff(f, x)                                                                   |                                                                                  |
|     diff(f, y)                                                                   |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the 'integration' slide }}}                                             | Now, let us look at integration. We shall use the expression obtained            |
|                                                                                  | from the differentiation that we calculated before, ``diff(f, y)``               |
|                                                                                  | which gave us the expression ---``cos(-x^2 + y)*e^(sin(-x^2 + y))/x``.           |
|                                                                                  | The ``integrate`` command is used to obtain the integral of an                   |
|                                                                                  | expression or function. So, switch to sage notebook and type.                    |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Switch to sage }}}                                                           | As we can see, we get back the correct expression. The minus sign being          |
| ::                                                                               | inside or outside the ``sin`` function doesn't change much.                      |
|                                                                                  |                                                                                  |
|     integrate(cos(-x^2 + y)*e^(sin(-x^2 + y))/x, y)                              | Now, let us find the value of the integral between the limits 0 and              |
|                                                                                  | pi/2.                                                                            |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | Hence we get our solution for the definite integration.                          |
|                                                                                  | Let us now see how to obtain the Taylor expansion of an expression               |
|     integral(e^(sin(-x^2 + y))*cos(-x^2 + y)/x, y, 0, pi/2)                      | using sage. We will obtain the Taylor expansion of ``(x + 1)^n`` up to           |
|                                                                                  | degree 4 about 0.                                                                |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | We easily got the Taylor expansion,using the function ``taylor()``.              |
|                                                                                  | This brings us to the end of the features of Sage for Calculus, that             |
|     var('x n')                                                                   | we will be looking at.                                                           |
|     taylor((x+1)^n, x, 0, 4)                                                     |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the 'More on Calculus' slide }}}                                        | For more on calculus you may look at the Calculus quick-ref from the Sage        |
|                                                                                  | documentation at the given link.                                                 |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ show the 'Equation' slide }}}                                                | Next let us move on to Matrix Algebra.                                           |
|                                                                                  | Let us begin with solving the equation ``Ax = v``, where A is the                |
|                                                                                  | matrix ``matrix([[1,2],[3,4]])`` and v is the vector                             |
|                                                                                  | ``vector([1,2])``.                                                               |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Switch back to sage notebook page }}}                                        | To solve the equation, ``Ax = v`` we simply say                                  |
| ::                                                                               |                                                                                  |
|                                                                                  |                                                                                  |
|     A = matrix([[1,2],                                                           |                                                                                  |
|                 [3,4]])                                                          |                                                                                  |
|     v = vector([1,2])                                                            |                                                                                  |
|     x = A.solve_right(v)                                                         |                                                                                  |
|     x                                                                            |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | To solve the equation, ``xA = v`` we simply say.                                 |
|                                                                                  | The left and right here, denote the position of ``A``, relative to x.            |
|     x = A.solve_left(v)                                                          |                                                                                  |
|     x                                                                            |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ show the 'Summary' slide }}}                                                 | This brings us to the end of this tutorial. In this tutorial we have learned to  |
|                                                                                  |                                                                                  |
|                                                                                  | 1. Use functions like lim(), integrate(), integral(), solve()                    |
|                                                                                  | #. Use sage for performing matrix algebra, integrations & other calculus         |
|                                                                                  | operations using the above mentioned functions.                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the 'Evaluation' slide }}}                                              | Here are some self assessment questions for you to solve.                        |
|                                                                                  |                                                                                  |
|                                                                                  |  1. How do you find the limit of the function x/sin(x) as x tends to 0 from the  |
|                                                                                  |     negative side.                                                               |
|                                                                                  |                                                                                  |
|                                                                                  |  #. Solve the system of linear equations                                         |
|                                                                                  |     x-2y+3z = 7                                                                  |
|                                                                                  |     2x+3y-z = 5                                                                  |
|                                                                                  |     x+2y+4z = 9                                                                  |
|                                                                                  |                                                                                  |
|                                                                                  | Try the xercises and switch to next slide for solutions.                         |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the 'Solutions' slide }}}                                               | 1. To find the limit of the function x/sin(x) as x tends to 0 from negative      |
|                                                                                  | side, use the lim function as: lim(x/sin(x), x=0, dir'left')                     |
|                                                                                  |                                                                                  |
|                                                                                  |  #. A = Matrix([1, -2, 3], [2, 3, -1], [1, 2, 4]])                               |
|                                                                                  |     b = vector([7, 5, 9])                                                        |
|                                                                                  |     x = A.solve_right(b)                                                         |
|                                                                                  |     x                                                                            |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the 'FOSSEE' slide }}}                                                  | FOSSEE is Free and Open-source Software for Science and Engineering Education.   |
|                                                                                  | The goal of this project is to enable all to use open source software tools.     |
|                                                                                  | For more details, please visit the given link.                                   |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the 'About the Spoken Tutorial Project' slide }}}                       | Watch the video available at the following link. It summarizes the Spoken        |
|                                                                                  | Tutorial project. If you do not have good bandwidth, you can download and        |
|                                                                                  | watch it.                                                                        |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the 'Spoken Tutorial Workshops' slide }}}                               | The Spoken Tutorial Project Team conducts workshops using spoken tutorials,      |
|                                                                                  | gives certificates to those who pass an online test.                             |
|                                                                                  |                                                                                  |
|                                                                                  | For more details, please write to contact@spoken-tutorial.org                    |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the 'Acknowledgements' slide }}}                                        | Spoken Tutorial Project is a part of the "Talk to a Teacher" project.            |
|                                                                                  | It is supported by the National Mission on Education through ICT, MHRD,          |
|                                                                                  | Government of India. More information on this mission is available at the        |
|                                                                                  | given link.                                                                      |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Show the 'Thank you' slide }}}                                                | Hope you have enjoyed this tutorial and found it useful.                         |
|                                                                                  | Thank you!                                                                       |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
