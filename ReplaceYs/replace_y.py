lst = ["yesyy", "yoyo", "shady", "parise", "lady"]
counter = []
for item in lst:
    count = 0
    for i in item:
        if i == "y":
            count += 1
    counter.append(count)
new_lst = [lst[i].replace("y", "s") for i in range(len(lst)) if counter[i] >= 2]
print(new_lst)
