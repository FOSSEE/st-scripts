.. Objectives
.. ----------

.. By the end of this tutorial you will be able to

.. #. Retrieve your ipython history 
.. #. View a part of the history 
.. #. Save a part of your history to a file. 
.. #. Run a script from within ipython 


.. Prerequisites
.. -------------

..   1. Embellishing Plots
     
.. Author              : Nishanth Amuluru
   Internal Reviewer   : Amit
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <15-11-2010, Anand, OK> [2010-10-05]

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to the tutorial on "Additional Features of IPython".

.. L2

{{{ Show the slide containing the outline slide }}}

.. R2

At the end of this tutorial, you will be able to,

   1. Retrieve your ipython history. 
   #. View a part of the history. 
   #. Save a part of your history to a file. 
   #. Run a script from within ipython. 

.. R3

Let us start ipython with pylab loaded, by typing ipython -pylab on the terminal.

.. L3

{{{ shift to terminal and type ipython -pylab }}}

::

    ipython -pylab

.. R4

We shall first make a plot and then view the history and save it.

.. L4

::

    x = linspace(-2*pi, 2*pi, 100)
    plot(x, xsinx(x))

.. R5

We got an error saying "xsinx is not defined".This is because
xsin(x) is actually x * sin(x)

.. L5

::

    plot(x, x*sin(x))
    plot(x, sin(x))
    xlabel("x")
    ylabel("$f(x)$")   
    title("x and xsin")

.. R6

We now have the plot. Let us look at the commands that we have typed in. The
history can be retreived by using =%hist= command.Type %hist in your terminal.

.. L6

::

    %hist

.. R7

As you can see, it displays a list of recent commands that we typed. Every
command has a number in front, to specify in which order and when it was typed.

Please note that there is a % sign before the hist command. This implies that 
%hist is a command that is specific to IPython only and not to any other version of python.
These type of commands are called as magic commands.

Also note that, the =%hist= itself is a command and is displayed as the most
recent command. We should note that anything we type in is stored as history, 
irrespective of whether it is command or an error or IPython magic command.

.. L7

.. R8

If we want only the recent 5 commands to be displayed, we pass the number as an argument
to =%hist= command. Hence %hist 5 displays the recent 5 commands, inclusive of the =%hist= command.
The default number is 40.

.. L8

::

    %hist 5 

.. R9

Pause here and try out the following exercise

     Read through the documentation of %hist and find out how to
     list all the commands between 5 and 10.

.. L9

.. L10

{{{ continue from paused state }}}

::

    %hist 5 10

.. R10

As we can see from =%hist= documentation,%hist 5 10 displays the commands from 5 to 10

Now that we have the history, we would like to save the required line of code
from history. This is possible by using the =%save= command.

.. R11

Before we do that, let us first look at history and identify what lines of code we require.Type %hist again.

.. L11

::

    %hist

.. L12

{{{ point to the lines }}}

.. R12

The first command is linspace. But second command is a command that gave us an
error. Hence we do not need second command. The commands from third to sixth are 
required. The seventh command although is correct, we do not need it since we
are setting the title correctly in the eighth command.

.. R13

So we need first third to sixth and the eighth command for our program.
Hence the syntax of =%save= will be

.. L13

{{{ Type as you say }}}

::

    %save /home/fossee/plot_script.py 1 3-6 8

.. L14

{{{ point to the output of the command }}}

.. R14

The command saves the first line of code and then third to sixth followed by the eighth lines of code into
the specified file.

The first argument to %save is the path of file to save the commands and the
arguments there after are the commands to be saved in the given order.

.. L15

{{{ goto the file and open it and show it }}}

.. R15

.. R16

Pause here and try out the following exercise

    Change the label on y-axis to "y" and save the lines of code accordingly.

.. L16

.. L17

{{{ continue from paused state }}}

::

    ylabel("y")

.. R17

we use the command =ylabel= on interpreter 

.. R18

and then do

.. L18

{{{Type as you say}}}

::

    %save /home/fossee/example_plot.py 1 3-6 10

.. R19

Now that we have the required lines of code in a file, let us learn how to run
the file as a python script.

We use the IPython magic command =%run= to do this. Type

.. L19

::

    %run -i /home/fossee/plot_script.py

.. R20

The script runs but we do not see the plot. This happens because when we are running
a script and we are not in interactive mode anymore.

Hence to view the plot type ``show()`` on your terminal 

.. L20

::

    show()

.. R21

Pause here and try out the following exercise

     Use %hist and %save and create a script that has show in it and run it
     to produce and show the plot.

<Pause>

We first look at the history using

.. L21

::

    %hist 20

.. R22

Then save the script using

.. L22

{{{ Say as you type }}}

::

    %save /home/fossee/show_included.py 1 3-6 8 10 13
    %run -i /home/fossee/show_included.py
    show()    

.. R23

We get the desired plot.

The reason for including a -i after run is to tell the interpreter that if any
name is not found in script, search for it in the interpreter. Hence all these
sin, plot, pi and show which are not available in script, are taken from the
interpreter and used to run the script.

.. L23

.. R24

Pause here and try out the following exercise

   Run the script without using the -i option. Do you find any difference?

<Pause>

.. L24

.. L25

::

    %run -i /home/fossee/show_included.py

.. R25

We see that it raises NameError saying that the name linspace is not found.

.. L26

{{{ Show summary slide }}}

.. R26

This brings us to the end of the tutorial.let's revise quickly what we have learnt today- 

 1. to retreive the history using =%hist= command.
 #. to view only a part of history by passing an argument to %hist.
 #. to save the required lines of code in required order using %save.
 #. to use %run -i command to run the saved script.

.. L27

{{Show self assessment questions slide}}

.. R27

Here are some self assessment questions for you to solve

1. How do you retrieve the recent 5 commands

    - ``%hist``
    - ``%hist -5``
    - ``%hist 5``
    - ``%hist 5-10``


2. How do you save the lines 2 3 4 5 7 9 10 11

    - ``%save filepath 2-5 7 9-11``
    - ``%save filepath 2-11``
    - ``%save filepath``
    - ``%save 2-5 7 9 10 11``


3. What will the command ``%hist 5 10`` display.

    - The recently typed commands from 5 to 10 inclusive of the history command	
    - The recently typed commands from 5 to 10 excluding the history command

.. L28

(solution of self assessment questions on slide)

.. R28

And the answers,

1. In order to retrieve the recently typed 5 commands,we say ``%hist 5``.

2. ``%save filepath 2-5 7 9-11`` is the correct option to the specified lines of codes.

3. ``%hist 5 10`` will display the recently typed commands from 5 to 10 inclusive of the history command.

.. L29

{{a thank you slide}}

.. R29

Hope you have enjoyed and found it useful.
Thank You!
 
