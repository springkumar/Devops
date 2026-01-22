with open("output.txt", "r") as f:
    content = f.read().strip()   # "Addition: 30"

# Extract number
result = int(content.split(":")[1].strip())

# Test condition
assert result == 30
print("Test passed successfully")
