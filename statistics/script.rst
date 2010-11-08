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
     
.. Author              : Amit Sethi
   Internal Reviewer   : Puneeth
   External Reviewer   :
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]

.. #[punch; add slides, exercises!]

Hello friends and welcome to the tutorial on Statistics using Python

{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline slide }}}

In this tutorial, we shall learn
 * Doing simple statistical operations in Python  
 * Applying these to real world problems 


.. #[punch: since loadtxt is anyway a pre-req, I would recommend you
.. to use a data file and load data from that. that is good, since you
.. would get to deal with arrays, instead of lists. 

.. Talking of rows and columns of 2-D lists etc is confusing. Also,
.. converting to float can be avoided. The tutorial will feel more
.. natural, is what I think. 

.. The idea of separating the main problem and giving toy examples
.. doesn't sound good. Use the same problem to explain stuff. Or use a
.. smaller data-set or something. Using lists doesn't seem natural.]


We will first start with the most necessary statistical operation i.e
finding mean.

We have a list of ages of a random group of people ::
   
   age_list = [4,45,23,34,34,38,65,42,32,7]

One way of getting the mean could be getting sum of all the ages and
dividing by the number of people in the group. ::

    sum_age_list = sum(age_list)

sum function gives us the sum of the elements. Note that the
``sum_age_list`` variable is an integer and the number of people or
length of the list is also an integer. We will need to convert one of
them to a float before carrying out the division. ::

    mean_using_sum = float(sum_age_list)/len(age_list)

This obviously gives the mean age but there is a simpler way to do
this in Python - using the mean function::

       mean(age_list)

Mean can be used in more ways in case of 2 dimensional lists.  Take a
two dimensional list ::
     
     two_dimension=[[1,5,6,8],[1,3,4,5]]

The mean function by default gives the mean of the flattened sequence.
A Flattened sequence means a list obtained by concatenating all the
smaller lists into a large long list. In this case, the list obtained
by writing the two lists one after the other. ::

    mean(two_dimension)
    flattened_seq=[1,5,6,8,1,3,4,5]
    mean(flattened_seq)

As you can see both the results are same. ``mean`` function can also
give us the mean of each column, or the mean of corresponding elements
in the smaller lists. ::
   
   mean(two_dimension, 0)
   array([ 1. ,  4. ,  5. ,  6.5])

we pass an extra argument 0 in that case.

If we use an argument 1, we obtain the mean along the rows. ::
   
   mean(two_dimension, 1)
   array([ 5.  ,  3.25])

We can see more option of mean using ::
   
   mean?

Similarly we can calculate median and stanard deviation of a list
using the functions median and std::
      
      median(age_list)
      std(age_list)

Median and std can also be calculated for two dimensional arrays along
columns and rows just like mean.

For example ::
       
       median(two_dimension, 0)
       std(two_dimension, 1)

This gives us the median along the colums and standard devition along
the rows.
       
Now lets apply this to a real world example 
    
We will a data file that is at the a path ``/home/fossee/sslc2.txt``.
It contains record of students and their performance in one of the
State Secondary Board Examination. It has 180, 000 lines of record. We
are going to read it and process this data.  We can see the content of
file by double clicking on it. It might take some time to open since
it is quite a large file.  Please don't edit the data.  This file has
a particular structure.

We can do ::
   
   cat /home/fossee/sslc2.txt

to check the contents of the file.

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


Now lets try and find the mean of English marks of all students.

For this we do. ::

     L=loadtxt('/home/fossee/sslc2.txt',usecols=(3,),delimiter=';')
     L
     mean(L)

loadtxt function loads data from an external file.Delimiter specifies
the kind of character are the fields of data seperated by. 
usecols specifies  the columns to be used so (3,). The 'comma' is added
because usecols is a sequence.

To get the median marks. ::
   
    median(L)
   
Standard deviation. ::
	
    std(L)


Now lets try and and get the mean for all the subjects ::

     L=loadtxt('/home/fossee/sslc2.txt',usecols=(3,4,5,6,7),delimiter=';')
     mean(L,0)
     array([ 73.55452504,  53.79828941,  62.83342759,  50.69806158,  63.17056881])

As we can see from the result mean(L,0). The resultant sequence  
is the mean marks of all students that gave the exam for the five subjects.

and ::
    
    mean(L,1)

    
is the average accumalative marks of individual students. Clearly, mean(L,0)
was a row wise calcultaion while mean(L,1) was a column wise calculation.


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

