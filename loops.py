class loops:
    @staticmethod
    def factorial(n: int):
        """Computes the factorial of a specified number.

        Args:
            n (int): specified number; for example, 6

        Returns:
            int: computed factorial
        """ 

        # the counter variable i more or less contains the 
        # #same value as the parameter n 

        # the loop will repeat as long as i > 1
        # the condition that will cause the loop to stop
        # is when i == 1 -> stopping case for the loop

        #with each iteration of the loop, we're decrementing
        # the counter variable by 1      
        i = n - 1
        while (i > 1):
            n = n * i
            # n = 6 * 5
            # n = 30 * 4
            # n = 120 * 3
            # n = 360 * 2
            i = i - 1

        return n 
    
    @staticmethod
    def power(number: int, power: int):
        """Takes a specified number to a specified power

        Args:
            number (int): specified number; for example, 2
            power (int): specified powerl for example, 5

         Returns:
            int: computed power   
        """ 
        # the counter variable for the loop contains the 
        # same value as power

        # the loop will repeat as long as i > 1
        # the condition that will cause the loop to stop
        # is when i == 0 -> stopping case for the loop


        # with each iteration of the loop, we're decrementing 
        # the counter variable by 1
        result = 1

#power(number,power) = number * power(number, power - 1)

        i = power
        while (i > 0):
            result = result * number
            # result = 1 * 2 : i = 5
            # result  = 2 * 2 : i = 4
            # result = 4 * 2 : i = 3
            #result = 8 * 2  : i = 2
            #result = 16 * 2 : i = 1
            i = i - 1

        return result

    @staticmethod
    def computeMin(nums):
        """Finds the minimum number is a specified list of numbers

        Args:
            nums (_type_): specified list

        Returns:
            int: minimum number
        """  
        # the counter variable of the loop is the 
        # index used to iterate through the elements in the list


        # the loop will repeat as long as i < len(nums)
        # the condition that will cause the loop to stop 
        # is i == len(nums) -> stopping case for the loop

        #with each iteration of the loop we're incrementing
        # the counter variable by 1

        # when the loop stops, it returns min      
        i = 0
        min = nums[i]
        
        while (i < len(nums)):
            if (nums[i] <=min): 
                min = nums[i]
            i += 1

        return min
    
    @staticmethod
    def reverse(s: str):
        """ Displays a specified string in reverse

            Args:
            s (str): specified string
        """ 
    # the counter variable in the loop is the index
    # used to iterate through the characters in the string
    # the stopping case for the loops is i == 0

    # with each iteration of the loop, we're
    # decrementing the counter variable

    #when the loop stops, we're printing a message   
        i = len(s)
        while(i > 0):
            print(s[i - 1], end="")
            i -= 1
        print(" is the reverse of %s using a loop." % (s))

    @staticmethod
    def search(a, first: int, size: int, target):
        """Searches for a desired element in a list of elements
    starting at a [first]

    Args:
        a (int):the list to search
        first (int): the list index at which the search will start
        size (int): the number of elements to search
        target (_type_): the element to search for


    Returns:
    int: If target appears in the list, indez of the element
    that contains the target, else -1
    """           

# set an int variable i to 0
        i = 0
# set a boolean variable found to false
        found = False
# while there are more elements to search
# and the target hasn't been found and
# i plus first doesn't exceed the length of
# the list
        while ((i < size) and not found and (i + first < len(a))):
# if the current element is the target
            if (a[i + first] == target):
# set found to true
                found = True
            else:
# increment i by 1
                i += 1

# check if the target was found
            if (found):
# return index of the target
                return i + first
            else:
# return negative 1
                return -1
            

    @staticmethod
    def evens (start: int, end: int):
        """Finds and displays the even numbers between a specified
starting and ending value.
Args:
start (int): specified starting value
end (int): specified ending value
"""
        i = start
        while (i <= end):
            if (i % 2 == 0):
                print(i, end=" ")
                i += 1