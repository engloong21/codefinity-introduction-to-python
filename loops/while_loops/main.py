start_number = 5
countdown_values = []

current = start_number
while current >=1:
    # add this number to the list
    countdown_values.append (current)
    # move one step closer to zero
    current -= 1

print ("Discount countdown complete!")
print (countdown_values)