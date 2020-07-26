# put your code here.
import string


file = open("test.txt")
word_dict = {}
new_word = ""

for line in file:
    words = line.strip("\n").lower().split(" ")

    for items in words:
        if "http" in items:
            new_word = items
        else:
            for i in range (0,len(items)):
                if items[i] == "-" or items[i] >="a" and items[i]<"z":
                    new_word += items[i]
        word_dict[new_word] = word_dict.get(new_word, 0)+1
        new_word=""



for key, value in word_dict.items():
    print(f"{key} {value}")


    