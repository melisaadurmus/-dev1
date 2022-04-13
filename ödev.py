def compareTo(arr1, arr2) :
    alice=[];
    bob=[];
    result=[];
    sum1=0;
    sum2=0;
    for i in range(len(arr1)):
        if arr1[i]<arr2[i]:
           
               bob.append(1)
           
        if arr1[i]>arr2[i]:
            
                alice.append(1)
            
        
        
    for i in alice:
        sum1 = sum1 + i
    result.append(sum1)
    for i in bob:
        sum2 = sum2 + i
    result.append(sum2)
          

    return result;

print(compareTo([1,4],[1,3]))