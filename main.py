from loops import *
from recursion import*

print("Factorial of 6 using a loop is:", loops.factorial(6))
print("Factorial of 5 using a loop is:", loops.factorial(5))
print("Factorial of 1 using a loop is:", loops.factorial(1))

print("Factorial of 6 using a recursion is:", recursion.factorial(6))
print("Factorial of 5 using a recursion is:", recursion.factorial(5))
print("Factorial of 1 using a recursion is:", recursion.factorial(1))

print("2 to the 5th power using a loop is:", loops.power(2,5))
print("2 to the 4th power using a loop is:", loops.power(2,4))
print("2 to the 0 power using a loop is:", loops.power(2,0))

print("2 to the 5th power using a recursion is:", recursion.power(2,5))
print("2 to the 4th power using a recursion is:", recursion.power(2,4))
print("2 to the 0 power using a recursion is:", recursion.power(2,0))

nums = [5,12,3,4]
print("Mininum number using a loop is", loops.computeMin(nums))
print("Mininum number using a recursion is", recursion.computeMin(nums,0, nums[0]))

str= "CAT"
loops.reverse(str)
recursion.reverse(str, len(str))





a = input("Enter 7 numbers separated by a space:")
a = input("Enter the index:")
a = input("Enter the size of the list that will be search:")
#print("Target found at index ... ", loops.search(a, first, size, target, i, found))
#print("Target found at index ... ", recursion.search(a, first, size, target, i, found))

#Question 7
def testRecursion():
    recursion.dis(-10, -8, -6, -4, -2, 0 , 2, 4, 6, 8 ,10) 