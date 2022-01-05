weight = int(input('Put the weight of your package in lb: \n'))

#Ground Shipping
if weight <= 2:
  cost = (weight * 1.50) + 20.00
  print('The cost is $' + str(cost))
elif weight > 2 and weight <= 6:
  cost = (weight * 3.00) + 20.00
  print('The cost is $' + str(cost))
elif weight > 6 and weight <= 10:
  cost = (weight * 4.00) + 20.00
  print('The cost is $' + str(cost))
else:
  cost = (weight * 4.75) + 20.00
  print('The cost is $' + str(cost))

premium = 125.00
print ('Price of ground shipping premium: $', premium)

#Drone Shipping 
if weight <= 2:
  cost = (weight * 4.50)
  print('The cost is $' + str(cost))
elif weight > 2 and weight <= 6:
  cost = (weight * 9.00)
  print('The cost is $' + str(cost))
elif weight > 6 and weight <= 10:
  cost = (weight * 12.00)
  print('The cost is $' + str(cost))
else:
  cost = (weight * 14.25)
  print('The cost is $' + str(cost))