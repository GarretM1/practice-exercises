BeeScript = []
wordlist = []
with open("markovTestData.txt", "r", newline='', encoding="cp437", errors='ignore') as f:
    for line in f:
        for word in line.split():
            n = word
            BeeScript.append(n)

with open("markovTestData.txt", "r", newline='', encoding="cp437", errors='ignore') as f:
    for line in f:
        for word in line.split():
            n = word
            if word in wordlist:
                continue
            else:
                wordlist.append(n)


with open("markovOccurChance.txt", "w", newline='', encoding="cp437", errors='ignore') as f:
    for word in BeeScript:

            f.write("%s: " % word)
            f.write("[")
            position = -1
            count = 0
            start = 0

            for ele in BeeScript:

                if ele == word:
                    y = position + 2
                    if y < len(BeeScript) - 3:
                        z = BeeScript[y]
                        f.write("%s, " % z)
                    count = count + 1

                position = BeeScript.index(ele, start)
                start = position
            Y = count
            Z = 1/Y * 100
            f.write("(%s percent chance each to come after.)]\n" % Z)

