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

{{{ Show the first slide }}}

Hello and welcome to the tutorial saving plots.

{{{ switch to next slide, outline slide }}}

In this tutorial you will learn how to save plots using Python, saving
in different formats, and locating the file in the file system.

.. #[Puneeth: file-system is too technical.]

{{{ switch to next slide, a sine wave}}}

Start your IPython interpreter with the command ::

  ipython -pylab

As you know, it will start your IPython interpreter with the required
python modules for plotting and saving your plots.

{{{ Open ipython }}}

Now let us plot something, let us plot a sine wave from minus 3 pi to
3 pi. Let us start by calculating the required points for the plot. It
can be done using linspace as, ::

  x = linspace(-3*pi,3*pi,100)

We have stored required points in x. Now let us plot the points using
the statement ::

  plot(x,sin(x))

{{{ Keep the plot open }}}

Done! we have made a very basic sine plot, now let us see how to save
the plot for future use so that you can embed the plot in your
reports.

.. #[Puneeth: All this is known stuff. You don't have to elaborate so
.. much on it. Just say, let us plot sin function from -3 pi to 3
.. pi. Show the commands, and be done with it. ]

{{{ switch to next slide, savefig() }}}

{{{ Switch the focus to IPython interpreter window }}}

For saving the plot, we will use ``savefig()`` function, and it has to be
done with the plot window open. The statement is, ::

  savefig('/home/fossee/sine.png')

Notice that ``savefig`` function takes one argument which is the
filename. The last 3 characters after the ``.`` in the filename is the
extension or type of the file which determines the format in which you
want to save.

.. #[Puneeth: removed mention of string]

.. #[[Anoop: I think this treatment is better :) ]]

{{{ Highlight the /home/fossee part using mouse movements }}}

Also, note that we gave the full path or the absolute path to which we
want to save the file.

{{{ Highlight the .png part using mouse movements }}}

Here I have used an extension ``.png`` which means I want to save the
image as a PNG file.

Now let us locate ``sine.png`` file saved. We saved the file to
``/home/fossee`` so let us navigate to ``/home/fossee`` using the
file browser.

{{{ Open the browser, navigate to /home/fossee and highlight the file
sine.png }}}

Yes, the file ``sine.png`` is here and let us check it.

{{{ Open the file sine.png and show it for two-three seconds and then
close it and return to IPython interpreter, make sure the plot window
is still open, also don't close the file browser window }}}

{{{ switch to next slide, More on savefig() }}}

So in-order to save a plot, we use ``savefig`` function. ``savefig``
can save the plot in many formats, such as pdf - portable document
format, ps - post script, eps - encapsulated post script, svg -
scalable vector graphics, png - portable network graphics which
support transparency etc.

.. #[[slide must give the extensions for the files - Anoop]]

{{{ switch to next slide, exercise 1 }}}

Let us now try to save the plot in eps format. ``eps`` stands for
encapsulated post script, and it can be embedded in your latex
documents. Pause here and try to figure it out yourself.

{{{ Switch focus to the already open plot window }}}

We still have the sine plot with us, and now let us save the plot as
``sine.eps``.

{{{ switch to next slide, solution 1 }}}

{{{ Switch focus to IPython interpreter }}}

Now, We will save the plot using the function ``savefig`` ::

  savefig('/home/fossee/sine.eps')

{{{ Switch focus to file browser window }}}

Now let us go to ``/home/fossee`` and see the new file created.

{{{ Highlight the file sine.eps with a single mouse click for 2
seconds and then double click and open the file }}}

Yes! the new file ``sine.eps`` is here.

{{{ switch to next slide, exercise 2 }}}

Now you may try saving the same in pdf, ps, svg formats.

{{{ Switch to summary slide }}}

This brings us to the end of this tutorial, in this tutorial we
learned to save plots using the function ``savefig()``. Saving the
plots in different formats and locating the files in the file system.

{{{ switch to Thank you slide }}}

Thank you!
