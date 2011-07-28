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

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to the tutorial on "Parsing Data".

.. L2

{{{ Show the slide containing objectives }}}

.. R2

At the end of this tutorial, you will be able to,

 1. Split a string using a delimiter.
 #. Remove the whitespace around the string.
 #. Convert the datatypes of variables from one type to other.

.. L3

{{{ Show the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with Lists".

.. R4

Invoke the ipython interpreter by typing ipython on your terminal.

.. L4

{{{ Open the terminal }}}
::

    ipython

.. R5

Let us start this tutorial with the help of an an exercise.

There is an input file containing huge no. of records. Each record 
corresponds to a student.

.. L5

{{{ Open the file sslc.txt and show }}}

.. L6

{{{ show the slide 'Data set' }}}

.. R6

As you can see, each record consists of fields separated by a semicolon.
The first record is region code, then roll number,name, marks of second 
language,first language, maths, science and social and total marks.

Our job is to calculate the arithmetic mean of all the maths marks in 
the region "B".

.. L7

{{{ Open the file sslc.txt and show }}}

.. R7

Now let us understand, what is meant by 'parsing data'.
From the input file, we can see that the data we have is in the form of
text. Parsing this data is all about reading it and converting it into a 
form which can be used for computations -- in our case,it will be a 
sequence of numbers.

We can clearly see that the problem involves reading files and 
tokenizing.

.. R8

Let us learn about tokenizing strings. We shall define a string first. 
Type

.. L8

{{{ Switch to the terminal }}}
::

    line = "parse this           string"

.. R9

We are now going to split this string on whitespace.

.. L9
::

    line.split()

.. R10

As you can see, we get a list of strings, which means, when ``split`` is 
called without any arguments, it splits on whitespace. In simple words, 
all the spaces are treated as one big space.

.. L10

.. R11

The function ``split`` can also split on a string of our choice. 
This is achieved by passing that as an argument. But first lets define 
a sample record from the file.

.. L11
::

    record = "A;015163;JOSEPH RAJ S;083;042;47;0;72;244"
    record.split(';')

.. R12

We can see that the string is split on the semi-colon and we get each 
field separately.We can also observe that an empty string appears in 
the list since there are two semi colons without anything in between.

In short, ``split`` splits on whitespace if called without an argument 
and splits on the given argument if it is called with an argument.

Pause the video here, try out the following exercise and resume the video 

.. L12

.. L13

{{{ Show slide with Exercise 1 }}}

.. R13
 
 Split the variable line using a space as argument. Is it same as
 splitting without an argument ?

.. R14

Switch to terminal for the solution

.. L14

{{{ continue from paused state }}}
{{{ Switch to the terminal }}}
::

    record.split()

.. L15

{{{ Show slide with Solution 1 }}}

.. R15

We see that when we split on space, multiple whitespaces are not clubbed 
as one and there is an empty string every time there are two consecutive 
spaces.

.. L16

{{{ Switch to the terminal }}}

.. R16

Now that we know how to split a string, we can split the record and 
retrieve each field separately. But there is one problem. The region 
code "B" and a "B" surrounded by whitespace are treated as two different 
regions.Hence, we must find a way to remove all the whitespace around a 
string so that the region code "B" and a "B" with white spaces are dealt 
as same.

This is possible by using the ``strip`` method of strings. Let us define 
a string by typing

.. L17
::

    unstripped = "     B    "
    unstripped.strip()

.. R17

We can see that strip removes all the whitespace around the sentence.

Pause the video here, try out the following exercise and resume the video 

.. L18

{{{ Show slide with Exercise 2 }}}

.. R18

 What happens to the white space inside the sentence when it is stripped

.. R19

Switch to the terminal for solution

.. L19

{{{ continue from paused state }}}
{{{ Switch to the terminal }}}
::

    a_str = "         white      space            "
    a_str.strip()

.. R20

We see that, the whitespace inside the sentence is only removed and the 
rest remains unaffected.

.. L20

.. R21

By now we know enough to separate fields from the record and to strip 
out any white space. The only road block we now have, is conversion of 
string to float.

The splitting and stripping operations are done on a string and their 
result is also a string. Hence the marks that we have, are still strings 
and mathematical operations are not possible on them. We must convert 
them into numbers (integers or floats), before we can perform mathematical 
operations on them. 

.. L21

.. R22

We shall now look at converting strings into floats. We define a float string
first. Type 

.. L22
::

    mark_str = "1.25"
    mark = int(mark_str)
    type(mark_str)
    type(mark)

.. R23

We can see that string is converted to float. We can perform mathematical
operations on them now.

 Pause the video here, try out the following exercise and resume the video 

.. L23

.. L24

{{{ Show slide with Exercise 3 }}}

.. R24

 What happens if you do int("1.25")

.. R25

Switch to the terminal for solution

.. L25

{{{ continue from paused state }}}
{{{ Switch to the terminal }}}
::

    int("1.25")

.. R26

It raises an error since converting a float string into integer directly 
is not possible. It involves an intermediate step of converting to float.
Hence we will have to do the following conversions.

.. L26
::

    dcml_str = "1.25"
    flt = float(dcml_str)
    flt
    number = int(flt)
    number

.. R26

.. R27

Using ``int``, it is also possible to convert float into integers.

Now that we have all the machinery required to parse the file, let us 
solve the problem. We first read the file line by line and parse each 
record. We then see if the region code is B and store the marks 
accordingly.

.. L27

.. L28
::

    math_marks_B = [] # an empty list to store the marks
    for line in open("/home/fossee/sslc.txt"):
        fields = line.split(";")

        region_code = fields[0]
        region_code_stripped = region_code.strip()

        math_mark_str = fields[5]
        math_mark = float(math_mark_str)

        if region_code == "B":
            math_marks_B.append(math_mark)
            
.. R28

.. R29

Now we have all the math marks of region "B" in the list math_marks_B.
To get the mean, we just have to sum the marks and divide by the length.

.. L29
::

        math_marks_mean = sum(math_marks_B) / len(math_marks_B)
        math_marks_mean

.. R30

Hence we get our final output. This is how we split and read such a huge 
data and perform computations on it.

.. L30

.. L31

{{{ Show summary slide }}}

.. R31

This brings us to the end of the tutorial.
In this tutorial, we have learnt to, 

 1. Tokenize a string using various delimiters like semi-colons.
 #. Split a data separated by delimiters by using the function ``split()``.
 #. Get rid of extra white spaces around using the ``strip()`` function.
 #. Convert datatypes of numbers from one type to another.
 #. Parse input data and perform computations on it.

.. L32

{{{Show self assessment questions slide}}}

.. R32

Here are some self assessment questions for you to solve

1. How do you split the string "Guido;Rossum;Python" to get the words.


2. How will you remove the extra whitespace in this sentence
   "      Hello    World    "

3. What does int("20.0") produce

   - 20
   - 20.0
   - Error
   - "20"

.. L33

{{{solution of self assessment questions on slide}}}

.. R33

And the answers,

1. We can split the string the semi-colons by passing it as an argument 
   to the ``split`` function as line.split(';')

2. "      Hello    World    ".strip() will remove the extra whitespaces 
   around the string.

3. int("20.0") will give an error, because converting a float string, 
   20.0, directly into integer is not possible.

.. L34

{{{ Show the Thank you slide }}}

.. R34

Hope you have enjoyed this tutorial and found it useful.
Thank you.
 

