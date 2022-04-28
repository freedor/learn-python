weight = 41.5
ground_cost = ""
drone_cost = ""
if weight <= 2:
  ground_cost = (20 + weight * 1.5)
  drone_cost = (weight * 4.5)
elif weight <= 6:
  ground_cost = (20 + weight * 3)
  drone_cost = (weight * 9)
elif weight <= 10:
  ground_cost = (20 + weight * 4)
  drone_cost = (weight * 12)
elif weight > 10:
  ground_cost = (20 + weight *4.75)
  drone_cost = (weight * 14.25)
print ("Ground Shipping cost is: " + str(ground_cost))
premium_ground_shipping = 125
print ("Premium Ground Shipping cost is: " + str(premium_ground_shipping))
print ("Drone Shipping cost is: " + str(drone_cost))

