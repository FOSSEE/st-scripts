Hello friends and welcome to the tutorial on "Writing Python scripts"

{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline slide }}}

In this tutorial, we shall learn

 * How write Python scripts 

Often we will have to reuse the code that we haave written. We do that by
writing functions. Functions are bundled into packages and are imported as and
required in the script.

Let us first write a function that computes the gcd of two numbers and save it
in a script.

{{{ Open an editor and start typing out the following code }}}
::

    def gcd(a, b):

        while b:
            a, b = b, a%b

        return a

We shall write an test function in the script that tests the gcd function every
time the script is run.

{{{ Add to the script }}}

::

    if gcd(40, 12) == 4:
        print "Everything OK"
    else:
        print "The GCD function is wrong"

Let us save the file as script.py in /home/fossee

We shall run the script by doing
::

    $ python /home/fossee/script.py

We can see that the script is executed and everything is fine.

What if we want to use the gcd function in some of our later scripts. This
is also possible since every python file can be used as a module.

Let us understand what happens when you import a module.

Open IPython and type
::

    import sys

{{{ Show summary slide }}}

This brings us to the end of the tutorial.
we have learnt

 * how to use loadtxt to read files
 * how to generate a least square fit

{{{ Show the "sponsored by FOSSEE" slide }}}

#[Nishanth]: Will add this line after all of us fix on one.
This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thankyou
 
.. Author              : Nishanth
   Internal Reviewer 1 : 
   Internal Reviewer 2 : 
   External Reviewer   :
