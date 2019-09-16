#Control flow uses if, for, while, elseif statements

#Input can happen with the function input()
x = int(input("Please enter an integer: "))

if x < 0:
    x == 0
    print('Negative changed to zero')
elif x == 0:    #elif stands for else if.
    print('Zero')
elif x > 1:
    print('X is super large!')
else:       #The else part is optional but is a good coding practice.
    print("x is", x)

#if-elif is a substitue for switch or case in other languages like Java.

#For Statements############

#for in python interates over values in a string or list, not just an
#arithmetic progression of numbers like 1:2:3.

words = ['cat', 'dog', 'bird']

for w in words:
    print(w, len(w)) #Prints each word and its corresponding length.

#Input of a string is made possible by str(input)
x = str(input("Please enter a word: "))

#iterates over a string value.
for y in x:
    print(y)

#We can make a slice copy of the sequence using the slice operator.

for word in words[:]: #If we don't make a copy, then a new object will be created
                        #and the for loop will start over, which will
                        #occur an infinite amount of times resulting in
                        #stack overflow.
    if len(word) == 3:
        words.insert(1, word) #inserts this word at the element index of 1.
        print(words)

#range can do arithmetic progression. Never includes the given end point.
print(range(10))
print(range(1,10))

sum = 0
for i in range(10):
    sum = sum + i# The idea is to sum up numbers from 0 to 10
    print(sum)

#Step size is the third argument.
sum = 0
for i in range(0,101,2): #This is a range that goes from 0 to 100 up by two.
    sum = i + sum
    print(sum, end = ', ')

print('\n')

#To iterate over the indecies of a sequence, use len() and range() together.

ode = ['I', 'love', 'programming', 'so', 'much']
for i in range(len(ode)):
    print(i, ode[i])


#Range is not a list. It is just an object that returns the successive items
#of the sequence as we iterate over it. It doesn't actually make the list though

#for statements are iterators.
#An iterator is any object that can be targetted by functions and constructs
#until their supply of items is exhausted.
