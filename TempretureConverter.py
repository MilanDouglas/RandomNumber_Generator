#Temperature Converter: Write a program that converts temperatures between Fahrenheit and Celsius. Allow the user to input the temperature and the scale (F or C) and convert it to the other scale.
def fahrenheit_to_celcius(fahrenheit):
  return (fahrenheit  - 32) * 5/9

def celcius_to_fahrenheit(Celcius):
  return (Celcius * 9/5) + 32
#Get user input
temp = float(input("Enter Temperature: "))
scale = input("Enter scale (C/F): ")

try:
  if scale.upper() == "F":
    celcius =  fahrenheit_to_celcius(temp)
    print(f"Temperature: {temp:.2F} F = {celcius:.2f} C")
  elif scale.upper() == "C": 
    fahrenheit = celcius_to_fahrenheit(temp)
    print(f"Temperature: {temp:.2F} C = {fahrenheit:.2f} F")
  else:
    raise ValueError("Invalid scale. Please enter 'C' or 'F'.")
except ValueError as e:
    print(f"Error: {e}")