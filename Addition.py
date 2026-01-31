a = 10
b = 20
result = a + b

print("Addition:", result)

# Save output for test program
with open("output.txt", "w") as f:
    f.write(str(result))
