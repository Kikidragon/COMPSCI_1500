''' Women: Calories = ((Age x 0.074) - (Weight x 0.05741) + (Heart Rate x 0.4472) - 20.4022) x Time / 4.184 '''
''' Men: Calories = ((Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) - 55.0969) x Time / 4.184 '''
import math
''' Type your code here. '''
age = int(input())
weight = int(input())
heart_rate = int(input())
time = int(input())
calories_w = ((age * 0.074) - (weight * 0.05741) + (heart_rate * 0.4472) - 20.4022) * time / 4.184
calories_m = ((age * 0.2017) + (weight * 0.09036) + (heart_rate * 0.6309) - 55.0969) * time / 4.184

print('Women: {:.2f} calories'.format(calories_w))
print('Men: {:.2f} calories'.format(calories_m))