#!/usr/bin/python3
"""6-peak.py module for find_peak function."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers.
    Args:
     list_of_integers(list): list of unsorted ints to find the peak of.
    """
    if list_of_integers:
        # Keep track of highest value integer(peak).
        peak = 0
        # Iterate through the list while keeping track of the peak.
        for element in list_of_integers:
            if peak < element:
                peak = element
        return peak
    return None
