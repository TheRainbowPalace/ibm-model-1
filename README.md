# IBM Model 1

This is an implementation of the IBM Model 1 EM algorithm.
Given a bitext (of a source and target language aligned on a sentence level), 
it calculates the probability between 

# Usage
To run the program you are gonna need python version > 3.6 installed on 
your computer. Then download or clone the project and run
`> cd ibm-model-1`
`> ./main.py test-source.txt test-target.txt`
Also you can use your own source and target files of your own. Please note
that this implementation shall give an understanding of the IBM 1 algorithm with
EM.  
Besides running the the tool itself it can also be used as a library by 
including `ibm1_library.py` into your python file.

# Sentence alignment
If your bitext is not sentence aligned you can use a tool like sentalign.
You can either find the paper here 
https://www.microsoft.com/en-us/research/wp-content/uploads/2002/10/sent-align2-amta-final.pdf 
or use the implementation provided by Microsoft 
https://www.microsoft.com/en-us/download/details.aspx?id=52608.
