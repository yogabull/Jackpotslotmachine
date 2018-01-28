# code to open and read from a .txt file

file=open("fruits.txt","r")
content = file.readlines()
#the above code will print:"['pear\n', 'apple\n', 'orange\n', 'mandarin\n', 'watermelon\n', 'pomegranate\n']"
print (content)

# use this to strip out the paragraph characters: \n
content = [i.strip ("\n") for i in content]

# that wil print: ['pear', 'apple', 'orange', 'mandarin', 'watermelon', 'pomegranate']

# .readlines leaves the 'pointer' at then end of the content.
# move th pointer back to the beginning with:
file.seek(0)

# need to use close method to retain file info
file.close()

# to append a file use an 'a' when you open a file:
file=open("example.txt","a")
