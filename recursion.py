# factorial(n) = n * factorial(n-1)

class recursion:
    @staticmethod
    def factorial(n: int):
        """Computes the factorial of a specified number.

        Args:
            n (int): specified number; for example, 6

        Returns:
            int: computed factorial
        """
        # this is the stopping case  
        if (n == 1):
            return n 
        else:
           # this is the general rule that includes the 
           # recursive call
           return n * recursion.factorial(n - 1)
        
    @staticmethod
    def power(number: int, power: int):
        """Takes a specified number to a specified power

        Args:
            number (int): specified number; for example, 2
            power (int): specified powerl for example, 5

         Returns:
            int: computed power   
        """ 
        # this is our stopping case
        if (power == 0):
            return 1
        else:
            return number * recursion.power(number,power - 1)
        
    @staticmethod
    def computeMin(nums, i: int, min: int):
        """Finds the mininum number is a specified list of numbers 

        Args:
             nums: specified list
            
        Returns:
            int: mininum number
        """        
        
        # this is the stopping case 
    
        while (i == len(nums)):
            return min
        else:
             if (nums[i] <=min): 
                min = nums[i]
             return recursion.computeMin(nums, i + 1 , min)
        
    @staticmethod
    def reverse(s: str, i: int):
        """ Displays a specified string in reverse

        Args:
        s (str): specified string
        """ 
        if (i == 0):
            print(" is the reverse of %s using recursion." % (s))
        else:
            print(s[i - 1], end="")
            recursion.reverse(s, i - 1)
        
    @staticmethod
    def search (a, first: int, size: int, target, i: int, found: bool):
        """Searches for a desired element in a list of elements
    starting at a[first].
    Args:
    a: the list to search
    first (int): the list index at which the search will start
    size (int): the number of elements to search
target: the element to search for
i: the counter variable used to iterate through list
found: the variable used to denote if the target has been found
Returns:
int: If target appears in the list, index of the element
that contains the target, else -1.
    """
    
  #stopping case
        while ((i < size) and not found and (i + first < len(a))):     
            return found
        
        else:
            if (a[i + first] == target):
                found = True
                i + 1

           
                return i + first
            
            else: 
                return recursion.search(i + 1, a, first, size, target, found )

#Question 8
class recursion:
    @staticmethod
    def dis(num: int):

        if (num == 0):
            print('loop')

        else:
            print(num,num)
            print(num - 1)

            recursion.dis(num - 1)

           