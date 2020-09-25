from sys import argv
#unpacking module argv
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read()) 
#call function on txt named read
print("Type the file name again:")
file_again = input ('>')

txt_again = open(file_again)

print('This is the end')
print(txt_again.read)


