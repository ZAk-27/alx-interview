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
    realmadrid = 1 << 8
    mancity = 1 << 7
    byteCt = 0
    for wembly in data:
        uefaCl = 1 << 7
        if byteCt == 0:
            while uefaCl & wembly:
                byteCt += 1
                uefaCl = uefaCl >> 1
            if byteCt == 0:
                continue
            if byteCt == 1 or byteCt > 4:
                return False
        else:
            if not (wembly & realmadrid and not (wembly & mancity)):
                return False
        byteCt -= 1
    return not byteCt
