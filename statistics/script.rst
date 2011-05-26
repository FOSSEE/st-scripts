.. Objectives
.. ----------

.. By the end of this tutorial you will --

.. 1. Get to know simple statistics functions like mean,std etc .. (Remembering)
.. #. Apply them on a real world example. (Applying)


.. Prerequisites
.. -------------

.. Getting started with IPython
.. Loading Data from files
.. Getting started with Lists
.. Accessing Pieces of Arrays

     
.. Author              : Amit Sethi
   Internal Reviewer   : Puneeth
   External Reviewer   :
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]

=======
Script
=======

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to the tutorial on 'Statistics' using Python.

.. L2

{{{ Show the slide containing the objectives }}}

.. R2

At the end of this tutorial,you will be able to,
   
   1. Do statistical operations in Python  
   #. Sum a set of numbers
   #. Find their mean,median and standard deviation

.. L3

{{{ Show slide with pre-requisite }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on 
   "Loading Data from files"
   "Getting started with Lists"
   "Accessing Pieces of Arrays".

.. L4

Let us invoke our ipython interpreter with pylab loaded.

.. R4
::

    ipython -pylab

.. L5
   
{{{ Open the file sslc2.txt and show }}}

.. R5

For this tutorial, we will use data file that is at the  path
``/home/fossee/sslc2.txt``.  It contains record of students and their
performance in one of the State Secondary Board Examination. It has
180,000 lines of record. We are going to read it and process this
data.  We can see the content of file by double clicking on it. It
might take some time to open since it is quite a large file.  Please
don't edit the data since it has a particular structure.

.. R6

To check the contents of the file, we use the cat command.

.. L6
::
   
    cat /home/fossee/sslc2.txt

.. L7

{{{ Show the data structure on a slide }}}

.. R7

Each line in the file is a set of 11 fields separated 
by semi-colons. Consider a sample line from this file.  
A;015163;JOSEPH RAJ S;083;042;47;00;72;244;;; 

The following are the fields in any given line.
* Region Code which is 'A'
* Roll Number 015163
* Name JOSEPH RAJ S
* Marks of 5 subjects: ** English 083 ** Hindi 042 ** Maths 47 **
  Science 35 ** Social 72
* Total marks 244

.. R8

Lets load this data as an array and then run various functions on
it.

To get the data as an array, we use the loadtxt command

.. L8
::
   
    L=loadtxt('/home/fossee/sslc2.txt',usecols=(3,4,5,6,7,),delimiter=';')
    L

.. R9
     
We get our output in the form of an array.
loadtxt function loads data from an external file.Delimiter specifies
the kind of character, that the fields of data seperated by.  usecols
specifies the columns to be used. So (3,4,5,6,7) loads those
colums. The 'comma' is added because usecols is a sequence.

As we can see L is an array. We can get the shape of this array using

.. L9
::
   
    L.shape

.. R10
    
We get a tuple stating the numbers of rows and columns respectively.
Lets start applying statistical operations on these. We will start with
the most basic, summing. How do you find the sum of marks of all
subjects for the first student.

.. L10

.. R11

As we know from our knowledge of accessing pieces of arrays, to acess
the first row, we will do 

.. L11
::
   
    L[0,:]

.. R12

Now to sum this we can say 

.. L12
::

    totalmarks=sum(L[0,:]) 
    totalmarks

.. R13

Now to get the mean we can divide the totalmarks by the length

.. L13
::

    totalmarks/len(L[0,:])

.. R14

or simply use the function ``mean``. 

.. L14
::

    mean(L[0,:])

.. R15

But we have such a large data set and  calculating the mean for each student one by one 
is impossible. Is there a way to reduce the work.

For this we will look into the documentation of mean 

.. L15
::

    mean?

.. R16

As we know L is a two dimensional array. We can calculate the mean
across each of the axis of the array. The axis of rows is referred by
number 0 and columns by 1. So to calculate mean accross all columns, we
will pass extra parameter 1 for the axis.

.. L16
::

    mean(L,1)

.. R17

L here, is a two dimensional array.

Similarly to calculate average marks scored by all the students for each
subject can be calculated using 

.. L17
::

    mean(L,0)

.. R18

Next, let us calculate the median of English marks for the all the students.
We can access English marks of all students using 

.. L18
::

    L[:,0]

.. R19
   
To get the median we will simply use the function ``median``. 

.. L19
::

    median(L[:,0])

.. R20

For all the subjects we can use the same syntax as mean and calculate
median across all rows using median 

.. L20
::

    median(L,0)
  
.. R21

Similarly to calculate standard deviation for English we will use the function ``std``

.. L21
::
  
    std(L[:,0])

.. R22

and for all rows, we do,

.. L22
::

    std(L,0)

.. R23

Pause the video here, try out the following exercise and resume the video.

.. L23

.. L24

{{{ Show slide with exercise 1 }}} 

.. R24

In the given file football.txt at path /home/fossee/football.txt , one column is player name,second is goals at home and third goals away.
   1.Find the total goals for each player
   2.Mean of home and away goals
   3.Standard deviation of home and away goals 

.. L25

{{{ Open the file football.txt and keep open for some time }}}

.. R25

This is the required data.

.. L26

{{{ Switch to slide Solution 1 }}}

.. R26

The solution is on your screen.

.. L27

{{{ Show summary slide }}}

.. R27

This brings us to the end of the tutorial.
In this tutorial,we have learnt to,

 1. Do the standard statistical operations sum , mean
    median and standard deviation in Python.
 #. Combine text loading and the statistical operation to solve
    real world problems.

.. L28

{{{Show self assessment questions slide}}}

.. R28

Here are some self assessment questionss for you to solve

1. Given a two dimensional list,
   two_dimensional_list=[[3,5,8,2,1],[4,3,6,2,1]]
   how do we calculate the mean  of each row?
   

2. Calcutate the median of the given list?
   student_marks=[74,78,56,87,91,82]

  
3. Suppose there is a file with 6 columns but we wish to load text 
   only in columns 2,3,4,5. How do we specify that?

.. L29

{{{solution of self assessment questions on slide}}}

.. R29

And the answers,

1. To get the mean of each row, we just pass 1 as the second parameter to the function ``mean``.
::

    mean(two_dimensional_list,1)

2. We use the function ``median`` to calculate the median of the list
::

    median(student_marks)

3. To specify the particular columns of a file, we use the parameter usecols=(2,3,4,5)

.. L30

{{{ Show the Thank you slide }}}

.. R30

Hope you have enjoyed this tutorial and found it useful.
Thank you!

