# Reverse list and join list with space:
l = ["be", "to", "not", "or", "be", "to"]
result = " ".join(str(item) for item in l[::-1])
print(result)