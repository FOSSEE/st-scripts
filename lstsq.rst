Hello friends and welcome to the tutorial on Least Square Fit

{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline slide }}}

In this tutorial, we shall look at generating the least square fit line for a
given set of points.

First let us have a look at the problem.

{{{ Show the slide containing problem statement. }}}

We have an input file generated from a simple pendulum experiment.

It contains two columns of data. The first column is the length of the
pendulum and the second is the corresponding time period of the pendulum.

As we know, the square of time period of a pendulum is directly proportional to
its length, we shall plot l vs t^2 and verify if the proportionality is linear.

If it is not linear, we shall generate a least square fit line.

{{{ show the slide containing explanation on least square fit }}}

As shown in the slide, we are first going to generate the two matrices tsq and
A. Then we are going to use the =lstsq= function to find the values of m and c.

To read the input file and parse the data, we are going to loadtxt function.
Type::

    data = loadtxt("/home/fossee/pendulum.txt")
    data

As you can see, data is a sequence containing 90 records. Each record contains
two values. The first is length and second is time period. But what we need is 
two sequences. One sequence containing all the length values and one containing
all the time values.

Hence we have to use the unpack option with loadtxt. It unpacks the data into
 sequences depending on the structure of data.

Type::

    l, t = loadtxt("/home/fossee/pendulum.txt", unpack=True)
    l
    t

We can see that l and t are two sequences containing length and time values
correspondingly.

Let us first plot l vs t^2. Type::

    tsq = t * t
    plot(l, tsq, 'bo')


{{{ switch to the plot window }}}

We can see that there is a visible linear trend.

let us now generate the A matrix with l values.
We shall first generate a 2 x 90 matrix with the first row as l values and the
second row as ones. Then take the transpose of it. Type::

    inter_mat = array((l, ones_like(l)))
    inter_mat

We see that we have intermediate matrix. Now we need the transpose.Type::

    A = inter_mat.T
    A

Now we have both the matrices A and tsq. We only need to use the =lstsq=
Type::

    result = lstsq(A, tsq)

The result is a sequence of values. The first item is the matrix p or in simple
words, the values of m and c. Hence, ::

    m, c = result[0]
    m
    c

Now that we have m and c, we need to generate the fitted values of t^2. Type::

    tsq_fit = m * l + c
    plot(l, tsq, 'bo')
    plot(l, tsq_fit, 'r')

We get the least square fit of l vs t^2

{{{ Pause here and try out the following exercises }}}

%% 2 %% change the label on y-axis to "y" and save the lines of code
        accordingly

{{{ continue from paused state }}}

{{{ Show summary slide }}}

This brings us to the end of the tutorial.
we have learnt
 * how to use loadtxt to read files
 * how to generate a least square fit

{{{ Show the "sponsored by FOSSEE" slide }}}

#[Nishanth]: Will add this line after all of us fix on one.
This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thankyou
 
.. Author              : Nishanth
   Internal Reviewer 1 : 
   Internal Reviewer 2 : 
   External Reviewer   :
