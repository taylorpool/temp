# Creates a string named formatter that contains four string format operators
# of repr()
formatter = "%r %r %r %r"

#Outputs 1 2 3 4
print formatter % (1, 2, 3, 4)

#Outputs one two three four
print formatter % ("one", "two", "three", "four")

#Outputs True False False True
print formatter % (True, False, False, True)

#Outputs %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r
print formatter % (formatter, formatter, formatter, formatter)

#Outputs all of the following string but on one line
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
