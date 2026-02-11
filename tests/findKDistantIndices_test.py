# 2200. Find All K-Distant Indices in an Array
from src.findKDistantIndices import Solution

s = Solution()


def test_example1():
    nums = [3, 4, 9, 1, 3, 9, 5]
    key = 9
    k = 1
    out = [1, 2, 3, 4, 5, 6]
    assert s.findKDistantIndices(nums, key, k) == out


def test_example2():
    nums = [2, 2, 2, 2, 2]
    key = 2
    k = 2
    out = [0, 1, 2, 3, 4]
    assert s.findKDistantIndices(nums, key, k) == out


def test_example3():
    nums = [
        734,
        228,
        636,
        204,
        552,
        732,
        686,
        461,
        973,
        874,
        90,
        537,
        939,
        986,
        855,
        387,
        344,
        939,
        552,
        389,
        116,
        93,
        545,
        805,
        572,
        306,
        157,
        899,
        276,
        479,
        337,
        219,
        936,
        416,
        457,
        612,
        795,
        221,
        51,
        363,
        667,
        112,
        686,
        21,
        416,
        264,
        942,
        2,
        127,
        47,
        151,
        277,
        603,
        842,
        586,
        630,
        508,
        147,
        866,
        434,
        973,
        216,
        656,
        413,
        504,
        360,
        990,
        228,
        22,
        368,
        660,
        945,
        99,
        685,
        28,
        725,
        673,
        545,
        918,
        733,
        158,
        254,
        207,
        742,
        705,
        432,
        771,
        578,
        549,
        228,
        766,
        998,
        782,
        757,
        561,
        444,
        426,
        625,
        706,
        946,
    ]
    key = 939
    k = 34
    out = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
    ]
    assert s.findKDistantIndices(nums, key, k) == out


def test_example4():
    nums = [2, 1, 1, 1, 2]
    key = 2
    k = 1
    out = [0, 1, 3, 4]
    assert s.findKDistantIndices(nums, key, k) == out
