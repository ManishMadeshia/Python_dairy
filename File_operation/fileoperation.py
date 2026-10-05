#read a whole file

with open('example.txt','r') as file:
    context = file.read()
    print(context)

#Read a file line by line

with open('example.txt','r') as file:
    for line in file:
        print(line.strip()) #strip() remove the newline character


#writing a file with overwriting clause

with open("example.txt",'w') as file:
    file.write("Hello World!\n")
    file.write("this is a new line!")


#writing a file with overwriting clause
 
with open("example.txt",'a') as file:
    file.write("Append operation taking place\n")


##writing a list of lines to a file

lines = ['First line\n','Second line\n','Third line\n']

with open('example.txt','a') as file:
    file.writelines(lines)


#binary files

#writing to a binary files

data = b'\x00\x01\x02\x03\x04'

with open("example.bin",'wb') as file:
    file.write(data)


#reading from a binary files

with open('example.bin','rb') as file:
    context = file.read()
    print(context)

#copying a text file from source to destination

with open('example.txt','r') as source_file:
    context = source_file.read()
    print(context)

with open("destination.txt",'w') as destination_file:
    destination_file.write(context)
    print(destination_file)


#read a text file and count the no of line , word and character



#writing and reading a file

with open("example.txt",'w+') as file:
    file.write("Hello world\n")
    file.write("Hello my name is Manish\n")

    #move the file cursor to the beginning
    file.seek(0)

    ##read the content of file
    content = file.read()
    print(content)