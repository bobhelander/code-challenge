

def compute(value1, value2):

    # Validation
    if len(value1) != len(value2):
        if len(value1) > len(value2):
            raise ValueError("Value1 is longer")
        raise ValueError("value2 is longer")

    # for each value, compare
    count = 0
    index = 0
    for item in value1:
        if item != value2[index]:
            count += 1
        index += 1
    return count
