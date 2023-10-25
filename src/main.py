from node.node import *

def main():
    testInit()

    #testInit
    #testGetterAndSetters()
    testAddNodeAfter()

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