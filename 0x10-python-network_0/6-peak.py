#!/usr/bin/python3
"""6-peak.py module for find_peak function."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers.
    Args:
     list_of_integers(list): list of unsorted ints to find the peak of.
    """
    if list_of_integers != []:
        size = len(list_of_integers)
        if size == 1:
            return list_of_integers[0]
        elif size == 2:
            return max(list_of_integers)

        midindex = int(size / 2)
        peak = list_of_integers[midindex]
        if peak > list_of_integers[midindex - 1] \
                and peak > list_of_integers[midindex + 1]:
            return peak
        elif peak < list_of_integers[midindex - 1] \
                and peak < list_of_integers[midindex + 1]:
            return find_peak(list_of_integers[:midindex])
        else:
            return find_peak(list_of_integers[midindex:])

    return None
