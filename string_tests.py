print("""\
Hello
    World
        How
            Are
                You\
""")

#If I put a backslash \ after the first quotation marks and after the last
#word it makes all of fit nicely with no extra lines.

#Concatenation

a = 'Apple'
b = 'banana'
c = 'chocolate'

print (a + b + 3*c) #This outputs applebananachocolatechocolatechocolate
print('Py' 'thon') #This prints the concatenated word Python
print('Vertical '
        'becomes '
        'horizontal') #Multiple lines put into one lines

#This doesn't work though with variables. Use + instead
#Strings are indexed with the first character having
#index of zero

word = "auvsi"

#Concatenation may be done like this
print(word[0]+word[4]+" " + word[4] + word[3]
        + " " + word[1] + word[3])

#We can start from the other side of the word starting at an index of -1
print(word[-1] == word[4]) #Returns the value of true because it's using the same Strings

#Indexing gets one value, but slicing gets a substring

print(word[0:4]) #This goes from the 0th value until the 4th value. Not the 5th value.

print(word[0:2] + word[2:5]) #This allows us to keep track of middle values. auvsi

print(word[:3]) #goes from beginning until the third letter auv

print(word[2:]) # goes from the third element to the end vsi

print(word[-2:]) #goes from the second last to the end. si

#Python strings cannot be changed. They are immutable so we can't assign an indexed position in the string.
#Instead we create a brand new string.
#Dont' do word[0] = 's'. Doesn't work
print('s' + word[1:]) #prints suvsi

#We can find the length of a string using len(str)
print(len(word[0:5]))
