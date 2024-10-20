strings = ["hello","comp","student"]
new_string = [s.replace(s[-2:],s[-1]+s[-2]) for s in strings]
print(new_string)
