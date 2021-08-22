# 1.
name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", 'r')
name = in_file.read()
in_file.close()
print(f"Your name is {name}")


# 3.
in_file = open("numbers.txt", 'r')
first_second_total = int(in_file.readline()) + int(in_file.readline())
in_file.close()
print(first_second_total)

# 4.
FILE_NAME = "numbers.txt"
in_file = open(FILE_NAME, 'r')
total = 0
for line in in_file:
    total += int(line)
in_file.close()
print(total)
