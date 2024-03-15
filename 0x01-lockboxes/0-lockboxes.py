#!/usr/bin/python3
'''lockboxes.
'''


def canUnlockAll(boxes):
    '''doc style.
    '''
    n = len(boxes)
    v_boxes = set([0])
    unv_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxkey = unv_boxes.pop()
        if not boxkey or boxkey >= n or boxkey < 0:
            continue
        if boxkey not in v_boxes:
            unv_boxes = unv_boxes.union(boxes[boxkey])
            v_boxes.add(boxkey)
    return n == len(v_boxes)
