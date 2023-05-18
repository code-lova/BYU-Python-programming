"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""


print("Please Enter Your Age",end=" ")
age = float(input(""))
max_rate = 220 - age
slow_rate = max_rate * 0.65
fast_rate = max_rate * 0.85

print("When you exercise to strengthen your heart, you should",end=" ")
print("keep your heart rate between {:.0f} and {:.0f} beats per minutes" .format(slow_rate, fast_rate))