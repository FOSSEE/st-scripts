.. Objectives
.. ----------

.. At the end of this tutorial, you will be able to 

.. 1. Save plots using ``savefig()`` function.
.. #. Save plots in different formats.


.. Prerequisites
.. -------------

..   1. should have ``ipython`` and ``pylab`` installed. 
..   #. getting started with ``ipython``.
..   #. using plot command interactively.
     
.. Author              : Anoop Jacob Thomas <anoop@fossee.in>
   Internal Reviewer   : Puneeth
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <10-11-2010, Anand, OK> [2010-10-05]

.. #[Puneeth: Quickref missing.]

=======
Savefig
=======
.. L1

{{{ Show the first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello and welcome to the tutorial on "saving plots".

.. L2

{{{ Show slide with objectives }}}

.. R2

At the end of this tutorial, you will be able to,

 1. Save plots using ``savefig()`` function.
 #. Save plots in different formats.  

.. L3

{{{ switch to next slide, a sine wave}}}

.. R3

Start your IPython interpreter with the command 
ipython -pylab

.. L4

::

    ipython -pylab

.. R4

As you know, it will start your IPython interpreter with the required
python modules for plotting and saving your plots.

To start with let us plot a sine wave from minus 3 pi to 3 pi.
Let us start by calculating the required points for the plot. It
can be done using linspace as, 

.. L5

::

    x = linspace(-3*pi,3*pi,100)

.. R5

We have stored the required points in x. Now let us plot the points using
the plot statement. 

.. L6

::

    plot(x,sin(x))

{{{ Keep the plot open }}}

.. R6

Done! we have made a very basic sine plot, now let us see how to save
the plot for future use so that you can embed the plot in your
reports.

.. L7

{{{ switch to next slide, savefig() }}}

{{{ Switch the focus to IPython interpreter window }}}

.. R7

For saving the plot, we will use ``savefig()`` function.For this we shall keep the 
plot window open alongside the terminal. The statement is, 

.. L8

::

    savefig('/home/fossee/sine.png')

.. R8

Notice that ``savefig`` function takes one argument which is the
filename. The last 3 characters after the ``.`` in the filename is the
extension or type of the file which determines the format in which you
want to save.

.. L9

{{{ Highlight the /home/fossee part using mouse movements }}}

.. R9

Also, note that we gave the full path or the absolute path to which we
want to save the file.

.. L10

{{{ Highlight the .png part using mouse movements }}}

.. R10

Here we have used an extension ``.png`` which means we want to save the
image as a PNG file.

Now let us locate the file ``sine.png`` which we had saved a while ago.We saved the file to
``/home/fossee`` so let us navigate to ``/home/fossee`` using the
file browser.

.. L11

{{{ Open the browser, navigate to /home/fossee and highlight the file
sine.png }}}

.. R11

Yes, the file ``sine.png`` is here.let us open it and check.

.. L12

{{{ Open the file sine.png and show it for two-three seconds and then
close it and return to IPython interpreter, make sure the plot window
is still open, also don't close the file browser window }}}

{{{ switch to next slide, More on savefig() }}}

.. R12

So in-order to save a plot, we use ``savefig`` function. ``savefig``
can save the plot in many formats, such as pdf - portable document
format, ps - post script, eps - encapsulated post script, svg -
scalable vector graphics, png - portable network graphics which
support transparency etc.

.. L13

{{{ switch to next slide, exercise 1 }}}

.. R13

Let us now try to save the plot in eps format. ``eps`` stands for
encapsulated post script, and it can be embedded in your latex
documents. Pause here and try to figure it out yourself.

.. L14

{{{ Switch focus to the already open plot window }}}

.. R14

We still have the sine plot with us, and now let us save the plot as
``sine.eps``.

.. L15

{{{ switch to next slide, solution 1 }}}

{{{ Switch focus to IPython interpreter }}}

.. R15

Now, We will save the plot using the function ``savefig``

.. L16

::

    savefig('/home/fossee/sine.eps')

{{{ Switch focus to file browser window }}}

.. R16

Now let us go to ``/home/fossee`` and see the new file created.

.. L17

{{{ Highlight the file sine.eps with a single mouse click for 2
seconds and then double click and open the file }}}

.. R17

Yes! the new file ``sine.eps`` is here.

.. L18

{{{ switch to next slide, exercise 2 }}}

.. R18

Now you may try saving the same in pdf, ps, svg formats.

.. L19

{{{ Switch to summary slide }}}

.. R19

This brings us to the end of this tutorial,
let's revise quickly what we have learnt today

 1. to save plots using the ``savefig()`` function.
 #. to save the plots in differnt formats.
    - pdf
    - ps
    - png
    - svg
    - epg
 #. to locate files in the file system.

.. R20

Here are some self assessment questions for you to solve

1. Which command is used to save a plot.

   - saveplot()
   - savefig()
   - savefigure()
   - saveplt()

 
2. ``savefig('sine.png')`` saves the plot in,

   - The root directory ``/`` (on GNU/Linux, Unix based systems)
      ``c:\`` (on windows).
   - Will result in an error as full path is not supplied.
   - The current working directory.
   - Predefined directory like ``/documents``.

.. L20

{{Show self assessment questions slide}}

.. L21

(solution of self assessment questions on slide)

.. R21

And the answers,

1.To save a plot,we use the ``savefig()`` function.

2.Whenever we save a file,it gets saved in the current working directory.

.. L22

{{{ a thank you slide }}}

.. R22

Hope you have enjoyed and found it useful.
Thank you!
