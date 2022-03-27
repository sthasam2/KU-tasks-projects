"""Test for correctness of sorting algorithms"""

from sorting import insertion_sort, merge, merge_sort


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
