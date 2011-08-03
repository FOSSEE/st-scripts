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

 
.. Author              : Puneeth
   Internal Reviewer   : 
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <06-11-2010, Anand,  OK> [2010-10-05]

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 
'Accessing pieces of arrays'.

.. L2

{{{ Show slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,
   
 1. Access and change individual elements of arrays, both one
    dimensional and multi-dimensional.
 #. Access and change rows and columns of arrays. 
 #. Access and change other chunks from an array, using slicing
    and striding. 
 #. Read images into arrays and perform processing on them, using
    simple array manipulations.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with arrays".

.. R4

As usual, we start IPython, using 

.. L4

{{{ Open the terminal }}}
::

    ipython -pylab 

.. L5

{{ Show the slide with the arrays, A and C }}

.. R5

Let us begin with the help of an example.
Let us have two arrays, A and C, as the sample arrays that we will
use to work through this tutorial. 

.. L6
::

    A = array([12, 23, 34, 45, 56])

    C = array([[11, 12, 13, 14, 15],
               [21, 22, 23, 24, 25],
               [31, 32, 33, 34, 35],
               [41, 42, 43, 44, 45],
               [51, 52, 53, 54, 55]])

.. R6

 Pause the recording and type the arrays A and C. also make sure 
 that you have typed the arrays correctly.
 <Pause>
 
Let us begin with the most elementary thing, accessing individual
elements. Also, let us first do it with the one-dimensional array
A, and then do the same thing with the two-dimensional array. 

.. R7

To access, the element 34 in array A, we say, 
A of 2, note that we are using square brackets.

.. L7
::

    A[2]

.. R8

Like lists, indexing starts from 0 in arrays, too. So, 34, the
third element has the index 2. 

Now, let us access the element 34 from C. To do this, we say,
C of 2,3.

.. L8
::

    C[2, 3]

.. R9

34 is in the third row and the fourth column, and since indexing
begins from zero, the row index is 2 and column index is 3. 

Now, that we have accessed one element of the array, let us change
it. We shall change 34 to -34 in both A and C. To do this, we
simply assign the new value after accessing the element. 

.. L9
::

    A[2] = -34
    C[2, 3] = -34

.. R10

Let us check our operations,

.. L10
::

    A[2]
    C[2,3]

.. R11

Now that we have accessed and changed a single element, let us
access and change more than one element at a time; first rows and
then columns.

Let us access one row of C, say the third row. We do it by saying, 

.. L11
::

    C[2] 

.. R12

How do we access the last row of C? We could say,

.. L12
::

    C[4] 

.. R13

or as with lists,we could use negative indexing and say,

.. L13
::

    C[-1]

.. R14

Now, we could change the last row into all zeros, using either 

.. L14
::

    C[-1] = [0, 0, 0, 0, 0]

.. R15

or, we can use, 

.. L15
::
  
    C[-1] = 0

.. R16

Now, how do we access one column of C? As with accessing individual
elements, the column is the second parameter to be specified (after
the comma). The first parameter, is replaced with a ``:``. This
specifies that we want all the elements of that dimension, instead of
just one particular element. We access the third column by saying,

.. L16
::
  
    C[:, 2]

.. R17

Pause the video here, try out the following exercise and resume the video.

.. L17

.. L18

{{{ Show slide with exercise 1 }}}

.. R18

 Change the last column of C to zeros. 

.. R19

Switch to the terminal for solution.To change the entire last column of 
C to zeros, we simply say,

.. L19

{{{ Continue from paused state }}}
{{{ Switch to the terminal }}}
::
  
    C[:, -1] = 0

.. R20

Since A is one dimensional, rows and columns of A don't make much
sense. It has just one row and A of colon gives the whole of A.

.. L20
::

    A[:]  

.. R21

Pause the video here, try out the following exercise and resume the video.

.. L21

.. L22

{{{ show slide containing exercise 2 }}} 

.. R22

 Change ``A`` to ``[11, 12, 13, 14, 15]``. 

.. R23

Switch to the terminal for solution.
To change A, we say,

.. L23

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    A[:] = [11, 12, 13, 14, 15]

.. R24

Now, that we know how to access, rows and columns of an array, we
shall learn how to access other pieces of an array. For this
purpose, we will be using image arrays. 

To read an image into an array, we use the ``imread`` command. We
shall use the image ``squares.png`` present in ``/home/fossee``. We
first navigate to that path in the OS and see what the image
contains. 

.. L24

{{{ switch to the browser and show the image }}}

{{{ switch back to the ipython terminal }}}

.. R25

Let us now read the data in ``squares.png`` into the array ``I``. 

.. L25
::

    I = imread('/home/fossee/squares.png')

.. R26

We can see the contents of the image, using the command
``imshow``. We say, imshow(I) to see what has been read into ``I``.

.. L26
::

    imshow(I) 

.. R27

We do not see white and black because, ``pylab`` has mapped 
white and black to different colors. 
This can be changed by using a different color map. 

To see that ``I`` is really, just an array, we say, I, at the prompt 

.. L27
::

    I 

.. R28

We see that an array is displayed. 

To check the dimensions of any array, we can use ``.shape`` function.

.. L28
::

    I.shape 

.. R29

As we can see,we got the dimensions of the image.The image,``squares.png``
has the dimensions of 300x300. 

.. L29

.. L30

{{{ Switch to slide squares.png }}}
{{{ Point at top-left quadrant of the image }}}

.. R30

Our goal for this part of the tutorial would be to get the
top-left quadrant of the image. To do this, we need to access, a
few of the rows and a few of the columns of the array. 

To access, the third column of C, we said, ``C[:, 2]``. Essentially,
we are accessing all the rows in column three of C. Now, let us
modify this to access only the first three rows, of column three
of C. 

We say, 

.. L31
::

    C[0:3, 2]

.. R31

C[0:3, 2] gives, the elements of rows indexed from 0 to 3, 3 not 
included and column indexed 2. Note that, the index before the colon is
included and the index after it is not included in the slice that
we have obtained. This is very similar to the ``range`` function,
where ``range`` returns a list, in which the upper limit or stop
value is not included.

.. R32

Now, if we wish to access the elements of row with index 2, and in
columns indexed 0 to 2 (included), we say, 

.. L32
::

    C[2, 0:3]

.. R33

Pause the video here, try out the following exercise and resume the video.

.. L33

.. L34

{{{ show slide containing exercise 3 }}} 

.. R34

First, obtain the elements [22, 23] from C. Then, obtain the
elements [11, 21, 31, 41] from C. Finally, obtain the elements 
[21,31, 41, 0]. 
<Pause>
Switch to the terminal for solution.

.. L35

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    C[1, 1:3] 

.. R35

C[1, 1:3] gives the elements [22, 23]

.. L36
::

    C[0:4, 0]

.. R36

C[0:4, 0] gives the elements [11, 21, 31, 41]

.. L37
::

    C[1:5, 0]

.. R37

C[1:5, 0] gives the elements [21, 31, 41, 0]

Note that when specifying ranges, if you are starting from the
beginning or going up-to the end, the corresponding element may be
dropped. So, in the previous example to obtain [11, 21, 31, 41], we
could have simply said, 

.. L38
::

    C[:4, 0]
    C[1:, 0]

.. R38

We get the elements [21, 31, 41, 0]. If we skip both the indexes,
we get the slice from end to end, as we already know. 

Pause the video here, try out the following exercise and resume the video.

.. L39
 
{{{ show slide containing exercise 4 }}} 

.. R39

 Obtain the elements [[23, 24], [33, -34]] from C. 

.. R40

Switch to the terminal for solution.

.. L40

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    C[1:3, 2:4] 

.. R41

C[1:3, 2:4] will give us the required elements. 

Now, we wish to obtain the top left quarter of the image. How do
we go about doing it? Since, we know the shape of the image is
300, we know that we need to get the first 150 rows and the first 150
columns. 

.. L41
::

    I[:150, :150]

.. R42

I[:150, :150] gives us the top-left corner of the image. 

.. R43

We use the ``imshow`` command to see the slice we obtained in the
form of an image and confirm. 

.. L43
::

    imshow(I[:150, :150])

.. R44

Pause the video here, try out the following exercise and resume the video.

.. L44

.. L45

{{{ show slide containing exercise 5 }}} 

.. R45

 Obtain the square in the center of the image.

.. R46

Switch to the terminal for solution.

.. L46

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    imshow(I[75:225, 75:225])

.. R47

Hence, we get the center of the image.

Our next goal is to compress the image, using a very simple
technique, so as to reduce the space that the image takes on disk, while
not compromising too heavily on the image quality. The idea is to
drop alternate rows and columns of the image and save it. This way
we will be reducing the data to one-fourth of the original data but
losing only a little of visual information. 

We shall first learn the idea of striding using the smaller array
C. Suppose we wish to access only the odd rows and columns (first,
third, fifth). We do this by, 

.. L47
::

    C[0:5:2, 0:5:2]

.. R48

if we wish to be explicit, we say, 

.. L48
::

    C[::2, ::2]

.. R49

This is very similar to the step specified to the ``range``
function. It specifies, the jump or step in which to move, while
accessing the elements. If no step is specified, a default value
of 1 is assumed. 

.. L49
::

    C[1::2, ::2] 

.. R50

we get the elements, [[21, 23, 0], [41, 43, 0]]
Pause the video here, try out the following exercise and resume the video.

.. L50

.. L51

{{{ show slide containing exercise 6 }}} 

.. R51

 Obtain the following. 
[[12, 0], [42, 0]]
[[12, 13, 14], [0, 0, 0]]

.. R52

The solution is on your screen.

.. L52

{{{continue from paused state}}}
{{{ show slide containing Solution 6 }}} 

.. R53

Now, that we know how to stride over an array, we can drop
alternate rows and columns out of the image in I. 

.. L53
::

    I[::2, ::2]

.. R54

To see this image, we say, 

.. L54
::

    imshow(I[::2, ::2])

.. R55

This does not have much data to notice any real difference, but
notice that the scale has reduced to show that we have dropped
alternate rows and columns. If you notice carefully, you will be
able to observe some blurring near the edges. To notice this
effect more clearly, increase the step to 4. 

.. L55
::

    imshow(I[::4, ::4])

.. L56

{{{ show summary slide }}}

.. R56

This brings us to the end of this tutorial. In this tutorial, we
have learnt to, 
 
 1. Manipulate single & multi dimensional arrays.
 #. Access and change individual elements by using their index numbers. 
 #. Access and change rows and columns of arrays by specifying the row 
    and column numbers.
 #. Slice and stride on arrays.
 #. Read images into arrays and manipulate them.

.. L57

{{{Show self assessment questions slide}}}

.. R57

Here are some self assessment questions for you to solve

1. Given the array, ``A = array([12, 15, 18, 21])``, how do we access
   the element ``18``?


2. Given the array, 
   
::
   
    B = array([[10, 11, 12, 13],
               [20, 21, 22, 23],
               [30, 31, 32, 33],
               [40, 41, 42, 43]])

Obtain the elements, ``[[21, 22], [31, 32]]``


3. Given the array, 
::
   
    C = array([[10, 11, 12, 13],
               [20, 21, 22, 23]])

Change the array to 
::
   
    C = array([[10, 11, 10, 11],
               [20, 21, 20, 21]])

.. L58
  
{{{solution of self assessment questions on slide}}}

.. R58

And the answers,

1. The element 18 in array A has index number 2.Hence, we access it as 
   A of 2
::

    A[2]

2. To obtain the center four numbers in the array B, we say,B[1:3, 1:3]
::

    B[1:3, 1:3]

3. We can change the elements of array C,by using slicing and striding
::

    C[:2, 2:] = C[:2, :2]

.. L59

{{{ Show the Thank you slide }}}

.. R59

Hope you have enjoyed this tutorial and found it useful.
Thank you!

