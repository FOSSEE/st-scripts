Hello friends and welcome to the tutorial on statistics using Python

{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline slide }}}

In this tutorial, we shall learn
 * Doing simple statistical operations in Python  
 * Applying these to real world problems 

You will need Ipython with pylab running on your computer
to use this tutorial.

Also you will need to know about loading data using loadtxt to be 
able to follow the real world application.

We will first start with the most necessary statistical 
operation i.e finding mean.

We have a list of ages of a random group of people ::
   
   age_list=[4,45,23,34,34,38,65,42,32,7]

One way of getting the mean could be getting sum of 
all the elements and dividing by length of the list.::

    sum_age_list =sum(age_list)

sum function gives us the sum of the elements.::

    mean_using_sum=float(sum_age_list)/len(age_list)

This obviously gives the mean age but python has another 
method for getting the mean. This is the mean function::

       mean(age_list)

Mean can be used in more ways in case of 2 dimensional lists.
Take a two dimensional list ::
     
     two_dimension=[[1,5,6,8],[1,3,4,5]]

the mean function used in default manner will give the mean of the 
flattened sequence. Flattened sequence means the two lists taken 
as if it was a single list of elements ::

    mean(two_dimension)
    flattened_seq=[1,5,6,8,1,3,4,5]
    mean(flattened_seq)

As you can see both the results are same. The other way is mean 
of each column.::
   
   mean(two_dimension,0)
   array([ 1. ,  4. ,  5. ,  6.5])

we pass an extra argument 0 in that case.

In case of getting mean along the rows the argument is 1::
   
   mean(two_dimension,1)
   array([ 5.  ,  3.25])

We can see more option of mean using ::
   
   mean?

Similarly we can calculate median and stanard deviation of a list
using the functions median and std::
      
      median(age_list)
      std(age_list)

Median and std can also be calculated for two dimensional arrays along columns and rows just like mean.

       For example ::
       
       median(two_dimension,0)
       std(two_dimension,1)

This gives us the median along the colums and standard devition along the rows.
       
Now lets apply this to a real world example 
    
We will a data file that is at the a path
``/home/fossee/sslc2.txt``.It contains record of students and their
performance in one of the State Secondary Board Examination. It has
180, 000 lines of record. We are going to read it and process this
data.  We can see the content of file by double clicking on it. It
might take some time to open since it is quite a large file.  Please
don't edit the data.  This file has a particular structure.

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
Science AA (Absent) ** Social 72
* Total marks 244
*

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
Thankyou
 
.. Author              : Amit Sethi
   Internal Reviewer 1 : 
   Internal Reviewer 2 : 
   External Reviewer   :

