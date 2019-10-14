import datetime
import math

from PIL import Image, ImageDraw




def remap_number(src, old_min, old_max, new_min, new_max):
    return ((src - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)


def calc_value(in_size, out_size):

    value = int((in_size[1] - out_size[1]) * 0.5)
    # print(value)

    return value


def get_color_to_memory(img, value, out_size):

    cl_l = []

    for i in range(value, out_size[1] + value):

        cl = []

        for j in range(size_src[0]):

            c = img.getpixel((j, i))
            cl.append(c)
        
        cl_l.append(cl)
    
    return cl_l


def slice_list(ll, size_):

    out = []
    start = 128
    
    for i in range(len(ll)):
        l = ll[i]
        ls = l[start : start + size_[0]]
        out.append(ls)
    
    return out


def slice_list_wave(ll, wave_count, size_, size_src):

    out = []
    amp = (size_src[0] - size_[0]) * 0.5
    
    for i in range(len(ll)):
        l = ll[i]
        
        shift_ = remap_number(i, 0, len(ll), 0, math.pi * wave_count)
        sine_ = (math.sin(shift_) + 1) * 0.5
        
        start = int(sine_ * amp)

        ls = l[start : start + size_[0]]
        out.append(ls)
    
    return out


def draw_from_list(ll, size):

    ### Create Canvas
    white_ = (255, 255, 255, 255)
    canvas_ = Image.new("RGBA", size_, white_)

    for i in range(len(ll)):
        l = ll[i]
        for j in range(len(ll[0])):
            c = l[j]
            # print(c)
            canvas_.putpixel((j, i), c)
    
    return canvas_






### input image
in_grid = "src/Grid-Color.png"
img = Image.open(in_grid)
size_src = img.size
# print(size_src)
### (1024, 1024)


### output image
size_ = (800, 800)




v_ = calc_value(size_src, size_)
cl_ = get_color_to_memory(img, v_, size_)
# cls_ = slice_list(cl_, size_)
cls_ = slice_list_wave(cl_, 4, size_, size_src)
canvas = draw_from_list(cls_, size_)


# print(len(cl_))
# print(len(cl_[0]))
# print(len(cl_[0][0]))
# print(cl_[0][0]) # RGBA



### Export png
now_ = str(datetime.datetime.now().strftime("%H:%M:%S"))
out_path = "result/{}.png".format(now_)
canvas.save(out_path, quality=100)
print("Export, {}".format(out_path))
