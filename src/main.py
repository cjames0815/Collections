from node.node import *

def main():
    testInit()

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