import unittest
import array_distance


class FindClosestElementTest(unittest.TestCase):

    def test_simple(self):
        res = array_distance.find_closest_element_by_binary_search(2, [-3, 3, 7])
        self.assertEqual((1, 1), res)

    def test_longer(self):
        res = array_distance.find_closest_element_by_binary_search(1000, [-9954, -7992, -6966, -2569, -1295, -1248, 1957, 6649, 7952, 7967])
        self.assertEqual((6, 957), res)

    def test_right_edge_case_with_lower(self):
        res = array_distance.find_closest_element_by_binary_search(7966, [-9954, -7992, -6966, -2569, -1295, -1248, 1957, 6649, 7952, 7967])
        self.assertEqual((9, 1), res)

    def test_right_edge_case_with_higher(self):
        res = array_distance.find_closest_element_by_binary_search(7968, [-9954, -7992, -6966, -2569, -1295, -1248, 1957, 6649, 7952, 7967])
        self.assertEqual((9, 1), res)

    def test_left_edge_case_with_lower(self):
        res = array_distance.find_closest_element_by_binary_search(-9955, [-9954, -7992, -6966, -2569, -1295, -1248, 1957, 6649, 7952, 7967])
        self.assertEqual((0, 1), res)

    def test_left_edge_case_with_higher(self):
        res = array_distance.find_closest_element_by_binary_search(-9953, [-9954, -7992, -6966, -2569, -1295, -1248, 1957, 6649, 7952, 7967])
        self.assertEqual((0, 1), res)

    def test_exact_match_in_middle(self):
        res = array_distance.find_closest_element_by_binary_search(-1295, [-9954, -7992, -6966, -2569, -1295, -1248, 1957, 6649, 7952, 7967])
        self.assertEqual((4, 0), res)

    def test_exact_match_in_first(self):
        res = array_distance.find_closest_element_by_binary_search(-9954, [-9954, -7992, -6966, -2569, -1295, -1248, 1957, 6649, 7952, 7967])
        self.assertEqual((0, 0), res)

    def test_exact_match_in_last(self):
        res = array_distance.find_closest_element_by_binary_search(7967, [-9954, -7992, -6966, -2569, -1295, -1248, 1957, 6649, 7952, 7967])
        self.assertEqual((9, 0), res)
