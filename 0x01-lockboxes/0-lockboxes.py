def canUnlockAll(boxes):
    if not boxes or len(boxes) == 0:
        return False

    # Use a set to keep track of opened boxes
    opened_boxes = {0}
    keys = [0]  # Start with the keys in the first box

    # Keep exploring new keys until no more new keys are found
    while keys:
        current_key = keys.pop()

        # Iterate through the keys in the current box
        for key in boxes[current_key]:
            if key not in opened_boxes and key < len(boxes):
                keys.append(key)
                opened_boxes.add(key)

    # If all boxes are opened (len(opened_boxes) equals len(boxes)), return True
    return len(opened_boxes) == len(boxes)
