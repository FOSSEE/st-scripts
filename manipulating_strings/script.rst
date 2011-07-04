.. Objectives
.. ----------

.. By the end of this tutorial, you will be able to

.. 1. Slice strings and get sub-strings out of them
.. #. Reverse strings
.. #. Replace characters in strings. 
.. #. Convert strings to upper or lower case
.. #. joining a list of strings

.. Prerequisites
.. -------------

..   1. getting started with strings
..   #. getting started with lists
..   #. basic datatypes and operators
     
.. Author              : Puneeth 
   Internal Reviewer   : Amit 
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <08-11-2010, Anand, OK> [2010-10-05]

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello Friends and Welcome to this tutorial on 'manipulating strings'. 

.. L2

{{{ show the slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. Slice strings and get sub-strings out of them.
 #. Reverse strings.
 #. Replace characters in strings. 
 #. Convert strings to upper or lower case.
 #. Join a list of strings.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "getting started with strings", "getting started with lists"
and "basic datatypes and operators".

.. R4

Let us invoke our ipython interpreter

.. L4

{{{ Open the terminal }}}
::

    ipython

.. R5

Let us consider a simple problem, and learn how to slice strings and
get sub-strings. 

Let's say the variable ``week`` has the list of the names of the days
of the week. 

.. L5
::

    week = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]

.. R6

Now given a string ``s``, we should be able to check if the string is a
valid name of a day of the week or not.Let us define our string as, 

.. L6
::

    s = "saturday"

.. L7

{{{ show the slide with forms }}}

.. R7

``s`` could be in any of the forms --- sat, saturday, Sat, Saturday,
SAT, SATURDAY. For now, we shall be solving the problem only for the 
forms,sat and saturday. We shall solve it for the other forms, at the 
end of the tutorial. 

.. R8

So, we need to check if the first three characters of the given string
exists in the variable ``week``. 

As with any of the sequence data-types, strings can be sliced into
sub-strings. To get the first three characters of s, we say,

.. L8

{{{ Switch to the terminal }}}
::

    s[0:3]

.. R9

Note that, we are slicing the string from the index 0 to index 3, 3
not included. 

As we already know, the last element of the string can be accessed
using ``s[-1]``.  

Pause the video here, try out the following exercise and resume the video.

.. L9

.. L10

{{{ Show slide with exercise 1 }}}

.. R10

 Obtain the sub-string excluding the first and last characters
 from the string s. 

.. R11

Switch to the terminal for solution

.. L11

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    s[1:-1]

.. R12

We get the substring of s, without the first and the last
characters of s. 

Now let us check if a particular substring is present in the variable
``week``. We shall check for 'sat'.

.. L12
::

    s[:3]
    s[:3] in week          

.. R13

We get the result as true.
Let us now consider the problem of finding out, if a given string is
palindromic or not. First of all, a palindromic string is a string
that remains same even when it has been reversed.

Let the string given be ``malayalam``.

.. L13
::

    s1 = "malayalam"

.. R14

Now, we need to compare this string with it's reverse. 

Again, we will use a technique common to all sequence data-types,
that is, [::-1]

So, we obtain the reverse of s, by simply saying, 

.. L14
::

    s1[::-1]

.. R15

Now, to check if the string is ``s`` is palindromic, we say

.. L15
::

    s1 == s1[::-1]

.. R16

As, expected, we get ``True``. 

Now, if the string we are given is ``Malayalam`` instead of
``malayalam``, the above comparison would return a False. So, we will
have to convert the string to all lower case or to all upper case, 
before comparing. Python provides methods, ``s.lower`` and ``s.upper`` 
to achieve this. 

Let's try it out. 

.. L16
::

    s1 = "Malayalam"
    s1.upper()
    s1

.. R17

As you can see, s has not changed. It is because, ``upper`` returns a
new string. It doesn't change the original string. Similarly,

.. L17
::

    s1.lower()
    s1.lower() == s1.lower()[::-1]
 
.. R18
  
Pause the video here, try out the following exercise and resume the video.

.. L18

.. L19

{{{ Show slide with exercise 2 }}}

.. R19

 Check if ``s`` is a valid name of a day of the week. Change the
 solution to this problem, to include forms like, SAT, SATURDAY,
 Saturday and Sat.

.. R20

Switch to your terminal for solution

.. L20

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    s in week

    s.lower()[:3] in week

.. R21

So, as you can see, now we can check for presence of ``s`` in
``week``, in whichever format it is present -- capitalized, or all
caps, full name or short form.

We just convert any input string to lower case and then check if it is
present in the list ``week``. 

Now, let us consider another problem. We often encounter e-mail id's
which have '@' and periods replaced with text, something like
info[at]fossee[dot]in. We now wish to get back proper e-mail
addresses.  

Let's say the variable email has the email address. 

.. L21
::

    email = "info[at]fossee[dot]in"

.. R22

Now, we first replace the ``[at]`` with the ``@``, using the replace
method of strings. 

.. L22
::

    email = email.replace("[at]", "@")
    print email

.. R23

Pause the video here, try out the following exercise and resume the video.

.. L23

.. L24

{{{ Show slide with exercise 3 }}}

.. R24

 Replace the ``[dot]`` with ``.`` in ``email``

.. R25

Switch to the terminal for solution 

.. L25

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    email = email.replace("[dot]", ".")        
    print email

.. R26

Now, let us look at another interesting problem where we have a list of
e-mail addresses and we wish to obtain one long string of e-mail
addresses separated by commas or semi-colons. 

.. L26
::

    email_list = ["info@fossee.in", "enquiries@fossee.in", "help@fossee.in"]

.. R27

Now, if we wish to obtain one long string, separating each of the
email id by a comma, we use the join operator on ``,``. 

.. L27
::

    email_str = ", ".join(email_list)
    print email_str

.. R28

Notice that the email ids are joined by a comma followed by a space. 

 Pause the video here, try out the following exercise and resume the video.

.. L28

.. L29

{{{ Show slide with exercise 4 }}}

.. R29

 From the email_str that we generated, change the separator to be
 a semicolon instead of a comma. 

.. R30

Switch to the terminal for solution 

.. L30

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    email_str = email_str.replace(",", ";")
    print email_str

.. R31

We see that the email ids are joined by a  semicolon followed by a space.

.. L31

.. L32

{{{ show summary slide }}}

.. R32

This brings us to the end of this tutorial. 
In this tutorial, we have learnt to, 

 1. Obtain sub-strings and reverse of strings by using the index numbers
 #. Use following functions -
    - ``upper()`` -- to obtain the upper case of a string
    - ``lower()`` -- to obtain the lower case of a string
    - ``replace()`` -- to replace a character by another one
    - ``join()`` -- to join a list of strings with an operator

.. L33

{{{Show self assessment questions slide}}}

.. R33

Here are some self assessment questions for you to solve

1. Given a string ``s = "this is a string"``, how will you change it
   to ``"this isn't a list"`` ?
 

2. Given the string "F.R.I.E.N.D.S" in s, obtain the string "friends".

.. L34
   
{{{solution of self assessment questions on slide}}}

.. R34

And the answers,

1. We will use the ``replace`` function to accomplish this.
::
    
    s = s.replace("string", "list")
    s = s.replace("is", "isn't")
    s

We notice that every 'is' in the statement has been replaced by ``isn't``.

2. In order to change the string to lower case, we use the 
   method ``lower()``
::

    s[::2].lower()
    
.. L35

{{{ Show the 'Thankyou' slide }}}

.. R35

Hope you have enjoyed this tutorial and found it useful.
Thank you!

