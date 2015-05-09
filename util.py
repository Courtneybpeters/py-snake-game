def move(rect, speed, side, direction):

    # Side - top or left
    # Direction - 1 for positive or 0 for negative

    # Top (+) --> Down
    # Top (-) --> Up
    # Left (+) --> Right
    # Left (-) --> Left

    if side.lower() == 'top':
        if direction == 1:
            rect.top += speed
        else:
            rect.top -= speed
    else:
        if direction == 1:
            rect.left += speed
        else:
            rect.left -= speed
