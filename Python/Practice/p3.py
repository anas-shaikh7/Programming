def main():
    list = []
    while True:
        try:
            item = input("").upper()
            list.append(item)
        except EOFError:
            break
    list2 = []
    for thing in list:
        c = list.count(thing)
        x = f"{c} {thing}"
        if not x in list2:
            list2.append(x)
    # print()
    list_updated = "\n".join(sorted(list2, key=lambda x: x.split(" ", 1)[1]))
    print(list_updated)
main()
