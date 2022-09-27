


str = 'The quick Brow Fox'

upper = 0
lower = 0
for i in str:
    if i.isupper():
        upper  = upper+1
    else:
        lower = lower+1
    
print("No.of upper case character:",upper)
print("No.of lower case character:",lower)
