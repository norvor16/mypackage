def top_n(item,n):
    """
    Returns the top n numbers in descending order
    
    Args:
    item(array): array or list 
    n(int): the number of items to be returned to be returned
    
    Return: 
    array:Top n items in desc order
    
    Example:
    >>>([10,15,8,9,4],2)
    [15,20]
    """
    for i in range(n): #keep sorting until we have the top n items
        for j in range(len(item)-1-i):
            if item[j] > item[j+1]: #if this is bigger than the next line
                item[j],item[j+1] = item[j+1],item[j] #swap the two
    top_n = item[-n:] #return the last n items
    return top_n[::-1]   #return the list of n items in descending order        