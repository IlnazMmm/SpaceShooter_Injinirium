def swamp():
    trees = {}
    while True:
        try:
            item = input()
            if "," not in item:
                continue
            list_of_item = item.split(", ")
            trees[list_of_item[0]] = list_of_item[-1]
        except EOFError:
            break
    return trees

print(swamp())

