import cv2
import numpy as np
import random


# Global variable definitions


# Static function definitions

def getBlue(img):
    res = img.copy()
    res[:, :, 1] = 0
    res[:, :, 2] = 0
    return res


def getGreen(img):
    res = img.copy()
    res[:, :, 0] = 0
    res[:, :, 2] = 0
    return res


def getRed(img):
    res = img.copy()
    res[:, :, 0] = 0
    res[:, :, 1] = 0
    return res


def addVLines(img, minWidth, maxWidth, lines):
    res = img.copy()

    height, width, pix = res.shape
    for x in range(lines):
        # Create left and right bounds for vertical line
        left = random.randint(0, width)
        right = left + random.randint(minWidth, maxWidth)
        if right > width:
            right = width

        # Mess up line
        if random.randint(1, 2) % 2 == 0:
            res[:, left:right, 0] += random.randint(0, 255)
        else:
            res[:, left:right, 0] -= random.randint(0, 255)
        if random.randint(1, 2) % 2 == 0:
            res[:, left:right, 1] += random.randint(0, 255)
        else:
            res[:, left:right, 1] -= random.randint(0, 255)
        if random.randint(1, 2) % 2 == 0:
            res[:, left:right, 2] += random.randint(0, 255)
        else:
            res[:, left:right, 2] -= random.randint(0, 255)

    return res


def addHLines(img, minWidth, maxWidth, lines):
    res = img.copy()

    height, width, pix = res.shape
    for x in range(lines):
        # Create left and right bounds for vertical line
        top = random.randint(0, width)
        bottom = top + random.randint(minWidth, maxWidth)
        if bottom > width:
            bottom = width

        # Mess up line
        if random.randint(1, 2) % 2 == 0:
            res[top:bottom, :, 0] += random.randint(0, 255)
        else:
            res[top:bottom, :, 0] -= random.randint(0, 255)
        if random.randint(1, 2) % 2 == 0:
            res[top:bottom, :, 1] += random.randint(0, 255)
        else:
            res[top:bottom, :, 1] -= random.randint(0, 255)
        if random.randint(1, 2) % 2 == 0:
            res[top:bottom, :, 2] += random.randint(0, 255)
        else:
            res[top:bottom, :, 2] -= random.randint(0, 255)

    return res


def shift(img, xShift, yShift):
    shifted = img.copy()
    shifted = np.roll(shifted, xShift, 1)
    shifted = np.roll(shifted, yShift, 0)

    return shifted


# def shiftSubsetV(img, minWidth, maxWidth, shifts):
#     res = img.copy()

#     height, width, pix = res.shape
#     for x in range(shifts):
#         dist = random.randint(0, height)
#         left = random.randint(0, width)
#         right = left + random.randint(minWidth, maxWidth)
#         if right > width:
#             right = width

#         resSub = res[:, left:right, :].copy()
#         resSub = np.roll(resSub, dist, 0)
#         res[:, left:right, :] = resSub

#     return res

def shiftSubsetV(img, leftBound, subsetWidth, shiftDist):
    res = img.copy()
    height, width, pix = res.shape

    rightBound = leftBound + subsetWidth
    print(rightBound)
    print(width)
    print()
    if rightBound > width:
        if leftBound > width:
            res = shiftSubsetV(res, leftBound - width, rightBound - width, shiftDist)
        else:
            res = shiftSubsetV(res, 0, rightBound - width, shiftDist)
        rightBound = width
    resSub = res[:, leftBound:rightBound, :].copy()
    resSub = np.roll(resSub, shiftDist, 0)
    res[:, leftBound:rightBound, :] = resSub

    return res

def shiftSubsetH(img, topBound, subsetWidth, shiftDist):
    res = img.copy()
    height, width, pix = res.shape

    bottomBound = topBound + subsetWidth
    if bottomBound > height:
        if topBound > height:
            res = shiftSubsetH(res, topBound - height, bottomBound - height, shiftDist)
        else:
            res = shiftSubsetH(res, 0, bottomBound - height, shiftDist)
        bottomBound = height
    resSub = res[topBound:bottomBound, :, :].copy()
    resSub = np.roll(resSub, shiftDist, 1)
    res[topBound:bottomBound, :, :] = resSub

    return res

def wavy(img):
    res = img.copy()
    height, width, pix = res.shape

    for x in range(height):
        y = (x % 10) - 5

        res = shiftSubsetH(res, 5 * x, height - (10 * x), y)

    return res

# def shiftSubsetH(img, minWidth, maxWidth, shifts):
#     res = img.copy()

#     height, width, pix = res.shape
#     for x in range(shifts):
#         dist = random.randint(0, width)
#         top = random.randint(0, height)
#         bottom = top + random.randint(minWidth, maxWidth)
#         if bottom > width:
#             right = width

#         resSub = res[top:bottom, :, :].copy()
#         resSub = np.roll(resSub, dist, 1)
#         res[top:bottom, :, :] = resSub

#     return res


def shiftBlue(img, xShift, yShift):
    shifted = img.copy()
    shifted[:, :, 1] = 0
    shifted[:, :, 2] = 0
    shifted = np.roll(shifted, xShift, 1)
    shifted = np.roll(shifted, yShift, 0)

    unshifted = img.copy()
    unshifted[:, :, 0] = 0

    result = np.add(unshifted, shifted)
    return result


def shiftGreen(img, xShift, yShift):
    shifted = img.copy()
    shifted[:, :, 0] = 0
    shifted[:, :, 2] = 0
    shifted = np.roll(shifted, xShift, 1)
    shifted = np.roll(shifted, yShift, 0)

    unshifted = img.copy()
    unshifted[:, :, 1] = 0

    result = np.add(unshifted, shifted)
    return result


def shiftRed(img, xShift, yShift):
    shifted = img.copy()
    shifted[:, :, 0] = 0
    shifted[:, :, 1] = 0
    shifted = np.roll(shifted, xShift, 1)
    shifted = np.roll(shifted, yShift, 0)

    unshifted = img.copy()
    unshifted[:, :, 2] = 0

    result = np.add(unshifted, shifted)
    return result


def fuzzify(img):
    res = img.copy()
    height, width, x = res.shape

    rand = np.random.rand(height, width, x) * 2
    res = (res * rand) // 1
    return res


def scanlineify(img, width, offset=0, space=None):
    if space is None:
        space = width

    res = img.copy()

    # for x in range(width):
    #     res[x::width * 2 + (space - 1), :, :] *= 0
    for x in range(width):
        res[offset + x::width + space, :, :] *= 0

    return res

def bitify(img, bits):
    res1 = img.copy()
    res2 = img.copy()

    res1 //= (256 // bits)
    res1 *= (256 // bits)

    res2 //= (256 // bits)
    res2 += 1
    res2 *= (256 // bits)
    res2 -= 1

    res1 //= 2
    res2 //= 2

    res = np.add(res1, res2)# // 2
    # print(res)
    return res
