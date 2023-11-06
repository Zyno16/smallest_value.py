  
#thi is to displlay the smallest value in the arrays
# you can use == instead is but is is more powerfull
smallest = None
print ("before")
for value in [5,12,14,3,1,17,7,1,15,87]:
    if smallest is None:
        smallest = value
    elif value < smallest:
         smallest = value
    print (smallest ,value)
print ("the smallest valus is ",smallest )

