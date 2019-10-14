from PIL import Image, ImageDraw
import math


def remap_number(src, old_min, old_max, new_min, new_max):
    return ((src - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)

wave_count = 8
count = 100
amp = 1


for i in range(count):
    v = remap_number(i, 0, 100, 0, wave_count * math.pi)
    s = math.sin(v)
    sr = remap_number(s, -1, 1, 0, 1 * amp)
    print(sr)