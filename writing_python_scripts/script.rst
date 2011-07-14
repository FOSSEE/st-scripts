.. Objectives
.. ----------

.. By the end of this tutorial, you will be able to 

..  * Understand what is importing
..  * Write your own Python modules
..  * Understand the ``__name__=="__main__"`` idiom

.. Prerequisites
.. -------------
.. 1. Using Python modules
     
.. Author              : Nishanth Amuluru
   Internal Reviewer   : Punch
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <15-11-2010, Anand, OK> [2010-10-05]

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to the tutorial on "Writing Python scripts".

.. L2

{{{ Show the slide containing the objectives }}}

..R2

At the end of this tutorial, you will be able to, 

  1. Understand what is importing.
  #. Write your own Python modules.
  #. Understand the ``__name__=="__main__"`` idiom

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Using Python modules".

.. R4

Often we will have to reuse the code that we have written. We do that by
writing functions. Functions are bundled into packages and are imported 
as and when required in other scripts.

.. L4

.. R5

Let us first write a function that computes the gcd of two numbers and 
save it in a script.Open an editor and type the code.Please take care 
of the indentation.

.. L5

{{{ Open an editor and start typing out the following code }}}
::

    def gcd(a, b):

        while b:
            a, b = b, a%b

        return a

.. R6

We shall write a test function in the script that tests the gcd function 
every time the script is run.

.. L6

{{{ Add the following lines to the script }}}
::

    if gcd(40, 12) == 4:
        print "Everything OK"
    else:
        print "The GCD function is wrong"

.. L7

{{{ Show slide containing GCD code }}}
{{{ Keep open for sometime and then continue }}}

.. R7

.. R8

Let us save the file as script.py in ``/home/fossee/gcd_script.py``

.. L8

{{{ Save the script as ``gcd_script.py`` }}}

.. R9

We shall run the script by typing

.. L9

{{{ Open a terminal }}}
::

    python /home/fossee/gcd_script.py

.. R10

We can see that the script is executed and everything is fine.

What if we want to use the gcd function in some of our other scripts. 
This is also possible since every python file can be used as a module.

But first, we shall understand what happens when you import a module.

.. L10

.. R11

Open IPython and type

.. L11

{{{ Open another terminal and type ipython }}}
::

    import sys
    sys.path

.. R12

This is a list of locations where python searches for a module when it
encounters an import statement.

Hence, when we just did ``import sys``, python searches for a file
named sys.py or a folder named sys in all these locations one by one,
until it finds one.

We can place our script in any one of these locations and can import it.

The first item in the list is an empty string which means the current
working directory is also searched.

Alternatively, we can also import the module if we are working in same 
directory where the script exists.

.. L12

.. L13

{{{ Close the current terminal }}}

.. R13

.. R14

Since we are in /home/fossee, we can simply do

.. L14

{{{ Switch to the first terminal }}}
::

    import gcd_script.py

.. R15
    
We can see that the gcd_script is imported. But the test code that we 
added at the end of the file is also executed.

But we want the test code to be executed only when the file is run as 
a python script and not when it is imported.

This is possible by using ``__name__`` variable.

First, we shall look at how to use the idiom and then understand how 
it works.

.. L15

.. L16

{{{ Switch to slide, __name__ variable }}}

.. R16

Go to the file and add this line as the beginning of the code
and indent the code accordingly.

.. L17

{{{ Switch to gcd_script.py and add this line after the 
    line ``return a`` }}}
::

    if __name__ == "__main__":
     
.. R17

.. R18
   
Let us first run the code.

.. L18

{{{ Switch back to the terminal }}}
::

    python gcd_script.py

.. R19

We can see that the test runs successfully.

Now we shall import the file

.. L19
::
    
    import gcd_script

.. R20

We see that now the test code is not executed.

The ``__name__`` variable is local to every module and it is equal to
``__main__`` only when the file is run as a script.

Hence, all the code that goes in to the if block, ``if __name__ ==
"__main__":`` is executed only when the file is run as a python
script.

.. L20

.. L21

{{{ Show summary slide }}}

.. R21

This brings us to the end of the tutorial.In this tutorial, we have 
learnt to,

 1. Know what happens when we import a module.
 #. Use a script as a module.
 #. Write test functions using the ``__name__`` idiom. 

.. L22

{{{Show self assessment questions slide}}}

.. R22

Here are some self assessment questions for you to solve

1. Which of the following variables contains the locations to search for
    python modules

   - sys.pythonpath
   - sys.path
   - os.pythonpath
   - os.path


2. A module should contain only functions.
   - True 
   - False

  
3. The script ``utils.py`` is in one of locations of PYTHONPATH and 
   contains the following code
::

    def show(x):
        print x

    show("Hello World")

    if __name__ == "__main__":

        show("Hello Test")

  How do you use the ``show`` function after doing ``import utils``

   - utils.show("hey")
   - show("hey")
   - utils.py.show("hey")
   - utils.py.show.py("hey")

.. L23

{{{solution of self assessment questions on slide}}}

.. R23

And the answers,

1. ``sys.path`` contains the locations to search for python modules.

2. False. A module can contain a wide range of functions.

3. After doing ``import utils``, we can use the function ``show()`` as,
::

    utils.show("hey")

.. L24

{{{ Show the Thank you slide }}}

.. R24

Hope you have enjoyed this tutorial and found it useful.
Thank you!

