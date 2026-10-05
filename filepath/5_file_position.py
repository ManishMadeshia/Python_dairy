#Q1. Open data.txt and print the initial position using tell().
file = open("data.txt",'r')
print(file.tell())

#Q2. Read 5 characters and print the position using tell().

file = open("data.txt",'r')
print(file.read(5))
print(file.tell())

#Q3. Read the entire file, then use seek(0) and read it again.

file = open('data.txt','r')
print(file.read())
file.seek(0)
print(file.read())

#Q4. Open a file, use seek(5), then read the remaining content.

file = open('data.txt','r')
file.seek(5)
print(file.read())

#Q5. Explain tell() in your own words.
#using tell() it tell us about item current postiiton in file

#Q6. Explain seek() in your own words.
# using seek we can modify the postiton on cursor eg we can move to 0 postion or 5 postiton

#Q7. What does seek(0) do?
#move cursor point to index 0 position

#Q8. What happens to the file pointer after read() reads the entire file?
# if we use read function it move the cursor to file end  eg if file contain 20 character 

#Q9. Use tell() after reading 10 characters.
file = open('data.txt','r')
file.read(10)
print(file.tell())


#10 Final: Read the first 5 characters, move back to the beginning using seek(0), then read the entire file.

file = open("data.txt",'r')

print(file.read(5))
file.seek(0)

print(file.read())
