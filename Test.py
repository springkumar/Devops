# Read output from DEV job
with open("output.txt", "r") as f:
    result = int(f.read())

# Simple test
if result == 30:
    print("TEST PASSED: Addition is correct")
else:
    print("TEST FAILED")
    exit(1)
