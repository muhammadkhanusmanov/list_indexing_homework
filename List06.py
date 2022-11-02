def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a=[]
    i=0
    while i<len(list1):
        if list1[i]==1:
            a+=[True]
        else:
            a+=[list1[i]]
        i+=1
    return a 