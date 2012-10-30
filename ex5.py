my_name = 'Foo B. Baz'
my_age = 42
my_height = 64
my_weight = 192
my_eyes = 'Purple'
my_teeth = 'Coffee-stained'
my_hair = 'Red'

print "Let's talk about %s." % my_name
print "He is %d inches tall." % my_height
print "He is %d pound heavy." % my_weight
print "Actually that is very heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the time of day." % my_teeth

# tricky
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight,
        my_age + my_height + my_weight)
