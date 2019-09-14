name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#Metric System
height_cm = height*2.54
weight_kg = weight*.453592

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That's %d cm tall." % height_cm
print "He's %d pounds heavy." % weight
print "That's %d kilograms heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
