def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    b=""
    for i in range(n):
        b+=str(i)+","

    return b
print(main(3))