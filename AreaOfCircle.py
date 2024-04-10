#AreaOfCircle.py
#Calculate Area of a Circle: Write a Python program that takes the radius of a circle as input and calculates its area. Use the formula area = π * radius^2.
#This code uses math.pi for a more accurate value of Pi, ensures that the radius is a positive number, and rounds the result to 2 decimal places for better readability.Use math.pi for Pi: Python's math module provides a more accurate value for Pi. 

#Import the pi constant and use it instead of an approximate value like 3.14.
import math

#Error Handling for Input
try:
  radius = float(input("Enter radius: "))
  if radius <= 0:
    raise ValueError("Radius must be a positive number.")
  area = math.pi * radius**2
  print(f"Area of cirlce is {area:.2f}")
except ValueError as e:
  print(f"Error: {e}")
  