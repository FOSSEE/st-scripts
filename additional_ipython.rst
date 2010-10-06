.. Author              : Nishanth
   Internal Reviewer 1 : 
   Internal Reviewer 2 : 
   External Reviewer   :

.. Prerequisites: Embellinshing plots

Script
======


Hello friends and welcome to the tutorial on Additional Features of IPython

{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline slide }}}

In this tutorial, we shall look at additional features of IPython that help us
to retreive the commands that we type on the interpreter and then save them
into a file and run it.

Let us start ipython with pylab loaded, by typing
::

    $ ipython -pylab

on the terminal

{{{ shit to terminal and type ipython -pylab }}}

We shall first make a plot and then view the history and save it.
::

    x = linspace(-2*pi, 2*pi, 100)
    plot(x, xsinx(x))

xsin(x) is actually x * sin(x)
::

    plot(x, x*sin(x))
    plot(x, sin(x))
    xlabel("x")
    ylabel("$f(x)$")   
    title("x and xsin")

We now have the plot. Let us look at the commands that we have typed in. The
history can be retreived by using =%hist= command. Type
::

    %hist

As you can see, it displays a list of recent commands that we typed. Every
command has a number in front, to specify in which order and when it was typed.

Please note that there is a % sign before the hist command. This implies that 
%hist is a command that is specific to IPython and not available in vannila 
Python interpreter. These type of commands are called as magic commands.

Also note that, the =%hist= itself is a command and is displayed as the most
recent command. This implies that anything we type in is stored as history, 
irrespective of whether it is command or an error or IPython magic command.

If we want only the recent 5 to be displayed, we pass the number as an argument
to =%hist= command. Hence
::

    %hist 5 

displays the recent 5 commands, inclusive of the =%hist= command.
The default number is 40.

{{{ Pause here and try out the following exercises }}}

%% 1 %% Read through the %hist documenatation and find out how can we list all
        the commands between 5 and 10

{{{ continue from paused state }}}

As we can see from =%hist= documentation,
::

    %hist 5 10

displays the commands from 5 to 10

Now that we have the history, we would like to save the required line of code
from history. This is possible by using the =%save= command.

Before we do that, let us first look at history and identify what lines of code
we require.Type
::

    %hist


{{{ point to the lines }}}

The first command is linspace. But second command is a command that gave us an
error. Hence we do not need seconf. The commands from third to sixth are 
required. The seventh command although is correct, we do not need it since we
are setting the title correctly in the eigthth command.

So we need first third to sixth and the eigthth command for our program.
Hence the syntax of =%save= is
::

    %save /home/fossee/plot_script.py 1 3-6 8

{{{ point to the output of the command }}}

The command saves first and then third to sixth and eighth lines of code into
the specified file.

The first argument to %save is the path of file to save the commands and the
arguments there after are the commands to be saved in the given order.

{{{ goto the file and open it and show it }}}

{{{ Pause here and try out the following exercises }}}

%% 2 %% change the label on y-axis to "y" and save the lines of code
        accordingly

{{{ continue from paused state }}}

we use the command =ylabel= on interpreter as
::

    ylabel("y")

and then do
::

    %save /home/fossee/example_plot.py 1 3-6 10

Now that we have the required lines of code in a file, let us learn how to run
the file as a python script.

We use the IPython magic command =%run= to do this. Type
::

   %run -i /home/fossee/plot_script.py

The script runs but we do not see the plot. This happens because we are running
a script and we are not in interactive mode anymore.

Hence on your terminal type
::

    show()

to show the plot.

{{{ Pause here and try out the following exercises }}}

%% 3 %% Use %hist and %save and create a script that has show in it and run it
        to produce and show the plot.

{{{ continue from paused state }}}

We first look at the history using
::

    %hist 20

Then save the script using
::

    %save /home/fossee/show_included.py 1 3-6 8 10 13
    %run -i /home/fossee/show_included.py

We get the desired plot.

The reason for including a -i after run is to tell the interpreter that if any
name is not found in script, search for it in the interpreter. Hence all these
sin, plot, pi and show which are not available in script, are taken from the
interpreter and used to run the script.

{{{ Pause here and try out the following exercises }}}

%% 4 %% Run the script without using the -i option. Do you find any difference?

{{{ continue from paused state }}}

We see that it raises nameerror saying the name linspace is not found.

{{{ Show summary slide }}}

This brings us to the end of the tutorial.
we have looked at 

 * Retreiving history using =%hist= command
 * Vieweing only a part of history by passing an argument to %hist
 * saving the required lines of code in required order using %save
 * using %run -i command to run the saved script

{{{ Show the "sponsored by FOSSEE" slide }}}

#[Nishanth]: Will add this line after all of us fix on one.
This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thankyou
 
Questions
=========

 1. How do you retrieve the recent 5 commands

    a. ``%hist``
    #. ``%hist -5``
    #. ``%hist 5``
    #. ``%hist 5-10``

    Answer: ``%hist 5``
    
 2. If there were 20 commands typed and ``%hist`` is used. How many commands 
    will be displayed.

    a. 10
    #. 20
    #. 21
    #. 19

    Answer: 21

 3. is ``%hist`` considered as a command

    a. True
    #. False

    Answer: True

 4. how do you retreive the commands from 20 to 50 (inclusive of 20 and 50)

    a. ``%hist 20 50``
    #. ``%hist 19 50``
    #. ``%hist 19 51``
    #. ``%hist 21 50``

    Answer: ``%hist 20 50``

 5. What does the ``%hist 2 5 7`` command do

    a. lists the second, fifth and seventh commands
    #. lists the commands from 2 to 5 and the seventh command
    #. raises an error
    #. lists the commands 2 to 7

    Answer: raises an error

 6. How many commands are displayed when lot of coomands were typed and 
    ``%hist`` is used.

    a. 20
    #. 10
    #. 50
    #. 40

    Answer: 40

 7. How do you save the lines 2 3 4 5 7 9 10 11

    a. ``%save filepath 2-5 7 9-11``
    #. ``%save filepath 2-11``
    #. ``%save filepath``
    #. ``%save 2-5 7 9 10 11``

    Answer: ``%save filepath 2-5 7 9-11``

 8. You are working in /home/user. Where is the file saved when you do
    ``%save hello.py 1-3`` 

    a. /home/user/hello.py
    #. /hello.py
    #. /home/hello.py
    #. /home/user/ipython/hello.py

    Answer: /home/user/hello.py

 9. Which lines are saved by the command ``%save filepath 2-5 7 1`` and in
    which order

    a. 2 3 4 5 7 1
    #. 1 2 3 4 5 6 7
    #. 2 5 7 1
    #. 1 2 5 7

 10. What happens when ``%save filepath line_numbers`` is used and a file
     already exists in that path.

    a. It is overwritten
    #. The commands are added to the file
    #. It raises an error
    #. A prompt to confirm overwriting is displayed 

    Answer: A prompt to confirm overwriting is displayed 

 11. Read through the documentation of ``%hist`` and find its alternative name

    Answer: ``%history``

 12. Are ``%run /home/user/saved.py`` and ``%run /home/user/saved`` the same

   a. Yes
   #. No

   Answer: Yes

 13. The file hello.py contains only one command ``x = x + 1``. What happens
     when you do ``%run hello.py``

    Answer: Raises a nameerror

  14. The file hello.py contains only one command ``x = x + 1``. If value of x
      is 5 and what does ``%run -i hello.py`` do.

    a. raises an error
    #. increments value of x by 1
    #. Does nothing
    
    Answer: increments the value of x by 1
