.. Objectives
.. ----------

.. At the end of this tutorial, you will be able to 

.. 1. Create dictionaries
.. #. Add and delete data from dictionaries
.. #. Retrieve data from dictionaries
.. #. Check for container-ship of keys
.. #. Iterate over elements

.. Prerequisites
.. -------------

..   1. should have ``ipython``  installed. 
..   #. getting started with ``ipython``.
..   #. basic datatypes.
     
.. Author              : Anoop Jacob Thomas <anoop@fossee.in>
   Internal Reviewer   : Puneeth
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <11-11-2010, Anand, OK> [2010-10-05]


============
Dictionaries
============

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the spoken tutorial on 'dictionaries'.

.. L2

{{{ switch to slide containing objectives }}}

.. R2

At the end of this tutorial, you will be able to,

 1. Create dictionaries.
 #. Add and delete data from dictionaries.
 #. Retrieve data from dictionaries.
 #. Check for container-ship of keys.
 #. Iterate over elements.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Basic datatypes and operators".

.. L4

{{{ switch to next slide on overview of dictionaries }}}

.. R4

A dictionary in general, is designed to look up for meanings of
words. Similarly, Python dictionary is also designed to look up for a
specific key and retrieve the corresponding value. Dictionaries are
data structures that provide key-value mappings.  Dictionaries are
similar to lists except that instead of the values having integer
indexes, dictionaries have keys or strings as indexes.

.. R5

We start our ipython interpreter as,

.. L5

{{{ Open the terminal }}}
::

    ipython

.. R6

Let us start by creating an empty dictionary. Type the following in
your IPython interpreter.

.. L6
::

    mt_dict = {}    

.. R7

Notice that unlike lists, curly braces are used to define a ``dictionary``.

.. L7

{{{ move the mouse over curly braces }}}

.. R8

Now let us see how to create a non-empty dictionary,

.. L8
::

    extensions = {'jpg' : 'JPEG Image', 'py' : 'Python script', 
    'html' : 'Html document', 'pdf' : 'Portable Document Format'}

.. R9

Notice that each key-value pair is separated by a comma.

.. L9

{{{ move the mouse over the commas }}}

.. R10

and each key and value are separated using a colon.

.. L10

{{{ move the mouse over the colon one by one  }}}

.. R11

Here, we have defined four entries in the dictionary extensions. 
The keys are

jpg, py, html, and pdf.

Simply type,extensions in the interpreter to see the content 
of the dictionary.

.. L11
::

    extensions

.. R12

Notice that, in dictionaries, the order cannot be predicted and you can 
see that the values are not in the order that we entered in.

.. L12

{{{ switch to next slide, accessing elements }}}

.. R13

Like in lists, the elements in a dictionary can be accessed using the
index, here the index is the key. We type,

.. L13

{{{ Switch to terminal }}}
::

    print extensions['jpg']

.. R14

It printed JPEG Image. And now try,

.. L14
::

    print extensions['zip']

.. R15

Well it gave us an error, saying that the key 'zip' is not in the
dictionary.

Pause here for some time and try few more keys. Also try jpg in
capital letters.
<continue from paused state>
Well that was about creating dictionaries, now how do we add or delete
items. We can add new items into dictionaries as,

.. L15
::

    extensions['cpp'] = 'C++ code'

.. R16

and delete items using the ``del`` keyword as,

.. L16
::

    del extensions['pdf']

.. R17

Let us check the content of the dictionary now,

.. L17
::

    extensions

.. R18

So the changes have been made. Now let us try one more thing,

.. L18
::

    extensions['cpp'] = 'C++ source code'
    extensions

.. R19

As you can see, it neither added a new thing nor gave an error, but it
simply replaced the existing value with the new one.

Now let us learn how to check if a particular key is present in the
dictionary. For that we can use the method ``in``,

.. L19
::

    'py' in extensions
    'odt' in extensions

.. R20

It will return ``True`` if the key is found in the dictionary, and
will return ``False`` if key is not present. Note that we can check
only for container-ship of keys in dictionaries and not values.

.. L20

{{{ switch to next slide, Retrieve keys and values }}}

.. R21

Now let us see how to retrieve the keys and values. We can use the
method ``keys()`` for getting a list of the keys in a particular
dictionary and the method ``values()`` for getting a list of
values. 

.. R22

Let us try them,

.. L22
 
{{{ Switch to terminal }}}
::

    extensions.keys()

.. R23

It returned the ``list`` of keys in the dictionary extensions. And now
the other one,

.. L23
::

    extensions.values()

.. R24

It returned the ``list`` of values in the dictionary.

Pause the video here, try out the following exercise and resume the video.

.. L24

.. L25

{{{ Show slide with exercise 1 }}}

.. R25

 Print the keys and values in the dictionary one by one.

.. R26

Switch to terminal for solution.

.. L26

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    for each in extensions.keys():
        print each, "-->", extensions[each]


.. L27

{{{ Show summary slide }}}

.. R27

This brings us to the end of this tutorial.In this tutorial, 
we have learnt to,

 1. Create dictionaries namely --
    - empty dictionaries
    - dictionaries with data.
 #. Access elements in the dictionaries using the keys.
 #. Add elements to a dictionary by assigning a value to a key.
 #. Delete elements from a dictionary by using the function ``del``.
 #. Retrieve the keys and values by using the methods ``.keys()`` and 
    ``.values()`` respectively.
 #. Iterate over elements of a dictionary using a ``for`` loop.
 
.. L28

{{{Show self assessment questions slide}}}

.. R28

Here are some self assessment questions for you to solve


1. Container-ship of values can be checked in a python dictionary

   - True
   - False

2. Consider the python dictionary ``x = {'a' : ['a','b','c'], 'b' :
   (1, 2, 3), 1 : {1 : 'one', 2 : 'two'}, 10 : {10 : 'ten', 11 :
   'eleven'}}``. What will the following code return? 
     ``(1, 2, 3) in x.values()``.

   - True
   - False
   - Container-ship of values cannot be checked in dictionaries
   - The dictionary is invalid

.. L29

{{{solution of self assessment questions on slide}}}

.. R29

And the answers,

1. False.Container-ship of only keys can be checked in a python 
   dictionary.

2. True 

.. L30

{{{ switch to thank you slide }}}

.. R30

Hope you have enjoyed this tutorial and found it useful.
Thank you!
