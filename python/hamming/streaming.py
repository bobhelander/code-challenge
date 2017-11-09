
def compute(value1, value2):
    differences = hamming_generator(value1,value2)

    # We now have a generator that will work on file streams and
    # we can also output the differences while it is processing.

    # For the test we will just make a list() object and return the length
    return len(list(differences))


def hamming_generator(value1, value2):
    """
    hamming_generator returns a tuple for every mismatched element of the sequence.  The tuple contains
        the index of the mismatch and the values that mismatched.
    :param value1: Iterable value to compare
    :param value2: Iterable value to compare
    :return: (index_number, element_1, element_2)
    """

    index_counter = 0
    itr1 = iter(value1)
    itr2 = iter(value2)

    while True:
        element1 = next(itr1, None)   # Use default value of None to stop iteration
        element2 = next(itr2, None)

        # Check for stop conditions
        if not element1 or not element2:
            if element1 == element2:
                return
            if not element1:
                raise ValueError("value1 is shorter")
            raise ValueError("value2 is shorter")

        # Return unmatched pairs and the index number
        if element1 != element2:
            yield (index_counter, element1, element2)

        index_counter += 1
