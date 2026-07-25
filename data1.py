# Writing data to a text file
with open("data.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python file handling snippet.\n")

# Reading data back from the file
with open("data.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)
