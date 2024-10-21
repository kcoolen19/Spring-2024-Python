def least_common(dct):
    values = []
    for i in dct:
        values.append(dct[i])
    repetition = {}
    for i in values:
        if i in repetition:
            repetition[i] += 1
        else:
            repetition[i] = 1
    occurrences = []
    for i in repetition:
        occurrences.append(repetition[i])
    minimum = occurrences[0]
    for i in occurrences:
        if i < minimum:
            minimum = i
    for key, value in repetition.items():
        if value == minimum:
            return key
