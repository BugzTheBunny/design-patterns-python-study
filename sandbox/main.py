x = ["a", "c", 5, "d", 6, 29, "f"]


def get_nums(items):
    for f in items:

        if isinstance(f, int):
            print(f"{f} is int")
            yield f
        else:
            print(f"{f} is not int")

 for m in get_nums(x):
    print(f"num : {m}")
