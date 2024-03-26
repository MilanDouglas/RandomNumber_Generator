Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
i = 0
New_animals = []
while i < len(Animals):
    if len(Animals[i]) == 7:
        New_animals.append(Animals[i])
    i = i + 1
print(New_animals)   