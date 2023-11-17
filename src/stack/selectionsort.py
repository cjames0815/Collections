from node.node import *
from stack.stack import *
from stack.balanceparens import *
from stack.calculator import *
from stack.serialsearch import*


def selectionsort (data: stack, first: int):
    """Sorts a stack from smallest to largest 
    bypassing the nodes to the left of first.

    Args:
        data (stack): stack to be sorted
        first (int): the node position at which
        the sort will begin
    """    
    
    cursor = stack # used to step through calling node
    i = 1 # used to count nodes
    try:
# if position is less than one, raise error
        if (first < 1):
            raise ValueError("Position may not be less than 1.")
    except ValueError as e:
# display error and exit
        exit(e)
    else:
# move cursor forward the correct number nodes

# keep looping as long as i is less than specified position
# and cursor isn't equal to None
# if cursor becomes None that means specified position was greater than
# number of nodes in specified node
     while ((i < first) and (cursor != None)):
# move cursor to next node
         cursor = cursor.getLink()
# increment counter
         i = i + 1
# set data value in node cursor refers to
     cursor.getData(data)





    
    

         
    
    
   