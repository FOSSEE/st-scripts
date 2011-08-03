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

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello Friends and Welcome to the tutorial on 'Testing and Debugging'.

.. L2

{{{ Show the objective slide }}}

.. R2

At the end of the tutorial, you will be able to,

 1. Understand what is software testing.
 #. Test simple functions for their functionality.
 #. Automate tests. 
 #. Understand the need for coding style 
 #. Learn some of the standards followed by the Python Community.
 #. Handle Errors and Exceptions.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with functions" and 
"Advanced Features of Functions".

.. R4

Now, what is software testing?
Software testing is an activity aimed at evaluating a program 
and determining that it meets its required results.

... R5

Lets first write a simple function to calculate gcd of two numbers.
Open an editor and type the code shown on the slide.

.. L5
 
{{{ Show slide, gcd function }}}

def gcd(a, b):
    if b == 0:
       return a
    return gcd(b, a%b)

{{{ Pause for some time and then continue }}}

.. R6

Now we need to evaluate this function. That is, we have to check whether 
this function successfully gives us the gcd of two whole numbers. Thus 
we need a set of inputs and the exact outputs that are expected for 
those input test cases.

Let our test case be 48 and 64 as *a* and *b* respectively. For this 
test case we know that the GCD is 16. So that is the expected output. 

.. L6

.. L7

{{{ Show slide,Test for gcd.py }}}

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a%b)
  
    if __name__ == '__main__':
        result = gcd(48, 64)
        if result != 16:
            print "Test failed"
        print "Test Passed"

{{{ Pause for some time and then continue }}}

.. R7

Let us include code for testing in our  gcd.py file 
Add the remaining lines of code to the file.
    
.. R8

Save the file as gcd.py in /home/fossee/ path

.. L8

{{{ Save the file as gcd.py }}}

.. R9

Let us now run the script and test our code
We run the code by providing the entire path where the file is located.

.. L9

{{{ Open a terminal }}}
::

    python /home/fossee/gcd_py

.. R10
          
We get the output as 'test passed' which means our code is correct.
Note that we have introduced a new semantic which uses two new magic 
names in Python *__name__* and *__main__*. This is a very common idiom 
used in Python. Every Python code in a file can be run in two ways: 
Either as an independent stand-alone script or as a Python module which 
can be imported by other Python scripts or modules.

.. L10

.. L11

{{{ Slide with the idiom }}}

.. R11

When the idiom
  
   if __name__ == '__main__':

is used, the code within this if block is executed first when we run the
Python file as a stand-alone script. In other words, when we run this
python file as a stand-alone script, the control of the program first 
starts from the code that is within this if block after which the control 
is transferred to other parts of the program or to other modules from
here. This comes as an extremely handy feature especially when we want to
test our modules individually.
      
But there can be a number of places where the gcd function might break. 
Would we have to write a seperate test case for all of them. 

Pause the video here, try out the following exercise and resume the video.

.. L12

{{{ Show slide with exercise 1 }}}

.. R12

  Write code for gcd and write tests for it  

.. R13

Well thats where automating tests come in. We can run many tests to 
check where our code can break. Lets see this with an example.First lets try 
and automate tests on the  gcd function. For this we will write a file 
with test cases and call the function for all of them.

.. L13

.. L14

{{{ Slide with the structure of file }}}
   
    |   12 |    28 |    4 |
    |   18 |    36 |   18 |
    | 4678 | 39763 | 2339 |

.. R14

The file structure is shown in form a table here.

The structure of the file will be the two parameters and the output result 
seperated by space
    
.. R15
   
Let us have this data in a file. 

.. L15

{{{ Open the file testcases.txt and show }}}

.. R15

We have seperated the elements by a space.

.. L16

{{{ Slide with code piece }}}

   if __name__ == '__main__':
       for line in open('testcases.txt'):
           numbers = line.split()
           x = int(numbers[0])
           y = int(numbers[1])
           result = int(numbers[2])
       if gcd(x, y) != result:
         print "Failed gcd test for", x, y
       else:
         print "Test passed", result

.. R16

We add this code piece to automate the test.         

.. L17

Let us now test this code. 
Open the file gcd.py which we had created before and add this piece of code

.. R17

{{{ Open the file gcd.py and add the above piece of code appropriately }}}

.. R18

Now, we run it as,

.. L18

{{{ Switch to terminal }}}
::

    python /home/fossee/gcd_py

.. R19

We see that our code has passed the test.

Pause the video here, try out the following exercise and resume the video.

.. L19

.. L20

{{{ Show slide with exercise 2 }}}

.. R20

For the same inputs as gcd write automated tests for LCM.

.. R21

We shall make use of the same automated test code which we had used for GCD
with minor changes.
The solution is on your screen.

.. L21

{{{ Switch to slide solution 2 }}}
 
  def gcd(a, b):
      if a % b == 0: 
          return b
      return gcd(b, a%b)
  def lcm(a, b):
      return (a * b) / gcd(a, b)
  if __name__ == '__main__':
      for line in open('lcmtestcases.txt'):
          numbers = line.split()
          x = int(numbers[0])
          y = int(numbers[1])
          result = int(numbers[2])
   if lcm(x, y) != result:
       print "Failed lcm test for", x, y
   else:
       print "Test passed", result

{{{ Pause for some time and then continue }}}

.. R22

This is the complete solution for the problem
You can test this code by running it on your terminal as we had done for gcd.py

.. L22

.. R23

Thus, for any program there can be innumerable test cases. 
Hence practically, it is not possible to test cases. However there are many 
ideas to reduce the set of test cases by testing those cases that are
 more likely to show errors.

Moving from testing lets talk a bit about coding style now.

Apart from from being able to perform the required task, a property
of a good program is its readability. Code is read more often than it is
written. This is because, that way, other people can learn from it and 
extend  and improve it. There are certain pointers for readable code 
that I am going to discuss.

First, Naming variables.

.. L23

.. L24

{{{ show slide, Meaning full names }}}

.. R24

We choose a name so that it becomes easier to understand it's usage.
Lets look at this with an example

  amount = 12.68
  denom = 0.05
  nCoins = round(amount/denom)
  rAmount = nCoins * denom
 
As we can see in the example it is very easy to make what the code is 
doing.

One can almost read it as English sentences.
Amount is 12.68
Denomination is .05
Number of coins is round of amount by denominations.

Proper naming helps so much in understanding the code.

.. L25

{{{ Slide with code style points }}}

.. R25

Also one should keep in mind the following things while writing a code. 
     
  1. Four Space Indentation
  2. Limit to 79 characters a line, but readability should come first.
  3. Functions and methods should be separated with two blank lines. 
  4. No inline comments, comments should be above the line they comment.
  5. Use Docstring to explain units of code performing specific task like
     functions.
  6. We should always have whitespace around operators and after 
     punctuation. 

Pause the video here, try out the following exercise and resume the video.

.. L26

{{{ Show slide with exercise 3 }}}

.. R26

 Give meaningful names to the variables in following code
  c=a/b

.. L27

{{{ Show slide with solution 3 }}}

.. R27

The solution is on your screen.

As you saw, this will help enormously towards making our program more 
readable.

.. R28

Now let us move on to handling errors and exceptions.  
Lets try out the following piece of code

.. L28

{{{ Open the terminal and navigate to the current location
you are working in }}}
::
    
    ipython
    while True print 'Hello world'

.. R29

So what happens when we do this on the interpreter. The interpreter 
says that this is a syntax error. Syntax error are caused when we
do not follow the rules of the programming language.

However lets try an expression like 

.. L29
::

    1/0

.. R30

Although this expression follows the programming language rules,
however it is not possible to express the solution of this expression.
Thus python throws an exception called ``ZeroDivisionError``. Exception 
is special kind of failure reported by the programming language.

Lets see why and how we can use Exception in our programs.

.. L30

{{{Open another terminal and type ipython }}} 
::
    
    ipython  
    a = raw_input("Enter a number:")

{{{ Enter a non-numeric input }}}
::

    num = int(a) 

.. R31

You will notice that when you run this program and give and
non-numeric input it throws a 'ValueError' Exception. 

.. L31

.. R32

So now we can 'catch' this exception and write code to 
handle it.

.. L32

{{{ Slide with code snippet }}} 

.. R33

For this we have try and except clause in python. Lets change our 
previous code slightly.

.. L33
::
 
    a = raw_input("Enter a number")

{{{ Enter a decimal number }}}

::

   try:
      num = int(a)
    except:
     print "Wrong input ..."

.. R34

In this piece of code, python tries to run the code inside the ``try``
block but when if it fails it executes the code block in ``except``.
In previous example we encountered a problem with running our conversion
to integer code. We found out what caused the error and then deviced a 
solution for it. This whole process is called debugging.
 
One can understand the debugging process using the figure.

In debugging process, we form a hypothesis of what causes the error.
Test if it is correct by changing the code. And refine the hypothesis 
on the basis of our result.

.. L34

.. R35

Lets see another example of debugging. Create a file mymodule.py and
add the following code

.. L35

{{{ Open an editor and type the following code }}}
::
    
    def test():
     total=1+1
     print spam

{{{ Save it as file mymodule.py }}}

.. R36

Lets now try and run this code on the ipython interpreter

.. L36
::
    
    import mymodule 
    mymodule.test()

.. L37

{{{ Slide with idb and total being accessed }}}

.. R37

Interpreter gives us an error because spam is not defined. 

.. R38

lets now do %debug on ipython interpreter. 

.. L38
::

    %debug

.. R39

The prompt on the shell has changed to ipdb. This is debugger here 
you can access variables in that code block for example 'total'unlike 
the normal interpreter.
Type,

.. L39
::

    total

.. R40

We get the correct output.
To exit from the ipdb prompt, press q

.. L40

.. L41

{{{ Show the summary slide }}}
 
.. R41
	 
This brings us to the end of this tutorial.In this tutorial,we have learnt to,

 1. Create simple tests for a function.
 #. Automate tests using many predefined test cases.
 #. Use the python coding standards.
 #. Differentiate between syntax error and exception.
 #. Handle exception using ``try`` and ``except``.
 #. Use ``%debug`` for debugging on ipython.

.. L42

{{{Show self assessment questions slide}}}

.. R42

Here are some self assessment questions for you to solve

1. What is proper indentation for python code according to style 
   guidelines?

    - two space identation
    - three space identation
    - four Space Indentation
    - no Indentation 
   

2. How do you start the debugger on ipython?
    - debug
    - %debug
    - %debugger
    - start debugger
  

3. What is the idiom used for running python scripts in a standalone 
   manner?
   
.. L43
  
{{{solution of self assessment questions on slide}}}

.. R43

And the answers,

1. Four Space Indentation is required for writing a python code 
   according to style guidelines.

2. We start the debugger on ipython by saying,
::

    %debug

3. ``if __name__ == '__main__':`` is the idiom used for running python 
   scripts in a standalone manner.


.. L44

{{{ Show the Thank you slide }}}

.. R44

Hope you have enjoyed this tutorial and found it useful.
Thank you!


