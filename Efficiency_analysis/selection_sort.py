def selectionSort(arr, l, r):

    size = r+1
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            
            if arr[j] < arr[min_index]:
                min_index = j
        
        (arr[ind], arr[min_index]) = (arr[min_index], arr[ind])