
phrase = "John1367"

numList = []

for ch in phrase:
    if ch.isdigit():
        numList += ch

print("there are ", len(numList), " numbers")
