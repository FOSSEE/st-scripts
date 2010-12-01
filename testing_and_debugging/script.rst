.. Objectives
.. ----------

.. Writing Simple Tests (Applying)
.. Automating these tests
.. Coding Style
.. Errors and Exceptions 

.. Prerequisites
.. -------------

..   1. Getting started with functions
..   2. Advanced Features of Functions   
     
.. Author              : Amit Sethi
   Internal Reviewer   : 
   External Reviewer   :
   Checklist OK?       : <put date stamp here, if OK> [2010-10-05]

Script
------

{{{ Show the slide containing title }}}

Hello Friends. Welcome to this tutorial on Testing and Debugging.

{{{ Show the outline slide }}}

In this tutorial we will learn.

1.What software Testing is? 
2.Learn to test simple functions for their functionality.
3.Learn how to automate tests. 
4.Need for coding style and some of the standards followed by the Python Community.
5.Handling Errors and Exceptions.

Software testing is an activity aimed at evaluating a program 
and determining that it meets its required results.

{{{ Slide with the function }}}

Lets first write a simple function to calculate gcd of two numbers.::

     def gcd(a, b):
      	 if b == 0:
            return a
      	 return gcd(b, a%b)

save this into a file "/home/fossee/gcd.py".

Now we need to evaluate this function. Thus we have to check whether 
function successfully gives us the gcd of two whole numbers. Thus we need
a set of inputs and the exact outputs that are expected for those input 
test cases.

Let our test case be 48 and 64 as *a* and *b* respectively. For this test
case we know that the GCD is 16. So that is the expected output. 

{{{ Slide with change in code }}}

Let us include code for testing in our  **gcd.py** file ::

  def gcd(a, b):
      if b == 0:
          return a
      return gcd(b, a%b)
  
  if __name__ == '__main__':
      result = gcd(48, 64)
      if result != 16:
          print "Test failed"
      print "Test Passed"
          
Note that we have introduced a new semantic which uses two new magic names
in Python *__name__* and *__main__*. This is a very common idiom used in
Python. Every Python code in a file can be run in two ways: Either as an
independent stand-alone script or as a Python module which can be imported
by other Python scripts or modules. When the idiom::

  if __name__ == '__main__':

{{{ Slide with the idiom }}}


is used, the code within this if block is executed first when we run the
Python file as a stand-alone script. In other words, when we run this
python file as a stand-alone script the control of the program first starts
from the code that is within this if block from which the control is
transferred to other parts of the program or to other modules from
here. This comes as an extremely handy feature especially when we want to
test our modules individually.
      
But there can be a number of places where the gcd function might break would we
have to right a seperate test case for all of them. 

Following is an (are) exercise(s) that you must do. 

%% %% Write code for lcm and write tests for it  

%% %% Answer is on the screen.

Well thats where automating tests come in. We can run many tests to check where our
code can break. Lets see this with an example. Lets try and automate tests on the 
gcd function. For this we will write a file with test cases and call the function
for all of them.

{{{ Slide with the structure of file }}}

The structure of the file will be the two parameters and the output result seperated 
by space::
    
    |   12 |    28 |    4 |
    |   18 |    36 |   18 |
    | 4678 | 39763 | 2339 |

The file structure is shown in form a table here.


{{{ Slide with code piece }}}

We add the code piece to automate the test.::


   if __name__ == '__main__':
      for line in open('testcases.txt'):
        numbers = line.split()
        x = int(numbers[0])
        y = int(numbers[1])
        result = int(numbers[2])
       	if gcd(x, y) != result:
            print "Failed gcd test for", x, y

%% %% Pause the video do the following exercise 
%% %% For the same inputs as gcd write automated tests for LCM.
%% %% The solution is on the screen

For any program there can be innumerable test cases thus it is not
possible to test cases. However there are many ideas to reduce the set of
test cases by testing those cases that are more likely to show errors.

Moving from testing lets talk a bit about coding style now.

Apart from from being able to perform the required task, a property
of a good program is its readability. Code is read more often than it is
written. This is because that way other people can learn from it and extend 
and improve it. There are certain pointers for readable code that I am going to discuss.

First, Naming variables.

{{{ Slide with code snippet }}}

Choose name that by which people will most likely guess the usage.Lets look at this 
with an example::

       amount = 12.68
       denom = 0.05
       nCoins = round(amount/denom)
       rAmount = nCoins * denom
 
As we can see in the example it is very easy to make what the code is doing.

One can almost read it as English sentences.
Amount is 12.68
Denomination is .05
Number of coins is round of amount by denominations.

Proper naming helps so much in understanding the code.

{{{ Slide with code style points }}}

Also one should use. ::
     
     1.Four Space Indentation
     2.Limit to 79 characters a line, but readability should come first.
     3.Functions and methods should be separated with two blank lines. 
     4.No inline comments, comments should be above the line they comment.
     5.Use Docstring to explain units of code performing specific task like
     	functions.
     6.We should always have whitespace around operators and after punctuation. 

%% %% Pause and do the following exercise
%% %% Give meaningful names to the variables in following
code
	c=a/b


This will help enormously towards making our program more readable.

From coding style lets move on to handling errors and exceptions.  

{{{ Slide with code snippet }}}

Lets try out the following piece of code::

     while True print 'Hello world'

{{{ Slide with Error }}}

what happens when we do this on the interpreter. The interpreter 
says that this is a syntax error. Syntax error are caused when we
do not follow the rules of the programming language.
   
{{{ Slide with expression }}}

However lets try an expression like ::

	1/0

{{{ Slide with Error }}}

Although this expression follows the programming language rules,
however it is not possible to express the solution of this expression.
Thus python throws an exception called ZeroDivisionError. Exception 
is special kind of failure reported by the programming language.



Lets see why and how we can use Exception in our programs.



Type on your interpreter::

     a = raw_input("Enter a number:")
     num = int(a) 

{{{ Run this code on interpreter with a character input }}}

You will notice that when you run this program and give and
non-numeric input it throws a 'ValueError' Exception. 

So now we can 'catch' this exception and write code to 
handle it.

{{{ Slide with code snippet }}} 

For this we have try and except clause in python. Lets change our 
previous code slightly.::

	 a = raw_input("Enter a number")
	 try:
		num = int(a)
   	 except:
		print "Wrong input ..."

{{{ Run the code with character input }}}

In this piece of code python tries to run the code inside the try
block but when if it fails it executes the code block in except.
	  
In previous example we encountered a problem with running our conversion
to integer code. We found out what caused the error and then deviced a solution
for it this whole process is called debugging.
 
One can understand the debugging process using the figure.

In debugging process we form a hypothesis of what causes the error.
Test if it is correct by changing the code. And refine the hypothesis 
on the basis of our result.



Lets see another example of debugging. Create a file mymodule.py and
add the following code::
    
    def test():
	total=1+1	
	print spam



Lets now try and run this code ::
     
     import mymodule 
     mymodule.test()


{{{ Slide with idb and total being accessed }}}

Interpreter gives us an error because spam is not defined 
but lets now do %debug on ipython interpreter. The prompt on the shell has changed to ipdb. This is debugger here you can access variables in that code block for example 'total'unlike the normal interpreter.

%% %% Pause and do the following exercise
%% %% Do the gcd program which takes input from user which tells
%% %% the user wrong input if it is not valid and quits for 'q'.
 


This brings us to the end of this tutorial on testing and debugging. 




{{{ Show the summary slide }}}
 	
In this tutorial we have learned to
1.Create simple tests for a function.
2.Learn to Automate tests using many predefined test cases.
3.Good coding standards.
4.Difference between syntax error and exception.
5.Handling exception using try and except.
6.Using %debug for debugging on ipython.

{{{ Show the "sponsored by FOSSEE" slide }}}

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!







