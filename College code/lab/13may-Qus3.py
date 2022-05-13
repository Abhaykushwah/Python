#W.A.P to allow user to write something in a text file. Then user will input a word,
# you have to tell user to line number in which that word that word exists or not exists or not if not found.

file = open("abc3.txt",'w+')
#data = readlines(file)
user_in = input("Enter the data you want to write in the file \n\n")
wdata = file.write(user_in)
file.close()
file = open("abc3.txt","r")
find_word = input("Enter the word you want to search : ")
count = 0
for i in file:
    count += 1
    if (find_word in i):
        print("Word Found at line ",count)
    else:
        print("Word not found")

