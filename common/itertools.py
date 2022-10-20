def cycle(i):
    while True:
        for item in i:
            yield item


def yoyo(i):
    while True:
        for item in i:
            yield item
        for item in reversed(i):
            yield item
