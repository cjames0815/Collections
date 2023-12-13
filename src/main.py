from node.node import*
from stack.stack import*
from stack.balanceparens import*
from stack.calculator import*
from stack.serialsearch import*
from stack.selectionsort import*
from queues.queue import*
from queues.palindrome import*
from queues.practiceassignment import*
from queues.majorassignment import*


def main():
    #testInit()

    #testInit
    #testGetterAndSetters()
    #testAddNodeAfter()
    #testRemoveNodeAfter()
    #review()
    #testListLength()
    #testListSearch()
    #testListPosition()
    #testListCopy()
    #testListCopyWithTail()
    #testreview()
    #assignment()
    #testPush()
    #testPop()
    #testIsEmpty()
    #testPeek()
    #print("Parenthesis are balanced?", balancedparens.isBalanced("{X+Y")) #False
    #print("Parenthesis are balanced?", balancedparens.isBalanced("{X+Y")) #False
    #print("Parenthesis are balanced?", balancedparens.isBalanced("({X+Y}*Z)")) #True
    #print("Parenthesis are balanced?", balancedparens.isBalanced("[A+B]*({X+Y}*Z)")) #True
    #print("(((6+9)/3)*(6-4)) = ", calculator.evaluate("(((6+9)/3)*(6-4))"))
    #print("(6+(3*(6-4))) = ", calculator.evaluate("(6+(3*(6-4)))"))
    #print(" ((5+2)-(3*(6/9))) = ", calculator.evaluate("((5+2)-(3*(6/9)))"))
    #print("((5*2)-(3*(6/2))) = ", calculator.evaluate("((5*2)-(3*(6/2)))"))
    
    
    #testSerialSearch()

    #testSelectionSort()

    #testEnqueue()
    #testQueueisEmpty()
    #testDequeue()
    #testQueuePeek()
    #testIsPalindrome()
    #testpracticeassignment1()
    #testmajorassignment1()
    santaClaus()
    getPalindromes()
    

#Question 1
def santaClaus():
    s = node('A',None)
    s = node('T', s)
    s = node('N', s)
    s = node('A', s)
    s = node('S', s)

    s.setData('A')
    s.addNodeAfter('A')
    s.setData('T')
    s.addNodeAfter('T')
    s.setData('N')
    s.addNodeAfter('N')
    s.setData('A')
    s.addNodeAfter('A')
    s.setData('S')
    s.addNodeAfter('S')

#Question 2
    c = node('S', None)
    c = node('U', c)
    c = node('A', c)
    c = node('L', c)
    c = node('C', c)

    c.setData('S')
    c.addNodeAfter('S')
    c.setData('U')
    c.addNodeAfter('U')
    c.setData('A')
    c.addNodeAfter('A')
    c.setData('L')
    c.addNodeAfter('L')
    c.setData('C')
    c.addNodeAfter('C')


#Question 3
    selection = s

#Question 4
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()

#Question 5
    selection.setLink(s)

#Question 6
def getPalindromes():
    s1 = stack()
    s2 = stack()
    mismatches = 0
    


    ispalindrome = list(input("Enter ten words speparated by a space:")) 
    for pal in ispalindrome:
        if pal == ispalindrome:
            s1.push(pal)

    for pal in ispalindrome:
        if pal != ispalindrome:
            s2.push(pal)

    
            #if the current character is an alphabetic character
        if pal.isalpha():
                #push it onto the stack 
            s1.push(pal)
            s2.push(pal)


    print('These words are palindromes', end= " ")
    while(not  s1.isEmpty()):
        print(s1.pop(), end="")
    print(pal)

    print('These words are not palindromes', end= " ")
    while(not  s2.isEmpty()):
        print(s2.pop(), end="")
    print(pal)

    while (not s1.isEmpty()):
            #if the element at the front of the queue isn't 
            #equal to the element at the top of tge stack
            if (s1.pop() != s2.pop()):
                #increment mismatches
                mismatches += 1

        #return True if mismatches is equal to 0, else return False
            return(mismatches == 0)

    



    
    
    





def testmajorassignment1():
    exp = input("Please enter an expression:")
    

    if (majorassignment.majorassignment1(exp)):
       print("Your expression is a palindrome.")
    
    else:
        print("Your expression is not a palindrome")
        print(f"Mismatch detected at: ")

    
    

def testpracticeassignment1():
    
    
    exp = input("Please enter an expression:")
    while exp != '':

        if (practiceassignment.practiceassignment1(exp)):
            print("Your expression is a palindrome.")
    
        else:
            print("Your expression is not a palindrome")

        exp = input("Please enter an expression:")



def testIsPalindrome():
    exp = input("Please enter an expression:")

    if (palindrome.isPalindrome(exp)):
        print("Your expression is a palindrome.")
    
    else:
        print("Your expression is not a palindrome")

def testQueuePeek():
    print("Testing QueuePeek /method in Queue Class")

    s = queue()

    print("Queue size is:", s.size())               #0
    print("Queue contains:", s)                     #[]
    s.enqueue('S')
    print("Queue size is:", s.size())               #1
    print("Queue contains:", s)                     #[S]
    print("Front element in queue is:", s.peek())     # S

    #s.push('B')
    s.enqueue(1)                                     #2
    print("Queue size is:", s.size())               #[S]
    print("Queue contains:", s)                     #[B,S]
    print("Front element in queue is:", s.peek())     #[B]

    #s.push('O')
    s.enqueue((1,2))
    print("Queue size is:", s.size())               #3
    print("Queue contains:", s)                     #[O,B,S]
    print("Front element in stack is:", s.peek())     #O

    s.enqueue('S')
    s.enqueue([1,2,3])
    print("Queue size is:", s.size())               #4
    print("Queue contains:", s)                     #[J,O,B,S]
    print("Front element in queue is:", s.peek())     # J



def testDequeue():
    print("Testing Dequeue Method in Queue Class")

    s = queue()
    s.enqueue('S')
    s.enqueue('B')
    s.enqueue('O')
    s.enqueue('J')

    print("Queue size is:", s.size()) #4
    print("Queue contains:", s)       #[JOBS]
    print("Just dequeued:", s.dequeue())    #J

    print("Queue size is:", s.size()) #3
    print("Queue contains:", s)       #[OBS]
    print("Just dequeued:", s.dequeue())    #O

    print("Queue size is:", s.size()) #2
    print("Queue contains:", s)       #[BS]
    print("Just dequeued:", s.dequeue())    #B

    print("Queue size is:", s.size()) #1
    print("Queue contains:", s)       #[S]
    print("Just dequeued:", s.dequeue())    #S

    print("Just dequeued:", s.dequeue())



def testQueueisEmpty():
    print("Testing Is Empty Method in Queue Class")

    s = queue()
    s.enqueue('S')
    s.enqueue('B')
    s.enqueue('O')
    s.enqueue('J')

    print("Queue size is:", s.size()) #4
    print("Queue contains:", s)       #[JOBS]

    while(not s.isEmpty()):
        print("Just dequeued:", s.dequeue())

    print("Queue size is:", s.size()) #0
    print("Queue contains:", s)       # []

def testEnqueue():
    print("Testing Enqueue Method in Stack Class")

    s = queue()
    print("Queue size is:", s.size()) # 0
    print("Queue contains:", s)       # []

    s.enqueue('S')
    print("Queue size is:", s.size()) # 1
    print(" Queue contains:", s)       # [S]

    #s.push('B')
    s.enqueue(1)
    print("Queue size is:", s.size()) # 2
    print("Queue contains:", s)       # [B S]

    #s.push('O')
    s.enqueue((1,2))
    print("Queue size is:", s.size()) # 3
    print("Queue contains:", s)       # [O B S]

    #s.push('J')
    s.enqueue([1,2,3])
    print("Queue size is:", s.size()) # 4
    print("Queue contains:", s)       # [J O B S]


def testSelectionSort():

# create an empty stack
    s = stack()
# initialize first
    first = 1 

    
# push -7 onto the top of the stack
    s.push(-7)
# push 42 onto the top of the stack
    s.push(42)
# push 70 onto the top of the stack
    s.push(70)
# push 39 onto the top of the stack
    s.push(39)
# push 3 onto the top of the stack
    s.push(3)
# push 63 onto the top of the stack
    s.push(63)
# push 8 onto the top of the stack
    s.push(8)
# print unsorted stack
    print(s)
# call selection sort method
    selectionsort(s,first)
# print sorted stack
    #setDataAtPosition(s, first)


def testSerialSearch():
    
    # create an empty stack
    s = stack()
    # initialize first
    first = 0
    # initialize size
    size = 0
    # initialize target
    target = 0
    # push -7 onto the top of the stack                     
    s.push('-7')
    # push 42 onto the top of the stack                    
    s.push('-42')
    # push 70 onto the top of the stack                  
    s.push('70')
    # push 39 onto the top of the stack              
    s.push('-39')
    # push 3 onto the top of the stack                     
    s.push('3')
    # push 63 onto the top of the stack                    
    s.push('63')
    # push 8 onto the top of the stack
    s.push('8')
    # print the stack
    print("Stack contains:", s)    
    # call serial search method and display its return.
    print ('Target found at index ...', serialsearch(s, first, size, target))
    


def testPeek():
    print("Testing Peek /method in Stack Class")

    s = stack()

    print("Stack size is:", s.size())               #0
    print("Stack contains:", s)                     #[]
    s.push('S')
    print("Stack size is:", s.size())               #1
    print("Stack contains:", s)                     #[S]
    print("Top element in stack is:", s.peek())     # S

    #s.push('B')
    s.push(1)                                     #2
    print("Stack size is:", s.size())               #[S]
    print("Stack contains:", s)                     #[B,S]
    print("Top element in stack is:", s.peek())     #[B]

    #s.push('O')
    s.push((1,2))
    print("Stack size is:", s.size())               #3
    print("Stack contains:", s)                     #[O,B,S]
    print("Top element in stack is:", s.peek())     #O

    s.push('S')
    s.push([1,2,3])
    print("Stack size is:", s.size())               #4
    print("Stack contains:", s)                     #[J,O,B,S]
    print("Top element in stack is:", s.peek())     # J




def testIsEmpty():
    print("Testing Is Empty Method in Stack Class")

    s = stack()
    s.push('S')
    s.push('B')
    s.push('O')
    s.push('J')

    print("Stack size is:", s.size()) #4
    print("Stack contains:", s)       #[JOBS]

    while(not s.isEmpty()):
        print("Just popped:", s.pop())

    print("Stack size is:", s.size()) #0
    print("Stack contains:", s)       # []

    

def testPop():
    print("Testing Pop Method in Stack Class")

    s = stack()
    s.push('S')
    s.push('B')
    s.push('O')
    s.push('J')

    print("Stack size is:", s.size()) #4
    print("Stack contains:", s)       #[JOBS]
    print("Just popped:", s.pop())    #J

    print("Stack size is:", s.size()) #3
    print("Stack contains:", s)       #[OBS]
    print("Just popped:", s.pop())    #O

    print("Stack size is:", s.size()) #2
    print("Stack contains:", s)       #[BS]
    print("Just popped:", s.pop())    #B

    print("Stack size is:", s.size()) #1
    print("Stack contains:", s)       #[S]
    print("Just popped:", s.pop())    #S

    print("Just popped:", s.pop())



def testPush():
    print("Testing Push Method in Stack Class")

    s = stack()
    print("Stack size is:", s.size()) # 0
    print("Stack contains:", s)       # []

    s.push('S')
    print("Stack size is:", s.size()) # 1
    print("Stack contains:", s)       # [S]

    #s.push('B')
    s.push(1)
    print("Stack size is:", s.size()) # 2
    print("Stack contains:", s)       # [B S]

    #s.push('O')
    s.push((1,2))
    print("Stack size is:", s.size()) # 3
    print("Stack contains:", s)       # [O B S]

    #s.push('J')
    s.push([1,2,3])
    print("Stack size is:", s.size()) # 4
    print("Stack contains:", s)       # [J O B S]

def assignment():

    #Question 1 - creating a linked list using the variable head
    head = node('1',None)
    head = node('+', head)
    head = node('1',head)
    head = node ('=',head)
    head = node('2', head)

    #Question 2 - creating the second reference names operator 
    #to the linked list of nodes

    operator = head

    #Question 3 - changing the node operator 
    
    operator = operator.getLink()

    #Question 4 - creating a third reference named result to the linked list of nodes
    result = operator

    #Question 5 - changing the node result  for operator
    
    operator  = operator.getLink()

    #Question 6 - changing the linked list of nodes for operator
    operator = operator.getLink()

    #Question 7 - changing the linked list of nodes for operator
    operator = operator.getLink()

    
    #Question 8 - changing the linked list of nodes for operator
    
    operator = operator.getLink()

    #Question 9 - changing the linked list of nodes for operator
    operator = operator.getLink()

    #Question 10 - changing the linked list of nodes for operator
    
    operator = operator.getLink()
    


    #Question 11 - changing the linked list of nodes for operator
    operator = operator.getLink()
    
    #Question 12 displaying the following line to the terminal
    print("Head contains 3 Nodes", node.listSearch (head, [3]).getData())
    print("Operator contains 2 Nodes", node.listSearch (operator, [2]).getData())
    print("Result contains 1 Node", node.listSearch (result, [1]).getData())

    #Question 13 - displaying the following line to the terminal 
    print("Head contains character 1", node.listSearch (head, [1]).getData())
    print("Operator contains character 1", node.listSearch (operator, [1]).getData())
    print("Result doesn't contain character 1", node.listSearch (result, [1]).getData())

    #Question 14 - Creating lines of code that create the node copies 
    copy = node.listCopyWithTail(head)
    print("First node in copy[0] contains 3 nodes", copy[0].getData())
    print("First node in copy[1] contains 1 node", copy[1].getData())

    #Question 15 - Displaying code to the terminal 
    print("copy[0] contains 3 nodes", copy[0].getData())
    print("copy[1] contains 1 node", copy[1].getData())

    #Question 16 - displaying code to the terminal 
    print("Copy[0] contains the character", node.listSearch(head, [1]).getData())
    print("Copy[1] does not contain the character", node.listSearch(operator, [1]).getData())

def testreview():
    #Question 1
    print('Review')

    #Question 1 
    head = node('L',None)
    head = node('I', head)
    head = node('N', head)
    head = node('K', head)
    head = node('T', head)

    #Question 2 
    selection = head

    #Question 3 
    selection.setData('K')

    #Question 4
    selection.addNodeAfter('K')

    #Question 5
    selection = selection.getLink()

    #Question 6
    selection.addNodeAfter('E')

    #Question 7
    selection = selection.getLink()

    #Question 8
    selection.addNodeAfter('D')

    #Question 9
    selection = selection.getLink()

    #Question 10
    selection.addNodeAfter('L')

    #Question 11
    selection = selection.getLink()

    #Question 12
    selection.addNodeAfter('I')

    #Question 13
    print('How many nodes does head contain?')
    print('How many nodes does selection contain?')

    #Question 14
    tail = selection

    #Question 15
    tail = tail.getLink()

    #Question 16
    print('How many nodes does tail contain?')

    #Question 17
    selection.removeNodeAfter()

    #Question 18 
    print('How many nodes does head contain?')
    print('How many nodes does selection contain?')
    print('How many nodes does tail contain?')

    #Question 19
    tail = tail.getLink()

    #Question 20
    tail = node('I',None)

    #Question 21
    print('How many nodes does head contain?')
    print('How many nodes does selection contain?')
    print('How many nodes does tail contain?')

    #Question 22
    print('Head contains the letter K')
    print('Selection contains the letter I')



    #Question 23
    copy = node.listCopyWithTail(head)
    
    print('Copy head contains',node.listlength(copy[0],6).getData())
   
    print("Copy tail contains", node.listlength(copy[1], 1).getData())

    #Question 24





def testListCopyWithTail():
    # construct a node with data equal to S and link equal to None
    # and assign its reference to source
    source = node('S', None) # S
    
    # construct a node with data equla to B anf link equla to head
    # and assign its reference to source
    source = node('B', source) # B -> s

    # construct a node with data equal to O and link equal to head
    # and assign its reference to source
    source = node('O', source) # O -> B -> S

    # consctruct a node with data equal to J and link equal to head
    # and assign its reference to source
    source = node('J', source) # J -> O -> B -> S

    copy = node.listCopyWithTail(source) 
    
    # [J -> O -> B -> S,S] 

    print("Source contains", node.listPosition(source, 1).getData(),
          node.listPosition(source, 2).getData(),
          node.listPosition(source, 3).getData(),
          node.listPosition(source, 4).getData())
    
    print("Copy head contains", node.listPosition(copy[0], 1).getData(),
          node.listPosition(copy[0], 2).getData(),
          node.listPosition(copy[0], 3).getData(),
          node.listPosition(copy[0], 4).getData())
    print("Copy tail contains", node.listPosition(copy[1], 1).getData())
def testListCopy():
    print("Testimg List Copy")

    # construct a node with data equal to S and link equal to None
    # and assign its reference to source
    source = node('S', None) # S
    
    # construct a node with data equla to B anf link equla to head
    # and assign its reference to source
    source = node('B', source) # B -> s

    # construct a node with data equal to O and link equal to head
    # and assign its reference to source
    source = node('O', source) # O -> B -> S

    # consctruct a node with data equal to J and link equal to head
    # and assign its reference to source
    source = node('J', source) # J -> O -> B -> S

    copy = node.listCopy(source) # J -> O -> B -> S, but at a different memory location

    print("Source contains", node.listPosition(source, 1).getData(),
          node.listPosition(copy, 2).getData(),
          node.listPosition(copy, 3).getData(),
          node.listPosition(copy, 4).getData())
    
    print("Source contains", node.listPosition(source, 1).getData(),
          node.listPosition(copy, 2).getData(),
          node.listPosition(copy, 3).getData(),
          node.listPosition(copy, 4).getData())

def testListPosition():
    print('Testing List Position')
        # construct a node with data equal to S and link equal to None
    # and assign its reference to head
    head = node('S', None) # S
    
    # construct a node with data equla to B anf link equla to head
    # and assign its reference to head
    head = node('B', head) # B -> s

    # construct a node with data equal to O and link equal to head
    # and assign its reference to head
    head = node('O', head) # O -> B -> S

    # consctruct a node with data equal to J and link equal to head
    # and assign its reference to head
    head = node('J', head) # J -> O -> B -> S

    print("Head contains", node.listPosition(head,1).getData()) # J -> O -> B -> S
    print("Head contains", node.listPosition(head,2).getData()) # O -> B -> S
    print("Head contains", node.listPosition(head,3).getData()) # B -> S
    print("Head contains", node.listPosition(head,4).getData()) # S

    if (node.listPosition(head, 5) != None):
        print("Fifth node contains data:", node.listPosition(head,S).getData())
    else:
        print("There is node fifth node.")


def testListSearch():
    print("Testing List Search")

    # construct a node with data equal to S and link equal to None
    # and assign its reference to head
    head = node('S', None) # S
    
    # construct a node with data equla to B anf link equla to head
    # and assign its reference to head
    head = node('B', head) # B -> s

    # construct a node with data equal to O and link equal to head
    # and assign its reference to head
    head = node('O', head) # O -> B -> S

    # consctruct a node with data equal to J and link equal to head
    # and assign its reference to head
    head = node('J', head) # J -> O -> B -> S

    print("Head contains", node.listSearch(head,'J').getData())
    print("Head contains", node.listSearch(head,'O').getData())
    print("Head contains", node.listSearch(head,'B').getData())
    print("Head contains", node.listSearch(head,'S').getData())

    if(node.listSearch(head, 'Z')!= None):    
        print("Head contains", node.listSearch(head,'Z').getData())

    else:
        print("Head doesn't contain Z.")





def testListLength():
    print("Testing List Length")

     # construct a node with data equal to S and link equal to None
    # and assign its reference to head
    head = node('S', None) # S
    
    # construct a node with data equla to B anf link equla to head
    # and assign its reference to head
    head = node('B', head) # B -> s

    # construct a node with data equal to O and link equal to head
    # and assign its reference to head
    head = node('O', head) # O -> B -> S

    # consctruct a node with data equal to J and link equal to head
    # and assign its reference to head
    head = node('J', head) # J -> O -> B -> S

    print("Length of head is:", node.listlength(head))

def review():
    print('Review')

    #Question 1 
    head = node('X',None)
    head = node('X', head)
    head = node('X', head)
    head = node('X', head)

    #Question 2
    selection1 = head

    #Question 3 
    selection1.addNodeAfter('O')

    #Question 4 
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()

    #Question 5 
    selection1.addNodeAfter('O')

    #Question 6
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()

    #Question 7 
    selection1.addNodeAfter('O')

    # Question 8 
    tail = head

    #Question 9 
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()

    #Question 10
    selection2 = head

    #Question 11
    selection2 = selection2.getLink()
    selection2 = selection2.getLink()

    #Question 12
    head.setData('A')
    selection2.setData('A')
    selection1.setData('A')
    tail.setData('A')

    #Question 13
    head.removeNodeAfter()
    selection1.removeNodeAfter()
    selection1.removeNodeAfter()

    #Question 14

def testRemoveNodeAfter():
    print("Testing Remove Node After")

     # construct a node with data equal to S and link equal to None
    # and assign its reference to head
    head = node('S', None) # S
    
    # construct a node with data equla to B anf link equla to head
    # and assign its reference to head
    head = node('B', head) # B -> s

    # construct a node with data equal to O and link equal to head
    # and assign its reference to head
    head = node('O', head) # O -> B -> S

    # consctruct a node with data equal to J and link equal to head
    # and assign its reference to head
    head = node('J', head) # J -> O -> B -> S

    print("The head node contains data:", head.getData())

    # remove the node after the node head refers to (node that has data equal to S)
    head.removeNodeAfter()

    head = head.getLink()

    print("The head node contains data:", head.getData())

    # remove the node after the head refers to (node that contains data value equal to S)
    head.removeNodeAfter() #S

    print("The head node contains data:", head.getData())

def testAddNodeAfter():
    print("Testing Add Node After")

    # construct a node with data equal to R and link equal to None
    # and assign its reference to head
    head = node('J', None) # J
    
    print("The head node contains data:", head.getData())

    #declare a new node named selection and make it refer 
    #to the same node as head
    selection = head

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    #add a node with dataequal to 0 after the node selection 
    #refers to
    selection.addNodeAfter('O') #J -> O
   
   #get selection's link and assign its reference back to 
   #selection
    selection = selection.getLink() # O

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    #add a node with dataequal to B after the node selection 
    #refers to
    selection.addNodeAfter('B') #J -> O -> B
   
   #get selection's link and assign its reference back to 
   #selection
    selection = selection.getLink() # O

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

     
     
     #add a node with dataequal to S after the node selection 
    #refers to
    selection.addNodeAfter('S') #B -> S
   
   #get selection's link and assign its reference back to 
   #selection
    selection = selection.getLink() # S

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    #declare a new node named tail andd make it refer to the same 
    #node as head
    tail = head

    # get tail's limk and assign its reference to tail 
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()

    # add a new node with data equal to Z after the node tail
    #refers to 
    tail.addNodeAfter('Z')

    #gets tail's link and assign its reference to tail
    tail = tail.getLink()

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())
    print("The tail node contains data:", tail.getData())





def testGetterAndSetters():
    print("Testing Getters And Setters")



    # construct a node with data equal to R and link equal to None
    # and assign its reference to head
    head = node('R', None) # R

    print("The head node contains data:", head.getData())

    head.setData('S') #S
    print("The head node contains data:", head.getData())

    head = node('B', head) # B -> S

    print("The head node contains data:", head.getData())

    head = node('O', head) # O-> B -> S

    print("The head node contains data:", head.getData())

    head = node('J', head) # J-> O-> B -> S

    print("The head node contains data:", head.getData())

    #get head's link and assign its reference back to head
    head = head.getLink()# O-> B -> S
    print("The head node contains data:", head.getData())

     #get head's link and assign its reference back to head
    head = head.getLink() # B -> S
    print("The head node contains data:", head.getData())

     #get head's link and assign its reference back to head
    head = head.getLink() # S
    print("The head node contains data:", head.getData())

     #get head's link and assign its reference back to head
    """head = head.getLink()# O-> B -> S
    print("The head node contains data:", head.getData())"""

    print("The head node contains link:", head.getLink())

    #set head's link to a new code
    head.setLink(node('O', None)) #S -> O

def testInit():
    print("Testing Node Init")

    # construct a node with data equal to S and link equal to None
    # and assign its reference to head
    head = node('S', None) # S
    
    # construct a node with data equla to B anf link equla to head
    # and assign its reference to head
    head = node('B', head) # B -> s

    # construct a node with data equal to O and link equal to head
    # and assign its reference to head
    head = node('O', head) # O -> B -> S

    # consctruct a node with data equal to J and link equal to head
    # and assign its reference to head
    head = node('J', head) # J -> O -> B -> S

    head = node(1, head) #1 -> J -> O -> B -> S

    head =node(1.5,head) #1.5 -> 1 -> J -> O -> B -> S
    head = node([1,2], head) # [1,2] -> 1.5 -> 1 -> J -> O -> B -> S
    head = node (('A', 'B'), head) #('A', 'B') -> [1,2] -> 1.5 -> 1 -> J -> O -> B -> S
    print()

if __name__ == "__main__":
    main()