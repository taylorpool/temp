#Lists are compound data types that are used to group together other values
#Lists can contain items of different types but usually they contain items of
#just one type.

squares = [1, 4, 9, 16, 25]
print(squares)

#Lists can be indexed just like strings. This is because both lists and strings
#are sequence types

print(squares[1])

#We can slice our lists as well. When we slice, we create a new list containing
#the requested elements
print(squares[1:])

cubes = [1, 8, 27, 64, 125]

#We can concatenate lists together.

print(squares + cubes) #Outputs [1, 4, 9, 16, 25, 1, 8, 27, 64, 125]

#Lists are mutable. This means that we can change the contents of lists by
#indexing in and performing surgery

cubes = [1, 8, 30, 64, 125]
print(cubes)
cubes[2] = 27 #Change the third value of cubes to 27
print(cubes)

#Lists and Strings have methods. We can use the .append method to append
#things on the backs of lists.

cubes.append(36*6)
cubes.append(7**3) #We can only append one value at a time

print(cubes)

#We can change the contents of lists by assigning to slices as well.
letters = ['a', 'b', 'c', 'd']

letters[0:3] = ['A', 'B', 'C'] #Changes letters to ['A', 'B', 'C', 'd']

print(letters) # prints letters

letters[2:4] = [] #removes the third and fourth values of letters

print(letters) #prints out the result

letters[:] = [] #clears the lists

print(letters)

#We can find the length of a list using the builtin function len().

print(len(letters)) #Prings the length of letters which is zero

#We can nest lists inside of lists.

a = [1, 2, 3, 4,]
b = [1, 2, 3]
x = [a, b] #Nests a and b inside of x.

print(x)
print(x[0]) #Prints a

#We can use x[number][number] to index into multidimentional lists.
print(x[0][3]) #Prints the fourth element of a which is 4


#Fibonacci Series starts with two numbers 0 and 1.

a, b = 0, 1 #multiple assignment of variables is possible in the same line.

while(a < 10): #any nonzero integer value is true. zero is false
    print(a)
    a, b = b, a+b   #Sets a equal to b. And then adds b and that new a value
                    #to get the new b value.

                #Python groups statements together by indentation.

#We can insert variables into print functions with commas.

print("The value of a is", a) #The print function automatically inserts a
                                #space in there before a.
#When we print, we can use the keyword end to avoid the newline after
#The output.

a, b = 0, 1

while (a <= 13):
    print(a, end = ',') #The keyword end makes each one have a comma between
                        #the next.
    a, b = b, a + b
print('\n')
