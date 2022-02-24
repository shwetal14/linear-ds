#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number.


def find(array,len,summ):
       print("Pairs whose sum is : ",summ)
       for i in range(len):
           for j in range(i,len):
                if (array[i]+array[j])==summ:
                     print(array[i],array[j])


len=int(input("Enter length of array: "))

array=[]

print("Enter elements")
for i in range(len):
     array.append(int(input()))

summ=int(input("Enter sum "))

print("Array= ",array)

find(array,len,summ)



# Q2. Write a program to reverse an array in place? In place means you cannot create a new array.You have to update
#      the original array.




def reverseList(arr, size):
    i = 0
    j = size-1
    while i<size/2:
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        j = j - 1
def printListElements(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()
    
arr = [45, 12, 67, 63, 9, 23, 74]
size = len(arr)


print("Original Array:")
printListElements(arr, size)

reverseList(arr, size)

print("Reversed Array:")
printListElements(arr, size)



 # Q3. Write a program to check if two strings are a rotation of each other.
    
    


def checkRotation(s1, s2): 
    temp = '' 
  
    
    if len(s1) != len(s2): 
        return False
  
    temp = s1 + s1 
  
    
    if s2 in temp: 
        return True 
    else: 
        return False
  
string1 = "HELLO"
string2 = "LOHEL"

if checkRotation(string1, string2): 
    print("Given Strings are rotations of each other.")
else: 
    print("Given Strings are not rotations of each other.")


# Q4. Write a program to print the first non-repeated character from a string.



def first_non_repeating_character(str1):
    char_order = []
    ctr = {}
    for c in str1:
    if c in ctr:
        ctr[c] += 1
    else:
        ctr[c] = 1 
    char_order.append(c)
for c in char_order:
    if ctr[c] == 1:
        return c
    return None

print(first_non_repeating_character('abcdef'))
print(first_non_repeating_character('abcabcdef'))
print(first_non_repeating_character('aabbcc'))



# Q5.  Read about the Tower of Hanoi algorithm. Write a program to implement it.


def tower_of_hanoi(numbers, start, aux, end):  
    if(numbers == 1):  
        print('Move disk 1 from rod {} to rod {}'.format(start, end))  
        return
    tower_of_hanoi(numbers - 1, start, end, aux)  
    print('Move disk {} from rod {} to rod {}'.format(numbers, start, end))  
    tower_of_hanoi(numbers - 1, aux, start, end)  
   
numbers = 3
tower_of_hanoi(numbers, 'A', 'B', 'C')



# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.


def push(x):
    global stack 
    global top
    top+=1
    stack[top]=x
def pop():
        global stack
        global top
        x=stack[top]
        top-=1
        return x
def is_operator(x):
    if x=='+' or x=='-' or x=='*' or x=='/':
        return True
    else:
        return False
def convert():
        global stack
        global top
        l= len(exp)
        for i in range(0,l):
            if is_operator(exp[i])==True:
                op1=stack[top]
                pop()
                op2=stack[top]
                pop()
                tmp=exp[i]+op2+op1
                push(tmp)
            else:
                push(exp[i])
    print("The prefix expression is: ", stack[top])         
# main function     
stack=[]
top=-1
exp=input("Enter the postfix expression: ")
for i in range(50):
     stack.append(0)
convert()



# Q7. Write a program to convert prefix expression to infix expression.


import java.util.Stack;
public class PreFixToInFix{
    public String convert(String expression)
    {

        Stack<String> stack = new Stack<>();
        for (int i = expression.length()-1; i >=0 ; i--) 
        {
            char c = expression.charAt(i);

            if(isOperator(c)){
                String s1 = stack.pop();
                String s2 = stack.pop();
                String temp = "("+s1+c+s2+")";
                stack.push(temp);
            }
            else
            {
                stack.push(c+"");
            }
        }

        String result=stack.pop();

        return result;
    }

    boolean isOperator(char x) 
    {
        switch (x)
        {
            case '+':
            case '-':
            case '/':
            case '*':
                return true;
        }
        return false;
    }

    public static void main(String[] args) 
    {
        String exp = "*-A/BC-/AKL";
        System.out.println("Prefix Expression: " + exp);
        System.out.println("Infix Expression: " + new PreFixToInFix().convert(exp));
    }
}



# Q8.   Write a program to check if all the brackets are closed in a given code snippet.


class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))



# Q9. Write a program to reverse a stack.



class  Stack_to_reverse  :
    def __init__(  self  ):
        self.items  =  list()
        self.size=-1
    def  isEmpty(  self  ):
        if(self.size==-1):
            return True
        else:
            return False
 
    def  pop(  self  ):
        if  self.isEmpty():
            print("Stack is empty")
        else:
            return self.items.pop()
            self.size-=1
 
    def  push(  self,  item  ):
        self.items.append(item)
        self.size+=1
 
    def reverse(self,string):
        n = len(string)
 
        for i in range(0,n):
            S.push(string[i])
 
        string=""

        for i in range(0,n):
            string+=S.pop()
        return string
 
S=Stack_to_reverse()
seq=input("Enter a string to be reversed")
sequence = S.reverse(seq)
print("Reversed string is " + sequence)



# Q10. Write a program to find the smallest number using a stack.



class MinStack(object):
   min=float('inf')
   def __init__(self):
      self.min=float('inf')
      self.stack = []
   def push(self, x):
      if x<=self.min:
         self.stack.append(self.min)
         self.min = x
      self.stack.append(x)
   def pop(self):
      t = self.stack[-1]
      self.stack.pop()
      if self.min == t:
         self.min = self.stack[-1]
         self.stack.pop()
   def top(self):
      return self.stack[-1]
   def getMin(self):
      return self.min
m = MinStack()
m.push(-2)
m.push(0)
m.push(-3)
print(m.getMin())
m.pop()
print(m.top())
print(m.getMin())


