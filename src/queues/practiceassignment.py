from queues.queue import*

class practiceassignment:
    @staticmethod
    def practiceassignment1(expression: str):
        """Checks if the expression its given reads the same forward and backward.

        Args:
            expression (str): specified expression

        Returns:
            Boolean: True is the specified expression is a palindrome, else
            False.
        """        
        q = queue() # queue to read the expression forward
        q2 = queue() # queue to read the expression backwards


        mismatches = 0 #used to keep track of the differences in the queue and stack

        # convert expression to upper-case
        expression = expression.upper()

       

        # loop through the expression a character at a time
        for e in expression:
            #if the current character is an alphabetic character
            if e.isalpha():
                
                
                q.enqueue(e)
        #use the reverse function thats what i was missing here
        for i in list(reversed(expression)):
            if i.isalpha():
                q2.enqueue(i)

        # while the queue isn't empty
        while (not q.isEmpty()):
            #if the element at the front of the queue isn't 
            #equal to the element at the top of the stack
            if (q.dequeue() != q2.dequeue()):
                #increment mismatches
                mismatches += 1

        #return True if mismatches is equal to 0, else return False
        return(mismatches == 0)
