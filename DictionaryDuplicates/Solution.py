def dict_duplicate(dct):
    values = []

    for i in dct:
        values.append(dct[i])

    for item_1 in values:
        count_item = 0
        for item_2 in values:
            if item_1 == item_2:
                count_item += 1

        if count_item > 1:
            return True

    return False
