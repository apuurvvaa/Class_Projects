# Python3 program to find the  
# frequency of a digit in a number 
  
# function to find frequency 
# of digit in a number 
def frequencyDigits(n, d): 
      
    # Counter variable to  
    # store the frequency 
    c = 0; 
      
    # iterate till number 
    # reduces to zero 
    while (n > 0):  
          
        # check for equality 
        if (n % 10 == d): 
            c += 1; 
        # reduce the number 
        n = int(n / 10); 
  
    return c; 
  
# Driver Code 
  
# input number N 
N = 1122322; 
  
# input digit D 
D = 2; 
  
print(frequencyDigits(N, D));
