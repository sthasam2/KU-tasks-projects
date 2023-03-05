"""Test for correctness of sorting algorithms"""

from sorting import (
    insertion_sort,
    merge,
    merge_internal,
    merge_sort,
    merge_sort_internal,
)


class TestInsertionSort(object):
    """Test for Insertion sort correct ness"""

    def test_insertion_sort_zero_elements(self):
        """Test for zero elements"""
        sample = []
        expectation = []
        insertion_sort(sample)
        assert sample == expectation, "Zero Elements test for Insertion sort failed"

    def test_insertion_sort_one_element(self):
        """Test for single elements"""
        sample = [96]
        expectation = [96]
        insertion_sort(sample)
        assert sample == expectation, "Single Element test for Insertion sort failed"

    def test_insertion_sort_many_elements(self):
        """Test for many elements"""
        sample = [69, 7, 81, 44, 27, 52, 420, 32, 1]
        expectation = [1, 7, 27, 32, 44, 52, 69, 81, 420]
        insertion_sort(sample)
        assert sample == expectation, "Many elements test for Insertion sort failed"


class TestMergeSort(object):
    """Test for Merge sort correct ness"""

    def test_merge_function(self):
        """Test for merge algorithm"""
        sample1 = [777, 69, 420]
        sample2 = [13, 7, 2022]
        combined = [0] * 6
        expectation = [13, 7, 777, 69, 420, 2022]
        merge(sample1, sample2, combined)
        assert expectation == combined, "Merge Algorithm test failed"

    def test_merge_sort_zero_elements(self):
        """Test for zero elements"""
        sample = []
        expectation = []
        merge_sort(sample)
        assert sample == expectation, "Zero Elements test for merge sort failed"

    def test_merge_sort_one_element(self):
        """Test for single elements"""
        sample = [96]
        expectation = [96]
        merge_sort(sample)
        assert sample == expectation, "Single Element test for merge sort failed"

    def test_merge_sort_many_elements(self):
        """Test for zero elements"""
        sample = [69, 7, 81, 44, 27, 52, 420, 32, 1]
        expectation = [1, 7, 27, 32, 44, 52, 69, 81, 420]
        merge_sort(sample)
        assert sample == expectation, "Many elements test for merge sort failed"


class TestMergeSortInternal(object):
    """Test for Merge sort (internal version) for correct ness"""

    def test_merge_internal_function(self):
        """Test for merge algorithm"""

        sample3 = [1, 3, 15, 12, 10, 16, 2, 9]
        expectation = [1, 3, 15, 12, 2, 9, 10, 16]

        merge_internal(4, 5, 7, sample3)
        assert expectation == sample3, "Merge Algorithm test failed"

    def test_merge_sort_internal_zero_elements(self):
        """Test for zero elements"""
        sample = []
        expectation = []
        merge_sort_internal(0, len(sample) - 1, sample)
        assert sample == expectation, "Zero Elements test for merge sort failed"

    def test_merge_sort_internal_one_element(self):
        """Test for single elements"""
        sample = [96]
        expectation = [96]
        merge_sort_internal(0, len(sample) - 1, sample)
        assert sample == expectation, "Single Element test for merge sort failed"

    def test_merge_sort_internal_many_elements(self):
        """Test for zero elements"""

        sample = [68, 419, 1, 4, 331, 619, 45]
        expected = [1, 4, 45, 68, 331, 419, 619]
        merge_sort_internal(0, len(sample) - 1, sample)
        assert sample == expected, "merge sort assertion error for manu elements"

        sample = [1, 5, 2, 7]
        expected = [1, 2, 5, 7]
        merge_sort_internal(0, len(sample) - 1, sample)
        assert sample == expected, "merge sort assertion error for manu elements"
