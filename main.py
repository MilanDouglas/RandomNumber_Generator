input_list = [1,"hello", 1.618, "world"]
result = ''.join(map(lambda x: str(x).replace('.', ''),input_list))
print(result)