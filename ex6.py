# This uses a string format operator d that is given the value of 10
x = "There are %d types of people." % 10

# This creates a string called binary containing the word "binary"
binary = "binary"

# This creates a string called do_not that contains the word "don't"
do_not = "don't"

#This creates a string with two string formatting operators. The first is a string
# The second is also a string.
y = "Those who know %s and those who %s." % (binary, do_not)

#Finally the values of x and y are outputted
print x
print y

# X and Y are printed again with introductions. %r is used for debugging
print "I said: %r." % x
print "I also said: '%s'" % y

# Now we create a binary variable named hilarious that is given the value False
hilarious = False

#Now we create a string that contains a string format operator that transforms
# the binary operator into a string
joke_evaluation = "Isn't that joke so funny?! %r"

# Now we print the string
print joke_evaluation % hilarious

#Finally we practice string concatenation. We combine two strings using the plus operator
w = "This is the left side of..."
e = "a string with a right side."

#Then we print the result
print w + e
