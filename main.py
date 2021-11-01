import re
num = 0
with open("classiccrazy_raw.txt", "r", encoding='utf-8')as har:
    for line in har:
        ids = re.findall('/avatars/([0-9]+)', line)
        r = open("output.txt", "a")
        if not ids == []:
            r.write(ids[0])
            r.write("\n")
            num += 1

print(f"Obtained {num} IDs!")


