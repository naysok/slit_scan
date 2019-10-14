def remap_number(src, old_min, old_max, new_min, new_max):
    return ((src - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)



v0 = remap_number(4, 0, 10, 0, 100)
print(v0)


v1 = remap_number(4, 0, 4, 0, 100)
print(v1)