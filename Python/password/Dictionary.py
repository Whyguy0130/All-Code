import itertools as its
words = "0123456789"
word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
r = its.product(words,repeat=4)  # random combination of 8 characters
s = its.product(word,repeat=8)
dic = open(r"C:\Users\KittellWyL\Documents\GitHub\All-Code\Python\password\Passwords\Schlagepasskey.txt","a")# store wifi combinations in file
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()