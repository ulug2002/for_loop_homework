def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    a = []
    for i in range(n):
        a.append(k)
        i+=1
    return a
print(main(4,3))