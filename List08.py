def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a=[]
    i=0
    while i<len(list1):
        if list1[i]==0:
            a+=[False]
        else:
            a+=[True]
        i+=1
    return a 