def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i=0
    a=list1[0]
    if list1.count(a)==len(list1):
        b=True
    else:
        b=False
    return b 