# Writing data to a file
with open('data.txt', 'w') as file:
    file.write("Name: Alice\n")
    file.write("Age: 30\n")
    file.write("Occupation: Engineer\n")

# Reading data from the file
print("File Content:")
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)