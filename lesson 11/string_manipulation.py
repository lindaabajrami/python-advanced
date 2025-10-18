with open("example.txt", "r") as file:
    for line in file:
        cleaned_line = line.strip()
        print(cleaned_line)


with open("example.txt", "r") as file:
    for line in file:
        words = line.strip().split()
        print(words)

name = "drin"
age  = "17"

with open("output.txt", "w") as file:
    file.write("name: " +name + "\n")
    file.write("age: " +str(age) + "\n")

with open("output.txt", "w") as file:
    file.write(f"name: {name}\n")
    file.write(f"age: {age}\n")

with open("output.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        cleaned_line = line.strip()
        modified_line = cleaned_line.replace("line 1 ", "line x")
        outfile.write(modified_line + "\n")


