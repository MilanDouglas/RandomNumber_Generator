#Join List with Custom Separator: Write a program that takes a list of strings and joins them into a single string using a custom separator. Allow the user to input the separator. For example, if the input list is ["apple", "orange", "banana"] and the separator is ";", the output should be "apple;orange;banana"
fruits = ["apple", "orange", "banana"]
separator = input("Enter the separator: ")
result = separator.join(fruits)
print(result)