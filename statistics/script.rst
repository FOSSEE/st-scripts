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

.. #[punch; add slides, exercises!]

Hello friends and welcome to the tutorial on Statistics using Python

{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline slide }}}

In this tutorial, we shall learn
 * Doing statistical operations in Python  
   * Summing set of numbers
   * Finding there mean
   * Finding there Median
   * Finding there Standard Deviation 
   


.. #[punch: since loadtxt is anyway a pre-req, I would recommend you
.. to use a data file and load data from that. that is good, since you
.. would get to deal with arrays, instead of lists. 

.. Talking of rows and columns of 2-D lists etc is confusing. Also,
.. converting to float can be avoided. The tutorial will feel more
.. natural, is what I think. 

.. The idea of separating the main problem and giving toy examples
.. doesn't sound good. Use the same problem to explain stuff. Or use a
.. smaller data-set or something. Using lists doesn't seem natural.]


For this tutorial We will use data file that is at the a path
``/home/fossee/sslc2.txt``.  It contains record of students and their
performance in one of the State Secondary Board Examination. It has
180,000 lines of record. We are going to read it and process this
data.  We can see the content of file by double clicking on it. It
might take some time to open since it is quite a large file.  Please
don't edit the data.  This file has a particular structure.

We can do ::
   
   cat /home/fossee/sslc2.txt

to check the contents of the file.


{{{ Show the data structure on a slide }}}

Each line in the file is a set of 11 fields separated 
by semi-colons Consider a sample line from this file.  
A;015163;JOSEPH RAJ S;083;042;47;00;72;244;;; 

The following are the fields in any given line.
* Region Code which is 'A'
* Roll Number 015163
* Name JOSEPH RAJ S
* Marks of 5 subjects: ** English 083 ** Hindi 042 ** Maths 47 **
Science 35 ** Social 72
* Total marks 244


Lets try and load this data as an array and then run various function on
it.

To get the data as an array we do. ::
   
     L=loadtxt('/home/amit/sslc2.txt',usecols=(3,4,5,6,7,),delimiter=';')
     L
     

loadtxt function loads data from an external file.Delimiter specifies
the kind of character are the fields of data seperated by.  usecols
specifies the columns to be used so (3,4,5,6,7) loads those
colums. The 'comma' is added because usecols is a sequence.

As we can see L is an array. We can get the shape of this array using::
   
   L.shape
   (185667, 5)

Lets start applying statistics operations on these. We will start with
the most basic, summing. How do you find the sum of marks of all
subjects for the first student.

As we know from our knowledge of accessing pieces of arrays. To acess
the first row we will do ::
   
   L[0,:]

Now to sum this we can say ::

    totalmarks=sum(L[0,:]) 
    totalmarks

To get the mean we can do ::

   totalmarks/len(L[0,:])

or simply ::

   mean(L[0,:])

But we have such a large data set calculating one by one the mean of
each student is impossible. Is there a way to reduce the work.

For this we will look into the documentation of mean by doing::

    mean?

As we know L is a two dimensional array. We can calculate the mean
across each of the axis of the array. The axis of rows is referred by
number 0 and columns by 1. So to calculate mean accross all colums we
will pass extra parameter 1 for the axis.::

    mean(L,1)

L here is the two dimensional array.

Similarly to calculate average marks scored by all the students for each
subject can be calculated using ::

   mean(L,0)

Next lets now calculate the median of English marks for the all the students
We can access English marks of all students using ::

   L[:,0]
   
To get the median we will do ::

   median(L[:,0])

For all the subjects we can use the same syntax as mean and calculate
median across all rows using ::

       median(L,0)
  

Similarly to calculate standard deviation for English we can do::

	  std(L[:,0])

and for all rows::

    std(L,0)

Following is an exercise that you must do. 

%% %% In the given file football.txt at path /home/fossee/football.txt , one column is player name,second is goals at home and third goals away.
   1.Find the total goals for each player
   2.Mean home and away goals
   3.Standard deviation of home and away goals 

{{{ Show summary slide }}}

This brings us to the end of the tutorial.
we have learnt

 * How to do the standard statistical operations sum , mean
   median and standard deviation in Python.
 * Combine text loading and the statistical operation to solve
   real world problems.

{{{ Show the "sponsored by FOSSEE" slide }}}


This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.

Thank you!

