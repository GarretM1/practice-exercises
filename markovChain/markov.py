import csv

wordlist = []
BeeScript = []
occur = []
with open("markovTestData.txt", "r", newline='', encoding="cp437", errors='ignore') as f:
    for line in f:
        for word in line.split():
            n = word
            if word in wordlist:
                continue
            else:
                wordlist.append(n)

with open("markovTestData.txt", "r", newline='', encoding="cp437", errors='ignore') as f:
    for line in f:
        for word in line.split():
            n = word
            BeeScript.append(n)


with open("markovWordList.txt", "w", newline='', encoding="cp437", errors='ignore') as f:
    for word in wordlist:
        f.write("%s\n" % word)
with open("markovScript.txt", "w", newline='', encoding="cp437", errors='ignore') as f:
    for word in BeeScript:
        f.write("%s\n" % word)

def countX(BeeScript, word):
    count = 0
    for ele in BeeScript:
        if ele == word:
            count = count + 1
    return count

with open("markovOccur.txt", "w", newline='', encoding="cp437", errors='ignore') as f:
    for word in BeeScript:
        if word in wordlist:
            n1 = word
            g = countX(BeeScript, word)
            f.write("%s " % word)
            f.write("%s\n" % g)

