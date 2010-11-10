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
..   #. basic datatypes
     
.. Author              : Puneeth 
   Internal Reviewer   : Amit 
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <08-11-2010, Anand, OK> [2010-10-05]

Script
------

{{{ Show the slide containing title }}}

Hello Friends. Welcome to this tutorial on manipulating strings. 

{{{ show the slide with outline }}} 

In this tutorial we shall learn to manipulate strings, specifically
slicing and reversing them, or replacing characters, converting from
upper to lower case and vice-versa and joining a list of strings.

We have an ``ipython`` shell open, in which we are going to work,
through out this session. 

Let us consider a simple problem, and learn how to slice strings and
get sub-strings. 

Let's say the variable ``week`` has the list of the names of the days
of the week. 

::

    week = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]


Now given a string ``s``, we should be able to check if the string is a
valid name of a day of the week or not. 

::

    s = saturday


``s`` could be in any of the forms --- sat, saturday, Sat, Saturday,
SAT, SATURDAY. For now, shall now be solving the problem only for the forms,
sat and saturday. We shall solve it for the other forms, at the end of
the tutorial. 

{{{ show these forms in a slide }}}

So, we need to check if the first three characters of the given string
exists in the variable ``week``. 

As, with any of the sequence data-types, strings can be sliced into
sub-strings. To get the first three characters of s, we say,

::

    s[0:3]

Note that, we are slicing the string from the index 0 to index 3, 3
not included. 

As we already know, the last element of the string can be accessed
using ``s[-1]``.  

Following is an exercise that you must do. 

%%1%% Obtain the sub-string excluding the first and last characters
from the string s. 

Please, pause the video here. Do the exercise(s) and then continue. 

::

    s[1:-1]

gives the substring of s, without the first and the last
characters of s. 

::

    s = saturday
    s[:3]

Now, we just check if that substring is present in the variable
``week``. 

::

    s[:3] in week          

Let us now consider the problem of finding out if a given string is
palindromic or not. First of all, a palindromic string is a string
that remains same even when it has been reversed.

Let the string given be ``malayalam``.

::

    s = "malayalam"

Now, we need to compare this string with it's reverse. 

Again, we will use a technique common to all sequence data-types,
[::-1]

So, we obtain the reverse of s, by simply saying, 

::

    s[::-1]

Now, to check if the string is ``s`` is palindromic, we say
::

    s == s[::-1]

As, expected, we get ``True``. 

Now, if the string we are given is ``Malayalam`` instead of
``malayalam``, the above comparison would return a False. So, we will
have to convert the string to all lower case or all upper case, before
comparing. Python provides methods, ``s.lower`` and ``s.upper`` to
achieve this. 

Let's try it out. 
::

   s = "Malayalam"

   s.upper()

   s

As you can see, s has not changed. It is because, ``upper`` returns a
new string. It doesn't change the original string. 

::

   s.lower()

   s.lower() == s.lower()[::-1]
   
Following is an exercise that you must do. 

%%2%% Check if ``s`` is a valid name of a day of the week. Change the
solution to this problem, to include forms like, SAT, SATURDAY,
Saturday and Sat.

Please, pause the video here. Do the exercise and then continue. 

::

    s in week

    s.lower()[:3] in week


So, as you can see, now we can check for presence of ``s`` in
``week``, in whichever format it is present -- capitalized, or all
caps, full name or short form.

We just convert any input string to lower case and then check if it is
present in the list ``week``. 

Now, let us consider another problem. We often encounter e-mail id's
which have @ and periods replaced with text, something like
info[at]fossee[dot]in. We now wish to get back proper e-mail
addresses.  

Let's say the variable email has the email address. 
::

   email = "info[at]fossee[dot]in"

Now, we first replace the ``[at]`` with the ``@``, using the replace
method of strings. 
::

   email = email.replace("[at]", "@")
   print email

Following is an exercise that you must do. 

%%3%% Replace the ``[dot]`` with ``.`` in ``email``

Please, pause the video here. Do the exercise and then continue. 

::

   email = email.replace("[dot]", ".")        
   print email

Now, let's look at another interesting problem where we have a list of
e-mail addresses and we wish to obtain one long string of e-mail
addresses separated by commas or semi-colons. 

::

  email_list = ["info@fossee.in", "enquiries@fossee.in",  "help@fossee.in"]


Now, if we wish to obtain one long string, separating each of the
email id by a comma, we use the join operator on ``,``. 

::

  email_str = ", ".join(email_list)
  print email_str

Notice that the email ids are joined by a comma followed by a space. 

Following is an exercise that you must do. 

%%3%% From the email_str that we generated, change the separator to be
a semicolon instead of a comma. 

Please, pause the video here. Do the exercise and then continue. 

::

  email_str = email_str.replace(",", ";")

That brings us to the end of the tutorial. 

{{{ show summary slide }}}

In this tutorial, we have learnt how to get substrings, reverse
strings and a few useful methods, namely upper, lower, replace and
join. 

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!

