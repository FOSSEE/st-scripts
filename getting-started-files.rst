========
 Script
========

Welcome to the tutorial on getting started with files. 

{{{ Screen shows welcome slide }}}

{{{ Show the outline for this tutorial }}} 

In this tutorial we shall learn to read files, and do some basic
actions on the file, like opening and reading a file, closing a
file, iterating through the file line-by-line, and appending the
lines of a file to a list. 

{{{ switch back to the terminal }}}

As usual, we start IPython, using 
::

  ipython -pylab 

Let us first open the file, ``pendulum.txt`` present in
``/home/fossee/``. 
::

  f = open('/home/fossee/pendulum.txt')

``f`` is called a file object. Let us type ``f`` on the terminal to
see what it is. 
::

  f

The file object shows, the file which is open and the mode (read
or write) in which it is open. 

We shall first learn to read the whole file into a single
variable. Later, we shall look at reading it line-by-line. We use
the ``read`` method of ``f`` to read, all the contents of the file
into the variable ``pend``. 
::

  pend = f.read()

Now, let us see what is in ``pend``, by typing 
::

  print pend

We can see that ``pend`` has all the data of file. Type just ``pend``
to see more explicitly, what it contains. 
::

  pend

%%1%% Pause the video here and split the variable into a list,
``pend_list``, of the lines in the file and then resume the
video. Hint, use the tab command to see what methods the string
variable has. 

#[punch: should this even be put? add dependency to strings LO,
where we mention that strings have methods for manipulation. hint:
use splitlines()]
::

  pend_list = pend.splitlines()

  pend_list

Now, let us learn to read the file line-by-line. But, before that
we will have to close the file, since the file has already been
read till the end. 
#[punch: should we mention file-pointer?]

Let us close the file opened into f.
::

  f.close()

Let us again type ``f`` on the prompt to see what it shows. 
::

  f

Notice, that it now says the file has been closed. It is a good
programming practice to close any file objects that we have
opened, after their job is done.

Let us, now move on to reading files line-by-line. 

%%1%% Pause the video here and re-open the file ``pendulum.txt``
with ``f`` as the file object, and then resume the video.

We just use the up arrow until we reach the open command and issue
it again. 
::

  f = open('/home/fossee/pendulum.txt')

Now, to read the file line-by-line, we iterate over the file
object line-by-line, using the ``for`` command. Let us iterate over
the file line-wise and print each of the lines. 
::

  for line in f:
      print line

As we already know, ``line`` is just a dummy variable, and not a
keyword. We could have used any other variable name, but ``line``
seems meaningful enough.

Instead of just printing the lines, let us append them to a list,
``line_list``. We first initialize an empty list, ``line_list``. 
::

  line_list = [ ]

Let us then read the file line-by-line and then append each of the
lines, to the list. We could, as usual close the file using
``f.close`` and re-open it. But, this time, let's leave alone the
file object ``f`` and directly open the file within the for
statement. This will save us the trouble of closing the file, each
time we open it. 

for line in open('/home/fossee/pendulum.txt'):
line_list.append(line)

Let us see what ``line_list`` contains. 
::

  line_list

Notice that ``line_list`` is a list of the lines in the file, along
with the newline characters. If you noticed, ``pend_list`` did not
contain the newline characters, because the string ``pend`` was
split on the newline characters. 

{{{ show the summary slide }}}

That brings us to the end of this tutorial. In this tutorial we
have learnt to open and close files, read the data in the files as
a whole, using the read command or reading it line by line by
iterating over the file object. 

Thank you!   

