a = 10
b = 20
result = a + b
with open("output.txt", "w") as f:
    f.write(f"Addition: {result}\n")
print("Addition:", result)
