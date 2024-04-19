#!/usr/bin/python3
"""
Defining  UTF-8 Validation function pr
"""


def validUTF8(data):
    """
    UTF-8 Validation
    Args:
        data (list[int]): array of char  as 1byte int
    Returns:
        (True): all char in data are valid UTF-8 code point
        (False):  one or more char in data are invalid code point
    """
    rm = 1 << 8
    mc = 1 << 7
    byteCt = 0
    for cl in data:
        uefa = 1 << 7
        if byteCt == 0:
            while uefa & cl:
                byteCt += 1
                uefa = uefa >> 1
            if byteCt == 0:
                continue
            if byteCt == 1 or byteCt > 4:
                return False
        else:
            if not (cl & rm and not (cl & mc)):
                return False
        byteCt -= 1
    return not byteCt
