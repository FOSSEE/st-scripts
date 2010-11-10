1 Module 1: Basic Plotting (16) 
================================

1.1 ABCD 
---------
* Audience 
  + same 
* Behaviour 
  - should be able to generate plots with any combination of built-in
    mathematical functions provided by pylab
* Condition 
  - being learnt in a self-study tutorial.
  - have python setup in their machine
* Degree 
  - RBT - Ap
  

1.2 LO: getting started with =ipython= (2) [punch] 
---------------------------------------------------
* Objective 
  Participants will be able to invoke and use basic features of ipython. 
* ABCD 
  + Condition 
    - have =python= & =ipython= setup in their machine. no mention of =pylab=
* Assessment Strategy 
  Built-in interspersed exercises
  - workbook
    + errors, make connection with error message
* Outline 
  + invoking ipython 
    if there's a problem, pre-requisites are not met. 
  + getting out 
  + explain the prompt 
  + typing commands 
    - 1+2 
      * careful wording to differentiate from print 
    - print 1+2 
    - history (up, down arrows) 
    - backspace, delete key 
    - tab completion 
      * ab 
      * a 
      * rou 
      * ro 
      * r 
  + =abs?=, =round?= 
  + handling typing errors 
    - round(2.48,
      + close it
      + use ^C  

1.3 LO: using the =plot= command interactively (2) [amit] 
----------------------------------------------------------
* Outline 
  + ipython -pylab 
    - pylab brings in the libraries necessary for Scientific Computing. 
  + =linspace=, 
  + =len= 
  + =clf= 
  + =plot= 
  + using the plot ui 

1.4 LO: embellishing a plot (2) [nishanth] 
-------------------------------------------
* Outline 
  + [X]line width, color, style 
  + [X]Title 
  + [X]Label 
  + [X]annotations 

1.5 LO: saving plots (2) [anoop] 
---------------------------------
* Outline 
  + basic savefig 
  + png, pdf, ps, eps, svg 
  + going to OS and looking at the file 

1.6 LO: multiple plots (3) [madhu] 
-----------------------------------
* Outline 
  + overlays 
    - linspace 
      * give one with very few points, more points 
      * show smoothness of the curve 
  + legend 
  + figure 1, figure2 
  + subplots 

1.7 LO: additional features of IPython (2) [nishanth] 
------------------------------------------------------
* Outline 
  + =%save=, =%history=, =%run= 

1.8 LO: module level assessment (3) [madhu] 
--------------------------------------------
* 10-12 question, time the questions 
* pause & and play when ready to look at answers 
* show the answers 
* one large or two medium questions 
* ex: four_plot 
  

2 Module 2: Plotting Experimental Data (12) 
============================================

2.1 ABCD 
---------
* Audience 
  + same 
* Behaviour 
  - should be able to generate plots with numeric data from files.
* Condition 
  - being learnt in a self-study tutorial.
  - have python setup in their machine
* Degree 
  - Same

2.2 LO: loading data from files (3) [punch] 
--------------------------------------------
* loadtxt with unpack=True 
  + primes.list (one col) 
  + pendulum.txt (two col) 

2.3 LO: plotting the data (3) [amit] 
-------------------------------------
* plot L vs. T^2 
  + using square function 
* problem with 3 cols 
  + 3rd column is error 
  + error bar 

2.4 LO: other types of plots (3) [anoop] 
-----------------------------------------
* scatter 
* pie chart 
* bar chart 
* log 
* illustration of other plots, matplotlib help 

2.5 LO: module level assessment (3) [nishanth] 
-----------------------------------------------
* pos.txt is evaluation 
  

3 Module 3: Handling Large Data Files (17) 
===========================================

3.1 LO: getting started with lists (2) [amit] 
----------------------------------------------
* empty 
* filled lists 
  + heterogenity 
* accessing 
* len 
* =append= elements 
* del (+ remove) 

3.2 LO: getting started with =for= (2) [anoop] 
-----------------------------------------------
* blocks in python 
  + (indentation) 
* blocks in ipython 
  + ... prompt 
  + hitting enter 
* =for= with a list 
* =range= function 

3.3 LO: getting started with strings (2) [madhu] 
-------------------------------------------------
* strings 
  + single, double, triple quoted 
* accessing elements 
* show immutability 
* tell that there are methods for manipulation 

3.4 LO: getting started with files (3) [punch] 
-----------------------------------------------
* show file object 
* read the file with =read= 
* closing the file 
* for line in file: 
* print a line 
* append the lines to a list 

3.5 LO: parsing data (3) [nishanth] 
------------------------------------
* explain what is parsing 
* strip (with strings) 
* split (with strings) 
  + with delimiters 
    - specify space as delimiter 
* datatype conversion 
* reading from files 
  + do the same problem done with loadtxt (for pendulum) 
  + basic parse sslc text 

3.6 LO: statistics (2) [amit] 
------------------------------
* mean 
  + summing 
* median 
* std 

3.7 LO: module level assessment (3) [madhu] 
--------------------------------------------
* mean g 
  

4 Module 4: Arrays and Matrices (14) 
=====================================

4.1 LO: getting started with arrays (2) [anoop] 
------------------------------------------------
* why arrays 
  + speed - simply say 
  + array level operations 
* creating arrays 
  + direct data 
  + list conversion 
  + homogeneous 
  + builtins - identitiy, zeros, 
* array operations 
  + =+ - * /= 

4.2 LO: accessing parts of arrays (4) [punch] 
----------------------------------------------
* accessing individual elements 
* slicing, striding 
* image manipulation 

4.3 LO: Matrices (3) [anoop] 
-----------------------------
* creating matrices 
  + direct data 
  + list conversion 
  + builtins - identitiy, zeros, 
* matrix operations 
  + + - * / 
  + dot 
  + inv 
  + det 
  + eig 
  + norm 
  + svd 

4.4 LO: Least square fit (2) [nishanth] 
----------------------------------------
* show pendulum 
  + use loadtxt 
* lstsq 

4.5 LO: Assessment (3) [punch] 
-------------------------------
* extract faces from a group photograph 

5 Module 5: using Sage (13) 
============================

5.1 LO: getting started with sage notebook (3) [madhu] 
-------------------------------------------------------
* about sage 
  + ... 
* starting the notebook server 
* using the UI 
  + typesetting & print 
  + selecting language 
    - sage 
    - LaTeX 
    - python 
  + help 
    - sum(<tab> 
    - ? 

5.2 LO: getting started with symbolics (3) [amit] 
--------------------------------------------------
* symbolic expressions 
  + built-in constants & functions 
  + algebraic expressions, 
  + series 
  + integration, differentiation 
  + matrices 
* symbolic functions 
  + defining 
* simplification 
* finding roots & factors 
* substituting expressions 
* output formats 

5.3 LO: using Sage (4) [punch] 
-------------------------------
* ABCD 
  + Degree 
    - RBT - U 
* Calculus 
  + limits 
  + differentiation 
  + integration 
    - indefinite 
    - definite 
  + piece-wise functions 
  + differential equations 
  + maxima, minima 
* Linear Algebra 
  + Vectors and Matrices 
    - constructions 
  + Vector Operations 
    - linear combination 
    - dot 
    - cross 
    - pairwise 
  + Matrix Operations 
    - linear combination 
    - matrix multiplication 
    - inverse 
    - transpose 
    - adjoint 
    - rank 
    - determinant 
    - trace 
    - norm 
  + Solving equations 
  + Eigenvalues, eigenvectors 
* Graph Theory 
* Number Theory 

5.4 LO: using sage to teach (3) [nishanth] 
-------------------------------------------
* @interact 
* 2D, 3D graphics 
* Graph Theory 
* Share, Publish 
* print 

5.5 LO: Assessment (3) [anoop] 
-------------------------------
* 5 questions 
* choice of exercises from one area 

6 Module 6: Python Language: Basics (12)
=======================================

6.1 LO: basic datatypes & operators (4) [amit]
----------------------------------------------
* int 
  + L, long 
* float 
  + repr, str 
* complex
  + methods like imag, real
* boolean
  + short circuit logic
* conversion functions
* sequence datatypes & mutability 
  + list available sequence datatypes 
    - string 
    - list 
    - tuple 
  + mutability 
  + conversion 
  + common stuff 
    - len 
    - in 
    - max, min, sum, sorted, reversed 
    - accessing individual elements 
    - slicing, striding 
    - containership

6.2 LO: I/O (1) [nishanth]
--------------------------
* print statement
* raw_input

6.3 LO: conditionals (2) [Madhu]
--------------------------------
* if, elif, else 
* pass 
* ternary operator

6.4 LO: loops (2) [punch]
-------------------------
* while
* for
* pass, break, continue

6.5 LO: Assessment (3) [Anoop]
------------------------------
* 10 Questions
* One of collatz or armstrong numbers


7 Module 7: Python Language: Datastructures (14)
================================================

7.1 LO: manipulating lists (3) [Madhu]
--------------------------------------
* concatenation
* slicing
* striding
* .sort 
* sorted 
* .reverse 
* reversed 

7.2 LO: manipulating strings (2) [punch]
----------------------------------------
* upper, lower, 
* replace 
* slicing 
* [::-1] 
* reversed 
* palindrome check 

7.3 LO: getting started with tuples (2) [nishanth]
--------------------------------------------------
* immutability 
* tuple packing, unpacking 
  + a, b = b, a 
* accessing individual elements 
* slicing, striding 

7.4 LO: dictionaries (2) [anoop]
--------------------------------
* empty 
* filled 
* accessing via keys 
* .values(), .keys() 
* in 
* iteration

7.5 LO: sets (2) [nishanth] 
---------------------------
* Operations
  + Union
  + Intersection
  + Complement
  + Symmetric Difference
* Containership
* Subset
* len

7.6 LO: Assessment (3) [amit]
-----------------------------
* 10 Questions
* Anagrams for sets and dictionaries
* A problem for lists and strings

8 Module 8: Python Language: Advanced (16)
==========================================

8.1 LO: getting started with functions (3) [anoop]
-----------------------------------------------------
* defining function
* arguments
* docstrings
* return values
  + can return multiple values
* code reading exercises

8.2 LO: advanced features of functions (3) [punch]
--------------------------------------------------
* default arguments
* keyword arguments
* built-in functions show off

8.3 LO: using python modules (3) [anoop]
----------------------------------------
* executing python scripts from command line
* import
* scipy
* pylab
* sys
* STDLIB modules show off

8.4 LO: writing python scripts (2)  [nishanth]
----------------------------------------------
* importing our own modules
* if __name__ == '__main__'

8.5 LO: testing and debugging (2) [amit]
----------------------------------------
* Types of errors and exceptions
* Strategy for debugging
  + Using print

8.6 LO: Assessment (3) [punch]
------------------------------
* 10 Questions
* Find four digit numbers whose digits are all even
* Write a script to use methods from pylab (like plot, show and other commands) and execute it as a stand-alone script


