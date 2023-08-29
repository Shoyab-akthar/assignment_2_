def Sort_Tuple(List): 
    lst = len(List) 
    for i in range(0, lst): 
           
        for j in range(0, lst-i-1): 
            if (List[j][-1] > List[j + 1][-1]): 
                temp = List[j] 
                List[j]= List[j + 1] 
                List[j + 1]= temp 
    return List
   
List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
         
print(Sort_Tuple(List))