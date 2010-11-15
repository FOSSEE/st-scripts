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

{{{ Show the slide containing title }}}

Hello friends and welcome to the tutorial on "Writing Python scripts"

{{{ Show the slide containing the outline slide }}}

In this tutorial, we shall learn

 * How to write Python scripts 

Often we will have to reuse the code that we haave written. We do that by
writing functions. Functions are bundled into packages and are imported as and
when required in other scripts.

Let us first write a function that computes the gcd of two numbers and save it
in a script.

{{{ Open an editor and start typing out the following code }}}
::

    def gcd(a, b):

        while b:
            a, b = b, a%b

        return a

We shall write a test function in the script that tests the gcd function every
time the script is run.

{{{ Add to the script }}}

::

    if gcd(40, 12) == 4:
        print "Everything OK"
    else:
        print "The GCD function is wrong"

Let us save the file as script.py in ``/home/fossee/gcd_script.py``

We shall run the script by typing
::

    $ python /home/fossee/gcd_script.py

We can see that the script is executed and everything is fine.

What if we want to use the gcd function in some of our other scripts. This
is also possible since every python file can be used as a module.

But first, we shall understand what happens when you import a module.

Open IPython and type
::

    import sys
    sys.path

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

Since we are in /home/fossee, we can simply do
::

    import gcd_script
    
We can see that the gcd_script is imported. But the test code that we added at
the end of the file is also executed.

But we want the test code to be executed only when the file is run as a python 
script and not when it is imported.

This is possible by using ``__name__`` variable.

First, we shall look at how to use the idiom and then understand how it works.

Go to the file and add
::

    if __name__ == "__main__":
        
before the test code and indent the test code.

Let us first run the code.
::

    $ python gcd_script.py

We can see that the test runs successfully.

Now we shall import the file
::
    
    import gcd_script

We see that now the test code is not executed.

The ``__name__`` variable is local to every module and it is equal to
``__main__`` only when the file is run as a script.

Hence, all the code that goes in to the if block, ``if __name__ ==
"__main__":`` is executed only when the file is run as a python
script.

{{{ Show summary slide }}}

This brings us to the end of the tutorial.
we have learnt

 * What happens when we import a module
 * How to use a script as a module
 * How to write test functions using the __name__ idiom 

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!

