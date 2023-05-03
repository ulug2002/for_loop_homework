def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    n = []
    for i in range(A,B+1,1):
        n.append(i)
    return n
print(main(4,7))