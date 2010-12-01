.. Objectives
.. ----------
   
   .. By the end of this tutorial, you will be able to:
   
   ..   1. Access and change individual elements of arrays, both one
   ..   dimensional and multi-dimensional.
   ..   2. Access and change rows and columns of arrays. 
   ..   3. Access and change other chunks from an array, using slicing
   ..   and striding. 
   ..   4. Read images into arrays and perform processing on them, using
   ..   simple array manipulations. 

.. Prerequisites
.. -------------

..   1. getting started with arrays

.. #[anand: internal reviewer not mentioned]     
.. Author              : Puneeth
   Internal Reviewer   : 
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <06-11-2010, Anand,  OK> [2010-10-05]

Script
------

{{{ Screen shows welcome slide }}}

Welcome to the tutorial on accessing pieces of arrays

{{{ Show the outline for this tutorial }}} 

In this tutorial we shall learn to access individual elements of
arrays, get rows and columns and other chunks of arrays using
slicing and striding. 

{{{ switch back to the terminal }}}

As usual, we start IPython, using 
::

  ipython -pylab 


{{ Show the slide with the arrays, A and C }}

Let us have two arrays, A and C, as the sample arrays that we will
use to work through this tutorial. 

::

  A = array([12, 23, 34, 45, 56])

  C = array([[11, 12, 13, 14, 15],
             [21, 22, 23, 24, 25],
             [31, 32, 33, 34, 35],
             [41, 42, 43, 44, 45],
             [51, 52, 53, 54, 55]])

Pause the video here and make sure you have the arrays A and C,
typed in correctly.

{{{ Pause the recording and type the arrays A,C }}}

Let us begin with the most elementary thing, accessing individual
elements. Also, let us first do it with the one-dimensional array
A, and then do the same thing with the two-dimensional array. 

To access, the element 34 in A, we say, 

::

  A[2]

A of 2, note that we are using square brackets.

Like lists, indexing starts from 0 in arrays, too. So, 34, the
third element has the index 2. 

Now, let us access the element 34 from C. To do this, we say
::

  C[2, 3]

C of 2,3.

34 is in the third row and the fourth column, and since indexing
begins from zero, the row index is 2 and column index is 3. 

Now, that we have accessed one element of the array, let us change
it. We shall change the 34 to -34 in both A and C. To do this, we
simply assign the new value after accessing the element. 
::

  A[2] = -34
  C[2, 3] = -34

Now that we have accessed and changed a single element, let us
access and change more than one element at a time; first rows and
then columns.

Let us access one row of C, say the third row. We do it by saying, 
::

  C[2] 

How do we access the last row of C? We could say,
::

  C[4] 

for the fifth row, or as with lists, use negative indexing and say
::

  C[-1]

Now, we could change the last row into all zeros, using either 
::

  C[-1] = [0, 0, 0, 0, 0]

or 

::
  
  C[-1] = 0

Now, how do we access one column of C? As with accessing individual
elements, the column is the second parameter to be specified (after
the comma). The first parameter, is replaced with a ``:``. This
specifies that we want all the elements of that dimension, instead of
just one particular element. We access the third column by

::
  
  C[:, 2]

Following is an exercise that you must do. 

{{ show slide containing Question 1}} 

%%1%% Change the last column of C to zeroes. 

Please, pause the video here. Do the exercises and then continue. 

::
  
  C[:, -1] = 0

Since A is one dimensional, rows and columns of A don't make much
sense. It has just one row and 
::

  A[:] 

gives the whole of A. 

Following is an exercise that you must do. 

{{ show slide containing Question 2}} 

%%2%% Change ``A`` to ``[11, 12, 13, 14, 15]``. 

Please, pause the video here. Do the exercises and then continue. 

To change A, we say
::

  A[:] = [11, 12, 13, 14, 15]

Now, that we know how to access, rows and columns of an array, we
shall learn how to access other pieces of an array. For this
purpose, we will be using image arrays. 

To read an image into an array, we use the ``imread`` command. We
shall use the image ``squares.png`` present in ``/home/fossee``. We
shall first navigate to that path in the OS and see what the image
contains. 

{{{ switch to the browser and show the image }}}

{{{ switch back to the ipython terminal }}}

Let us now read the data in ``squares.png`` into the array ``I``. 
::

  I = imread('/home/fossee/squares.png')

We can see the contents of the image, using the command
``imshow``. We say, 
::

  imshow(I) 

to see what has been read into ``I``. We do not see white and black
because, ``pylab`` has mapped white and black to different
colors. This can be changed by using a different colormap. 

To see that ``I`` is really, just an array, we say, 
::

  I 

at the prompt, and see that an array is displayed. 

To check the dimensions of any array, we can use ``.shape``. We say

::

  I.shape 

to get the dimensions of the image. As we can see, ``squares.png``
has the dimensions of 300x300. 

Our goal for this part of the tutorial would be to get the
top-left quadrant of the image. To do this, we need to access, a
few of the rows and a few of the columns of the array. 

To access, the third column of C, we said, ``C[:, 2]``. Essentially,
we are accessing all the rows in column three of C. Now, let us
modify this to access only the first three rows, of column three
of C. 

We say, 
::

  C[0:3, 2]

to get the elements of rows indexed from 0 to 3, 3 not included
and column indexed 2. Note that, the index before the colon is
included and the index after it is not included in the slice that
we have obtained. This is very similar to the ``range`` function,
where ``range`` returns a list, in which the upper limit or stop
value is not included.

Now, if we wish to access the elements of row with index 2, and in
columns indexed 0 to 2 (included), we say, 
::

  C[2, 0:3]

Following is an exercise that you must do. 

{{ show slide containing Question 3 }} 

%%3%% First, obtain the elements [22, 23] from C. Then, obtain the
elements [11, 21, 31, 41] from C. Finally, obtain the elements [21,
31, 41, 0]. 

Please, pause the video here. Do the exercises and then continue. 

{{ show slide containing Solution 3 }}

::

  C[1, 1:3] 

gives the elements [22, 23]
::

  C[0:4, 0]

gives the elements [11, 21, 31, 41]
::

  C[1:5, 0]

gives the elements [21, 31, 41, 0]

Note that when specifying ranges, if you are starting from the
beginning or going up-to the end, the corresponding element may be
dropped. So, in the previous example to obtain [11, 21, 31, 41], we
could have simply said, ::

  C[:4, 0]

and 
::

  C[1:, 0]

gives the elements [21, 31, 41, 0]. If we skip both the indexes,
we get the slice from end to end, as we already know. 

Following is an exercise that you must do. 

{{ show slide containing Question 4 }} 

%%4%% Obtain the elements [[23, 24], [33, -34]] from C. 

Please, pause the video here. Do the exercises and then continue. 

{{ show slide containing Solution 4 }} 

::

  C[1:3, 2:4] 

gives us the elements, [[23, 24], [33, -34]]. 

Now, we wish to obtain the top left quarter of the image. How do
we go about doing it? Since, we know the shape of the image to be
300, we know that we need to get the first 150 rows and first 150
columns. 
::

  I[:150, :150]

gives us the top-left corner of the image. 

We use the ``imshow`` command to see the slice we obtained in the
form of an image and confirm. 
::

  imshow(I[:150, :150])

Following is an exercise that you must do. 

{{ show slide containing Question 5 }} 

%%5%% Obtain the square in the center of the image.

Please, pause the video here. Do the exercises and then continue. 

{{ show slide containing Solution 5 }} 

::

  imshow(I[75:225, 75:225])

Our next goal is to compress the image, using a very simple
technique to reduce the space that the image takes on disk while
not compromising too heavily on the image quality. The idea is to
drop alternate rows and columns of the image and save it. This way
we will be reducing the data to a fourth of the original data but
losing only so much of visual information. 

We shall first learn the idea of striding using the smaller array
C. Suppose we wish to access only the odd rows and columns (first,
third, fifth). We do this by, 
::

  C[0:5:2, 0:5:2]

if we wish to be explicit, or simply, 
::

  C[::2, ::2]

This is very similar to the step specified to the ``range``
function. It specifies, the jump or step in which to move, while
accessing the elements. If no step is specified, a default value
of 1 is assumed. 
::

  C[1::2, ::2] 

gives the elements, [[21, 23, 0], [41, 43, 0]]

{{ show slide containing Question 6 }} 

Following is an exercise that you must do. 

%%6%% Obtain the following. 
[[12, 0], [42, 0]]
[[12, 13, 14], [0, 0, 0]]

Please, pause the video here. Do the exercises and then continue. 

{{ show slide containing Solution 6 }} 

::

  C[::3, 1::3]

gives the elements [[12, 0], [42, 0]]
::

  C[::4, 1:4]

gives the elements [[12, 13, 14], [0, 0, 0]]

Now, that we know how to stride over an array, we can drop
alternate rows and columns out of the image in I. 
::

  I[::2, ::2]

To see this image, we say, 
::

  imshow(I[::2, ::2])

This does not have much data to notice any real difference, but
notice that the scale has reduced to show that we have dropped
alternate rows and columns. If you notice carefully, you will be
able to observe some blurring near the edges. To notice this
effect more clearly, increase the step to 4. 
::

  imshow(I[::4, ::4])

{{{ show summary slide }}}

That brings us to the end of this tutorial. In this tutorial, we
have learnt to access parts of arrays, specifically individual
elements, rows and columns and larger pieces of arrays. We have
also learnt how to modify arrays, element wise or in larger
pieces.

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 70
   End:
