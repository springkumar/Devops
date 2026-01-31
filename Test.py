with open("output.txt", "r") as f:
    content = f.read().strip()

result = int(content)

assert result == 30
print("Test passed successfully")
