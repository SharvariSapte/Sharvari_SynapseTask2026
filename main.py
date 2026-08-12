print("Enter your characters:")
letters = input().split()
print(letters)
count = {}

for i, ch in enumerate(letters, start=1):
    ch = ch.upper()

    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

    if (
        count.get("I", 0) >= 1 and
        count.get("T", 0) >= 1 and
        count.get("H", 0) >= 1 and
        count.get("C", 0) >= 1 and
        count.get("A", 0) >= 2
    ):
        print(i)
        break
else:
    print(-1)