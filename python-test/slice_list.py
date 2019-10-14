l = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],    
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]


# print(len(l))
# print(len(l[0]))


def slice_list(ll, count):

    out = []

    for i in range(len(ll)):
        l = ll[i]
        ls = l[i : i+count]
        out.append(ls)

    return out



ls = slice_list(l, 3)


print(ls)
#5x10 >> 5x3
