input = [0, 1, 2 ,3]
print(input)

output = [ ]

interleaved = [1, 2, 3, 0]

for index in interleaved:
    output.append(input[index])
print(output)
