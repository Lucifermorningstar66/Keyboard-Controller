
def is_inside(x, y, key):
    kx, ky = key.pos
    return kx < x < kx + key.w and ky < y < ky + key.h
