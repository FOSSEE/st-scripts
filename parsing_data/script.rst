.. Objectives
.. ----------

.. By the end of this tutorial you will be able to

..  * Split a string using a delimiter
..  * remove the whitespace around the string
..  * convert the variables from one type to other

.. Prerequisites
.. -------------

..   1. Getting started with lists
     
.. Author              : Nishanth Amuluru
   Internal Reviewer   : Amit
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <put date stamp here, not OK> [2010-10-05]

Script
------

Hello friends and welcome to the tutorial on Parsing Data

{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline slide }}}

In this tutorial, we shall learn

 * What we mean by parsing data
 * the string operations required for parsing data
 * datatype conversion

#[Puneeth]: Changed a few things, here.  

#[Puneeth]: I don't like the way the term "parsing data" has been used, all
through the script. See if that can be changed.

 Let us have a look at the problem

{{{ Show the slide containing problem statement. }}}

There is an input file containing huge no. of records. Each record corresponds
to a student.

{{{ show the slide explaining record structure }}}
As you can see, each record consists of fields seperated by a ";". The first
record is region code, then roll number, then name, marks of second language,
first language, maths, science and social, total marks, pass/fail indicatd by P
or F and finally W if withheld and empty otherwise.

Our job is to calculate the arithmetic mean of all the maths marks in the region "B".

#[Nishanth]: Please note that I am not telling anything about AA since they do
             not know about any if/else yet.

#[Puneeth]: Should we talk pass/fail etc? I think we should make the problem
 simple and leave out all the columns after total marks. 

Now what is parsing data.

From the input file, we can see that the data we have is in the form of
text. Parsing this data is all about reading it and converting it into a form
which can be used for computations -- in our case, sequence of numbers.

#[Puneeth]: should the word tokenizing, be used? Should it be defined before
 using it?

We can clearly see that the problem involves reading files and tokenizing.

#[Puneeth]: the sentence above seems kinda redundant. 

Let us learn about tokenizing strings. Let us define a string first. Type
::

    line = "parse this           string"

We are now going to split this string on whitespace.
::

    line.split()

As you can see, we get a list of strings. Which means, when ``split`` is called
without any arguments, it splits on whitespace. In simple words, all the spaces
are treated as one big space.

``split`` also can split on a string of our choice. This is acheived by passing
that as an argument. But first lets define a sample record from the file.
::

    record = "A;015163;JOSEPH RAJ S;083;042;47;AA;72;244;;;"
    record.split(';')

We can see that the string is split on ';' and we get each field seperately.
We can also observe that an empty string appears in the list since there are
two semi colons without anything in between.

To recap, ``split`` splits on whitespace if called without an argument and
splits on the given argument if it is called with an argument.

{{{ Pause here and try out the following exercises }}}

%% 1 %% split the variable line using a space as argument. Is it same as
        splitting without an argument ?

{{{ continue from paused state }}}

We see that when we split on space, multiple whitespaces are not clubbed as one
and there is an empty string everytime there are two consecutive spaces.

Now that we know how to split a string, we can split the record and retrieve
each field seperately. But there is one problem. The region code "B" and a "B"
surrounded by whitespace are treated as two different regions. We must find a
way to remove all the whitespace around a string so that "B" and a "B" with
white spaces are dealt as same.

This is possible by using the ``strip`` method of strings. Let us define a
string by typing
::

    unstripped = "     B    "
    unstripped.strip()

We can see that strip removes all the whitespace around the sentence

{{{ Pause here and try out the following exercises }}}

%% 2 %% What happens to the white space inside the sentence when it is stripped

{{{ continue from paused state }}}

Type
::

    a_str = "         white      space            "
    a_str.strip()

We see that the whitespace inside the sentence is only removed and anything
inside remains unaffected.

By now we know enough to seperate fields from the record and to strip out any
white space. The only road block we now have is conversion of string to float.

The splitting and stripping operations are done on a string and their result is
also a string. Hence the marks that we have are still strings and mathematical
operations are not possible on them. We must convert them into numbers
(integers or floats), before we can perform mathematical operations on them. 

We shall look at converting strings into floats. We define a float string
first. Type 
::

    mark_str = "1.25"
    mark = int(mark_str)
    type(mark_str)
    type(mark)

We can see that string is converted to float. We can perform mathematical
operations on them now.

{{{ Pause here and try out the following exercises }}}

%% 3 %% What happens if you do int("1.25")

{{{ continue from paused state }}}

It raises an error since converting a float string into integer directly is
not possible. It involves an intermediate step of converting to float.
::

    dcml_str = "1.25"
    flt = float(dcml_str)
    flt
    number = int(flt)
    number

Using ``int`` it is also possible to convert float into integers.

Now that we have all the machinery required to parse the file, let us solve the
problem. We first read the file line by line and parse each record. We see if
the region code is B and store the marks accordingly.
::

    math_marks_B = [] # an empty list to store the marks
    for line in open("/home/fossee/sslc1.txt"):
        fields = line.split(";")

        region_code = fields[0]
        region_code_stripped = region_code.strip()

        math_mark_str = fields[5]
        math_mark = float(math_mark_str)

        if region_code == "AA":
            math_marks_B.append(math_mark)


Now we have all the maths marks of region "B" in the list math_marks_B.
To get the mean, we just have to sum the marks and divide by the length.
::

        math_marks_mean = sum(math_marks_B) / len(math_marks_B)
        math_marks_mean

{{{ Show summary slide }}}

This brings us to the end of the tutorial.
we have learnt

 * how to tokenize a string using various delimiters
 * how to get rid of extra white space around
 * how to convert from one type to another
 * how to parse input data and perform computations on it

{{{ Show the "sponsored by FOSSEE" slide }}}

#[Nishanth]: Will add this line after all of us fix on one.
This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you
 

