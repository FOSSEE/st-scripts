.. Objectives
.. ----------

.. At the end of this tutorial, you will be able to,  

.. 1. invoke the ``ipython`` interpreter . 
.. #. quit the ``ipython`` interpreter. 
.. #. navigate in the history of ``ipython``. 
.. #. use of tab-completion for writing ipython functions. 
.. #. look-up documentation of functions. 
.. #. interrupt incomplete or incorrect commands.

.. Prerequisites
.. -------------
.. (it should be given in the first module)
.. should have ``ipython`` and ``pylab`` installed. 
     
.. Author              : Puneeth 
   Internal Reviewer   : Anoop Jacob Thomas<anoop@fossee.in>
   Language Review     : Bhanukiran 
   External Reviewer   :
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]


Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}


.. R1

Hello Friends and Welcome to the tutorial on "getting started with
``ipython``". 

.. L2

{{{ Show slide with objectives }}}

.. R2

At the end of this tutorial, you will be able to,  

 1. invoke the ``ipython`` interpreter . 
 #. quit the ``ipython`` interpreter. 
 #. navigate the ``ipython`` session history. 
 #. use tab-completion for writing ipython functions. 
 #. look-up documentation of functions. 
 #. interrupt incomplete or incorrect commands.


.. R3 

Let us first see how to start the ``ipython`` interpreter.First
open the terminal, type ``ipython`` in the terminal and hit enter.

.. L3

:: 

    ipython

.. R4

We get a prompt with ``In [1]:`` after getting some information about
the version of Python installed and some help commands. If you get an
error showing ``ipython is not installed``, please refer to the
tutorial on how to install the packages.

.. L4

{{Point to the version information with mouse}}
{{Point to the In[1]: prompt with mouse}}

.. R5

Now,lets see how we can quit the ipython interpreter, press Ctrl-D. 

.. L5

type Ctrl-D.

.. R6

A prompt will apperar to confirm whether you really want to exit, type
y to say yes and quit ipython and n to say no if you dont want to quit
the ipython. Press y.

.. L6
Press y and hit enter. 

.. R7

Now since we have quit the interpretor, let us start it again by
typing ``ipython``

.. L7

:: 

    ipython

.. R8

And now let's see, how to use the interpreter.

Start with the simplest thing, addition.

type 1+2 at the prompt. IPython promptly gives back the output as 3.
Notice that the output is displayed with an ``Out[1]`` indication.

.. L8

:: 

    1+2

    {{Point at the Out[1] prompt}}

.. R9

Let us now try few more operations such as, 5 minus 3, 7
minus 4, 6 into 5. 

.. L9

::

    5 - 3
    7 - 4
    6 * 5

.. R10

Now let's see how the ipython remembers the history of commands ?
let's try an example ``print 1+2``.

Instead of typing the whole thing,use the up arrow key to go back to
the command ``1+2`` which we did before, now use the left-arrow key to
navigate to the beginning of the line and type the word``print``and
press space.We have changed the line to print 1+2, now press enter.
The interpreter prints the result as 3. Please note that the
indication Out square brackets is not shown here.

.. L10

{{Use the up arrow key to go back to the command ``1+2``}}
{{Use left arrow to navigate to start of line }}
Type

::

    'print'

{{Hit enter}}
{{Point at the Out[] prompt}}

.. R11

Now let us do print 10 into 2.  We use the up arrow key to navigate to
the previous command 1+2. Now change ``1 plus 2`` to ``10 into 2`` and
press enter.

.. L11

{{{ Change from    ``print 1+2`` to   ``print 10*2`` }}}

.. R12

Till now, we saw how to invoke the ipython interpreter,quit the
ipython and navigate through previous commands in ipython.  Now, let's
see, what is tab-completion?.  let's take an example, suppose we want
to use the function ``round``. For this we just type ``ro`` at the
prompt and press the tab key.

.. L12

:: 

    ro<tab>
 
.. R13

As you can see on the terminal, IPython completes the command ``ro``
into round, This feature of ipython is called the tab-completion.

.. L13

{{Stay on the terminal}}

.. R14

Let's see some more possibilities of tab completion 
just type ``r`` and then press the  tab.

.. L14

:: 

    r<tab> 

.. R15

 As u can see that IPython does not complete the command. This is
because, there are many possibilities of ``r`` therefore it just lists
out all the possible completions of r.

.. L15

{{Stay on the terminal}}

.. L16

{{Show slide with question 1}}

.. R16

Now let's try out an exercise.Pause the video and solve the problem.

  1. find out the commands starting with "ab"?
  2. list out the commands starting with "a"?

.. R17

``ab`` tab completes to ``abs`` and ``a<tab>`` gives us a list of all
the commands starting with a.


.. L17

(show solution on terminal/slide)


.. R18

Now, let's see what the functions abs is used for.  We will use the
help features of ipython to find out this.  To see the documentation
of a function, type the function name followed by a question mark, and
hit enter. Ipython interpreter will show the documentation for the
function.  Lets us see the documentation of the function abs, type
abs? and press enter

.. L18

::
 
  abs?


.. L19

::

  abs(-19)

  abs(19)

.. R19

As the documentation says, ``abs`` accepts a number as an input and
returns it's absolute value.

lets see few examples,

We get 19, as expected, in both the cases.

.. R20

Now lets try it for decimal numbers; lets try abs(-10.5), we got 10.5
as the result.

.. L20

::

    abs(-10.5)

.. R21

Now try to solve Following exercise,
%%2%% Look-up the documentation of ``round`` and see how to use it.

.. L21   

{{Show slide with question 2}}

.. L22

::

   round?

.. R22

And you can look up the documentation of the function round by typing
round question mark in the ipython interpreter.

.. L23

{{highlight the syntax with mouse hover on terminal}}

.. R23

If you notice, there are extra square brackets around ``ndigits``.
This means that ``ndigits`` is optional and 0 is the default value.
Optional parameters are shown in square brackets in Python
documentation.

The function ``round``, rounds a number to a given precision.

.. R24

Let us now try few more examples with the function round.
Check the output of

::

    round(2.48)
    round(2.48,1)
    round(2.48,2)
    round(2.484)
    round(2.484,1)
    round(2.484,2)

.. L24

{{Show slide with question 3}}

.. L25

{{Show slide with solution 3}}

.. R25

We got 2.0, 2.5, and 2.48 as expected.

.. R26

Let's now see how to correct typing errors which we often make while
typing at the terminal. As already shown, if we haven't hit the enter
key already, we could navigate using the arrow keys and make deletions
using delete or backspace key and correct the errors.

let us make a typing error deliberately,
type 

::

     round(2.484

and hit enter, without closing the parenthesis.

.. L26

:: 

    round(2.484

{{Hit enter}}

.. R27

We get a prompt with dots.  This prompt is the continuation prompt of
``ipython``.  It appears when, the previous line is incomplete. now
complete the command of the same examples with close parenthesis and
press enter.  We got the expected output that is 2.0

.. L27
{{ Point at the prompt with three dots }}

::  

    )

.. R28

In other instances, if we commit a typing error with a longer and more
complex expression and end up with the continuation prompt, we can
type Ctrl-C to interrupt the command and to get back to the
``ipython`` input prompt.

.. L28

<Type any big random number>

:: 

    round(35.488762320
    Ctrl-C

.. R29

Try the following exercise

1. type round(2.484, and press enter. and then cancel the command
   using Ctrl-C.
2. type the command, round(2.484, 2) 

.. L29

{{Show slide with question 4}}
 

.. L30

{ show the solution on terminal and slide }

::

  round(2.484 
  ^C

  round(2.484, 2)

.. R30

.. L31

{{{ show the summary slide and read out the same }}}

.. R31 

let's revise quickly what we have learnt today.

  1. to invoke the ``ipython`` interpreter by typing ipython. 
  #. to quit the ``ipython`` interpreter by using <ctrl>d. 
  #. to navigate in the history of ``ipython`` by using the arrow keys. 
  #. what is tab-completion. 
  #. to see the documentation of functions using question mark.
  #. to interrupt using <ctrl>c when we make an error.

.. R32
  
Here are some self assessment questions for you to solve

1. Ipython is a programming similar to Python?
   True or False

2. Which key combination quits ``ipython``?

   - Ctrl + C
   - Ctrl + D
   - Alt + C
   - Alt + D

3. Which character is used at the end of a command, in Ipython to
   display the documentation.

   - under score (_)
   - question mark (?)
   - exclamation mark (!)
   - ampersand (&)

.. L32

{{Show self assessment questions slide}}


.. L33

(solution of self assessment questions on slide)


.. R33

And the answers,

1. Ipython is not a programming language, it is just an interpreter.
2. We use Ctrl D to quit Ipython interpreter.
3. We use ? at the end of the function name to display its documentation.

.. L34
{{a thank you slide}}

.. R34
Hope you have enjoyed and found it useful.
Thank you!
