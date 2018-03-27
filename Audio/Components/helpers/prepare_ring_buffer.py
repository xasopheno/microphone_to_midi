from collections import deque


def prepare_ring_buffer(size):
    rb = deque(maxlen=size)
    for i in range(size):
        rb.appendleft(0)
    return rb
