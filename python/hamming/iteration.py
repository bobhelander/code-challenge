
def compute(value1, value2):

    # Validation
    if len(value1) != len(value2):
        if len(value1) > len(value2):
            raise ValueError("Value1 is longer")
        raise ValueError("value2 is longer")

    # Use built-ins to build an array of zero and ones.  Sum() that array
    return sum(map(compute_element, value1, value2))


def compute_element(value1, value2):
    return 0 if value1 == value2 else 1