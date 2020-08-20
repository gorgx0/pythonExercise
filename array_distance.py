import sys


def array_distance_brute_force_no_optimization_whatsoever(A, B):
    min_distance = sys.maxsize
    min_distance_index_a = -1
    min_distance_index_b = -1
    for index_a, a in enumerate(A):
        for index_b, b in enumerate(B):
            dist = abs(a - b)
            if min_distance > dist:
                min_distance = dist
                min_distance_index_a = index_a
                min_distance_index_b = index_b
                if min_distance == 0:
                    return min_distance_index_a, min_distance_index_b, 0
    return min_distance_index_a, min_distance_index_b, min_distance


def find_closest_element_by_binary_search(a, B):
    low_idx = 0
    high_idx = len(B)-1
    diff = sys.maxsize
    while low_idx <= high_idx:
        mid = int((high_idx + low_idx)/2)
        if abs(a-B[mid]) < diff:
            diff = abs(a-B[mid])
        if mid > 0 and abs(a-B[mid-1]) < diff:
            high_idx = mid-1
            continue
        if mid+1<len(B) and abs(a-B[mid+1]) < diff:
            low_idx = mid+1
            continue
        break

    return mid, diff


def array_distance_with_search(A, B):
    min_distance = sys.maxsize
    min_distance_index_a = -1
    min_distance_index_b = -1
    for index_a, a in enumerate(A):
        index_b, dist = find_closest_element_by_binary_search(a, B)
        if min_distance > dist:
            min_distance = dist
            min_distance_index_a = index_a
            min_distance_index_b = index_b
            if min_distance == 0:
                return min_distance_index_a, min_distance_index_b, 0
    return min_distance_index_a, min_distance_index_b, min_distance
