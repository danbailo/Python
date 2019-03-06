# Python code to demonstrate range() vs xrange() 
# on  basis of memory 
  
import sys 
  
# initializing a with range() 
a = range(1,10000) 
  
# initializing a with xrange() 
x = list(range(1,10000))
  
# testing the size of a 
# range() takes more memory 
print ("The size allotted using range() is : ") 
print (sys.getsizeof(a)) 
  
# testing the size of a 
# range() takes less memory 
print ("The size allotted using xrange() is : ") 
print (sys.getsizeof(x)) 
