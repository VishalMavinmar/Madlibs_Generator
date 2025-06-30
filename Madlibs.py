
with open("story.txt","r") as f:
    story = f.read()

word =set()
startofwords =-1
targetstart ="<"
targetend =">"


for i,char in enumerate(story):

    if char == targetstart :
        startofwords =i

    if char==targetend and startofwords!=-1:
        words =story[startofwords:i+1]
        word.add(words)
        startofwords =-1

print(word)


answers ={}

for i in word:
    answer =input("enter a word "+ i +": ")
    answers[i] =answer

for i in word :
    story=story.replace(i,answers[i])
print(story)
