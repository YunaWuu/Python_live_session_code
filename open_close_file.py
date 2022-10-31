# using with we don't have to close the file
words = []
with open('words.txt', 'r') as in_file:
    for line in in_file:
        words.append(line.strip())
        # strip throws away white space such as line breaks
        # end specifies what the print line ends with (default is a new line)
        print(line.strip(), end=' ')
print()
print(words)
   
with open('out.txt', 'w') as out_file:
    for word in words:
        out_file.write(word + ' ')

   
########################################
# or we can open files and close them manually
# maybe better for dealing with multiple files at the same time
       
in_file2 = open('words.txt')
out_file2 = open('out.txt', 'w')  # w for writing
for line in in_file2:
    print(line.strip(), end=' ')
    out_file2.write(line.strip() + ' ')
   
in_file2.close()
out_file2.close()