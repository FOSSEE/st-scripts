.. Objectives
.. ----------

.. Clearly state the objectives of the LO (along with RBT level)

.. Prerequisites
.. -------------

..   1. Name of LO-1
..   2. Name of LO-2
..   3. Name of LO-3
     
.. Author              : Madhu
   Internal Reviewer   : 
   External Reviewer   :
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]


Script
------

{{{ Show the slide containing the title }}}

Hello friends. Welcome to this spoken tutorial on Getting started with
strings.

{{{ Show the slide containing the outline }}}

In this tutorial, we will learn the basic conditional constructs
available in Python. We learn the if/else, if/elif/else and ternary
conditional constructs available in Python. 

{{{ Shift to terminal and start ipython }}}

To begin with let us start ipython, by typing::

  ipython

on the terminal

Whenever we have two possible states that can occur depending on a
whether a certain condition we can use if/else construct in
Python. Say for example we have a variable "a" which stores integers
and we are required to find out whether the value of the variable "a"
is an even number or an odd number. To test out conditional statements
as an example, let us say the value of the variable "a" is 5::

  a = 5

In such a case we can write the if/else block as::

  if a % 2 == 0:
      print "Even"
  else:
      print "Odd"

When the value of the variable "a" is divided by 2 and the remainder
is 0 i.e. the result of the operation "a modulo 2" is 0 the condition
"a % 2 == 0" evaluates to True, so the code within the if block gets
executed. This means that the value of "a" is Even. 

If the operation "a modulo 2" is not 0 the condition "a % 2 == 0"
evaluates to False and hence the code block within else gets executed
which means that the value of "a" is Odd. 

Note in such a case only one of the two blocks get executed depending
on whether the condition is True or False.

There is a very important sytactic element to understand here. All the
statements which are inside a certain code block are indented by 4
spaces. The statement which starts a new code block after it, i.e. the
if statement in this example ends with a colon (:). So the next
immediate line will be inside the if block and hence indented by 4
spaces. To come out of the code block we have to come back to the
previous indentation level as shown in the else line here. Again the
line following else will be in a new block so else line ends with a
colon and the following block of code is indented by 4.

As we use if/else statement when we have a condition which can take
one of the two states, we may have conditions which can take more than
two states. In such a scenario Python provides if/elif/else
statements. Let us take an example. We have a variable "a" which holds
integer values. We need to print "positive" if the value of a is
positive, "negative" if it is negative and "zero" if the value of the
variable "a" is 0. Let us use if/elif/else ladder for it. For the
purposes of testing our code let us assume that the value of a is -3::

  a = -3

  if a > 0:
      print "positive"
  elif a < 0:
      print "negative"
  else:
      print "zero"

This if/elif/else ladder is self explanatory. All the syntax and rules
as said for if/else statements hold. The only addition here is the
elif statement which can have another condition of its own.

Here, exactly one block of code is executed and that block of code
corresponds to the condition which first evaluates to True. Even if
there is a situation where multiple conditions evaluate to True all
the subsequent conditions other than the first one which evaluates to
True are neglected. Consequently, the else block gets executed if and
only if all the conditions evaluate to False.

Also, the else block in both if/else statement and if/elif/else is
optional. We can have a single if statement or just if/elif statements
without having else block at all. Also, there can be any number of
elif's within an if/elif/else ladder. For example

{{{ Show slide for this }}}

  if user == 'admin':
      # Do admin operations
  elif user == 'moderator':
      # Do moderator operations
  elif user == 'client':
      # Do customer operations

{{{ end of slide switch to ipython }}}

is completely valid. Note that there are multiple elif blocks and there
is no else block.

In addition to these conditional statements, Python provides a very
convenient ternary conditional operator. Let us take the following
example where we read the marks data from a data file which is
obtained as a string as we read a file. The marks can be in the range
of 0 to 100 or 'AA' if the student is absent. In such a case to obtain
the marks as an integer we can use the ternary conditional
operator. Let us say the string score is stored in score_str
variable::

  score_str = 'AA'

Now let us use the ternary conditional operator::

  score = int(score_str) if score_str != 'AA' else 0

This is just the if/else statement block which written in a more
convenient form and is very helpful when we have only one statement
for each block. This conditional statement effectively means as we
would have exactly specified in the English language which will be
like score is integer of score_str is score_str is not 'AA' otherwise
it is 0. This means that we make the scores of the students who were
absent for the exam 0.

Moving on, there are certain situations where we will have to no
operations or statements within the block of code. For example, we
have a code where we are waiting for the keyboard input. If the user
enters "s" as the input we would perform some operation nothing
otherwise. In such cases "pass" statement comes very handy::

  a = raw_input("Enter 'c' to calculate and exit, 'd' to display the existing
  results exit and 'x' to exit and any other key to continue: ")

  if a == 'c':
     # Calculate the marks and exit
  elif a == 'd':
     # Display the results and exit
  elif a == 'x':
     # Exit the program
  else:
     pass

In this case "pass" statement acts as a place holder for the block of
code. It is equivalent to a null operation. It literally does
nothing. So "pass" statement can be used as a null operation
statement, or it can used as a place holder when the actual code
implementation for a particular block of code is not known yet but has
to be filled up later.

{{{ Show summary slide }}}

This brings us to the end of the tutorial session on conditional
statements in Python. In this tutorial session we learnt

  * What are conditional statements
  * if/else statement
  * if/elif/else statement
  * Ternary conditional statement - C if X else Y
  * and the "pass" statement

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!
 
