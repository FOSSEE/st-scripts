.. 2.5 LO: saving plots (2) 
.. -------------------------
.. * Outline 
..   + basic savefig 
..   + png, pdf, ps, eps, svg 
..   + going to OS and looking at the file 

=======
Savefig
=======

Hello and welcome to the tutorial. In this tutorial you will learn how
to save plots using Python.

Start your IPython interpreter with the command ::

  ipython -pylab

It will start your IPython interpreter with the required python
modules for plotting and saving your plots.

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

{{{ Switch the focus to IPython interpreter window }}}

For saving the plot, we will use savefig function, and it has to be
done with the plot window open. The statement is, ::

  savefig('/home/fossee/sine.png')

Notice that ``savefig`` function takes one argument which is a string
which is the filename. The last 3 characters after the ``.`` in the
filename is the extension or type of the file which determines the
format in which you want to save.

{{{ Highlight the /home/fossee part using mouse movements }}}

Also, note that we gave the full path or the absolute path to which we
want to save the file.

{{{ Highlight the .png part using mouse movements }}}

Here I have used an extension ``.png`` which means i want to save the
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

So in-order to save a plot, we use ``savefig`` function. ``savefig``
can save the plot in many formats, such as pdf - portable document
format, ps - post script, eps - encapsulated post script, svg -
scalable vector graphics, png - portable network graphics which
support transparency etc.

.. #[[slide must give the extensions for the files - Anoop]]

Let us now try to save the plot in eps format. ``eps`` stands for
encapsulated post script, and it can be embedded in your latex
documents.

{{{ Switch focus to the already open plot window }}}

We still have the sine plot with us, and now let us save the plot as
``sine.eps``.

{{{ Switch focus to IPython interpreter }}}

Now, We will save the plot using the function ``savefig`` ::

  savefig('/home/fossee/sine.eps')

{{{ Switch focus to file browser window }}}

Now let us go to ``/home/fossee`` and see the new file created.

{{{ Highlight the file sine.eps with a single mouse click for 2
seconds and then double click and open the file }}}

Yes! the new file ``sine.eps`` is here.

Now you may try saving the same in pdf, ps, svg formats.

Let us review what we have learned in this session! We have learned to
save plots in different formats using the function ``savefig()``.

Thank you!

..  Author: Anoop Jacob Thomas <anoop@fossee.in>
    Reviewer 1:
    Reviewer 2:
    External reviewer:
