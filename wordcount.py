# put your code here.
file = open("twain.txt")
word_dict = {}

for line in file:
    words = line.strip("\n").lower().split(" ")

    for items in words:
        word_dict[items] = word_dict.get(items, 0)+1


for key, value in word_dict.items():
    print(f"{key} {value}")

    
    