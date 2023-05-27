def enough(cap, on, wait):
    availCapacity = cap - on
    if wait > availCapacity:
        return wait - availCapacity
    else:
        return 0