.. Objectives
.. ----------

.. At the end of this tutorial, you will be able to 

.. 1. Create dictionaries
.. #. Add data to dictionaries
.. #. Retrieve data
.. #. use ``.keys()`` and ``.values()`` methods
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

.. #[Puneeth: Quickref]

============
Dictionaries
============

{{{ show the welcome slide }}}

Welcome to the spoken tutorial on dictionaries.

{{{ switch to next slide, outline slide }}}

In this tutorial, we will see how to create empty dictionaries, learn
about keys and values of dictionaries. Checking for elements and
iterating over elements.

{{{ switch to next slide on overview of dictionaries }}}

A dictionary in general, is designed to look up meanings of
words. Similarly, Python dictionary is also designed to look up for a
specific key and retrieve the corresponding value. Dictionaries are
data structures that provide key-value mappings.  Dictionaries are
similar to lists except that instead of the values having integer
indexes, dictionaries have keys or strings as indexes.

We need ipython interpreter for this tutorial, start it by issuing the
command ``ipython`` in command line.

.. #[Puneeth: We don't need pylab]

{{{ start ipython interpreter by issuing command ipython }}}

{{{ switch to next slide, Creating dictionary }}}

Let us start by creating an empty dictionary, type the following in
your IPython interpreter.
::

    mt_dict = {}    

Notice that unlike lists, curly braces are used define ``dictionary``.

{{{ move the mouse over curly braces to grab attention }}}

Now let us see how to create a non-empty dictionary,
::

    extensions = {'jpg' : 'JPEG Image', 'py' : 'Python script', 'html' : 'Html document', 'pdf' : 'Portable Document Format'}

Notice that each key-value pair is separated by a comma

{{{ move the mouse over the commas to grab attention }}}

and each key and value are separated using a colon.

{{{ move the mouse over the colon one by one to grab attention }}}

Here, we defined four entries in the dictionary extensions. The keys
are

{{{ spell the keys letter by letter }}}

jpg, py, html, and pdf.

Simply type,
::

    extensions

in the interpreter to see the content of the dictionary. Notice that
in dictionaries the order cannot be predicted and you can see that the
values are not in the order that we entered in.

{{{ switch to next slide, accessing elements }}}

Like in lists, the elements in a dictionary can be accessed using the
index, here the index is the key. Try,
::

    print extensions['jpg']

It printed JPEG Image. And now try,
::

    print extensions['zip']

Well it gave us an error, saying that the key 'zip' is not in the
dictionary.

Pause here for some time and try few more keys. Also try jpg in
capital letters.

{{{ switch to next slide, adding and deleting keys and values in
dictionaries }}}

Well that was about creating dictionaries, now how do we add or delete
items. We can add new items into dictionaries as,
::

    extensions['cpp'] = 'C++ code'

and delete items using the ``del`` keyword as,
::

    del extension['pdf']

Let us check the content of the dictionary now,
::

    extensions

So the changes have been made. Now let us try one more thing,
::

    extensions['cpp'] = 'C++ source code'
    extensions

As you can see, it neither added a new thing nor gave an error, but it
simply replaced the existing value with the new one.

Now let us learn how to check if a particular key is present in the
dictionary. For that we can use ``in``,
::

    'py' in extensions
    'odt' in extensions

It will return ``True`` if the key is found in the dictionary, and
will return ``False`` if key is not present. Note that we can check
only for container-ship of keys in dictionaries and not values.

{{{ switch to next slide, Retrieve keys and values }}}

Now let us see how to retrieve the keys and values. We can use the
method ``keys()`` for getting a list of the keys in a particular
dictionary and the method ``values()`` for getting a list of
values. Let us try them,
::

    extensions.keys()

It returned the ``list`` of keys in the dictionary extensions. And now
the other one,
::

    extensions.values()

It returned the ``list`` of values in the dictionary.

{{{ switch to next slide, problem statement for the next solved
exercise }}}

Now let us try to print the data in the dictionary. We can use ``for``
loop to iterate. Pause here and try to do it yourself.

It can be solved as,
::

    for each in extensions.keys():
        print each, "-->", extensions[each]


{{{ switch to next slide, summary }}}

This brings us to the end of this tutorial, we learned dictionaries
and saw how to create an empty dictionary, build a dictionary with
some data in it, adding data, ``keys()`` and ``values()`` methods, and
iterating over the dictionaries.

{{{ switch to next slide, thank you slide }}}

Thank you!
